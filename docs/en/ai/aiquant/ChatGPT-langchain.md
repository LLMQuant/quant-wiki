![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

# Building a Stock Research Framework with ChatGPT and LangChain: A Step-by-Step Guide
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

Investment analysts are increasingly leveraging artificial intelligence to process financial data, identify trends, and extract actionable insights. **LangChain**, a powerful open-source framework, enables the integration of language models like GPT with investment analysis workflows. This article explores how to use LangChain to streamline preliminary investment research, including **integrating financial data sources**, **building advanced custom models**, and making more informed **investment decisions** based on predictive insights.

In this article, we will focus on:

> 1. Why choose LangChain?
> 2. What is LangChain?
> 3. Core components of LangChain
> 4. How to perform stock analysis with LangChain and OpenAI in Python

## Why Choose LangChain?
Let us start by asking ChatGPT to analyze the NIFTY50 index's price performance over the past 5 years:

![](https://fastly.jsdelivr.net/gh/bucketio/img1@main/2025/02/15/1739656021954-842a89c6-5f12-4a7a-827b-082257fc13e7.png)

> **"When we ask ChatGPT about NIFTY50's performance over the past 5 years, it does not have ready access to the data needed for analysis."**

This is exactly where **LangChain** shines. LangChain connects financial data sources to large language models (LLMs), fundamentally changing how investors analyze and interpret market data. By processing vast quantities of textual data -- news articles, earnings reports, and social media sentiment -- LangChain provides analysts with richer, more timely insights to support better investment decisions.

## What is LangChain?
LangChain serves as an interface between large language models and external data sources, enabling users to build **AI-driven applications**. It allows developers to connect to various databases, retrieve relevant information, process inputs, and generate structured outputs.

![](https://fastly.jsdelivr.net/gh/bucketio/img19@main/2025/02/15/1739656034346-533c4045-ea5a-4aac-9c0c-fc97eb728621.png)

> "LLMs (Large Language Models) are deep learning models trained on massive datasets that generate responses to user queries. LangChain provides the tools and abstraction layers to enhance model output with greater customization, accuracy, and relevance."
> "LangChain supports a wide range of mainstream LLM providers. See the full list at: [https://python.langchain.com/docs/integrations/llms/](https://python.langchain.com/docs/integrations/llms/)."

## Core Components of LangChain
In the following examples, we demonstrate how to implement LangChain's key components in Python.

![](https://fastly.jsdelivr.net/gh/bucketio/img3@main/2025/02/15/1739656041606-31207779-b15e-4465-b329-c084e05150c4.png)

> **Note: Some code examples below use the langchain_openai version as indicated.**

![](https://fastly.jsdelivr.net/gh/bucketio/img18@main/2025/02/15/1739656100104-857e381f-88f8-4102-99e7-98381a1ba038.png)

### 1. Using LLMs
LangChain integrates multiple large language models through a **prompting** mechanism, generating more sophisticated and targeted responses for specific tasks or queries.
![](https://fastly.jsdelivr.net/gh/bucketio/img15@main/2025/02/15/1739656110396-a8674285-0267-4917-946d-cba8c90867b2.png)
- **Temperature**: Controls the randomness of model output. Setting it to 0 produces deterministic output, yielding identical results across multiple runs.

**Example output:**

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2025/02/15/1739656120414-4048f53d-2c01-4f8f-80d2-a72e7b3aeae4.png)

> **"Since the output contains multiple elements, we are most interested in the content portion, which can be extracted using the appropriate method."**

### 2. Prompt Templates
Prompt templates are **predefined structures or formats** used to generate prompts for language models like GPT-4. They help construct consistent, context-aware queries or instructions across different scenarios. Templates can include dynamic placeholders for injecting specific data or parameters.

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2025/02/15/1739656145141-983ccd3b-1bd6-4836-a849-34bbffa730a0.png)

### 3. Chains
In LangChain, a "chain" refers to an ordered sequence of steps or operations that links prompts, data processing steps, API calls, and other components together to accomplish more complex natural language processing tasks.
> **"chain = prompt | llm"**
means feeding the prompt into the language model (LLM) to generate a response.

![](https://fastly.jsdelivr.net/gh/bucketio/img7@main/2025/02/15/1739656160804-ab734299-fdf2-48d9-bc4f-525efdcd48be.png)

- Batch processing: Submitting multiple inputs to a chain simultaneously for parallel processing, improving efficiency.

![](https://fastly.jsdelivr.net/gh/bucketio/img7@main/2025/02/15/1739656167462-5c38f475-0dee-4285-98ef-ce7d1d3523b6.png)

### 4. Agents
An **Agent** is an automated entity that uses a large language model to complete a specific task. It can make decisions, execute actions, and dynamically interact with multiple data sources or APIs as needed.
In the example below, **PythonREPLTool()** serves as a tool for the Agent to execute Python code directly within the LangChain workflow, handling data processing, analysis, or computation.

> **Note:** The LangChain version used in the following example is "langchain-core<0.2".

![](https://fastly.jsdelivr.net/gh/bucketio/img6@main/2025/02/15/1739656174967-f3151ffb-1663-4ad9-a0d7-2a411b5bc85e.png)

![](https://fastly.jsdelivr.net/gh/bucketio/img17@main/2025/02/15/1739656182025-0bdc16cc-55a1-49c3-9899-1af7be302c07.png)

## Equity Analysis with LangChain and OpenAI (Python Example)
Next, we build a simple LLM-based application to determine whether a stock is worth investing in. The application uses the following data sources:

- **Google News**
- **Historical stock price data**
- A **ChatGPT Agent** that integrates these data points to generate comprehensive analysis and responses

In this example, we use **agents** to generate responses. You can also use **function calling** for more structured output.

### 1. Prerequisites
- An **OpenAI API Key** (obtainable from the OpenAI website).
- A **SERP API Key** (from [SERPAPI](https://serpapi.com/)) to fetch the latest news for a given stock.

### 2. Import Libraries
Before starting, ensure you have the correct version of **Pydantic** installed.

![](https://fastly.jsdelivr.net/gh/bucketio/img2@main/2025/02/15/1739656196722-23e2cba2-08cb-45dc-a34b-a1cb530fe7a8.png)

```python
# Install pydantic
!pip install pydantic==<appropriate_version>
```

Then import the required libraries and modules:
![](https://fastly.jsdelivr.net/gh/bucketio/img16@main/2025/02/15/1739656204753-b22580da-f346-4eb5-a138-88ef7f260212.png)

```python
import os
import requests
import datetime
import yfinance as yf
from typing import Dict
from langchain_core.tools import Tool
from langchain.agents import initialize_agent
from langchain_core.prompts import PromptTemplate
# ... other necessary imports
```

LangChain provides `langchain_core.tools` for defining and managing tools that Agents can use -- these tools execute specific tasks such as computations, database queries, web searches, or API calls.
`langchain.agents` provides the framework for building and running Agents capable of reasoning, decision-making, and invoking tools.
`langchain_core.prompts` is used to design and manage prompts that guide model responses.

### 3. Fetch Latest News
Below we define a `get_news` function that retrieves the latest news for a target stock via the **SERP API**. Replace "YOUR_SERPAPI_API_KEY" with your actual API key:
![](https://fastly.jsdelivr.net/gh/bucketio/img5@main/2025/02/15/1739656224205-d0288dfd-e4f6-4726-a82e-e6ac63d3700a.png)

```python
def get_news(ticker: str) -> str:
    # Example code to fetch news via SERP API
    ...
```

### 4. Retrieve Historical Stock Prices
Fetch the past year of historical price data via **Yahoo Finance**:

```python
def get_historical_data(ticker: str) -> str:
    # Uses yfinance library to retrieve historical stock price data
    ...
```

![](https://fastly.jsdelivr.net/gh/bucketio/img3@main/2025/02/15/1739656233507-63ea62a3-7096-4d48-bc62-115d2045df62.png)

### 5. Custom Analysis Function
Define an `analyze_stock` function that determines whether a stock is worth investing in. This function applies rules based on data performance and news content to generate analysis:

![](https://fastly.jsdelivr.net/gh/bucketio/img6@main/2025/02/15/1739656242065-6179ba65-adf0-44b0-a9cd-54109ca463c8.png)

```python
def analyze_stock(news: str, historical_data: str) -> str:
    # Custom logic for analysis
    ...
```

### 6. Define Tools
Wrap the three functions as LangChain **Tools** -- `get_news`, `get_historical_data`, and `analyze_stock` -- for use by the Agent:

```python
tools = [
    Tool(
        name="get_news",
        func=get_news,
        description="Fetch the latest news for a target stock"
    ),
    Tool(
        name="get_historical_data",
        func=get_historical_data,
        description="Fetch historical price data for a target stock"
    ),
    Tool(
        name="analyze_stock",
        func=analyze_stock,
        description="Analyze whether a stock is worth investing in"
    )
]
```

![](https://fastly.jsdelivr.net/gh/bucketio/img13@main/2025/02/15/1739656261255-d1e1ff87-d07a-400a-8ca3-43e07d158c53.png)

### 7. Define the Prompt

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2025/02/15/1739656271042-0aed56ef-505b-4812-a51b-6254c39eea96.png)

```python
prompt_template = PromptTemplate(
    input_variables=["ticker"],
    template="""
        I want to analyze the investment value of stock {ticker}.
        You can use the following tools:
        1. get_news: Fetch news
        2. get_historical_data: Fetch historical prices
        3. analyze_stock: Comprehensive analysis
        Please provide a final conclusion.
    """
)
```

![](https://fastly.jsdelivr.net/gh/bucketio/img13@main/2025/02/15/1739656278953-0c1fbbee-33e9-4576-915b-a92eff5e3d43.png)

### 8. Create the Agent and Generate Results
Finally, create an Agent to generate the stock analysis:

![](https://fastly.jsdelivr.net/gh/bucketio/img8@main/2025/02/15/1739656284236-f89caa6d-eb5d-4f3c-a709-384b3d2d0960.png)

```python
agent = initialize_agent(
    tools=tools,
    llm=OpenAI(temperature=0),
    prompt=prompt_template,
    # Other required parameters
)

response = agent.run({"ticker": "AAPL"})
print(response)
```

#### Example Response 1:
> **"Based on historical data and the latest news, Apple stock is worth considering, though personal risk tolerance should factor into the decision."**

![](https://fastly.jsdelivr.net/gh/bucketio/img7@main/2025/02/15/1739656292133-5bc8de64-3134-448b-9a17-5a6768ee9967.png)

#### Example Response 2:
> **"Recent news coverage is positive and historical trends show steady upward movement, making this a viable candidate for long-term investment."**

![](https://fastly.jsdelivr.net/gh/bucketio/img12@main/2025/02/15/1739656297603-2af17aa7-b9db-40c6-97b2-00ed934f9cd1.png)

The above example demonstrates a preliminary stock analysis workflow built with **LangChain**. It combines historical data and news to generate basic analytical conclusions. Note that these responses are based solely on the data and context provided in the example and **should not be treated as professional investment advice or final conclusions**. Real investment decisions require more comprehensive data and thorough research.

---

By integrating financial data sources (historical data and news) into an **LLM**, LangChain delivers faster, deeper market insights to support investment decision-making. As model capabilities and data source availability continue to improve, the efficiency and accuracy of investment analysis will only grow further.
