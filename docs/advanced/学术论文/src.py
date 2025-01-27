import argparse
import datetime
import json
import logging
import os
import re

import arxiv
import requests
import yaml

# from document_reader import load_and_process_pdfs_by_langchain

logging.basicConfig(format='[%(asctime)s %(levelname)s] %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S',
                    level=logging.INFO)

base_url = "https://arxiv.paperswithcode.com/api/v0/papers/"
github_url = "https://api.github.com/search/repositories"
arxiv_url = "http://arxiv.org/"

paper_index = {
    "传统量化金融": "traditional quantitative finance",
    "金融时间序列": "financial time-series forecasting",
    "金融大语言模型": "financial large language model",
}

def load_config(config_file:str) -> dict:
    def pretty_filters(**config) -> dict:
        keywords = dict()
        EXCAPE = '\"'
        QUOTA = '' # NO-USE
        OR = ' OR ' # TODO

        def parse_filters(filters:list):
            """
            将过滤器列表转换为特定格式的字符串。
            - 如果过滤器包含多个单词，则在过滤器两端添加双引号；
            - 否则，添加空字符串。
            多个过滤器之间用 " OR " 连接。
            """
            ret = ''
            for idx in range(0,len(filters)):
                filter = filters[idx]
                if len(filter.split()) > 1:
                    ret += (EXCAPE + filter + EXCAPE)
                else:
                    ret += (QUOTA + filter + QUOTA)
                if idx != len(filters) - 1:
                    ret += OR
            return ret

        for k, v in config['keywords'].items():
            keywords[k] = parse_filters(v['filters'])
        return keywords

    with open(config_file,'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        config['kv'] = pretty_filters(**config)
        logging.info(f'config = {config}')
    return config

def get_authors(authors, first_author = False):
    output = str()
    if first_author == False:
        output = ", ".join(str(author) for author in authors)
    else:
        output = authors[0]
    return output

def sort_papers(papers):
    output = dict()
    keys = list(papers.keys())
    keys.sort(reverse=True)
    for key in keys:
        output[key] = papers[key]
    return output

import requests


def get_code_link(qword:str) -> str:
    # query = f"arxiv:{arxiv_id}"
    query = f"{qword}"
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc"
    }
    r = requests.get(github_url, params=params)
    results = r.json()
    code_link = None
    if results["total_count"] > 0:
        code_link = results["items"][0]["html_url"]
    return code_link

def get_daily_papers(topic, query="quantitative finance", max_results=2):
    today_date = datetime.date.today().strftime("%Y-%m-%d")
    cn_query_key = paper_index[query]
    query_folder_path = os.path.join("docs/advanced/学术论文", cn_query_key, today_date)
    if not os.path.exists(query_folder_path):
        os.makedirs(query_folder_path)

    # output
    content = dict()
    content_to_web = dict()
    search_engine = arxiv.Search(
        query = query,
        max_results = max_results,
        sort_by = arxiv.SortCriterion.SubmittedDate
    )

    for result in search_engine.results():
        paper_id            = result.get_short_id()
        paper_title         = result.title
        paper_url           = result.entry_id
        code_url            = base_url + paper_id #TODO
        paper_abstract      = result.summary.replace("\n"," ")
        paper_authors       = get_authors(result.authors)
        paper_first_author  = get_authors(result.authors,first_author = True)
        primary_category    = result.primary_category
        publish_time        = result.published.date()
        update_time         = result.updated.date()
        comments            = result.comment
        paper_summary       = ""

        logging.info(f"Time = {update_time} title = {paper_title} author = {paper_first_author}")

        # eg: 2108.09112v1 -> 2108.09112
        ver_pos = paper_id.find('v')
        if ver_pos == -1:
            paper_key = paper_id
        else:
            paper_key = paper_id[0:ver_pos]
        paper_url = arxiv_url + 'abs/' + paper_key
        
        # Download PDF
        pdf_url = result.pdf_url
        pdf_response = requests.get(pdf_url)
        pdf_filename = os.path.join(query_folder_path, f"{paper_key}.pdf")
        with open(pdf_filename, 'wb') as pdf_file:
            pdf_file.write(pdf_response.content)
        logging.info(f"Downloaded PDF for {paper_title} to {pdf_filename}")

        # researh_paper_context = load_and_process_pdfs_by_langchain(pdf_filename)

        # from oai.llm_utils import APIBackend
        # from jinja2 import Environment, StrictUndefined

        # system_prompt_template = """
        # You are a helpful assistant. Please summarize the following research paper content in three sentences.
        # """
        # user_prompt_template = """
        # Here is the content of the research paper:
        # {{ researh_paper_context }}
        # Please provide a summary.
        # """

        # system_prompt = (
        #     Environment(undefined=StrictUndefined).from_string(system_prompt_template).render()
        # )
        # user_prompt = (
        #     Environment(undefined=StrictUndefined)
        #     .from_string(user_prompt_template)
        #     .render(researh_paper_context=researh_paper_context)
        # )

        # paper_summary = APIBackend().build_messages_and_create_chat_completion(user_prompt, system_prompt, json_mode=False)

        try:
            # source code link
            r = requests.get(code_url).json()
            repo_url = None
            if "official" in r and r["official"]:
                repo_url = r["official"]["url"]
            # TODO: not found, two more chances
            # else:
            #    repo_url = get_code_link(paper_title)
            #    if repo_url is None:
            #        repo_url = get_code_link(paper_key)
            if repo_url is not None:
                content[paper_key] = "|**{}**|**{}**|{} et.al.|[{}]({})|**[link]({})**|{}|\n".format(
                    update_time, paper_title, paper_first_author, paper_key, paper_url, repo_url, paper_summary
                )
                content_to_web[paper_key] = "- {}, **{}**, {} et.al., Paper: [{}]({}), Code: **[{}]({})**, Summary: {}\n".format(
                    update_time, paper_title, paper_first_author, paper_url, paper_url, repo_url, repo_url, paper_summary
                )
            else:
                content[paper_key] = "|**{}**|**{}**|{} et.al.|[{}]({})|null|{}|\n".format(
                    update_time, paper_title, paper_first_author, paper_key, paper_url, paper_summary
                )
                content_to_web[paper_key] = "- {}, **{}**, {} et.al., Paper: [{}]({}), Summary: {}\n".format(
                    update_time, paper_title, paper_first_author, paper_url, paper_url, paper_summary
                )

            # TODO: select useful comments
            comments = None
            if comments != None:
                content_to_web[paper_key] += f", {comments}\n"
            else:
                content_to_web[paper_key] += f"\n"

        except Exception as e:
            logging.error(f"exception: {e} with id: {paper_key}")

    data = {topic:content}
    data_web = {topic:content_to_web}
    return data, data_web

def update_paper_links(filename):
    '''
    weekly update paper links in json file
    '''
    def parse_arxiv_string(s):
        parts = s.split("|")
        date = parts[1].strip()
        title = parts[2].strip()
        authors = parts[3].strip()
        arxiv_id = parts[4].strip()
        code = parts[5].strip()
        summary = parts[6].strip() if len(parts) > 6 else "No summary available"
        arxiv_id = re.sub(r'v\d+', '', arxiv_id)
        return date, title, authors, arxiv_id, code, summary

    with open(filename,"r") as f:
        content = f.read()
        if not content:
            m = {}
        else:
            m = json.loads(content)

        json_data = m.copy()

        for keywords,v in json_data.items():
            logging.info(f'keywords = {keywords}')
            for paper_id,contents in v.items():
                contents = str(contents)

                update_time, paper_title, paper_first_author, paper_url, code_url, paper_summary = parse_arxiv_string(contents)

                contents = "|{}|{}|{}|{}|{}|{}|\n".format(
                    update_time, paper_title, paper_first_author, paper_url, code_url, paper_summary
                )
                json_data[keywords][paper_id] = str(contents)
                logging.info(f'paper_id = {paper_id}, contents = {contents}')

                valid_link = False if '|null|' in contents else True
                if valid_link:
                    continue
                try:
                    code_url = base_url + paper_id #TODO
                    r = requests.get(code_url).json()
                    repo_url = None
                    if "official" in r and r["official"]:
                        repo_url = r["official"]["url"]
                        if repo_url is not None:
                            new_cont = contents.replace('|null|',f'|**[link]({repo_url})**|')
                            logging.info(f'ID = {paper_id}, contents = {new_cont}')
                            json_data[keywords][paper_id] = str(new_cont)

                except Exception as e:
                    logging.error(f"exception: {e} with id: {paper_id}")
        # dump to json file
        with open(filename,"w") as f:
            json.dump(json_data,f)

def update_json_file(filename,data_dict):
    '''
    daily update json file using data_dict
    '''
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write("{}")

    with open(filename,"r") as f:
        content = f.read()
        if not content:
            m = {}
        else:
            m = json.loads(content)

    json_data = m.copy()

    # update papers in each keywords
    for data in data_dict:
        for keyword in data.keys():
            papers = data[keyword]

            if keyword in json_data.keys():
                json_data[keyword].update(papers)
            else:
                json_data[keyword] = papers

    with open(filename,"w") as f:
        json.dump(json_data,f)

def json_to_md(filename,md_filename,
               task = '',
               to_web = False,
               use_title = True,
               use_tc = True,
               show_badge = True,
               use_b2t = True):
    """
    @param filename: str
    @param md_filename: str
    @return None
    """
    def pretty_math(s:str) -> str:
        ret = ''
        match = re.search(r"\$.*\$", s)
        if match == None:
            return s
        math_start,math_end = match.span()
        space_trail = space_leading = ''
        if s[:math_start][-1] != ' ' and '*' != s[:math_start][-1]: space_trail = ' '
        if s[math_end:][0] != ' ' and '*' != s[math_end:][0]: space_leading = ' '
        ret += s[:math_start]
        ret += f'{space_trail}${match.group()[1:-1].strip()}${space_leading}'
        ret += s[math_end:]
        return ret

    DateNow = datetime.date.today()
    DateNow = str(DateNow)
    DateNow = DateNow.replace('-','.')

    with open(filename,"r") as f:
        content = f.read()
        if not content:
            data = {}
        else:
            data = json.loads(content)

    # clean README.md if daily already exist else create it
    with open(md_filename,"w+") as f:
        pass

    # write data into README.md
    with open(md_filename,"a+") as f:

        if (use_title == True) and (to_web == True):
            f.write("---\n" + "layout: default\n" + "---\n\n")

        # if show_badge == True:
        #     f.write(f"[![Contributors][contributors-shield]][contributors-url]\n")
        #     f.write(f"[![Forks][forks-shield]][forks-url]\n")
        #     f.write(f"[![Stargazers][stars-shield]][stars-url]\n")
        #     f.write(f"[![Issues][issues-shield]][issues-url]\n\n")

        if use_title == True:
            #f.write(("<p align="center"><h1 align="center"><br><ins>CV-ARXIV-DAILY"
            #         "</ins><br>Automatically Update CV Papers Daily</h1></p>\n"))
            f.write("## Updated on " + DateNow + "\n")
        else:
            f.write("> Updated on " + DateNow + "\n")

        #Add: table of contents
        if use_tc == True:
            f.write("<details>\n")
            f.write("  <summary>Table of Contents</summary>\n")
            f.write("  <ol>\n")
            for keyword in data.keys():
                day_content = data[keyword]
                if not day_content:
                    continue
                kw = keyword.replace(' ','-')
                f.write(f"    <li><a href=#{kw.lower()}>{keyword}</a></li>\n")
            f.write("  </ol>\n")
            f.write("</details>\n\n")

        for keyword in data.keys():
            day_content = data[keyword]
            if not day_content:
                continue
            # the head of each part
            f.write(f"## {keyword}\n\n")

            if use_title == True :
                if to_web == False:
                    f.write("|Publish Date|Title|Authors|PDF|Code|Summary|\n" + "|---|---|---|---|---|---|\n")
                else:
                    f.write("| Publish Date | Title | Authors | PDF | Code | Summary |\n")
                    f.write("|:---------|:-----------------------|:---------|:------|:------|:------|\n")

            # sort papers by date
            day_content = sort_papers(day_content)

            for _,v in day_content.items():
                if v is not None:
                    f.write(pretty_math(v)) # make latex pretty

            f.write(f"\n")

            #Add: back to top
            if use_b2t:
                top_info = f"#Updated on {DateNow}"
                top_info = top_info.replace(' ','-').replace('.','')
                f.write(f"<p align=right>(<a href={top_info.lower()}>back to top</a>)</p>\n\n")

    logging.info(f"{task} finished")

def demo(**config):
    data_collector = []
    data_collector_web= []

    keywords = config['kv']
    max_results = config['max_results']
    publish_readme = config['publish_readme']
    publish_gitpage = config['publish_gitpage']
    publish_wechat = config['publish_wechat']
    show_badge = config['show_badge']

    b_update = config['update_paper_links']
    logging.info(f'Update Paper Link = {b_update}')
    if config['update_paper_links'] == False:
        logging.info(f"GET daily papers begin")
        for topic, keyword in keywords.items():
            logging.info(f"Keyword: {topic}")
            data, data_web = get_daily_papers(topic, query = keyword,
                                            max_results = max_results)
            data_collector.append(data)
            data_collector_web.append(data_web)
            print("\n")
        logging.info(f"GET daily papers end")

    # 1. update README.md file
    if publish_readme:
        json_file = config['json_readme_path']
        md_file   = config['md_readme_path']
        # update paper links
        if config['update_paper_links']:
            update_paper_links(json_file)
        else:
            # update json data
            update_json_file(json_file,data_collector)
        # json data to markdown
        json_to_md(json_file,md_file, task ='Update Readme', \
            show_badge = show_badge)

    # 2. update docs/index.md file (to gitpage)
    if publish_gitpage:
        json_file = config['json_gitpage_path']
        md_file   = config['md_gitpage_path']
        # TODO: duplicated update paper links!!!
        if config['update_paper_links']:
            update_paper_links(json_file)
        else:
            update_json_file(json_file,data_collector)
        json_to_md(json_file, md_file, task ='Update GitPage', \
            to_web = True, show_badge = show_badge, \
            use_tc=False, use_b2t=False)

    # 3. Update docs/wechat.md file
    if publish_wechat:
        json_file = config['json_wechat_path']
        md_file   = config['md_wechat_path']
        # TODO: duplicated update paper links!!!
        if config['update_paper_links']:
            update_paper_links(json_file)
        else:
            update_json_file(json_file, data_collector_web)
        json_to_md(json_file, md_file, task ='Update Wechat', \
            to_web=False, use_title= False, show_badge = show_badge)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_path', type=str, default='config.yaml',
                            help='configuration file path')
    parser.add_argument('--update_paper_links', default=False,
                        action="store_true", help='whether to update paper links etc.')
    args = parser.parse_args()
    config = load_config(args.config_path)
    config = {**config, 'update_paper_links':args.update_paper_links}
    demo(**config)
