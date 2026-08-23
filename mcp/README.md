# Quant Wiki MCP

把 Quant Wiki 的目录接进 MCP 客户端（Claude Code、Cursor、Codex 等），让 AI Agent 知道 wiki 里有哪些内容、按需读取单页 —— 不需要上传所有页面（[#88](https://github.com/LLMQuant/quant-wiki/issues/88)）。

An MCP server exposing the Quant Wiki table of contents: agents discover what the wiki covers via the catalog and fetch single pages on demand.

## 工具

| 工具 | 作用 |
|---|---|
| `wiki_catalog()` | 顶层分区总览（每区页数）；`wiki_catalog(section="基本概念")` 列出该分区全部页面 |
| `wiki_search(query)` | 按标题/路径搜索页面，中英文都可（文件名同时带中英文，如 `债券_Bond.md`） |
| `wiki_page(path)` | 按 docs 路径读取单页 markdown，带站点引用 URL |

目录解析自 `mkdocs.yml`（与 [quant-wiki.com](https://quant-wiki.com) 渲染所用的同一棵导航树）。在本地 checkout 内运行时直接读本地文件；否则自动从 GitHub raw 拉取，因此**不 clone 仓库也能用**。

## 接入

只需要 [uv](https://docs.astral.sh/uv/)（会按脚本头部声明自动装 `mcp` 和 `PyYAML`）。

**Claude Code**（已 clone 本仓库）：

```bash
claude mcp add quant-wiki -- uv run /path/to/quant-wiki/mcp/server.py
```

**不 clone 仓库**（单文件即可运行，内容走远程拉取）：

```bash
curl -fsSLO https://raw.githubusercontent.com/LLMQuant/quant-wiki/master/mcp/server.py
claude mcp add quant-wiki -- uv run ./server.py
```

**Cursor / 其他 JSON 配置的客户端**：

```json
{
  "mcpServers": {
    "quant-wiki": {
      "command": "uv",
      "args": ["run", "/path/to/quant-wiki/mcp/server.py"]
    }
  }
}
```

## 自检

不需要 MCP 客户端即可验证目录解析与页面读取：

```bash
uv run mcp/server.py --check
```

输出目录页数、各分区统计、抽样页面与搜索结果。
