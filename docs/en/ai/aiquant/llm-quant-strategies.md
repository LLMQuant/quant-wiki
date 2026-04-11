![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

This article introduces a novel quantitative investment framework that leverages **large language models (LLMs)** and **multi-agent** collaboration to discover and optimize Alpha factors for stock investment strategies. The approach mines diversified Alpha sets from multimodal financial data (earnings reports, prices, news, charts), then dynamically evaluates and selects the best-performing factors through a multi-agent mechanism based on real-time market conditions -- ultimately constructing more adaptive and robust portfolios.

![](https://fastly.jsdelivr.net/gh/bucketio/img1@main/2025/02/01/1738398298801-307d1f4e-f7b3-498f-a775-a46708bb30c0.png)

---

## 1. Introduction

### 1.1 Background and Motivation

Deep learning has achieved notable progress in financial trading prediction, with many researchers and practitioners working to develop more stable and reliable quantitative investment models. However, current models often exhibit inconsistent performance across different market regimes, with predictive power degraded by noisy data and market volatility. Furthermore, real-world trading involves diverse data modalities (text, charts, financial indicators, etc.), making the effective integration and distillation of these information sources a central challenge in quantitative investing.

> The **core idea** of our proposed framework:
> **(1) Large language models (LLMs)** provide powerful information extraction and reasoning capabilities, automatically generating and screening diverse Alpha factors;
> **(2) A multi-agent system** dynamically assesses market conditions, enabling adaptive reweighting and combination of strategies in constantly changing environments.

### 1.2 Key Challenges in Alpha Mining

1. **Rigidity of traditional methods**: Many Alpha mining approaches rely on heuristic or experience-based rules that struggle to adapt quickly to different market regimes;
2. **Multi-source data integration**: Financial markets generate information far beyond prices and financial indicators -- news, social media sentiment, and economic data all play roles;
3. **Market regime changes**: A high-performing Alpha in one market environment may fail in another; capturing and adapting to structural market shifts is critical.

### 1.3 Framework Overview

To address these challenges, we propose a solution that unifies LLM exploration, multi-agent selection, and dynamic strategy reweighting.
- **LLM-generated Alpha**: Extracts seed Alpha factors from multimodal sources including academic papers, financial literature, financial data, and visual charts;
- **Multi-agent system**: Screens, validates, and assigns confidence scores to these Alphas under different risk preferences and market scenarios;
- **Dynamic reweighting**: Uses deep neural networks or other learning methods to automatically adjust each Alpha's weight in the final investment strategy based on market state.

> We conducted extensive empirical testing on the China A-share market (using the SSE 50 index), demonstrating superior performance across multiple metrics compared to traditional methods and state-of-the-art baselines.

---

## 2. Problem Formulation

### 2.1 Alpha Factors and Portfolio Strategy

In quantitative investing, we typically compute multiple Alpha factors for a selected universe of n stocks at each trading day or interval.

$\alpha = \sum_i w_i \alpha_i$

where $\alpha_i$ denotes a seed Alpha factor and $w_i$ is its weight in the final portfolio. Our objective is to identify the optimal factor combination for the current market regime through historical backtesting and real-time market assessment, dynamically allocating weights accordingly.

### 2.2 Seed Alpha Mining and Selection

Traditional Alpha mining often relies on static rules or expert experience, making it ill-equipped for sudden environmental changes or the challenge of processing massive multi-source data. To address this, we leverage the exploratory capacity of LLMs combined with a multi-agent system:
1. **LLM auto-generation**: Mining potential formulaic Alphas from academic papers, earnings reports, news, and other multimodal data;
2. **Rigorous multi-agent evaluation**: Backtesting and market-adaptability assessment, with confidence scores $\theta$ assigned to each factor;
3. **Categorization**: Organizing Alpha factors into independent categories such as momentum, mean reversion, volatility, and fundamentals for structured selection and combination.

### 2.3 Alpha Formulation

We require LLM-generated seed Alphas to take "interpretable formulaic form," including:
- **Cross-sectional operators** (e.g., addition, logarithm, and other short-term operations);
- **Time-series operators** (requiring multi-day data, such as moving averages, delays, etc.).

---

## 3. Methodology

Our overall approach consists of three main modules: **(1) Seed Alpha Factory**, **(2) Multimodal Multi-Agent Evaluation**, and **(3) Dynamic Weight Optimization**.

### 3.1 Framework Overview

1. **LLM Seed Alpha Factory**:
   - Filters and classifies multimodal literature, charts, and financial data through an LLM, outputting a batch of candidate seed Alphas;
   - Uses established Alpha categories from traditional finance (e.g., momentum, mean reversion) to ensure relative independence between factors;
2. **Multi-Agent Decision-Making**:
   - Under different risk preferences and market states, across multimodal data environments (text, numerical, visual, audio/video), multiple agents independently select high-confidence Alphas;
   - Each agent assigns confidence scores based on backtest performance and interpretation of market information;
3. **Dynamic Weight Optimization**:
   - A deep learning model (e.g., DNN) combines the selected Alpha candidates, learning their predictive power for future returns;
   - Weights are continuously adjusted based on market state, achieving an adaptive quantitative strategy.

### 3.2 LLM Filtering and Classification

In the first stage, we provide the LLM (e.g., a customized ChatGPT variant called "Alpha Grail") with multimodal research documents for summarization, classification, and structured seed Alpha list generation.
- **Document sources**: Academic papers, financial reports, charts, earnings filings;
- **Classification output**: Categories such as Momentum, Mean Reversion, Volatility, Fundamental, etc.;
- **Each category contains specific Alpha formulas**: e.g., momentum factors like (CLOSE - DELAY(CLOSE,14)), volatility factors like STD(CLOSE, 20), and so on.

### 3.3 Multimodal Multi-Agent Alpha Evaluation

In the second stage, the multi-agent system evaluates seed Alphas using **text, numerical, visual, and audio/video** multimodal data:
1. **Risk preference analysis**: Different agents embody different risk tolerances (conservative, neutral, aggressive), scoring Alpha historical performance accordingly;
2. **Adaptive backtesting**: Simulating trading performance across different market scenarios, focusing on metrics such as Information Coefficient (IC), Sharpe Ratio, etc.;
3. **Confidence scoring**: Each agent assigns a reliability score to filter out underperforming or unreliable factors;
4. **Algorithmic automated selection**: Setting confidence thresholds to select qualifying Alpha subsets.

### 3.4 Alpha Weight Optimization

In the third stage, we employ a DNN or similar deep learning model to perform multidimensional fitting on the selected Alpha factors:
- **Input**: Daily alpha values and historical stock prices;
- **Hidden layers**: ReLU or other activation functions for enhanced nonlinear fitting;
- **Output**: Predicted next-period returns, with network weights optimized via backtest error minimization.
The result is an optimal set of Alpha weights $\{w_i\}$, combined into a dynamic, robust quantitative investment strategy.

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2025/02/01/1738398665334-a4af048e-a5a3-4692-9c67-39591fe961e3.png)

## 4. Experiments

Our empirical study focuses on the SSE 50 index universe, addressing three core research questions:

1. **RQ1**: Can the framework effectively integrate multimodal information and capture new Alphas across different market environments?
2. **RQ2**: Does LLM-driven mining produce more predictive Alphas compared to traditional Alpha generation methods or existing Alpha factories?
3. **RQ3**: Can the combined confidence scoring and adaptive strategy consistently outperform the market index in live testing?

### 4.1 Dataset and Settings

- **Universe**: SSE 50 constituents;
- **Features**: Basic market data (Open, High, Low, Close, Volume, VWAP) and company financials;
- **Time split**: Training set 2021.01.01-2022.12.31; test set 2023.01.01-2023.12.31;
- **Evaluation metrics**: Information Coefficient (IC), cumulative returns, drawdown, Sharpe Ratio, etc.

### 4.2 Main Results

#### 4.2.1 RQ1: Multimodal and Dynamic Alpha Capture

- **Multimodal LLM analysis**: Combining text (company announcements, news), numerical (earnings data), and visual (candlestick charts, volume charts) information, the framework automatically identifies factors suited to the current market across different time periods (e.g., 2021.12.31-2022.09.30 vs. 2022.10.01-2023.xx.xx);
- **Case studies**:
  - **Case 1**: Selected momentum and volume factors such as RSI, MACD, and moving averages;
  - **Case 2**: Emphasized volatility and economic factors such as ATR, Bollinger Band width, gross margin, and operating income ratios.
  - Results demonstrate that the framework flexibly selects more relevant Alpha sets depending on market conditions.

#### 4.2.2 RQ2: Do LLM-Mined Alphas Offer Greater Predictive Value?

We measured IC to assess the correlation between selected Alphas and actual future returns. Compared to traditional "Alpha factories," the LLM framework achieved notably higher average IC for momentum, volatility, and fundamental factors, indicating stronger predictive effectiveness.

#### 4.2.3 RQ3: Can the Combined Strategy Beat the Market?

We employed a Top-k/Drop-n strategy, buying the k stocks with the highest Alpha scores daily and limiting portfolio turnover to n stocks per rebalance.
- **Backtest period**: 2023;
- **Results**:
  - Our framework achieved cumulative returns of **+53.17%**, while the SSE 50 index declined **-11.73%** over the same period, with other benchmark funds also trailing significantly;
  - Backtests confirm that the LLM-driven + confidence scoring + dynamic reweighting strategy outperforms the market during most market phases.

---

## 5. Related Work

1. **Formulaic Alpha**: Traditionally, Alpha factors are derived through genetic programming, genetic algorithms, or machine learning models (e.g., XGBoost, LSTM), but these lack dynamic adaptability in multimodal information settings;
2. **LLMs in Finance**: While general-purpose large model research is flourishing, financial applications (especially quantitative trading) remain in early stages, with most work concentrated on financial text summarization or news sentiment analysis;
3. **Multimodal and Multi-Agent Systems**: Recent literature shows that combining text, visual, and numerical data modalities significantly improves market sentiment and volatility capture. Additionally, multi-agent collaborative decision-making can simulate diverse strategies and preferences, enhancing overall robustness.

---

## 6. Conclusion

This paper presents a novel approach combining **large language models** with **multi-agent architectures** for quantitative stock investing and Alpha mining. By using LLMs to generate and filter diversified Alpha factors from multimodal financial information, then leveraging multi-agent structures for dynamic market evaluation and reweighting, the framework maintains strong investment returns and strategic robustness across varying market conditions. Empirical results on the China A-share market demonstrate significant outperformance over traditional methods across multiple metrics, establishing a new benchmark for AI-driven quantitative strategies.

> **Future Directions**:
> - Upgrading the multi-agent system to a Mixture of Experts model for improved learning efficiency;
> - Incorporating financial knowledge graphs to enhance understanding of implicit industry and company relationships;
> - Extending the formulaic Alpha paradigm to other time-series prediction domains such as energy forecasting, anomaly detection, and healthcare.

---

## References (Selected)

1. Fama, E.F. *Efficient capital markets: A review of theory and empirical work.* Journal of Finance, 1970.
2. Cui, C., Wang, W., Zhang, M., et al. *Alphaevolve: A learning framework to discover novel alphas in quantitative investment.* SIGMOD, 2021.
3. ... (See the original paper for the complete bibliography)

See the appendix for detailed Alpha factor lists, dataset and experimental setup descriptions, and LLM prompt templates.

## About LLMQuant

LLMQuant is a cutting-edge community composed of researchers from top universities and quantitative finance professionals worldwide, dedicated to exploring the intersection of artificial intelligence (AI) and quantitative finance (Quant). Our team members come from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other leading institutions, with external advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and top proprietary trading firms.

![](https://fastly.jsdelivr.net/gh/bucketio/img13@main/2025/01/29/1738120164157-32d67f79-b006-4f4e-bb7b-13db27759e2b.JPG)
