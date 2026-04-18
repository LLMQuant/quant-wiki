![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

# Year-End Highlight: 41 Selected AI + Quantitative Finance Papers of 2024 with Expert Commentary

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

As an LLMQuant year-end feature, this compilation brings together **41 papers** (curated selections plus extended reading) representing **cutting-edge research** in quantitative finance. These papers span a wide range of topics -- from equities, foreign exchange, commodities, fixed income, and credit markets to portfolio optimization, market prediction, derivatives modeling, macroeconomics, geopolitical risk, and cryptocurrencies & DeFi. Notably, a growing body of work is integrating artificial intelligence (AI) and large language models (LLMs) into financial analysis and trading, enhancing the precision and efficiency of forecasting and valuation while offering fresh perspectives on strategy design, investment decisions, and risk management.

The selected papers cover multiple asset classes and research directions, including but not limited to:

- **AI and LLMs in Finance**: Leveraging LLM fine-tuning, prompt engineering, multimodal Transformers, and diffusion models to tackle data imbalance and complex prediction challenges.
- **Market Microstructure and Liquidity Analysis**: Advancing theoretical and empirical research on limit order books (LOB), automated market makers (AMM), price impact, and market fragility.
- **Risk Management and Policy Guidance**: From multi-agent reinforcement learning models for ESG investing to quantitative risk assessment tools addressing geopolitical risk, credit, and macro volatility -- providing practical frameworks for policy and investment strategy.
- **Derivatives and Volatility Modeling**: Improving the accuracy and interpretability of rough volatility models, option pricing, and high-frequency forecasting through deep learning and explainability analysis.

This curated list serves as a guide for researchers, practitioners, and students to quickly grasp the latest trends, methods, and applications at the intersection of quantitative finance and AI, offering reference and inspiration for future academic and practical work.

## Table of Contents

### AI and LLMs in Financial Analysis and Trading

1. **CausalStock: Deep End-to-end Causal Discovery for News-driven Stock Movement Prediction**
2. **FinRobot: AI Agent for Equity Research and Valuation with Large Language Models**
3. **FinLlama: LLM-Based Financial Sentiment Analysis for Algorithmic Trading**
4. **AI in Investment Analysis: LLMs for Equity Stock Ratings**
5. **Adaptive and Explainable Margin Trading Via Large Language Models on Portfolio Management**
6. **Modality-aware Transformer for Financial Time series Forecasting**
7. **Imb-FinDiff: Conditional Diffusion Models for Class Imbalance Synthesis of Financial Tabular Data**
8. **InvestESG: A multi-agent Reinforcement Learning Benchmark for Studying Climate Investment As a Social Dilemma**

### Stock Market, Equity Market

9. **You Can Only Lend What You Own: Inferring Daily Institutional Trading from Security Lending Supply**
10. **Factor Momentum Versus Price momentum: Insights from International Markets**
11. **National Culture of Secrecy and Stock Price synchronicity: Cross-country Evidence**
12. **Asset Pricing in African Frontier Equity Markets**

### FX (Foreign Exchange)

13. **What Events Matter for Exchange Rate volatility?**
14. **How Institutions Interact with Exchange Rates After the 2024 US Presidential Election: New High-frequency evidence**

### Commodity Market

15. **Extrapolating the long-term Seasonal Component of Electricity Prices for Forecasting in the day-ahead Market**

### Fixed Income and Bonds Markets

16. **Real-world Models for Multiple Term structures: a Unifying HJM Framework**

### Credit Markets

17. **The Pricing of Asset-Backed Securities and Households' Pecking Order of Debt**
18. **Information Span and Credit Market Competition**

### Portfolio Optimization and Market Prediction

19. **The M6 Forecasting competition: Bridging the Gap Between Forecasting and Investment Decisions**
20. **Cluster-driven Hierarchical Representation of Large Asset Universes for Optimal Portfolio Construction**
21. **Interpretable Machine Learning Model for Predicting Activist Investment Targets**

### Electronic Financial Markets and Limit Order Books (LOB)

22. **Efficient Trading with Price Impact**
23. **Market Making Without Regret**
24. **Through Stormy seas: How Fragile Is Liquidity Across Asset Classes and time?**

### Derivative Modeling and Volatility

25. **Deep Learning Interpretability for Rough Volatility**
26. **Stable Multilevel Deep Neural Networks for Option Pricing and xVAs Using Forward-Backward Stochastic Differential Equations**
27. **Beyond the Traditional VIX: A Novel Approach to Identifying Uncertainty Shocks in Financial Markets**
28. **Short-maturity Options on Realized Variance in local-stochastic Volatility Models**

### Financial Markets, Economics, Game Theory, and Macroeconomics

29. **Stochastic Graphon Games with Memory**
30. **AI-generated production networks: Measurement and applications to global trade**
31. **Rg Before and After the Great Wars 1507-2023**
32. **Firm Heterogeneity and Macroeconomic Fluctuations: a Functional VAR Model**
33. **Taming Data Driven Probability Distributions**

### Quantitative Risk Management

34. **D5.12: Evaluation of Quantum Algorithms for Finance**
35. **An Empirical Implementation of the Shadow Riskless Rate**
36. **Efficient Nested Estimation of CoVaR: A Decoupled Approach**
37. **Volatility Connectedness Between Geopolitical Risk and Financial markets: Insights from Pandemic and Military Crisis Periods**
38. **Cross-quantile Risk assessment: the Interplay of Crude oil, Artificial intelligence, Clean tech, and Other Markets**

### Cryptocurrencies and Decentralized Finance (DeFi)

39. **Strategic Bonding Curves in Automated Market Makers**
40. **Price Divergence in Bitcoin Market**
41. **Automated Market Making: the case of Pegged Assets**

---

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/12/14/1734212989861-3c489e88-e079-41b1-bf7d-c78ebe47a3be.png)

## Expert Commentary

#### CausalStock: Deep End-to-end Causal Discovery for News-driven Stock Movement Prediction

S Li, Y Sun, Y Lin, X Gao, S Shang, R Yan - arXiv preprint arXiv, 2024 - arxiv.org
Peking University, Renmin University of China

![](https://fastly.jsdelivr.net/gh/bucketio/img1@main/2024/12/14/1734213395814-6b4e7dd7-3b10-4a81-b636-34d9269b3d34.png)

**Results -- Key Findings**
By discovering temporal causal relationships among stocks and employing advanced modeling techniques, CausalStock outperforms existing methods for multi-stock movement prediction across global markets.

- Introduces a Functional Causal Model with a time-lag-dependent temporal causal discovery mechanism, better suited for stock time series data.
- Uses a Denoised News Encoder (LLM-based) to extract meaningful information from noisy news, combining neural networks with variational inference for prediction.
- Tested on U.S., Chinese, Japanese, and UK market data, CausalStock surpasses existing methods with clear, interpretable predictions that support financial analysis and quantitative trading.

---

#### FinRobot: AI Agent for Equity Research and Valuation with Large Language Models

T Zhou, P Wang, Y Wu, H Yang - arXiv:2411.08804, 2024 - arxiv.org
AI4Finance Foundation, Brown University

![Overall Framework of FinRobot](https://fastly.jsdelivr.net/gh/bucketio/img14@main/2024/12/14/1734213424420-e6e238a4-fa44-4266-b469-e3c75900863e.png)

**Results -- Key Findings**
FinRobot introduces the first AI agent framework for equity research, employing multi-agent chain-of-thought reasoning that integrates quantitative and qualitative analysis to simulate human analyst reasoning.

- Multi-agent CoT framework (Data-CoT, Concept-CoT, Thesis-CoT) synthesizes human analyst thought processes.
- Integrates quantitative and qualitative analysis with real-time data and introduces new evaluation metrics (Accuracy, Logicality, Storytelling) to improve report quality and timeliness.
- Open-sources FinRobot to democratize advanced AI tools in finance and foster collaboration.

---

#### FinLlama: LLM-Based Financial Sentiment Analysis for Algorithmic Trading

G Iacovides, T Konstantinidis, M Xu, D Mandic - ACM AI in Finance, 2024
Imperial College London

![Training parameters used in the fine-tuning process of the proposed FinLlama](https://fastly.jsdelivr.net/gh/bucketio/img7@main/2024/12/14/1734213454721-b7a119f1-8d2c-441c-a0b4-998054d31ab4.png)

**Results -- Key Findings**
FinLlama, a financial sentiment fine-tuned version of Llama 2, improves algorithmic trading performance.

- Fine-tunes the Llama 2 (7B) model on labeled financial text data for accurate classification of sentiment and its intensity.
- Employs LoRA and 8-bit quantization to reduce computational requirements while maintaining high accuracy without expensive hardware.
- In portfolio simulations, FinLlama outperforms existing methods like FinBERT and demonstrates greater robustness in volatile markets.

---

#### AI in Investment Analysis: LLMs for Equity Stock Ratings

K Papasotiriou, S Sood, S Reynolds, T Balch - ACM AI in Finance, 2024
J.P. Morgan AI Research, Emory University

![](https://fastly.jsdelivr.net/gh/bucketio/img6@main/2024/12/14/1734213477673-6b5bd1db-04e3-4b6f-b8c0-094ae776a3a2.png)

**Results -- Key Findings**
By leveraging GPT-4 with financial data, LLMs outperform traditional analysts in stock rating predictions.

- Uses GPT-4-32k for rating predictions on S&P 500 companies, combining financial, market, and news data to outperform analyst ratings in forecasting future returns.
- Incorporating financial fundamentals significantly improves accuracy; using news sentiment in place of detailed summaries reduces token consumption without sacrificing performance.
- LLMs can efficiently integrate multimodal data, providing a low-cost, high-efficiency alternative to traditional rating approaches.

---

#### Adaptive and Explainable Margin Trading via Large Language Models on Portfolio Management

J Gu, J Ye, G Wang, W Yin - ACM AI in Finance, 2024
NJIT, Penn State

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/12/14/1734213497508-c1cf6bea-352b-4d5a-8bea-f5d0a8f1008a.png)

**Results -- Key Findings**
LLMs combined with reinforcement learning dynamically adjust positions, improving portfolio returns and Sharpe ratios.

- A two-stage framework (explainable market prediction/reasoning + position reallocation) triples benchmark returns and doubles the Sharpe ratio.
- Uses LLMs to process multi-source data for market trend prediction and dynamic position adjustment, enhancing profitability and risk management.
- Demonstrates LLM potential for strategy transparency and adaptability.

---

#### Modality-aware Transformer for Financial Time Series Forecasting

H Emami Gohari et al. - ACM AI in Finance, 2024
IBM T.J. Watson

![The Modality-aware Transformer (MAT) employs Intra-modal, Inter-modal, and Target-modal MHA, fused via feature-level attentions. This enhances temporal attention, leveraging modality and feature importance for richer embeddings. MAT's design optimizes information use across and within modalities](https://fastly.jsdelivr.net/gh/bucketio/img5@main/2024/12/14/1734213532472-1acc97b2-6bee-4932-9ddd-618fbc123efb.png)

**Results -- Key Findings**
The MAT model fuses textual reports with numerical data to improve financial time series forecasting accuracy.

- Feature-level attention layers focus on the most informative features, improving both accuracy and interpretability.
- Intra-modal, Inter-modal, and Target-modal attention mechanisms capture temporal and cross-modal dependencies.
- Empirical results significantly outperform existing methods, providing an effective solution for multimodal forecasting.

---

#### Imb-FinDiff: Conditional Diffusion Models for Class Imbalance Synthesis of Financial Tabular Data

M Schreyer et al. - ACM AI in Finance, 2024; LBNL, ICSI

![](https://fastly.jsdelivr.net/gh/bucketio/img18@main/2024/12/14/1734213579404-5bf29e79-e5eb-480d-b9a6-c072045ba5a7.png)

**Results -- Key Findings**
Imb-FinDiff uses diffusion models to synthesize minority class samples, improving classification performance on imbalanced data.

- A dual learning objective combining diffusion noise with class prediction enhances minority class synthesis quality.
- Outperforms SMOTE and ADASYN and is well-suited for mixed-type tabular data.
- Empirically demonstrates high fidelity and diversity on real-world data.

---

#### InvestESG: A Multi-agent Reinforcement Learning Benchmark for Studying Climate Investment as a Social Dilemma

X Hou et al. - arXiv:2411.09856, 2024
University of Washington, Google DeepMind

![](https://fastly.jsdelivr.net/gh/bucketio/img6@main/2024/12/14/1734213601249-f2cbdb5f-f8c9-45c9-992f-452e835cc0e6.png)

**Results -- Key Findings**
A critical mass of ESG investors can drive corporate cooperation on climate mitigation. MARL simulations show that information transparency incentivizes greater climate investment.

- Highlights the role of ESG disclosure and informed investors in driving corporate action.
- The MARL framework simulates firm-investor interactions, aiding policy design and market mechanism development.
- Underscores the importance of systematic disclosure of global climate risk information.

---

#### You Can Only Lend What You Own: Inferring Daily Institutional Trading from Security Lending Supply

YH Barardehi et al. - SSRN, 2024
U.S. SEC, Chapman University

**Results -- Key Findings**
Changes in lendable shares serve as a reliable proxy for institutional trading, more accurate than existing alternative measures.

- Changes in lendable shares better track shifts in institutional holdings.
- This proxy measure of institutional trading negatively predicts stock returns; institutions make strategic adjustments ahead of earnings announcements and stock splits.
- Provides a new tool for understanding institutional behavior and market dynamics.

---

#### Factor Momentum Versus Price Momentum: Insights from International Markets

N Cakici et al. - Journal of Banking & Finance, 2024
Fordham University, Montpellier Business School

**Results -- Key Findings**
Factor momentum is globally robust but cannot fully explain stock momentum, indicating that momentum is an independent anomaly.

- Factor momentum is strong across global markets and independent of common predictive factors.
- It cannot fully account for stock and industry momentum, suggesting that momentum has a unique character.
- Carries implications for investment management and risk assessment.

---

#### National Culture of Secrecy and Stock Price Synchronicity: Cross-country Evidence

C Gaganis et al. - Journal of Banking & Finance, 2024
University of Crete, Athens University of Economics and Business

**Results -- Key Findings**
Cultural secrecy reduces investor information-seeking, increasing stock price synchronicity and decreasing idiosyncratic volatility.

- In more secretive societies, investors are less inclined to search for information, resulting in greater stock price co-movement.
- Enforcement of insider trading laws can reduce private information trading and idiosyncratic volatility.
- Offers important insights into the influence of cultural factors on market dynamics.

---

#### Asset Pricing in African Frontier Equity Markets

B Hearn et al. - International Review of ..., 2024
University of Southampton

**Results -- Key Findings**
Traditional asset pricing models are poorly suited to African frontier markets, requiring localized, customized models.

- Analysis shows that local conditions significantly influence pricing outcomes, and traditional models exhibit notable bias.
- Provides a foundation for asset pricing research in emerging economies.

---

#### What Events Matter for Exchange Rate Volatility?

I Martins, HF Lopes - arXiv:2411.16244, 2024
INSPER, Orebro University

**Results -- Key Findings**
Incorporating macro events aligned with the Taylor rule improves exchange rate volatility prediction and portfolio performance.

- The new model outperforms conventional SV and GARCH models.
- Analysis of high-frequency AUD data reveals a W-shaped intraday seasonality pattern.

---

#### How Institutions Interact with Exchange Rates After the 2024 US Presidential Election: New High-frequency Evidence

J Aizenman, J Saadaoui - NBER, 2024
USC, NBER, Paris 8

**Results -- Key Findings**
Following the 2024 U.S. presidential election, countries with higher institutional quality scores experienced more pronounced currency depreciation against the dollar.

- Depreciation correlates positively with institutional scores; trade surpluses and exchange rate intervention also play a role.
- The EIU's Trump Risk Index influences short-term exchange rate dynamics.

---

#### Extrapolating the Long-term Seasonal Component of Electricity Prices for Forecasting in the Day-ahead Market

K Chec et al. - 2024
Wroclaw University of Science and Technology

**Results -- Key Findings**
Decomposing the long-term seasonal component improves electricity day-ahead market forecast accuracy and trading profitability.

- Autoregressive and LASSO modeling achieve a 3%-15% improvement in RMSE.
- Enhances strategy profitability.

---

#### Real-world Models for Multiple Term Structures: A Unifying HJM Framework

C Fontana et al. - arXiv:2411.01983, 2024
University of Padova, University of Technology Sydney

**Results -- Key Findings**
A unified HJM framework handles multiple term structures, ensuring no-arbitrage conditions and market viability.

- Introduces SPDEs for modeling multiple term structures and provides existence and uniqueness conditions.
- Highlights the necessity of drift restrictions for market viability.

---

#### The Pricing of Asset-Backed Securities and Households' Pecking Order of Debt

R Fuss et al. - Swiss Finance Institute, 2024
University of St. Gallen

**Results -- Key Findings**
Household debt ordering influences ABS and RMBS pricing and rating migration.

- Understanding consumer debt patterns helps predict ABS and RMBS performance.
- Provides new methods for assessing risk and return.

---

#### Information Span and Credit Market Competition

Z He et al. - NBER, 2024
Stanford University, NYU Stern

**Results -- Key Findings**
Broader information span enhances credit market competition, benefiting consumers.

- Information availability shapes market behavior and efficiency.
- Offers guidance for policy and financial decision-making.

---

#### The M6 Forecasting Competition: Bridging the Gap Between Forecasting and Investment Decisions

S Makridakis et al. - arXiv, 2023
University of Nicosia, Athens Polytechnic

**Results -- Key Findings**
The M6 competition reveals the difficulty of forecasting, but integrating multiple forecasts and collective wisdom can improve investment performance.

- Few teams outperform simple benchmarks.
- Combining multiple forecasts and information exchange improves outcomes.

---

#### Cluster-driven Hierarchical Representation of Large Asset Universes for Optimal Portfolio Construction

N Khelifa et al. - ACM AI in Finance, 2024
University of Oxford, Alan Turing Institute

**Results -- Key Findings**
Signed spectral clustering for dimensionality reduction of correlation matrices improves portfolio construction performance.

- New strategies outperform traditional benchmarks with higher Sharpe ratios.
- Cluster count and forecast quality are critical factors.

---

#### Interpretable Machine Learning Model for Predicting Activist Investment Targets

M Kim et al. - Journal of Finance and Data Science, 2024
University of Edinburgh, NYU Abu Dhabi

**Results -- Key Findings**
An interpretable logistic regression model predicts activist investment targets with an AUC-ROC of 0.782.

- Uses SHAP to explain feature importance.
- Helps companies and investors anticipate shareholder activism.

---

#### Efficient Trading with Price Impact

X Brokmann et al. - SSRN, 2024
Imperial College London, LSE

**Results -- Key Findings**
Linear feedback strategies in nonlinear price impact models perform comparably to neural network strategies, while being simpler and more interpretable.

- Balances expected returns, risk, and transaction costs.
- Offers a simple, robust alternative.

---

#### Market Making without Regret

N Cesa-Bianchi et al. - arXiv, 2024
University of Milan, Politecnico di Milano

**Results -- Key Findings**
A no-regret market-making meta-algorithm achieves O(T^(2/3)) regret under specific conditions.

- Also discusses the trade-off between information and regret under feedback models.
- Provides new perspectives for online learning strategies.

---

#### Through Stormy Seas: How Fragile Is Liquidity Across Asset Classes and Time?

N Aliyev et al. - BIS, 2024

**Results -- Key Findings**
Over the past 25 years, global liquidity has improved on average, but liquidity in equity and bond markets has become more fragile.

- Bid-ask spread means and standard deviations have declined, but skewness and kurtosis have increased.
- FX markets have not exhibited the same fragility.

---

#### Deep Learning Interpretability for Rough Volatility

B Yuan et al. - arXiv:2411.19317, 2024
Cambridge, Imperial College London, Alan Turing Institute

**Results -- Key Findings**
Interpretability analysis reveals that neural networks focus on implied volatility of short-dated deep-in-the-money options when calibrating rough Heston models.

- Enhances the safety of using deep learning in quantitative finance.
- Highlights differences between rough volatility models and classical models.

---

#### Stable Multilevel Deep Neural Networks for Option Pricing and xVAs Using FBSDEs

A Ashok Naarayan, P Parpas - ACM AI in Finance, 2024
Imperial College London

**Results -- Key Findings**
A multilevel DNN architecture inspired by multilevel Monte Carlo and FBSDEs dramatically improves option pricing and xVA computation efficiency.

- NAIS-Net ensures stability.
- Significantly outperforms existing methods, improving both accuracy and speed.

---

#### Beyond the Traditional VIX: A Novel Approach to Identifying Uncertainty Shocks in Financial Markets

A Jha et al. - arXiv, 2024
Texas Tech, Johns Hopkins

**Results -- Key Findings**
VVIX based on a doubly subordinated normal inverse Gaussian process more accurately captures heavy tails and skewness in financial markets.

- Addresses VIX shortcomings by capturing long memory and asymmetry.
- Deepens understanding of macroeconomic uncertainty shocks.

---

#### Short-maturity Options on Realized Variance in Local-stochastic Volatility Models

D Pirjol et al. - arXiv:2411.02520, 2024
Stevens Institute of Technology, Florida State University

**Results -- Key Findings**
Derives short-maturity asymptotic solutions for variance options under local-stochastic volatility models, providing practical pricing guidance.

- Analyzes the equivalence of variance options to Asian options.
- Numerical simulations are consistent with theoretical results.

---

#### Stochastic Graphon Games with Memory

E Neuman, S Tuschmann - arXiv:2411.05896, 2024
Imperial College London

**Results -- Key Findings**
Solves stochastic graphon games with memory to obtain explicit Nash equilibria; finite-player equilibria converge to the graphon equilibrium as the number of players increases.

- Provides spectral decomposition and convergence rate analysis.
- Advances understanding of large-scale heterogeneous agent games.

---

#### AI-generated Production Networks: Measurement and Applications to Global Trade

T Fetzer et al. - 2024
LSE, Warwick, Imperial College London

![](https://fastly.jsdelivr.net/gh/bucketio/img19@main/2024/12/14/1734213697580-5ad13d3f-2b49-400a-ad03-a90e4367b6a4.png)

**Results -- Key Findings**
AIPNET uses generative AI to map input-output relationships for over 5,000 products, revealing shifts in global trade patterns.

- Shows "reshoring" phenomena under supply shocks.
- Offers valuable reference for policymaking and international trade analysis.

---

#### rg Before and After the Great Wars 1507-2023

KS Rogoff, P Schmelzing - NBER, 2024
Harvard, Boston College

**Results -- Key Findings**
Five hundred years of data reveal long-run characteristics of the r-g spread and the impact of major historical events.

- The historical perspective uncovers long-term economic trends.
- Carries important implications for economic forecasting and policy.

---

#### Firm Heterogeneity and Macroeconomic Fluctuations: A Functional VAR Model

M Marcellino et al. - arXiv:2411.05695, 2024
Bocconi University

**Results -- Key Findings**
The FunVAR model captures how TFP shocks affect macroeconomic aggregates and the distribution of firm capital and labor.

- Employs tensor dimensionality reduction to model firm heterogeneity.
- Empirically validates model effectiveness.

---

#### Taming Data Driven Probability Distributions

J Barunik, L Hanus - Journal of Forecasting, 2024
Charles University, Czech Academy of Sciences

**Results -- Key Findings**
Deep learning improves forecasting accuracy for macroeconomic and financial time series, handling heavy tails and asymmetry.

- Strengthens probabilistic forecasting capability and decision support.
- Validated on two datasets.

---

#### Evaluation of Quantum Algorithms for Finance

A Manzano et al. - neasqc.eu
University of A Coruna

**Results -- Key Findings**
QAMC and QML show progress in financial applications, but quantum hardware limitations remain a barrier.

- Develops the QQuantLib toolbox.
- Further hardware and algorithm development is needed.

---

#### An Empirical Implementation of the Shadow Riskless Rate

D Lauria et al. - Risks, 2024
Texas Tech, Johns Hopkins

**Results -- Key Findings**
Uses PCA and SVD to estimate the Shadow Riskless Rate, providing a new tool for investment analysis and asset class differentiation.

- Improves risk-free rate measurement in financial markets.
- Supports asset class distinction and financial stability assessment.

---

#### Efficient Nested Estimation of CoVaR: A Decoupled Approach

N Lin et al. - arXiv:2411.01319, 2024
SJTU, Fudan University

**Results -- Key Findings**
Decouples event conditioning from repricing and applies smoothing techniques to improve CoVaR estimation efficiency and convergence rate.

- Compares multiple smoothing techniques, achieving an $O_P(n^{-1/2})$ convergence rate.
- Experiments validate practical applicability.

---

#### Volatility Connectedness Between Geopolitical Risk and Financial Markets: Insights from Pandemic and Military Crisis Periods

AK Banerjee et al. - Int. Rev. Econ. & Finance, 2024
XLRI, Bilkent University

![](https://fastly.jsdelivr.net/gh/bucketio/img4@main/2024/12/14/1734213725892-1873a49d-047e-4dbe-930d-4de62eaba312.png)

**Results -- Key Findings**
Geopolitical risk amplifies financial market volatility and interconnectedness, with stronger effects during military conflicts.

- Bonds transmit risk; gold absorbs risk.
- Provides guidance for policymakers and investor risk management.

---

#### Cross-quantile Risk Assessment: The Interplay of Crude Oil, AI, Clean Tech, and Other Markets

M Gubareva et al. - Energy Economics, 2024
University of Lisbon, BRAC University

**Results -- Key Findings**
A generalized quantile-on-quantile approach reveals risk transmission among crude oil, AI, clean tech, and traditional markets.

- Provides deep analysis of market interdependencies.
- Offers insights for policy and investment decisions.

---

#### Strategic Bonding Curves in Automated Market Makers

R Cartea et al. - SSRN, 2024
University of Oxford

**Results -- Key Findings**
Strategic bonding curves improve AMM efficiency, stability, and liquidity.

- Theoretical and empirical evidence indicates a more predictable and stable trading environment.
- Offers new ideas for modern financial system design.

---

#### Price Divergence in Bitcoin Market

G Chu et al. - Rev. Quant. Finance & Accounting, 2024
Nankai University, Birmingham Business School

**Results -- Key Findings**
National segmentation, cultural factors, and exchange risk drive Bitcoin price divergence, creating arbitrage opportunities.

- On-chain costs and trading activity increase price divergence.
- Higher blockchain security and user adoption reduce divergence.

---

#### Automated Market Making: The Case of Pegged Assets

P Bergault et al. - arXiv:2411.08145, 2024
Sorbonne University, Bachelier Institute, Paris Dauphine

**Results -- Key Findings**
Uses multi-level nested Ornstein-Uhlenbeck processes to build AMM models for pegged crypto assets, improving risk management and liquidity.

- Model efficiency validated on USDC/USDT and wstETH/WETH data.
- Improves market quoting and liquidity for pegged assets.

---

## About LLMQuant

LLMQuant is a cutting-edge community of researchers and practitioners from the world's leading universities and quantitative finance firms, dedicated to exploring the intersection of artificial intelligence (AI) and quantitative finance (Quant). Our team members come from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other top institutions, with external advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and leading proprietary trading firms.
