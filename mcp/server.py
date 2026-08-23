# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "mcp>=1.2",
#     "PyYAML>=6",
# ]
# ///
"""Quant Wiki MCP index server (issue #88).

Exposes the wiki's table of contents to MCP-capable agents (Claude Code,
Cursor, Codex, ...) so they can discover what the wiki covers and fetch a
page on demand — without uploading every page anywhere.

The catalog is parsed from ``mkdocs.yml`` (the same navigation tree that
renders https://quant-wiki.com). Page content is read from the local checkout
when the server runs inside one, and fetched from raw.githubusercontent.com
otherwise, so `uv run` works with or without a clone.

Tools:
    wiki_catalog(section=None)  Top-level sections with page counts, or one
                                section's full page listing.
    wiki_search(query)          Case-insensitive title/path search (Chinese
                                and English both work: filenames carry both).
    wiki_page(path)             One page's markdown by its docs path.

Run (stdio):
    uv run mcp/server.py

Smoke check (no MCP client needed):
    uv run mcp/server.py --check
"""

from __future__ import annotations

import sys
import urllib.parse
import urllib.request
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import yaml

try:  # mcp >= 2.0
    from mcp.server import MCPServer
except ImportError:  # mcp 1.x
    from mcp.server.fastmcp import FastMCP as MCPServer

_REPO_ROOT = Path(__file__).resolve().parent.parent
_REMOTE_RAW = "https://raw.githubusercontent.com/LLMQuant/quant-wiki/master/"
_SITE_URL = "https://quant-wiki.com/"
_USER_AGENT = "quant-wiki-mcp/1.0"
_MAX_SEARCH_HITS = 50


@dataclass(frozen=True)
class CatalogEntry:
    """One wiki page: its navigation title path and its docs file path."""

    title_path: tuple[str, ...]
    doc_path: str

    @property
    def site_url(self) -> str:
        path = self.doc_path
        if path.endswith("index.md"):
            path = path[: -len("index.md")]
        elif path.endswith(".md"):
            path = path[: -len(".md")] + "/"
        return _SITE_URL + urllib.parse.quote(path)


class _NavLoader(yaml.SafeLoader):
    """SafeLoader that tolerates mkdocs extension tags like !!python/name."""


_NavLoader.add_multi_constructor(
    "tag:yaml.org,2002:python/",
    lambda loader, suffix, node: None,
)


def _read_text(relative_path: str) -> str:
    """Read one repo file locally when possible, remotely otherwise."""
    local = _REPO_ROOT / relative_path
    if local.is_file():
        return local.read_text(encoding="utf-8")
    url = _REMOTE_RAW + urllib.parse.quote(relative_path)
    request = urllib.request.Request(url, headers={"User-Agent": _USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


def _walk_nav(node, title_path: tuple[str, ...], out: list[CatalogEntry]):
    if isinstance(node, str):
        out.append(CatalogEntry(title_path=title_path, doc_path=node))
        return
    if isinstance(node, list):
        for item in node:
            _walk_nav(item, title_path, out)
        return
    if isinstance(node, dict):
        for title, child in node.items():
            _walk_nav(child, (*title_path, str(title)), out)


@lru_cache(maxsize=1)
def _catalog() -> tuple[CatalogEntry, ...]:
    config = yaml.load(_read_text("mkdocs.yml"), Loader=_NavLoader)
    entries: list[CatalogEntry] = []
    _walk_nav(config.get("nav", []), (), entries)
    return tuple(
        entry for entry in entries if entry.doc_path.endswith(".md")
    )


def _format_entry(entry: CatalogEntry) -> str:
    return f"- {' / '.join(entry.title_path)} — `{entry.doc_path}`"


mcp = MCPServer(
    "quant-wiki",
    instructions=(
        "Index of Quant Wiki (quant-wiki.com), the open-source Chinese "
        "quantitative finance encyclopedia. Call wiki_catalog to see what "
        "exists, wiki_search to locate topics, and wiki_page to read one "
        "page. Cite pages by their site URL."
    ),
)


@mcp.tool()
def wiki_catalog(section: str | None = None) -> str:
    """List the wiki's sections, or every page inside one section.

    Args:
        section: Optional top-level section title (as returned by the
            no-argument call), e.g. "基本概念" or "量化百科". Omit it to get
            the section overview with page counts.

    Returns:
        Markdown: either the top-level section overview or the selected
        section's full page listing (navigation title path + docs path).
    """
    entries = _catalog()
    if section is None:
        counts: dict[str, int] = {}
        for entry in entries:
            top = entry.title_path[0] if entry.title_path else "(untitled)"
            counts[top] = counts.get(top, 0) + 1
        lines = [f"Quant Wiki catalog — {len(entries)} pages. Sections:"]
        lines += [
            f"- {top} ({count} pages)" for top, count in counts.items()
        ]
        lines.append(
            'Call wiki_catalog(section="<section title>") for its pages.'
        )
        return "\n".join(lines)
    matches = [
        entry
        for entry in entries
        if entry.title_path and entry.title_path[0] == section
    ]
    if not matches:
        return (
            f"No section titled {section!r}. Call wiki_catalog() without "
            "arguments to list valid section titles."
        )
    lines = [f"{section} — {len(matches)} pages:"]
    lines += [_format_entry(entry) for entry in matches]
    return "\n".join(lines)


@mcp.tool()
def wiki_search(query: str) -> str:
    """Find wiki pages whose title or path matches a query.

    Args:
        query: Case-insensitive substring. Chinese and English both match
            because page filenames carry both (e.g. "债券_Bond.md").

    Returns:
        Markdown list of up to 50 matches (navigation title path + docs
        path), or a not-found note.
    """
    needle = query.strip().lower()
    if not needle:
        return "Empty query. Provide a keyword such as '债券' or 'bond'."
    hits = [
        entry
        for entry in _catalog()
        if needle in " / ".join(entry.title_path).lower()
        or needle in entry.doc_path.lower()
    ]
    if not hits:
        return f"No wiki page matches {query!r}."
    shown = hits[:_MAX_SEARCH_HITS]
    lines = [f"{len(hits)} pages match {query!r}:"]
    lines += [_format_entry(entry) for entry in shown]
    if len(hits) > len(shown):
        lines.append(f"... and {len(hits) - len(shown)} more; refine the query.")
    return "\n".join(lines)


@mcp.tool()
def wiki_page(path: str) -> str:
    """Read one wiki page's markdown by its docs path.

    Args:
        path: The docs path exactly as listed by wiki_catalog or
            wiki_search, e.g. "basic/finance/债券_Bond.md".

    Returns:
        The page markdown, prefixed with its canonical site URL for
        citation. Unknown paths return guidance instead of content.
    """
    normalized = path.strip().lstrip("/")
    if normalized.startswith("docs/"):
        normalized = normalized[len("docs/"):]
    entry = next(
        (e for e in _catalog() if e.doc_path == normalized), None
    )
    if entry is None:
        return (
            f"{path!r} is not in the wiki catalog. Locate the exact docs "
            "path with wiki_search or wiki_catalog first."
        )
    content = _read_text(f"docs/{entry.doc_path}")
    header = (
        f"# Source: {entry.site_url}\n"
        f"# Section: {' / '.join(entry.title_path)}\n\n"
    )
    return header + content


def _check() -> int:
    entries = _catalog()
    sections: dict[str, int] = {}
    for entry in entries:
        top = entry.title_path[0] if entry.title_path else "(untitled)"
        sections[top] = sections.get(top, 0) + 1
    print(f"catalog: {len(entries)} pages, {len(sections)} sections")
    for top, count in sections.items():
        print(f"  {top}: {count}")
    sample = entries[len(entries) // 2]
    print(f"sample entry: {_format_entry(sample)}")
    print(f"sample url:   {sample.site_url}")
    content = wiki_page(sample.doc_path)
    print(f"sample page:  {len(content)} chars, starts: {content[:80]!r}")
    hits = wiki_search("债券")
    print(f"search '债券': {hits.splitlines()[0]}")
    return 0


if __name__ == "__main__":
    if "--check" in sys.argv:
        raise SystemExit(_check())
    mcp.run()
