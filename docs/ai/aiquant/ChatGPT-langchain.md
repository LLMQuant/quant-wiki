![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

# ChatGPT也能做投资分析？手把手教你利用 LangChain搭建股票研究框架
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)


投资分析师正越来越多地将人工智能应用于财务数据的处理、趋势识别以及深度洞察的获取。其中，**LangChain** 作为一个极具潜力的开源框架，能够将像 GPT 这样的语言模型与投资分析相结合。本篇文章将探讨如何利用 LangChain 简化初步的投资研究流程，包括**整合金融数据源**、**构建高级定制模型**，以及基于预测性洞察做出更明智的**投资决策**。

在这篇文章中，我们将重点讨论：

> 1. 为什么选择 LangChain？  
> 2. 什么是 LangChain？  
> 3. LangChain 的核心组件  
> 4. 如何利用 LangChain 与 OpenAI 在 Python 中进行股票分析  

## 为什么选择 LangChain？
让我们先尝试让 ChatGPT 分析过去 5 年 NIFTY50 指数的价格表现：

![](https://fastly.jsdelivr.net/gh/bucketio/img1@main/2025/02/15/1739656021954-842a89c6-5f12-4a7a-827b-082257fc13e7.png)


> **“当我们询问 ChatGPT 关于 NIFTY50 过去 5 年的表现时，它并没有现成的数据可用于分析。”**

这正是 **LangChain** 大显身手的地方。LangChain 能够将金融数据源与大型语言模型（LLM）相结合，从而改变投资者对市场数据的分析与解读方式。通过分析庞大的文本数据（如新闻报道、财报以及社交媒体舆情），LangChain 能够为分析师提供更丰富、更及时的洞察，辅助更优的投资决策。

## 什么是 LangChain？
LangChain 充当大型语言模型与外部数据源之间的接口，帮助用户构建 **AI 驱动的应用**。LangChain 允许开发者连接到各种数据库、检索所需信息、处理输入并输出结构化的结果。

![](https://fastly.jsdelivr.net/gh/bucketio/img19@main/2025/02/15/1739656034346-533c4045-ea5a-4aac-9c0c-fc97eb728621.png)


> “LLM（大型语言模型）是基于海量数据训练的深度学习模型，能够根据用户的查询生成回答。LangChain 提供了相应的工具和抽象层，以提升模型输出的定制化、准确性和相关性。”
> “LangChain 支持多种主流 LLM 模型，具体列表可查看：[https://python.langchain.com/docs/integrations/llms/](https://python.langchain.com/docs/integrations/llms/)。”

## LangChain 的核心组件
在接下来的示例中，我们将演示如何在 Python 中实现 LangChain 的主要组件。

![](https://fastly.jsdelivr.net/gh/bucketio/img3@main/2025/02/15/1739656041606-31207779-b15e-4465-b329-c084e05150c4.png)

> **注：下文示例中部分代码使用的 langchain_openai 版本如文中所示。**

![](https://fastly.jsdelivr.net/gh/bucketio/img18@main/2025/02/15/1739656100104-857e381f-88f8-4102-99e7-98381a1ba038.png)

### 1. 使用 LLMs
LangChain 可以通过 **Prompting** 机制集成多个大型语言模型，根据特定任务或查询生成更为复杂且针对性的回答。
![](https://fastly.jsdelivr.net/gh/bucketio/img15@main/2025/02/15/1739656110396-a8674285-0267-4917-946d-cba8c90867b2.png)
- **Temperature**：表示模型输出的随机度。如果将其设为 0，就会得到确定性的输出，也就是在多次运行时输出相同的结果。

**示例输出：**

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2025/02/15/1739656120414-4048f53d-2c01-4f8f-80d2-a72e7b3aeae4.png)


> **“由于输出包含多个元素，我们对其中的 content 部分更感兴趣，所以可以通过相应方法提取内容。”**

### 2. Prompt Templates
Prompt 模板是为 GPT-4 等语言模型生成提示（Prompt）时所使用的 **预定义结构或格式**。它能帮助我们在不同场景下快速构造一致、上下文相关的查询或指令。Prompt 模板中还可以包含动态插入的占位符，用以传递特定数据或参数。


![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2025/02/15/1739656145141-983ccd3b-1bd6-4836-a849-34bbffa730a0.png)


### 3. Chains
在 LangChain 中，“链”指的是一系列有序的步骤或操作，通过将 Prompt、数据处理步骤、API 调用等环节串联起来，完成更为复杂的自然语言处理任务。  
> **“chain = prompt | llm”**  
表示将 prompt（提示）输入到语言模型（LLM），再生成相应回答。

![](https://fastly.jsdelivr.net/gh/bucketio/img7@main/2025/02/15/1739656160804-ab734299-fdf2-48d9-bc4f-525efdcd48be.png)

- 批量处理（Batch）：指一次性向链中输入多条数据并并行处理，从而提升效率。

![](https://fastly.jsdelivr.net/gh/bucketio/img7@main/2025/02/15/1739656167462-5c38f475-0dee-4285-98ef-ce7d1d3523b6.png)

### 4. Agents
**Agent（代理）** 是利用大型语言模型来完成某个特定任务的自动化实体。它可以做决策、执行动作，并能根据设计需求与多种数据源或 API 动态交互。  
在下面的例子中，**PythonREPLTool()** 作为 Agent 的工具被用来在 LangChain 流程中直接运行 Python 代码，用于数据的处理、分析或计算。

> **提示：** 下面示例的 LangChain 版本为 “langchain-core<0.2”。

![](https://fastly.jsdelivr.net/gh/bucketio/img6@main/2025/02/15/1739656174967-f3151ffb-1663-4ad9-a0d7-2a411b5bc85e.png)


![](https://fastly.jsdelivr.net/gh/bucketio/img17@main/2025/02/15/1739656182025-0bdc16cc-55a1-49c3-9899-1af7be302c07.png)

## 使用 LangChain 和 OpenAI 进行股权分析（Python 案例）
接下来，我们将基于 LLM（大型语言模型）构建一个简单的应用，用来判断某个股票是否值得投资。该应用主要使用以下数据源：

- **Google 新闻**  
- **股票的历史价格数据**  
- **ChatGPT Agent** 通过整合这些数据进行综合判断并生成回答

在这个示例中，我们将用到 **agents** 来生成回答。你也可以使用 **function calling** 的方式，让输出更加结构化。

### 1. 准备工作
- 需要有一个 **OpenAI API Key**（可在 OpenAI 官网注册并购买后获取）。  
- 需要有一个 **SERP API Key**（访问 [SERPAPI](https://serpapi.com/) 获取），用来获取某只股票的最新新闻。





### 2. 导入库
在开始之前，先确保安装了适当版本的 **Pydantic** 库。

![](https://fastly.jsdelivr.net/gh/bucketio/img2@main/2025/02/15/1739656196722-23e2cba2-08cb-45dc-a34b-a1cb530fe7a8.png)




```python
# 安装 pydantic
!pip install pydantic==<相应版本>
```

然后导入需要的其它库和模块：
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
# ... 其它必要的导入
```

LangChain 提供了 `langChain_core.tools` 来定义和管理可被 Agents 使用的工具（Tools），这些工具可以执行特定任务，如计算、数据库查询、网络搜索或 API 调用。  
`langchain.agents` 则提供了构建和运行 Agents 的框架，使其能够进行推理、决策并调用工具来完成工作。  
`langchain_core.prompts` 用于设计、管理 Prompt，以指导语言模型如何响应。



### 3. 获取最新新闻
下面定义一个函数 `get_news`，通过 **SERP API** 获取目标股票的最新新闻。将其中的 “YOUR_SERPAPI_API_KEY” 替换为你的实际 API Key：
![](https://fastly.jsdelivr.net/gh/bucketio/img5@main/2025/02/15/1739656224205-d0288dfd-e4f6-4726-a82e-e6ac63d3700a.png)

```python
def get_news(ticker: str) -> str:
    # 通过SERP API获取新闻的示例代码
    ...
```

### 4. 获取历史股价数据
通过 **Yahoo Finance** 获取近一年的历史股价信息：

```python
def get_historical_data(ticker: str) -> str:
    # 使用 yfinance 库获取股票的历史价格数据
    ...
```

![](https://fastly.jsdelivr.net/gh/bucketio/img3@main/2025/02/15/1739656233507-63ea62a3-7096-4d48-bc62-115d2045df62.png)

### 5. 自定义分析函数
定义一个函数 `analyze_stock` 来决定是否值得投资。这个函数会根据一定的规则（如数据表现、新闻内容等）给出分析建议：

![](https://fastly.jsdelivr.net/gh/bucketio/img6@main/2025/02/15/1739656242065-6179ba65-adf0-44b0-a9cd-54109ca463c8.png)

```python
def analyze_stock(news: str, historical_data: str) -> str:
    # 根据自定义逻辑进行分析
    ...
```

### 6. 定义工具
将以上三个函数分别定义为三个 **Tool**：`get_news`、`get_historical_data` 和 `analyze_stock`，方便在后续的 Agent 中调用：

```python
tools = [
    Tool(
        name="get_news",
        func=get_news,
        description="获取目标股票的最新新闻"
    ),
    Tool(
        name="get_historical_data",
        func=get_historical_data,
        description="获取目标股票的历史价格信息"
    ),
    Tool(
        name="analyze_stock",
        func=analyze_stock,
        description="分析股票是否值得投资"
    )
]
```

![](https://fastly.jsdelivr.net/gh/bucketio/img13@main/2025/02/15/1739656261255-d1e1ff87-d07a-400a-8ca3-43e07d158c53.png)


### 7. 定义 Prompt

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2025/02/15/1739656271042-0aed56ef-505b-4812-a51b-6254c39eea96.png)

```python
prompt_template = PromptTemplate(
    input_variables=["ticker"],
    template="""
        我想要分析股票 {ticker} 的投资价值。 
        你可以使用以下工具：
        1. get_news：获取新闻
        2. get_historical_data：获取历史价格
        3. analyze_stock：综合分析
        请给出最终的结论。
    """
)
```

![](https://fastly.jsdelivr.net/gh/bucketio/img13@main/2025/02/15/1739656278953-0c1fbbee-33e9-4576-915b-a92eff5e3d43.png)


### 8. 创建 Agent 并生成结果
最后，我们创建一个 Agent 来生成对指定股票的分析结果：

![](https://fastly.jsdelivr.net/gh/bucketio/img8@main/2025/02/15/1739656284236-f89caa6d-eb5d-4f3c-a709-384b3d2d0960.png)


```python
agent = initialize_agent(
    tools=tools,
    llm=OpenAI(temperature=0),
    prompt=prompt_template,
    # 其它所需参数
)

response = agent.run({"ticker": "AAPL"})
print(response)
```

#### 示例回复 1：
> **“根据历史数据和最新新闻，可以考虑苹果股票，但仍需结合个人风险偏好。”**

![](https://fastly.jsdelivr.net/gh/bucketio/img7@main/2025/02/15/1739656292133-5bc8de64-3134-448b-9a17-5a6768ee9967.png)

#### 示例回复 2：
> **“近期新闻表现积极，历史趋势稳中有升，可作为长期投资的参考。”**


![](https://fastly.jsdelivr.net/gh/bucketio/img12@main/2025/02/15/1739656297603-2af17aa7-b9db-40c6-97b2-00ed934f9cd1.png)

以上示例展示了一个基于 **LangChain** 的初步股票分析流程。它结合了历史数据与新闻信息来生成简单的分析结论。需要注意的是，这些回答仅基于示例中提供的数据和上下文，**不应视为专业的投资建议或最终结论**。在真实投资中，仍需结合更多数据并进行更全面的研究。

---

通过将财务数据源（历史数据与新闻）整合到 **LLM** 中，LangChain 能够提供更快、更具深度的市场洞察，为投资决策提供支持。未来，随着模型能力与数据源数量的不断提升，投资分析的效率和准确性也有望进一步提高。









