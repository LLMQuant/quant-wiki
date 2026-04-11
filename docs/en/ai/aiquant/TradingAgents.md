![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

# TradingAgents: A Multi-Agent LLM Framework for Financial Trading

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

## Abstract

Recent advances in multi-agent collaboration powered by large language models (LLMs) have yielded impressive results in automated decision-making and problem-solving. In the financial domain, however, most prior work has focused on single-agent approaches to specific trading tasks, or has used multi-agent frameworks merely to collect data independently -- falling short of simulating the collaborative team dynamics found in real-world trading firms. The TradingAgents framework addresses this gap by modeling the organizational structure of professional trading firms through LLM-based agent teams. These teams include agents specializing in fundamental research, sentiment analysis, technical analysis, and trading with varying risk appetites. The framework also features bull and bear researchers to balance market perspectives, along with a dedicated risk management team for exposure monitoring. Under this architecture, the trading agent synthesizes team debates and historical data to make decisions, simulating a realistic collaborative trading environment. Experimental results demonstrate significant improvements in cumulative returns, Sharpe ratio, and maximum drawdown compared to baseline models, validating the potential of multi-agent LLMs in financial trading.

![](https://fastly.jsdelivr.net/gh/bucketio/img18@main/2025/01/18/1737234033648-6cf5f1c2-7345-437d-9fb8-96ed84ee3156.png)

## Introduction

The combination of LLMs with autonomous agents has demonstrated human-like decision-making and workflow replication across many domains (Park et al. [2023]; Havrilla et al. [2024]; Talebirad and Nadiri [2023]; Tang et al. [2024]). By equipping language agents with tools and enabling collaboration with other agents, complex problems can be decomposed into refined subtasks, improving overall problem-solving capabilities. Financial markets -- a highly complex system involving company fundamentals, market sentiment, technical indicators, and macroeconomic events -- represent an ideal application for such multi-agent systems.

Traditional quantitative trading systems typically rely on purely quantitative models and struggle to capture multi-dimensional influences. LLMs, with their efficient natural language processing capabilities, are particularly well-suited for analyzing text-based information such as news, earnings reports, and social media. Furthermore, while deep learning-driven black-box trading strategies often lack interpretability, multi-agent LLM frameworks can provide greater transparency through explicit reasoning processes and evidence chains (Li et al. [2023a]; Wang et al. [2024b]; Yu et al. [2024]).

Despite this promise, current frameworks for applying LLMs in finance face two critical bottlenecks:

1. **Failure to simulate real trading firm structures**: Most multi-agent financial applications focus on narrow tasks (Li et al. [2023a]; Wang et al. [2024b]; Yu et al. [2024]) and do not model the team collaboration and process management found in actual trading firms.

2. **Inefficient communication interfaces**: Many systems rely solely on natural language message logs or unstructured information pools for decision-making (Park et al. [2023]; Qian et al. [2024]). As conversation turns increase, information loss and "cross-talk" effects become more pronounced, making it difficult for agents to maintain consistent context and logical relationships over extended timeframes.

To address these challenges, this paper proposes a new multi-agent trading system. First, it simulates the multi-role, multi-tier collaboration of professional trading firms -- including fundamental analysts, sentiment/news analysts, technical analysts, and bull/bear researchers -- working together on dynamic decisions, with a risk management team monitoring exposure and controlling downside risk. Second, the communication layer employs a hybrid mechanism of structured reports and natural language debates, ensuring rigor and conciseness during information handoffs while enabling multi-round discussions of complex issues in natural language.

The framework is validated through backtesting experiments on historical financial datasets, compared against multiple baseline strategies using cumulative returns, Sharpe ratio, and maximum drawdown as performance metrics. Results confirm the framework's significant advantages in both trading performance and risk control.

---

## Related Work

### LLMs as Financial Assistants

Researchers have fine-tuned general-purpose LLMs on financial corpora, or trained finance-specific LLMs from scratch, to meet professional financial analysis, information retrieval, and decision support needs.

> **Fine-Tuned LLMs for Finance**: Models such as PIXIU (FinMA) (Xie et al. [2023]), FinGPT (Yang, Liu, and Wang [2023]), and Instruct-FinGPT (Zhang, Yang, and Liu [2023]) have been fine-tuned on large volumes of financial domain instructions and data, significantly improving classification and question-answering performance. Some even outperform BloombergGPT (Wu et al. [2023]) in certain scenarios, though they may lag behind GPT-4 on more generative tasks.

> **Finance LLMs Trained from Scratch**: Models such as BloombergGPT (Wu et al. [2023]), XuanYuan 2.0 (Zhang, Yang, and Xu [2023]), and Fin-T5 (Lu et al. [2023]) are jointly pre-trained on massive general and financial text corpora. These models often outperform same-sized general models on financial sentiment classification or summarization, though they may face scale limitations compared to closed-source models like GPT-3 or PaLM (Chowdhery et al. [2022]).

Overall, domain-adapted financial LLMs achieve strong results on specific tasks, highlighting the importance of domain adaptation. Building larger or higher-quality financial datasets remains the key path to further improving these models.

![](https://fastly.jsdelivr.net/gh/bucketio/img7@main/2025/01/18/1737234055721-e826d91a-41f6-4004-88af-b45fd0810e12.png)

> Figure 1: Overview of the TradingAgents framework. I. Analyst team collects market information in parallel; II. Research team debates and evaluates data; III. Trader synthesizes research opinions to make trading decisions; IV. Risk management team monitors risk exposure; V. Fund manager provides final approval and executes trades.

### LLMs as Traders

This line of work treats LLMs as direct trading execution agents, integrating news, earnings reports, and stock price data for automated buy/sell decisions. Three main categories emerge:

> **News-Driven Agents**: Embed news and macroeconomic events into LLM inputs for stock price prediction. Research shows both closed-source models (GPT-3.5, GPT-4) and open-source models (Qwen, Baichuan) can execute long/short strategies based on news sentiment scores (Lopez-Lira and Tang [2023]).

> **Reasoning-Driven Agents**: Enhance reflection and debate mechanisms in trading decisions. FinMem (Yu et al. [2023]) and FinAgent (Zhang et al. [2024b]) employ hierarchical memory extraction on multimodal data, while other work on multi-agent debate mechanisms (Xing [2024]; TradingGPT) allows LLMs with different roles to challenge each other, improving decision quality.

> **Reinforcement Learning-Driven Agents**: Use backtest returns as reward signals for reinforcement learning. For example, SEP (Koa et al. [2024]) uses RL with memory and reflection mechanisms to continuously optimize predictions.

### LLMs for Alpha Factor Mining

LLMs can also generate alpha factors rather than directly executing trades. QuantAgent (Wang et al. [2023]) employs a dual-loop (inner/outer) architecture, while AlphaGPT (Wang et al. [2023]) proposes a human-in-the-loop alpha mining workflow. Such research demonstrates the feasibility of using LLMs to generate and optimize trading strategies or factors.

---

## TradingAgents: Role Specifications

By assigning clear roles and objectives to LLM agents, the complex trading process can be decomposed into manageable subtasks. TradingAgents mirrors real trading firm structures, distributing seven roles across a simulated "trading firm": Fundamentals Analyst, Sentiment Analyst, News Analyst, Technical Analyst, Researcher, Trader, and Risk Manager.

### Analyst Team

The analyst team (Figure 2) consists of four specialized agents covering all facets of market information:

![](https://fastly.jsdelivr.net/gh/bucketio/img6@main/2025/01/18/1737234079367-1d92b86f-c1fd-4858-8dcb-5d7a835d4a1e.png)

> Figure 2: TradingAgents analyst team

- **Fundamental Analyst**: Analyzes financial statements, earnings reports, and insider trading data to assess intrinsic company value and determine whether a stock is under- or overvalued.

- **Sentiment Analyst**: Monitors social media, sentiment scores, and public opinion to predict short-term investor behavior impacts on stock prices.

- **News Analyst**: Tracks macroeconomic indicators, breaking news, and corporate events to identify potentially market-moving developments.

- **Technical Analyst**: Computes technical indicators such as MACD and RSI, analyzes price-volume relationships and chart patterns for timing buy/sell decisions.

### Research Team

The research team (Figure 3) critically evaluates analyst outputs through multi-round debates from opposing perspectives:

![](https://fastly.jsdelivr.net/gh/bucketio/img12@main/2025/01/18/1737234106063-b227bc1d-70c2-4211-aba2-73df9df02669.png)

> Figure 3: TradingAgents research team: Bull and bear perspectives

- **Bullish Researchers**: Emphasize positive aspects and growth potential, providing supportive arguments for long positions.

- **Bearish Researchers**: Highlight potential risks and negative signals, offering counterbalancing "contrarian" viewpoints.

Through this dialectical approach, the research team reaches balanced conclusions on market risk and reward.

### Trader Agent

The trader agent (Figure 4) aggregates analyst and research team inputs, combining quantitative data with sentiment information to make specific buy/sell decisions:

![](https://fastly.jsdelivr.net/gh/bucketio/img17@main/2025/01/18/1737234120399-46e853de-cc49-471c-9956-21ccb91edba6.png)

> Figure 4: TradingAgents trader decision flow

- Evaluates analyst and researcher recommendations
- Determines trading timing and position sizing
- Executes buy/sell orders
- Dynamically adjusts positions

### Risk Management Team

The risk management team (Figure 5) tracks portfolio risk exposure in real-time and ensures trading activities comply with pre-defined risk parameters:

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2025/01/18/1737234141836-9af89d93-289e-4021-9b3b-c51a0f6f1537.png)

> Figure 5: TradingAgents risk management and fund manager approval flow

- Assesses market volatility, liquidity, and counterparty risk
- Executes risk mitigation strategies such as stop-losses or position diversification
- Provides risk feedback and adjustment recommendations to the trader
- Ensures the overall portfolio aligns with the firm's risk appetite

All agents use the ReAct (Yao et al. [2023]) prompting framework, coordinating actions within a shared environment state and engaging in internal debates or tool calls as needed.

---

## TradingAgents: Agent Workflow

### Communication Protocol

Most multi-agent LLM frameworks still rely exclusively on natural language messages for communication. For financial trading tasks requiring long-horizon planning with complex information dimensions, purely natural language "continuous dialogue" tends to suffer from cross-talk or critical information loss.

TradingAgents introduces a **structured communication protocol** inspired by MetaGPT, using clearly defined formats for report transmission. This approach ensures only role-relevant information is read and processed, reducing extraneous messages and minimizing information distortion across conversation rounds.

### Agent Interaction Types

TradingAgents primarily relies on **structured documents** and **brief natural language dialogue** for collaboration:

- **Structured Reports**:
  - Analyst team: Each generates concise research reports containing key metrics, conclusions, and recommendations.
  - Trader: Reviews analyst reports and provides explicit trading signals and rationale, which are then reviewed by the risk management team.

- **Natural Language Discussion**:
  - Research team: Bull and bear researchers review the global state and analyst reports, conduct n rounds of dialogue, and a "moderator" agent summarizes and records the final perspective.
  - Risk management team: Debates trader decisions across different risk preferences (aggressive, neutral, conservative) over n rounds, with a moderator compiling recommendations.
  - Fund manager: Reviews risk management discussions and issues final execution decisions.

### Underlying LLM Models

The framework employs a mix of LLMs optimized for different task complexities:

- **"Fast-thinking" models (e.g., `gpt-4o-mini`, `gpt-4o`)**: Handle summaries, data retrieval, and table-to-text conversions efficiently.
- **"Deep-thinking" models (e.g., `o1-preview`)**: Excel at multi-round reasoning, decision-making, and long-form report generation.

By flexibly swapping different LLMs, TradingAgents can operate in API-only mode without GPUs, while remaining ready to integrate stronger reasoning or domain-specific models in the future.

---

## Experiments

### Backtesting

The framework was backtested on multi-asset, multimodal stock data for Apple, Nvidia, Microsoft, Meta, and Google, with data sources including:

- **Historical stock prices**: OHLCV data from January 1 to March 29, 2024
- **News data**: Daily news from Bloomberg, Yahoo, EODHD, FinnHub, Reddit, and others
- **Social media and sentiment**: Posts from Reddit and X/Twitter with LLM-computed sentiment scores
- **Insider trading and sentiment**: Corporate insider trading information and public filings
- **Financial statements**: Quarterly and annual reports
- **Company profiles and history**: Third-party summaries and historical financial data
- **Technical indicators**: 60+ common indicators including MACD, RSI, and Bollinger Bands

### Simulation Setup

The backtesting period spans January 1 to March 29, 2024. TradingAgents processes only current-day and historical data at each step (preventing look-ahead bias). Based on analysis outputs (buy, sell, or hold), corresponding orders are executed in the simulated environment, with daily returns and risk metrics recorded.

### Baselines

Comparison strategies include:

- **Buy and Hold**: Equal-weight buy-and-hold across all selected stocks.
- **MACD Strategy**: Generates buy/sell signals based on MACD line and signal line crossovers.
- **KDJ + RSI Strategy**: Combines KDJ and RSI indicators for overbought/oversold trading.
- **ZMR (Zero Mean Reversion)**: Trades based on price deviation from and reversion to a baseline.
- **SMA (Simple Moving Average)**: Uses long/short moving average crossovers.

### Evaluation Metrics

1. **Cumulative Return (CR)**

$$
\text{CR} = \left(\frac{V_{\text{end}} - V_{\text{start}}}{V_{\text{start}}}\right)\times 100\%
$$

2. **Annualized Return (AR)**

$$
\text{AR} = \left(\left(\frac{V_{\text{end}}}{V_{\text{start}}}\right)^{\frac{1}{N}} - 1\right)\times 100\%
$$

3. **Sharpe Ratio (SR)**

$$
\text{SR} = \frac{\bar{R} - R_{f}}{\sigma}
$$

4. **Maximum Drawdown (MDD)**

$$
\text{MDD} = \max_{t \in [0,T]} \Bigl(\frac{\text{Peak}_t - \text{Trough}_t}{\text{Peak}_t}\Bigr)\times 100\%
$$

## Results and Analysis

### Performance Comparison

Table 1 shows TradingAgents performance against multiple baseline strategies on AAPL, GOOGL, and AMZN. TradingAgents demonstrates clear advantages across all metrics.

| Categories | Models | **AAPL** |     | **GOOGL** |     | **AMZN** |
| --- | --- | --- | --- | --- | --- | --- |
| CR%↑ | ARR%↑ | SR↑ | MDD%↓ |  | CR%↑ | ARR%↑ | SR↑ | MDD%↓ |  | CR%↑ | ARR%↑ | SR↑ | MDD%↓ |
| Market | B&H | -5.23 | -5.09 | -1.29 | 11.90 |  | 7.78 | 8.09 | 1.35 | 13.04 |  | 17.1 | 17.6 | 3.53 | 3.80 |
| Rule | MACD | -1.49 | -1.48 | -0.81 | 4.53 |  | 6.20 | 6.26 | 2.31 | 1.22 |  | - | - | - | - |
| Based | KDJ&RSI | 2.05 | 2.07 | 1.64 | 1.09 |  | 0.4 | 0.4 | 0.02 | 1.58 |  | -0.77 | -0.76 | -2.25 | 1.08 |
|  | ZMR | 0.57 | 0.57 | 0.17 | 0.86 |  | -0.58 | 0.58 | 2.12 | 2.34 |  | -0.77 | -0.77 | -2.45 | 0.82 |
|  | SMA | -3.2 | -2.97 | -1.72 | 3.67 |  | 6.23 | 6.43 | 2.12 | 2.34 |  | 11.01 | 11.6 | 2.22 | 3.97 |
|  | TradingAgents | **26.62** | **30.5** | **8.21** | **0.91** |  | **24.36** | **27.58** | **6.39** | **1.69** |  | **23.21** | **24.90** | **5.60** | **2.11** |
|  | Improvement(%) | +24.57 | +28.43 | +6.57 | - |  | +16.58 | +19.49 | +4.26 | - |  | +6.10 | +7.30 | +2.07 | - |

#### Cumulative and Annualized Returns

TradingAgents achieves **at least 23.21% cumulative returns** and **24.90% annualized returns** across all three stocks, exceeding baselines by **over 6.1%**. On the volatile AAPL, it achieved **over 26%** returns in under three months.

![](https://fastly.jsdelivr.net/gh/bucketio/img8@main/2025/01/18/1737234726980-6d6ef67a-ac90-4fae-9780-eb6017ad9f78.png)

> (a) Cumulative return comparison for AAPL

![](https://fastly.jsdelivr.net/gh/bucketio/img1@main/2025/01/18/1737234738834-2023dd7d-baab-464e-9938-14ef7d78b3b7.png)

> (b) TradingAgents trade execution points on AAPL. Green/red arrows indicate long/short entries.

#### Sharpe Ratio

TradingAgents achieves Sharpe ratios of **5.60 or higher** across all stocks, exceeding the next-best strategy by **at least 2.07**, indicating superior risk-adjusted returns.

#### Maximum Drawdown

While rule-based strategies tend to have lower drawdowns, their returns are generally weak. TradingAgents, through multi-agent debates and risk management oversight, captures market opportunities while keeping maximum drawdown around 2, avoiding excessive risk-taking.

#### Interpretability

Unlike most deep learning trading models that function as "black boxes," multi-agent LLMs offer significantly greater interpretability. Operations and reasoning are expressed in natural language, facilitating understanding, debugging, and targeted adjustments. The appendix includes a complete daily log of TradingAgents' tool calls, reasoning, and decision execution.

### Discussion

Results demonstrate that role-based division of labor, mutual debate, and collaborative decision-making significantly enhance trading performance. Multi-source data and expert perspectives complement each other, enabling more comprehensive decisions. The risk management team provides timely constraints and optimization, while the natural language reasoning process ensures strong interpretability and auditability -- a critical requirement in financial practice.

---

## Conclusion

The TradingAgents framework simulates a multi-role, multi-tier collaborative environment resembling a real trading firm. Each LLM agent specializes in analyzing a specific dimension or assuming a particular responsibility, exchanging information and making decisions through multi-round dialogue and structured reports. In backtesting experiments, TradingAgents significantly outperforms multiple baselines on cumulative returns, Sharpe ratio, and maximum drawdown. Future work will focus on live deployment, expanding role types and task scopes, and integrating real-time data processing capabilities.

## About LLMQuant

LLMQuant is a cutting-edge community of researchers and practitioners from the world's top universities and quantitative finance firms, dedicated to exploring the intersection of artificial intelligence (AI) and quantitative finance (Quant). Our team members hail from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other leading institutions, with advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and top proprietary trading firms.
