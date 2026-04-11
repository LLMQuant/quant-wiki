![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

# InvestorBench: A Benchmark for LLM-Based Financial Decision-Making

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

Recent research has demonstrated that large language model (LLM)-based agents exhibit strong decision-making capabilities in complex, open-ended environments spanning multiple application scenarios, including financial trading (Zhang et al. (2024b); Guo et al. (2024); Eigner and Handler (2024); Wang et al. (2024)). However, building a multimodal LLM agent framework that can adapt to diverse financial tasks remains a significant challenge. This difficulty stems primarily from the high volatility and heterogeneity of financial markets: agents must capture time-sensitive core trading signals while continuously making high-quality decisions amid mixed information modalities and rapidly changing conditions.

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2025/01/18/1737237784124-94217376-4d7d-4a1c-a81e-660bd7bffe4f.png)
> **Figure 1: Overall architecture of the InvestorBench framework.**

Moreover, as application scenarios extend from single-asset trading to multiple financial tasks, the factors influencing decisions grow increasingly complex. For example, individual stock trading requires close attention to company- and sector-level fundamentals and earnings data (Yi et al. (2022)), while cryptocurrency trading is more heavily driven by real-time news and market sentiment (Bhatnagar et al. (2023)). ETF investing, by contrast, tends to focus on long-term asset allocation and passive investment strategies (Madhavan (2016)).

Although several LLM agent frameworks have recently emerged for specific financial scenarios -- such as **FinMem** (Yu et al. (2024a)), **FinAgent** (Zhang et al. (2024a)), **CryptoTrade** (Li et al. (2024)), **FinRobot** (Yang et al. (2024)), and **FinCon** (Yu et al. (2024b)) -- these solutions typically focus on a single task or a narrow subset, and most rely on proprietary data, making cross-comparison difficult. There is therefore an urgent need for an **open, multi-task benchmark** that can uniformly evaluate LLM agent performance across different financial decision-making tasks and facilitate fair comparison of multimodal data and different models.

![](https://fastly.jsdelivr.net/gh/bucketio/img1@main/2025/01/19/1737284464992-0582404b-c648-4999-bb22-4645fb092cd3.png)

To address this gap, we propose **InvestorBench**: an open-source benchmark system for **diverse financial decision-making tasks**. The framework extends the layered memory architecture of FinMem (Yu et al. (2024a)), covering three core domains -- stock trading, cryptocurrency trading, and ETF investing -- with multi-source data environments. Compared to traditional similarity-based retrieval methods (e.g., FinAgent), FinMem-style layered memory with multi-rate decay enables LLM agents to more effectively integrate and weigh information across multiple time scales and modalities, reinforcing critical long-term knowledge while responding to short-term trading signals in real time. InvestorBench also provides multiple data sources and evaluation metrics, creating a **unified and extensible** evaluation platform for researchers and practitioners.

> **Our key contributions:**
>
> 1. We establish **InvestorBench** -- the first LLM financial decision-making benchmark featuring multi-task and multimodal data sources, designed to evaluate LLM agent reasoning and sequential decision-making capabilities in complex, open-ended financial scenarios.
> 2. We provide **open multi-source financial environments** (stocks, cryptocurrencies, ETFs) along with relevant APIs and data repositories, ensuring reproducibility and extensibility.
> 3. We propose a **unified and flexible** LLM-Agent framework in which different LLMs can be easily swapped in as the core reasoning engine. In this study, we test **13 models**, including general-purpose LLMs and finance-specific fine-tuned LLMs, systematically evaluating their performance across three financial decision-making tasks.

---

## Introduction

Large language models (LLMs) have achieved remarkable results in decision-making tasks across many complex scenarios (Zhang et al. (2024b); Guo et al. (2024); Eigner and Handler (2024); Wang et al. (2024)). However, applying them to the **financial domain** remains challenging: financial markets are highly volatile, noisy, and time-sensitive, with rich data types (numerical, textual, macroeconomic indicators, sentiment analysis, etc.). Agents must capture information under partially observable conditions (POMDP) and make high-quality decisions continuously (Bertsekas and Shreve (1996); Liu et al. (2020); Kabbani and Duman (2022)).

> **Designing multi-task financial agents is even harder:**
> Different financial products have different priorities -- stocks demand sector-level earnings reports and fundamentals; cryptocurrencies are highly sensitive to real-time news and sentiment; ETFs emphasize long-term portfolio costs and allocation strategies. Uniformly evaluating LLM agent adaptability and decision quality across these different tasks has become a key research need.

Recent LLM multi-agent frameworks for finance -- such as FinMem, FinAgent, CryptoTrade, FinRobot, and FinCon -- offer different approaches for specific scenarios:

- **FinRobot** focuses on market analysis;
- **FinMem** and **FinAgent** primarily target stock/ETF trading;
- **CryptoTrade** covers only cryptocurrencies;
- **FinCon** addresses multi-asset portfolio management but is limited to a small number of stocks.

> **Limitation:** Most frameworks target only a limited set of financial decision-making tasks and lack generality; they frequently rely on proprietary data, creating obstacles for subsequent evaluation and reproducibility.

**InvestorBench** was proposed against this backdrop. Building on FinMem's "layered memory + multi-rate decay" foundation, it introduces multiple financial market environments to uniformly assess LLM-Agent performance in multi-task decision-making. Key features include:

- **Layered memory**: Unlike FinAgent's pure text similarity retrieval, InvestorBench inherits FinMem's layered memory structure with differentiated decay rates across layers, ensuring balance between time-sensitivity and long-term retention;
- **Three core tasks**: Stock trading, cryptocurrency trading, and ETF investing;
- **Open multimodal data sources**: Covering market data, news, company filings, sentiment, macroeconomic data, and more.

### Summary

1. We propose **InvestorBench**, an open benchmark for multi-task LLM evaluation in complex, open-ended financial scenarios;
2. We provide multi-source real data environments that can be combined with any LLM-agent design;
3. We systematically test **13 LLMs** (including closed-source, open-source, and finance-fine-tuned models), demonstrating their performance differences in financial sequential decision-making.

---

## LLM Trading Agents

In this section, we introduce the LLM agent framework provided by InvestorBench and formalize the financial decision-making task using a **Partially Observable Markov Decision Process (POMDP)** (Bertsekas and Shreve (1996); Liu et al. (2020); Kabbani and Duman (2022)).

### 2.1 Definitions

The LLM agent in **InvestorBench** comprises several sub-modules designed to simulate or surpass the research capabilities of professional investors:

- **Brain/Backbone (LLM core)**: The agent's core, responsible for understanding and generating natural language, supporting complex reasoning and interpretation of market information (e.g., making price forecasts, reviewing past performance).
- **Perception**: A sensing module that converts raw market data (numerical, textual, visual, etc.) into structured formats suitable for LLM processing.
- **Profile**: Role and task context descriptions.
  - Role: Set as a senior investor with a dynamic risk preference (e.g., more aggressive when market trends are favorable, more conservative otherwise).
  - Task context: Key information about the target asset (historical trends, sector overview, product characteristics, etc.).
- **Memory**: A module for storing and retrieving historical market information and reasoning experiences.
  - **Working Memory**: Handles current observations, summaries, and immediate reflections;
  - **Layered Long-term Memory**: Uses a multi-layer structure with different decay rates to distinguish and manage long-, medium-, and short-term information priorities.
- **Action**: Executes specific trading instructions, selecting "Buy," "Sell," or "Hold" based on LLM output, incorporating profit/loss records and risk feedback to inform subsequent decisions.

### 2.2 Financial Decision-Making Formulation

Financial trading is modeled as an **infinite-horizon POMDP** with time index $ \mathbb{T} = \{0,1,2,\dots\} $ and discount factor $ \alpha \in (0,1] $.

- **State space**: $ \mathcal{X} \times \mathcal{Y} $, where $ \mathcal{X} $ is the observable portion (e.g., market prices) and $ \mathcal{Y} $ is unobservable (e.g., market psychology).
- **Action space**: $ \mathcal{A} $, i.e., $ \{\text{Buy}, \text{Sell}, \text{Hold}\} $.
- **Reward function**: $ \mathcal{R}(o,b,a) $, directly using daily profit and loss (PnL).
- **Observation process**: $ \{O_t\} \subseteq \mathcal{X} $; **Reflection process**: $ \{B_t\} \subseteq \mathcal{Y} $, representing the LLM agent's self-review and reasoning.
- **Policy**: $ A_t \sim \pi(\cdot|\text{prompt}) $, where the LLM treats the prompt as a condition and outputs trading instructions.

Let $ R_t^\pi = \mathcal{R}(O_t, B_t, A_t) $ be the reward at time $t$. The objective function for financial decision-making is:

$$
\max_{\pi \in \Pi} \;\mathbb{E}\Biggl[\sum_{t \in \mathbb{T}} \alpha^t \,R_t^\pi\Biggr].
$$

---

## InvestorBench

We now describe the overall design of the InvestorBench framework, as illustrated in Figure 1.

### 3.1 Benchmark Components

InvestorBench consists of four major components:

1. **Data sources and market environments**: Integrates open-source data and third-party APIs (e.g., Yahoo Finance, SEC EDGAR) to build a multimodal market data repository.
2. **LLM Agent**: Equipped with Brain, Perception, Profile, Memory, and Action sub-modules, with access to external tools (table parsing, API calls, etc.) for data operations (vector database management, information augmentation and retrieval).
3. **Financial decision-making tasks**: Provides trading scenarios for three asset types (stocks, cryptocurrencies, ETFs).
4. **Evaluation metrics**: Uses standard quantitative finance metrics (e.g., Cumulative Return (CR), Sharpe Ratio (SR)) to assess LLM agent performance.

### 3.2 Trading Environments

We construct three open datasets -- one for each task type (stocks, cryptocurrencies, ETFs) -- aiming to provide comprehensive market-data-news-sentiment evaluation environments.

1. **Stock Environment**
   - **OHLCV**: Daily open, high, low, close, and volume data from Yahoo Finance.
   - **Company filings**: 10-Q, 10-K reports downloaded from SEC EDGAR.
   - **News**: Daily news for 7 stocks collected from 2020-07-01 to 2021-05-06. Some data comes from Zhou et al. (2021); Tesla and Apple news comes from Refinitiv Real-Time News.
   - **Sentiment**: News text classified as positive/negative/neutral using *gpt-3.5-turbo-0125*.

2. **Cryptocurrency Environment**
   - **OHLCV** data from CoinMarketCap.
   - **Multi-source crypto news** from cryptonews, cryptopotato, cointelegraph (Vanhoucke (2023)), and an additional dataset from Zhou et al. (2021).
   - **Sentiment** also generated by *gpt-3.5-turbo-0125*.

3. **ETF Environment**
   - Based on the **NIFTY** dataset (Saqur et al. (2024)), containing ETF-related news headlines and corresponding sentiment labels from 2019-07-29 to 2020-09-21.

During backtesting, data is split by date -- agents build their memory databases during a "warm-up" period, and final performance is evaluated during the test period.

### 3.3 Evaluation Metrics

We employ four standard metrics: **Cumulative Return (CR)**, **Sharpe Ratio (SR)**, **Annualized Volatility (AV)**, and **Maximum Drawdown (MDD)**. CR and SR are considered the primary metrics: CR reflects long-term return levels, and SR measures the risk-adjusted return.
> **Table 1** lists the 13 LLMs tested in InvestorBench, including closed-source API models, open-source models, and finance-specific fine-tuned models.

---

## Experiments and Results

We test three single-asset trading scenarios (stocks, cryptocurrencies, ETFs), comparing open-source models, closed-source models, and finance-specific models. To ensure fairness, we standardize experimental settings and evaluation metrics, running multiple repeated experiments for each model within the corresponding backtesting period and reporting median metrics.

### 4.1 Experimental Setup

- **Baseline strategy**: Buy & Hold for stocks and cryptocurrencies; the same approach or an equal-weight portfolio for ETFs.
- **Temperature parameter**: Uniformly set to 0.6 for the LLM-Agent system, balancing consistency and creativity.
- **Backtesting periods**:
  - **Stocks**: Warm-up 2020-07-01 to 2020-09-30; test 2020-10-01 to 2021-05-06;
  - **Cryptocurrencies**: Warm-up 2023-02-11 to 2023-04-04; test 2023-04-05 to 2023-11-05;
  - **ETFs**: Warm-up 2019-07-29 to 2019-12-30; test 2020-01-02 to 2020-09-21.
- **Model deployment**: Built on vllm; models under 10B parameters deployed on 2x RTX A6000 GPUs; mid-size models (10-65B) on 4x RTX A6000; models over 65B on 8x A100 80GB.

### 4.2 Result 1: Stock Trading

> **Table 2** presents the trading performance of 13 models across 7 stocks along with averages. Figures 3(a) and 3(b) provide further visual comparisons by category and parameter scale. Key findings:

1. **Closed-source models perform better in stock trading**
   > Compared to open-source or finance-fine-tuned models, closed-source models (e.g., GPT-4 family, GPT-o1-preview) show significantly higher and more stable CR and SR. This suggests that although some models have been fine-tuned on financial text (e.g., Palmyra-Fin-70B), they do not hold a clear advantage in sequential trading decision scenarios -- possibly because their fine-tuning focuses on long-text comprehension rather than reinforcement of sequential decision-making.

2. **Larger parameter counts significantly improve reasoning and robustness**
   > Among open-source models, those exceeding 67B parameters achieve higher average CR and SR with lower variance than smaller models (see Figure 3(b)). This aligns with the well-established finding that LLM reasoning capability scales with parameters, which holds for highly uncertain stock trading tasks as well.

3. **Closed-source LLMs hold a greater advantage in volatile, signal-mixed market environments**
   > During the test period, TSLA and NIO experienced severe price swings with mixed bullish and bearish signals; other assets were predominantly in uptrends. Closed-source models demonstrated a superior ability to synthesize historical momentum, position status, and self-reflection when dealing with volatile assets, yielding more accurate decisions. Large open-source models also showed some adaptability but were comparatively less effective.

### 4.3 Results 2 & 3: Cryptocurrency and ETF Trading

In cryptocurrency and ETF trading scenarios, market trends also exhibited **mixed bullish/sideways** patterns. Cryptocurrency volatility was relatively lower, while ETFs showed more pronounced price swings. Key observations:

1. **Capturing cryptocurrency trading signals requires large-scale open-source or closed-source LLMs**
   > As shown in Table 3, small-to-medium open-source models generally underperformed the Buy & Hold baseline on both CR and SR, indicating that for this highly sensitive, sentiment-driven market, LLMs need sufficient reasoning complexity to keep pace.

2. **ETF investing relies more heavily on powerful, broadly pre-trained models**
   > Table 4 shows that closed-source models substantially outperform others across multiple ETF metrics. This likely reflects the fact that ETF trading typically requires cross-sector macroeconomic reasoning and long-term strategic thinking; models without extensive pre-training knowledge struggle to identify key signals.

### 4.4 Discussion

Overall, LLM performance varies significantly across asset classes, reflecting both financial market complexity and the importance of **model selection and fine-tuning**. In general, **closed-source LLMs** exhibit stronger reasoning capabilities across stocks and ETFs, owing to their massive training scale and parameter richness. **Open-source models** must either scale up further or undergo reinforcement fine-tuning for sequential decision-making to compete. Additionally, whether an LLM-Agent can flexibly "remember" historical states and perform dynamic risk assessment significantly affects its robustness across different market environments. Layered memory and risk-adaptive designs prove valuable for complex scenarios.

---

## Related Work

### 5.1 Large Language Models in Finance

Rapid advances in general-purpose language models have spurred research into **finance-specific models** such as FinBERT (Liu et al. (2021); Yang et al. (2020)), FinGPT (Liu et al. (2023)), FinMA (Xie et al. (2023)), and BloombergGPT (Wu et al. (2023)). These models are pre-trained or fine-tuned on large-scale financial data to accommodate domain-specific terminology and task requirements. The rise of LLMs has also driven the adoption of **multi-agent financial systems** for trading and investment research, such as FinMem (Yu et al. (2024a)) and FinAgent (Zhang et al. (2024a)). However, significant differences in task scope and data types across frameworks mean that comprehensive evaluation of these LLM-Agents still lacks a unified standard.

### 5.2 Financial LLM Benchmarks

Existing benchmarks for financial NLP -- such as **FLUE** (Shah et al. (2022)), covering sentiment analysis, news classification, and entity recognition among five tasks; **Pixiu** (Xie et al. (2023)); and **FinBen** (Xie et al. (2024)), which extend to multimodal and document understanding -- primarily focus on **static NLP tasks** and have not yet evaluated **LLM agents in real-time trading and sequential decision-making** scenarios. InvestorBench addresses this gap by focusing on **dynamic, multi-step decision-making** evaluation.

---

## Conclusion

**InvestorBench** offers researchers two primary modes of use:

1. **Mode 1**: Plug your own or fine-tuned LLM into InvestorBench's agent framework for multi-task decision-making and compare against our baseline model results;
2. **Mode 2**: Directly invoke InvestorBench's environments and evaluation interfaces, integrating them into custom agent designs to compare the effectiveness of different agent architectures.
This provides a flexible platform for in-depth exploration of LLM financial decision-making capabilities in diverse real-world environments.

> **Outlook**: In the future, we plan to expand to richer data modalities (e.g., audio earnings calls, candlestick chart images) while maintaining framework usability, and to explore applications in multi-asset portfolio management and longer time horizons.

---

## Limitations

1. **InvestorBench** currently focuses on single-asset decision-making tasks and does not yet cover multi-asset portfolio management;
2. Due to copyright restrictions, some data quality may be limited, potentially affecting model evaluation.

## About LLMQuant

LLMQuant is a cutting-edge community composed of researchers from top universities and quantitative finance professionals worldwide, dedicated to exploring the intersection of artificial intelligence (AI) and quantitative finance (Quant). Our team members come from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other leading institutions, with external advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and top proprietary trading firms.
