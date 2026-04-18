![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

# Building a Professional Financial Analyst with DeepSeek-R1 or ChatGPT and LangChain (Open-Source Code)

In today's rapidly evolving financial markets, **using artificial intelligence to support investment decisions** is capturing the attention of an ever-growing number of investors. Leveraging large language models for **stock analysis** and **news insights** enables efficient access to critical data and generates more valuable investment recommendations. This article walks you through building two practical applications:

1. **Part One**: Build a **stock analysis agent** powered by **DeepSeek-R1** that retrieves stock prices, computes technical indicators, evaluates financial metrics, and outputs actionable conclusions.
2. **Part Two**: Build a **news analysis agent** powered by **ChatGPT** that extracts real-time news and performs sentiment analysis, providing a more comprehensive reference for investment decisions.

> If you are a finance professional, quantitative engineer, or data scientist, this article provides nearly complete sample code to help you quickly build your own intelligent analysis agent.

## Part One: Building a Stock Analysis Agent with DeepSeek-R1

In this section, we use the **DeepSeek-R1** model to analyze **stock price and financial data**. The main steps include:

1. Environment setup and installation
2. Retrieving historical stock prices and key technical indicators (RSI, MACD, VWAP, etc.)
3. Retrieving financial metrics (P/E ratio, Price-to-Book, Debt-to-Equity, Profit Margins, etc.)
4. Orchestrating the workflow with **LangChain** and **LangGraph**, using **DeepSeek-R1** for analysis generation

### 1. Installation

Install the required libraries (note: DeepSeek-R1 requires [Ollama](https://ollama.ai/) or an equivalent local deployment environment):

```bash
pip install -U langgraph langchain langchain-ollama pandas ta python-dotenv yfinance
```

Create a `.env` file in your project directory for custom environment variables (if needed):

```
# Optional
DEEPSEEK_API_KEY=your_deepseek_api_key
```

Skip this if you do not need a private API.

### 2. Retrieving Stock Prices and Technical Indicators

Ensure you have `yfinance` installed for stock data retrieval and `ta` for computing common technical indicators. The following utility function fetches **24 weeks** of price data for a given stock and calculates **RSI**, **MACD**, **Stochastic Oscillator**, and **VWAP**.

```python
from typing import Union, Dict, TypedDict
import pandas as pd
import yfinance as yf
import datetime as dt

# TA library
from ta.momentum import RSIIndicator, StochasticOscillator
from ta.trend import MACD
from ta.volume import volume_weighted_average_price

def get_stock_prices(ticker: str) -> Union[Dict, str]:
    """Fetch historical price data and key technical indicators for a given stock."""
    try:
        data = yf.download(
            ticker,
            start=dt.datetime.now() - dt.timedelta(weeks=24*3),
            end=dt.datetime.now(),
            interval='1wk'
        )
        df = data.copy()
        data.reset_index(inplace=True)
        data.Date = data.Date.astype(str)

        indicators = {}

        rsi_series = RSIIndicator(df['Close'], window=14).rsi().iloc[-12:]
        indicators["RSI"] = {
            date.strftime('%Y-%m-%d'): float(value)
            for date, value in rsi_series.dropna().to_dict().items()
        }

        sto_series = StochasticOscillator(
            df['High'], df['Low'], df['Close'], window=14
        ).stoch().iloc[-12:]
        indicators["Stochastic_Oscillator"] = {
            date.strftime('%Y-%m-%d'): float(value)
            for date, value in sto_series.dropna().to_dict().items()
        }

        macd = MACD(df['Close'])
        macd_series = macd.macd().iloc[-12:]
        indicators["MACD"] = {
            date.strftime('%Y-%m-%d'): float(value)
            for date, value in macd_series.to_dict().items()
        }

        macd_signal_series = macd.macd_signal().iloc[-12:]
        indicators["MACD_Signal"] = {
            date.strftime('%Y-%m-%d'): float(value)
            for date, value in macd_signal_series.to_dict().items()
        }

        vwap_series = volume_weighted_average_price(
            high=df['High'],
            low=df['Low'],
            close=df['Close'],
            volume=df['Volume'],
        ).iloc[-12:]
        indicators["vwap"] = {
            date.strftime('%Y-%m-%d'): float(value)
            for date, value in vwap_series.to_dict().items()
        }

        return {
            'stock_price': data.to_dict(orient='records'),
            'indicators': indicators
        }

    except Exception as e:
        return f"Error fetching price data: {str(e)}"
```

### 3. Retrieving Financial Metrics

Key financial health indicators include **P/E, Price-to-Book, Debt-to-Equity, and Profit Margins**:

```python
def get_financial_metrics(ticker: str) -> Union[Dict, str]:
    """Fetch key financial ratios for a given stock."""
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        return {
            'pe_ratio': info.get('forwardPE'),
            'price_to_book': info.get('priceToBook'),
            'debt_to_equity': info.get('debtToEquity'),
            'profit_margins': info.get('profitMargins')
        }
    except Exception as e:
        return f"Error fetching ratios: {str(e)}"
```

### 4. Comprehensive Analysis with LangGraph + DeepSeek-R1

#### 4.1 Configuration

We use **LangGraph** to orchestrate the conversation flow and tool invocations. The LLM is **DeepSeek-R1**, called via [OllamaLLM](https://pypi.org/project/langchain-ollama/).

```python
import dotenv
dotenv.load_dotenv()

from langgraph.graph import StateGraph, START, END
from langchain_core.nodes import ToolNode
from typing import TypedDict

class State(TypedDict):
    messages: list
    stock: str

graph_builder = StateGraph(State)
```

#### 4.2 Binding the DeepSeek-R1 Model

```python
from langchain_ollama.llms import OllamaLLM

# Initialize Ollama + DeepSeek-R1
llm = OllamaLLM(model="deepseek-r1:1.5b")
```

#### 4.3 Building the Prompt and Binding Tools

We want the agent to:
1. Retrieve stock history and technical indicators
2. Retrieve financial metrics
3. Produce a comprehensive analysis with readable conclusions

```python
from langchain.schema import SystemMessage
from langchain_core.tools import tool

FUNDAMENTAL_ANALYST_PROMPT = """
You are a fundamental analyst specializing in evaluating company performance based on stock prices, technical indicators, and financial metrics.
Your task: Provide a comprehensive summary for {company}.

Steps to follow:
1. Use get_stock_prices and get_financial_metrics to gather data.
2. Analyze trends, potential support/resistance, and financial health.
3. Provide a concise, objective summary in JSON with:
   - "stock": <symbol>
   - "price_analysis": ...
   - "technical_analysis": ...
   - "financial_analysis": ...
   - "final_summary": ...
   - "recommendation": ...
"""

def fundamental_analyst(state: State):
    system_message = SystemMessage(
        content=FUNDAMENTAL_ANALYST_PROMPT.format(company=state['stock'])
    )
    messages = [system_message] + state["messages"]
    result = llm.invoke(messages)
    return {"messages": result}
```

#### 4.4 Wiring Tool and Analysis Nodes into the Workflow

```python
tools = [get_stock_prices, get_financial_metrics]

# Wrap tools as a LangGraph node
graph_builder.add_node('fundamental_analyst', fundamental_analyst)
graph_builder.add_edge(START, 'fundamental_analyst')

def tools_condition(state: State) -> bool:
    return True

graph_builder.add_node(ToolNode(tools))
graph_builder.add_conditional_edges('fundamental_analyst', tools_condition)
graph_builder.add_edge('tools', 'fundamental_analyst')

graph = graph_builder.compile()
```

#### 4.5 Running the Agent

```python
events = graph.stream({
    "messages": [("user", "Should I buy this stock?")],
    "stock": "AAPL"
}, stream_mode='values')

for event in events:
    if 'messages' in event:
        print(event['messages'][-1].content)
```

Sample output:

```json
{
  "stock": "AAPL",
  "price_analysis": "Recent price shows an upward trend with moderate volatility...",
  "technical_analysis": "RSI is around 62 indicating slightly overbought range...",
  "financial_analysis": "PE ratio is 28.5, which is higher than industry median...",
  "final_summary": "Apple maintains strong fundamentals but currently trades at a premium...",
  "recommendation": "Consider a partial buy if you anticipate continued revenue growth."
}
```

---

## Part Two: Building a News Analysis Agent with ChatGPT

After completing stock price and financial data analysis, it is essential to also consider **market sentiment** and **real-time news dynamics**. This section describes how to use **ChatGPT** (or OpenAI GPT-4) to analyze relevant news, producing sentiment assessments and investment recommendations.

### 1. Key Features

- **Fetch stock-related news** (via Yahoo Finance)
- **Extract full article text** (using MarkItDown and similar tools)
- **Perform sentiment analysis** (Positive, Negative, Neutral)
- **Generate investment recommendations based on consolidated news analysis**

### 2. Installation and Setup

If you have already installed `langgraph`, `langchain`, etc., you can skip ahead -- just ensure the **OpenAI** dependency is installed:

```bash
pip install openai
```

Add to your `.env` file:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Fetching News Links

```python
import yfinance as yf
import pandas as pd

def get_news(stock: str) -> list:
    """
    Fetch a list of news articles related to the specified stock.
    """
    try:
        ticker = yf.Ticker(stock)
        news = ticker.news

        if not news:
            print(f"No news found for {stock}.")
            return []

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

### 4. Extracting and Cleaning Article Content

```python
from markitdown import MarkItDown
import requests
import re

session = requests.Session()
session.headers.update({
    'User-Agent': 'python-requests/2.32.3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'keep-alive'
})
md = MarkItDown(requests_session=session)

def remove_links(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'[#*()+\-\n]', '', text)
    text = re.sub(r'/\S*', '', text)
    text = re.sub(r'  ', '', text)
    return text

def extract_news(link):
    extracted = md.convert(link)
    title = extracted.title.strip()
    content = extracted.text_content.strip()
    return title + "\n" + remove_links(content)
```

### 5. Retrieving Full Article Content

```python
def extract_full_news(stock: str) -> list:
    news_list = get_news(stock)
    for i, item in enumerate(news_list):
        try:
            full_text = extract_news(item['url'])
            item['full_news'] = full_text
        except Exception as e:
            print(f"Error extracting news {i}: {e}")
            continue
    return news_list
```

### 6. Sentiment Analysis and Investment Recommendations with ChatGPT

Now we have **complete articles**. Below we use **LangChain** + **OpenAI** for sentiment analysis.

```python
import os
import openai
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models import ChatOpenAI

openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize ChatGPT (using gpt-4 here; substitute other models as needed)
chat = ChatOpenAI(model='gpt-4')

NEWS_ANALYSIS_PROMPT = """
You are an expert financial analyst.
I will provide you with a list of news articles related to a stock. For each article:
1. Determine sentiment: Positive, Negative, or Neutral.
2. Summarize key points relevant to the stock.
3. Provide an overall summary of all articles and a final investment recommendation.

Format your output as:
{
  "sentiment_analysis": {
    "title1": "Positive",
    "title2": "Negative",
    ...
  },
  "key_points": [
    "...",
    "..."
  ],
  "overall_summary": "...",
  "recommendation": "..."
}
"""

def analyze_news_with_chatgpt(stock: str):
    # Fetch and extract full news
    news_data = extract_full_news(stock)

    # Concatenate articles into the prompt
    articles_text = "\n\n".join([
        f"Title: {n['title']}\nContent: {n['full_news']}" for n in news_data if 'full_news' in n
    ])

    system_msg = SystemMessage(content=NEWS_ANALYSIS_PROMPT)
    user_msg = HumanMessage(content=f"Stock: {stock}\nNews:\n{articles_text}")

    response = chat([system_msg, user_msg])
    return response.content
```

Example invocation:

```python
# result = analyze_news_with_chatgpt("AAPL")
# print(result)
```

ChatGPT returns a JSON structure containing per-article sentiment assessments, key takeaways, an overall summary, and an investment recommendation. You can parse this output and integrate it into the workflow built earlier, achieving a **three-dimensional agent analysis** spanning sentiment, technical, and fundamental perspectives.

---

## Summary and Future Extensions

In this tutorial, we demonstrated two major capabilities:

1. **Building a stock analysis agent with DeepSeek-R1**:
   - Retrieving stock prices and technical indicators
   - Retrieving financial data
   - Using LangGraph to orchestrate the workflow and produce readable analysis reports

2. **Building a news analysis agent with ChatGPT**:
   - Fetching stock-related news links
   - Extracting and cleaning web article content
   - Performing sentiment analysis and generating investment recommendations

### What can you build next?

- **Multi-agent fusion**: Combine the "stock analysis agent" and "news analysis agent" into a single LangGraph workflow, producing unified output covering **price, financial, and news** analysis.
- **Enhanced factor models**: Incorporate industry comparisons, macroeconomic data, and additional factors based on market characteristics.
- **Visualization and automation**: Deploy analysis results on a web interface or in automated workflows that generate reports on a schedule.
- **Alternative open-source LLMs**: Experiment with BLOOM, LLaMA, ChatGLM, and others to compare analysis quality and performance.

> **Whether you choose DeepSeek-R1 or ChatGPT, both can be flexibly swapped or used in combination based on your needs.** We hope this tutorial helps you quickly build your own "agent-powered financial analyst" and gain deeper insights in dynamic markets.

## About LLMQuant

LLMQuant is a cutting-edge community composed of researchers from top universities and quantitative finance professionals worldwide, dedicated to exploring the intersection of artificial intelligence (AI) and quantitative finance (Quant). Our team members come from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other leading institutions, with external advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and top proprietary trading firms.
