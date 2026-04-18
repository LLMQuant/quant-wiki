![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

**TradeMaster** is an open-source platform for quantitative trading (QT) that fully integrates **reinforcement learning (RL)** into every stage of the quantitative trading pipeline. From data preparation and algorithm implementation to evaluation and deployment, TradeMaster provides developers and researchers with a comprehensive **end-to-end** solution.

---

### Recent Updates

| Update | Status |
| --- | --- |
| Added FinAgent and EarnMore | Updated October 29, 2024 |
| Updated Market Simulator | Updated September 21, 2023 |
| Updated Market Dynamics Modeling Tool | Updated July 7, 2023 |
| Support for automatic feature generation and selection | Tutorial updated May 11, 2023 |
| Released Python package | Updated May 11, 2023 |
| Launched TradeMaster website | April 23, 2023 |
| Published software documentation | Updated April 11, 2023 |
| Released Colab version | Updated March 29, 2023 |
| Added Hong Kong stocks and futures datasets | Updated March 27, 2023 |
| Support for Alpha158 indicators | Updated March 20, 2023 |
| Official release of TradeMaster 1.0.0 | March 5, 2023 |

---

### TradeMaster Overview

TradeMaster organizes the quantitative trading workflow into six modules:

![](https://fastly.jsdelivr.net/gh/bucketio/img12@main/2025/01/29/1738123026827-f604dec0-5a06-4fb4-b186-c296326e624a.png)

1. **Multimodal market data**: Covering various financial assets at multiple frequencies;
2. **Complete data preprocessing pipeline**: Automated cleaning, feature generation, and more;
3. **High-fidelity market simulator**: Supporting multiple mainstream quantitative trading scenarios;
4. **13+ reinforcement learning algorithms**: Significantly enhancing trading strategy performance;
5. **Systematic evaluation tools**: 6 dimensions with 17 metrics for comprehensive strategy assessment;
6. **Diverse interfaces**: Catering to cross-disciplinary users in both research and engineering.

---

### Installation and Usage

#### 1. Installation

- **Linux/Windows/macOS**
- **Docker**

The official [Installation](#) guide provides detailed environment configuration instructions.

#### 2. Core Tutorials

TradeMaster ships with example code and **Colab online tutorials** covering the following scenarios:

| Algorithm | Dataset | Market | Task | Code |
| --- | --- | --- | --- | --- |
| EIIE | DJ 30 | US Equities | Portfolio Management | [tutorial](#) |
| DeepScalper | BTC | Cryptocurrency | Intraday Trading | [tutorial](#) |
| SARL | DJ 30 | US Equities | Portfolio Management | [tutorial](#) |
| PPO | SSE 50 | China A-Shares | Portfolio Management | [tutorial](#) |
| ETEO | Bitcoin | Cryptocurrency | Order Execution | [tutorial](#) |
| Double DQN | Bitcoin | Cryptocurrency | High-Frequency Trading | [tutorial](#) |

---

### Utility Scripts

TradeMaster includes a rich set of utility scripts:

- **Automated hyperparameter tuning**
- **Automated feature generation**
- **Diffusion-model-based data interpolation and repair**
- **RL training with Alpha158 technical indicators**
- **TradeMaster Sandbox for testing**

Additionally, it provides Market Dynamics modeling tools and a corresponding web interface.

---

### Datasets

The platform includes a variety of common market datasets:

| Dataset | Source | Type | Range & Frequency | Data Type | Link |
| ------- | ------ | ---- | ------------------ | --------- | ---- |
| S&P 500 | Yahoo | US Equities | 2000/01/01-2022/01/01, 1 day | OHLCV | [SP500](#) |
| DJ 30 | Yahoo | US Equities | 2012/01/01-2021/12/31, 1 day | OHLCV | [DJ30](#) |
| BTC | Kaggle | Forex | 2000/01/01-2019/12/31, 1 day | OHLCV | [FX](#) |
| Crypto | Kaggle | Cryptocurrency | 2013/04/29-2021/07/06, 1 day | OHLCV | [Crypto](#) |
| SSE 50 | Yahoo | China A-Shares | 2009/01/02-2021/01/01, 1 day | OHLCV | [SSE50](#) |
| Bitcoin | Binance | Cryptocurrency | 2021/04/07-2021/04/19, 1 min | LOB | [Binance](#) |
| Futures | AKShare | Futures | 2023/03/07-2023/03/28, 5 min | OHLCV | [Future](#) |
| HS 30 | AKShare | Hong Kong Stocks | 1988/12/30-2023/03/27, 1 day | OHLCV | [HS30](#) |

Datasets are available for download from Google Drive or Baidu Cloud (extraction code: x24b).

---

### Model Zoo

TradeMaster provides efficient implementations of multiple RL trading algorithms, including:

- **DeepScalper (CIKM 22)**
- **OPD (AAAI 21)**
- **DeepTrader (AAAI 21)**
- **SARL (AAAI 20)**
- **ETEO (20)**
- **Investor-Imitator (KDD 18)**
- **EIIE (17)**

It also includes classic reinforcement learning algorithms built on PyTorch or Ray: PPO, A2C, Rainbow, SAC, DDPG, DQN, PG, TD3, and more.

---

### Visualization Tools

TradeMaster offers extensive visualization tools for multidimensional evaluation of RL-based quantitative strategies.
> For example, the **PRIDE-Star** radar chart provides an intuitive overview of multiple performance indicators -- return rate, Sharpe Ratio, and more -- at a glance, highlighting each strategy's strengths and weaknesses.

![](https://fastly.jsdelivr.net/gh/bucketio/img2@main/2025/01/29/1738123100989-f58db4af-6048-40c1-aaf2-1b3adbe6e98c.png)

![](https://fastly.jsdelivr.net/gh/bucketio/img3@main/2025/01/29/1738123086122-b3c91503-802d-4e17-b5c4-fda19faf4838.png)

For more details, see the related [paper](#) and [repository](#).

## Related Papers

- **PRUDEX-Compass**: Systematic Evaluation of RL in Financial Markets (TMLR 2023)
- **Reinforcement Learning for Quantitative Trading (Survey)** (ACM TIST 2023)
- **Deep RL for Quantitative Trading: Challenges & Opportunities** (IEEE Intelligent Systems 2022)
- **DeepScalper** (CIKM 2022)
- **Commission Fee is not Enough** (AAAI 2021)

## About LLMQuant

LLMQuant is a cutting-edge community composed of researchers from top universities and quantitative finance professionals worldwide, dedicated to exploring the intersection of artificial intelligence (AI) and quantitative finance (Quant). Our team members come from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other leading institutions, with external advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and top proprietary trading firms.

![](https://fastly.jsdelivr.net/gh/bucketio/img13@main/2025/01/29/1738120164157-32d67f79-b006-4f4e-bb7b-13db27759e2b.JPG)
