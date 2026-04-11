![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

# Deep Dive: Sentiment Analysis of Tesla News with DeepSeek-R1 for Investment Recommendations

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

In equity investing, **news sentiment** can have a significant impact on stock prices. Real-time monitoring and analysis of news helps gauge market sentiment and improve investment decisions. This article uses Tesla (**TSLA**) as a case study, combining **Yahoo Finance**, **MarkItDown**, and the **DeepSeek-R1** model to demonstrate a complete pipeline from "fetching news to extracting content to sentiment analysis to investment recommendations."

> **Target audience**: Quantitative engineers, data scientists, portfolio managers, and anyone interested in automated financial news analysis who wants to get started with news sentiment analysis quickly.

## Feature Overview

1. **Fetch Tesla-related news**: Use `yfinance` to retrieve the latest TSLA news.
2. **Extract and clean article content**: Use the MarkItDown library to parse web page content, with simple regex-based text cleaning.
3. **Sentiment analysis and recommendations**: Leverage the DeepSeek-R1 model to score multiple articles and generate investment recommendations.

These steps let you quickly build a compact "sentiment radar" that aggregates and analyzes multiple news articles.

## I. Environment Setup

1. Install Python dependencies:
   ```bash
   pip install yfinance pandas markitdown requests langchain langchain-ollama
   ```
2. Ensure **DeepSeek-R1** is successfully deployed locally or on a server, accessible via [Ollama](https://ollama.ai/) or a similar interface.

> If you do not yet have the DeepSeek-R1 model, you can set up the required environment locally or substitute a compatible alternative model.

---

## II. Fetching Tesla (TSLA) News

### 2.1 The `get_news` Function

The following function retrieves Tesla-related news via the `yfinance` `Ticker` object, extracting key fields (title, summary, URL, publication date):

```python
import yfinance as yf
import pandas as pd

def get_news(stock: str) -> list:
    """
    Fetch a list of news articles related to the specified stock.
    Returns a list of dictionaries with title, summary, URL, and publication date.
    """
    try:
        ticker = yf.Ticker(stock)
        news = ticker.news

        if not news:
            print(f"No news found for {stock}.")
            return []

        # Filter for STORY content type only
        relevant_news = [
            item for item in news if item.get('content', {}).get('contentType') == 'STORY'
        ]

        all_news = []
        for i, item in enumerate(relevant_news):
            try:
                content = item.get('content', {})
                current_news = {
                    'title': content.get('title'),
                    'summary': content.get('summary'),
                    'url': content.get('canonicalUrl', {}).get('url'),
                    'pubdate': content.get('pubDate', '').split('T')[0],
                }
                all_news.append(current_news)
            except Exception as e:
                print(f"Error processing news {i}: {e}")
                continue

        return all_news

    except Exception as e:
        print(f"An error occurred while fetching news for {stock}: {e}")
        return []
```

#### Example Usage

```python
news_list = get_news("TSLA")
print(len(news_list))  # Number of articles retrieved
print(news_list[0])    # First article details
```

Sample output structure:

```python
{
    'title': 'Tesla Poised to Beat Q1 Earnings Estimates...',
    'summary': '...',
    'url': 'https://finance.yahoo.com/news/...',
    'pubdate': '2025-01-20'
}
```

## III. Extracting and Cleaning Article Content

### 3.1 Parsing Web Pages with MarkItDown

`MarkItDown` converts HTML web pages into plain text, including titles and body content. During extraction, we remove **URLs** and **special characters** to produce cleaner text for downstream analysis.

```python
from markitdown import MarkItDown
import requests
import re

# Create a session for improved stability
session = requests.Session()
session.headers.update({
    'User-Agent': 'python-requests/2.32.3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'keep-alive'
})
md = MarkItDown(requests_session=session)

def remove_links(text: str) -> str:
    """
    Remove URLs, Markdown-format links, and extraneous characters.
    """
    text = re.sub(r'http\S+', '', text)       # Remove URLs
    text = re.sub(r'\[.*?\]', '', text)       # Remove Markdown links
    text = re.sub(r'[#*()+\-\n]', '', text)   # Remove special characters
    text = re.sub(r'/\S*', '', text)          # Remove slash-prefixed content
    text = re.sub(r'  ', '', text)            # Remove extra spaces
    return text

def extract_news(link: str) -> str:
    """
    Extract the page title and body content using MarkItDown, clean and return.
    """
    info = md.convert(link)
    text_title = info.title.strip()
    text_content = info.text_content.strip()
    return text_title + '\n' + remove_links(text_content)
```

### 3.2 Aggregating All News Content

With `get_news` and `extract_news`, we can batch-extract all articles:

```python
def extract_full_news(stock: str) -> list:
    """
    Add a full_news field containing the extracted web page body to each news item.
    """
    news_data = get_news(stock)
    for i, item in enumerate(news_data):
        try:
            content = extract_news(item['url'])
            item['full_news'] = content
        except Exception as e:
            print(f"Error extracting news {i}: {e}")
            continue
    return news_data

# Example with TSLA
full_news_list = extract_full_news("TSLA")

print(full_news_list[0]['title'])       # Article title
print(full_news_list[0]['full_news'])   # Extracted full text
```

The resulting `full_news_list` is a comprehensive collection containing all fields (title, summary, URL, full text, etc.).

![](https://fastly.jsdelivr.net/gh/bucketio/img5@main/2025/02/26/1740600002331-9d6ca907-4b79-48d9-bb67-94245f893670.png)

## IV. Sentiment Analysis and Investment Recommendations with DeepSeek-R1

### 4.1 Binding DeepSeek-R1 with LangChain

This example uses [OllamaLLM](https://pypi.org/project/langchain-ollama/) as the interface for calling DeepSeek-R1. Multiple articles are combined and sent to the LLM for sentiment analysis.

```python
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from pprint import pprint

# Initialize DeepSeek-R1
llm = OllamaLLM(model="deepseek-r1:1.5b")
```

### 4.2 Crafting the Prompt Template

We want the model to provide a "Positive/Negative/Neutral" sentiment assessment for each article, then synthesize all articles into a summary with an investment recommendation. This is written as a `system` prompt for the LLM:

```python
PROMPT = """
You are an expert financial analyst. I will provide you with a list of news articles related to Tesla (TSLA). Your tasks:

1. **Sentiment Analysis:**
   - For each news article, evaluate its sentiment as 'Positive', 'Negative', or 'Neutral'.
   - Present your evaluation in a dictionary format like: {"Article Title": "Positive", ...}

2. **Comprehensive Summary & Recommendation:**
   - Summarize the overall sentiment and key points from all articles.
   - Advise if investing in TSLA is advisable, with reasons derived from the news analysis.

**News Articles:**

{articles}

**Output Format:**

1. Sentiment Analysis Dictionary (JSON)
2. Summary
3. Investment Recommendation
"""

prompt_template = ChatPromptTemplate.from_messages(
    [
        ('system', PROMPT),
        ('human', "I want to analyze TSLA's news articles in detail.")
    ]
)
```

### 4.3 Invoking the Model and Viewing Results

Combine the extracted full text (`full_news`) into a list, pass it as `articles` to the PromptTemplate, and call the LLM:

```python
structure = prompt_template | llm

result = structure.invoke({
    "articles": [item['full_news'] for item in full_news_list]
})

pprint(result)
```

Once DeepSeek-R1 completes generation, you will see output similar to:

```txt
"<think>\n... [model internal reasoning] ...\n</think>\n\n
### Sentiment Analysis Dictionary
```json
{
   "Tesla Q4 Earnings: A Beat on Estimates?": "Positive",
   "Elon Musk's Latest Statement Sparks Controversy": "Neutral",
   ...
}
```
```
### Summary
Based on the articles, Tesla's expansion in Europe...
### Investment Recommendation
Tesla continues to demonstrate strong performance...
"
```

This output includes **per-article sentiment scores**, an **overall summary**, and an **investment recommendation**, providing an intuitive picture of recent Tesla news and additional reference points for decision-making.

---

## V. Advanced Extensions

1. **Combine with technical and fundamental analysis**: Integrate the "news sentiment" from this tutorial with stock technical indicators and financial metrics to build a multi-factor analysis agent.
2. **Automated scheduling**: Use tools like Airflow or cron to run this script periodically, maintaining up-to-date news tracking; push results to custom notifications or visualization dashboards.
3. **Swap in other LLMs or plugins**: To compare analysis quality across models, substitute DeepSeek-R1 with alternatives such as ChatGPT, LLaMA, etc., and benchmark sentiment accuracy and speed.

---

## Conclusion

By combining **yfinance** for news retrieval, **MarkItDown** for web content extraction, and **DeepSeek-R1** for sentiment analysis and investment recommendation generation, you can build a simple prototype for **real-time news sentiment analysis**.
- **Automated**: Capable of continuous, large-scale news collection.
- **Extensible**: Models can be swapped flexibly, and results can be integrated into more sophisticated financial decision-making workflows.

With the steps outlined above, you now have a complete pipeline from "data acquisition" to "model analysis." We encourage you to combine this approach with additional **factor analysis** and **visualization** tools to build a more comprehensive and intelligent "multidimensional financial analysis" workflow.

## About LLMQuant

LLMQuant is a cutting-edge community composed of researchers from top universities and quantitative finance professionals worldwide, dedicated to exploring the intersection of artificial intelligence (AI) and quantitative finance (Quant). Our team members come from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other leading institutions, with external advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and top proprietary trading firms.
