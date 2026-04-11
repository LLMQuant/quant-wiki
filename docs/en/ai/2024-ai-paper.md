![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

# Year-End Highlight: 48 Selected AI + Quantitative Finance Papers of 2024 with Expert Commentary

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

As an LLMQuant year-end feature, this compilation brings together **41 papers** (curated selections plus extended reading) representing **cutting-edge research** in quantitative finance. These papers span a wide range of topics -- from equities, foreign exchange, commodities, fixed income, and credit markets to portfolio optimization, market prediction, derivatives modeling, macroeconomics, geopolitical risk, and cryptocurrencies & DeFi. Notably, a growing body of work is integrating artificial intelligence (AI) and large language models (LLMs) into financial analysis and trading, enhancing the precision and efficiency of forecasting and valuation while offering fresh perspectives on strategy design, investment decisions, and risk management.

## Table of Contents

- AI and LLMs in Financial Analysis and Trading

  1. Extending Core Earnings Measures with Large Language Models
  2. Risk-Neutral Modeling of Yield Curves Using Autoencoders
  3. Applications and Benchmarking of LLMs in Finance and Investment Management
  4. Discovering Novel Financial Price Jump Categories via "Wavelet Riding"
  5. Modeling News Interactions and Impact for Financial Market Prediction
  6. Extracting Economic Insights with Generative AI
  7. Integrating Machine Learning into the Markowitz Portfolio Selection Paradigm
  8. The "Cocktail Effect" of Multi-task Fine-tuning: A Finance Case Study
  9. Spatiotemporal Diffusion Models for Missing and Real-time Financial Data Inference
  10. "Simulate and Optimize": A Bilevel Mortgage Simulator for Designing New Assistance Products
  11. A Less Discriminatory and Explainable XGBoost Binary Classification Framework

**Portfolio Strategy and Market Prediction Advances**

  12. Joint Estimation of Conditional Mean and Covariance for Unbalanced Panel Data
  13. Dynamic Factor Allocation with Regime-switching Signals
  14. Statistical Arbitrage in Rank Space
  15. Updates on Mean-Variance and Mean-ETL Optimization in Portfolio Selection
  16. Extracting Alpha from Financial Analyst Networks
  17. Forecasting Equity Premiums at High Risk Levels and Risk Prices
  18. Dynamic Portfolio Optimization via Global-in-time Neural Networks

**Electronic Financial Markets and Limit Order Books (LOB)**

  19. Linear Strategies for Nonlinear Price Impact
  20. No Tick Too Small: A Universal Approach to Modeling Small-tick Limit Order Books
  21. Multi-task Dynamic Pricing in Credit Markets Using Contextual Information
  22. Do Maker-Taker Limit Order Subsidies Improve Market Outcomes?
  23. Optimal Execution Under Deterministic Time-varying Liquidity: Well-posedness and Price Manipulation
  24. Simulation and Analysis of Sparse Order Books: Applications in Intraday Electricity Markets
  25. The Impact of Liquidity on the Feasibility of Spoofing in Financial Markets
  26. Inventory, Market Making, and OTC Market Liquidity

**Derivatives Modeling and Volatility Frontiers**

  27. Realized Volatility Forecasting with Spillover Effects: A Graph Neural Network Perspective
  28. Fast Deep Hedging with Second-order Optimization
  29. Global Equity Volatility Forecasting via Graph Signal Processing
  30. Hedging with Perpetual Derivatives: Trinomial Option Pricing and Implied Parameter Surfaces
  31. Modeling Monthly Average VIX with the Log Heston Model
  32. GARCH-Informed Neural Networks for Financial Volatility Forecasting

**Financial Markets and Macroeconomics**

  33. Drivers of Credit Bond Market Liquidity in China
  34. AI and Big Holdings Data: New Opportunities for Central Banks
  35. GMM Estimation with Brownian Kernels and Income Inequality Measurement
  36. Taming the Curse of Dimensionality: Quantitative Economics with Deep Learning
  37. Negative Mean Output Gaps and Symmetry Bias in Statistical Filters
  38. Stylized Facts of Money Markets: Empirical Analysis of Euro Area Data
  39. A Minimalist Model of Money Creation Under Regulatory Constraints
  40. Can Competition Increase Factor Investing Profits?
  41. Conditional Margin Call Forecasting with Dynamic Graph Neural Networks
  42. Time Series Foundation Models for Value-at-Risk
  43. Model Validation Practices in Banking: A Structured Approach

**Decentralized Finance (DeFi) Frontiers**

  44. Drivers of Liquidity in Decentralized Exchanges: Evidence from the Uniswap Protocol
  45. AgileRate: Bringing Adaptability and Robustness to DeFi Lending Markets

**Time Series Forecasting**

  46. XForecast: Evaluating Natural Language Explanations for Time Series Forecasting
  47. Prediction Intervals for Multi-step Time Series Forecasting with Online Conformal Inference

**Beyond the Curated Selection**
  48. Frontier Research Beyond the Curated List

## Extending Core Earnings Measures with Large Language Models

**Paper Information:**
M Shaffer, CCY Wang, SSRN, 2024
University of Southern California, Harvard Business School
[Original Link](https://papers.ssrn.com)

**Results and Key Findings**

This study evaluates the effectiveness of LLMs in measuring core corporate earnings from 10-K filings, finding significant improvements over traditional metrics.

- When using structured "sequential" prompts, LLM-generated core earnings metrics outperform GAAP net income and other common measures in predicting future average earnings.
- Unlike unstructured "baseline" approaches, the sequential method accurately distinguishes non-recurring from recurring earnings components, improving predictive validity and reducing confusion with other financial concepts.
- LLM-based core earnings measures demonstrate strong predictive power for long-term net income and correlate highly with future market valuations, potentially reducing the cost of financial information analysis substantially.

Figure 2 shows histograms of GAAP net income and two LLM core earnings estimates (per-share values).

## Risk-Neutral Modeling of Yield Curves Using Autoencoders

**Paper Information:**
A Lyashenko, F Mercurio, A Sokol, SSRN 4967989, 2024
Quantitative Risk Management, Bloomberg, CompatibL
[Original Link](https://papers.ssrn.com)

**Results and Key Findings**

This research uses autoencoders (AE) to model yield curves within a risk-neutral framework, preserving historical structure while ensuring arbitrage-free dynamics.

- Autoencoders provide low-dimensional representations of yield curves, achieving historical consistency and efficient market price calibration.
- The study proposes a convexity adjustment method for deviations from the AE manifold, ensuring arbitrage-free forward rate curve evolution.
- Numerical results on multi-currency interest rate swap data demonstrate improved curve representation accuracy and hedging stability.

## Applications and Benchmarking of LLMs in Finance and Investment Management

**Authors:**
Kong Y, Nie Y, Dong X, Mulvey JM, Poor HV, Wen Q, Zohren S
(University of Oxford, Princeton University, Squirrel Ai)

**Results and Key Findings**

- LLM-based multi-agent systems improve automated trading, corporate strategy planning, and market sentiment analysis through collaborative specialized agents and reflexive reasoning frameworks.
- Comprehensive benchmarks such as FLUE and PIXIU establish robust standards for evaluating LLMs on financial NLP tasks including financial forecasting, named entity recognition, and sentiment analysis.
- Language-specific benchmarks highlight the need for tailored evaluation across linguistic contexts to improve financial LLM adaptability in global markets, while addressing data privacy and computational cost challenges.

---

## Discovering Novel Financial Price Jump Categories via "Wavelet Riding"

**Authors:**
C Aubrun, R Morel, M Benzaquen, JP Bouchaud, 2024
(CNRS, Capital Fund Management, Ecole Polytechnique, ENS)

**Results and Key Findings**

This study proposes a novel unsupervised classification method using multi-scale wavelet representations to distinguish different types of financial price jumps and co-jumps, yielding new insights into their endogenous or exogenous nature.

- Temporal asymmetry in volatility is the primary feature distinguishing endogenous from exogenous price jumps: endogenous jumps are more symmetric, while exogenous jumps exhibit stronger post-jump volatility.
- The study identifies novel price jump categories with local mean-reversion and trend-alignment characteristics.
- Analysis shows that most large-scale co-jump events are driven by endogenous contagion mechanisms rather than exogenous news, underscoring the inherent interconnectedness and reflexivity of market dynamics.

---

## Modeling News Interactions and Impact for Financial Market Prediction

**Authors:**
M Wang, SB Cohen, T Ma - arXiv:2410.10614 (2024)
The University of Edinburgh

**Results and Key Findings**

The FININ model outperforms existing methods in market prediction by fusing news interactions with market data.

- FININ achieves daily Sharpe ratios of 0.429 and 0.341 for the S&P 500 and NASDAQ 100 respectively, demonstrating the effectiveness of integrating news with market data.
- The study reveals delayed news effects on market pricing, long memory in news, the limitations of pure sentiment analysis, and the importance of comprehensive news analysis.
- Tested on over 2.7 million news articles spanning 15 years using a data fusion encoder and market-aware impact quantifier.

---

## Extracting Economic Insights with Generative AI

**Authors:**
M Jha, J Qian, M Weber, B Yang - arXiv:2410.03897 (2024)
University of Chicago Booth, Georgia State University

**Results and Key Findings**

Introduces an AI Economy Score based on management expectations that effectively predicts future economic indicators, outperforming existing measures.

- The AI Economy Score significantly predicts GDP growth, output, and employment.
- Compared to survey-based forecasts, this index offers advantages in long-term prediction and micro-level analysis.
- Validated through a vector autoregressive framework for long-term predictability and micro-level insights, with practical value for policymakers, researchers, and investors.

---

## Integrating Machine Learning into the Markowitz Portfolio Selection Paradigm

**Authors:**
M Lopez de Prado, J Simonian, FA Fabozzi - Annals of Operations Research (2024)
Stevens Institute of Technology, Cornell University

**Results and Key Findings**

A Deep Q-Network (DQN) strategy significantly outperforms traditional methods in multi-asset portfolios, achieving higher returns and lower risk.

- The DQN strategy generates 30% more profit than 10 traditional portfolio management strategies, with superior Sharpe ratios and maximum drawdown performance.
- Adapts DQN to the discrete action space of multi-asset portfolios, combining CNN and dueling Q-network approaches.
- Tested on 5 low-correlation U.S. stocks, continuously optimizing future cumulative returns within a reinforcement learning framework.

---

## The "Cocktail Effect" of Multi-task Fine-tuning: A Finance Case Study

**Authors:**
M Brief, O Ovadia, G Shenderovitz, NB Yoash - arXiv:2024
Microsoft, Tel Aviv University

**Results and Key Findings**

Multi-task fine-tuning significantly enhances LLM performance on financial tasks, enabling smaller models to outperform larger ones through task integration.

- Through multi-task fine-tuning, the smaller Phi-3-Mini model surpasses the larger GPT-4-o on financial benchmarks.
- Empirically validates the "cocktail effect" -- training on multiple related tasks produces synergistic performance improvements.
- Introduces general instruction data as regularization and math data to boost numerical reasoning, with systematic exploration across 220 models verifying dataset interaction effects.

---

## Spatiotemporal Diffusion Models for Missing and Real-time Financial Data Inference

**Authors:**
Y Fang, R Liu, H Huang, P Zhao, Q Wu - ACM (2024)
City University of Hong Kong, Brunel University London

**Results and Key Findings**

Proposes an innovative spatiotemporal diffusion model (STDM) approach for financial data imputation that effectively captures spatiotemporal correlations.

- Key contributions include feature-specific projection, cross-sectional graph convolution, and an implicit sampler that reduces memory consumption while maintaining high accuracy.
- Outperforms existing methods on the OSAP dataset, with ablation studies and factor portfolio construction validating model effectiveness.

---

## "Simulate and Optimize": A Bilevel Mortgage Simulator for New Assistance Products

**Authors:**
L Ardon, BP Evans, D Garg, AL Narayanan - arXiv:2024
J.P. Morgan AI Research, University of Sydney

**Results and Key Findings**

Develops an innovative bilevel simulation approach for optimizing mortgage assistance products, enhancing household resilience to financial shocks.

- Extends agent-based models for counterfactual analysis and policy learning based on product conditions.
- The inner layer simulates household behavior while the outer layer optimizes product design, calibrated with demographic data.
- Identifies favorable configurations that reduce default rates and improve social welfare.

---

## A Less Discriminatory and Explainable XGBoost Binary Classification Framework

**Authors:**
A Pangia, A Sudjianto, A Zhang, T Khan - arXiv:2410.19067 (2024)
Wells Fargo, University of North Carolina at Charlotte

**Results and Key Findings**

The LDA-XGB1 framework integrates fairness constraints into XGBoost, providing a new approach for balancing accuracy and fairness in financial credit models.

- Incorporates fairness constraints and monotonicity into XGBoost, reducing bias against protected groups while maintaining interpretability.
- Proposes a dual-objective optimization method using binning and information value (IV), introducing "Less Discriminatory Alternative" and "Fair Information Value" (FIV) to reduce disparate impact.

---

## Joint Estimation of Conditional Mean and Covariance for Unbalanced Panel Data

**Authors:**
D Filipovic, P Schneider - arXiv:2410.21858 (2024)
EPFL, Swiss Finance Institute

**Results and Key Findings**

A nonparametric model for simultaneously estimating conditional mean and covariance of unbalanced panel data, outperforming traditional models in empirical asset pricing.

- Guarantees consistency and finite-sample performance while preserving covariance matrix positive-definiteness and symmetry.
- Shows significant out-of-sample Sharpe ratio improvements on 1962-2021 U.S. equity data.

---

## Dynamic Factor Allocation with Regime-switching Signals

**Authors:**
Y Shu, JM Mulvey - arXiv:2410.14841 (2024)
Princeton University

**Results and Key Findings**

Using Sparse Jump Models to identify market regimes improves factor allocation performance.

- Achieves positive Sharpe ratios across all factors with low inter-factor correlation.
- Integrating regime inference into the Black-Litterman framework outperforms static benchmarks on information ratio and maximum drawdown.

---

## Statistical Arbitrage in Rank Space

**Authors:**
YF Li, G Papanicolaou - arXiv:2410.06568 (2024)
Stanford University

**Results and Key Findings**

Applying neural networks for statistical arbitrage in rank space yields significantly higher returns and Sharpe ratios than traditional methods.

- Achieves an average annualized return of 35.68% with a Sharpe ratio of 3.28 from 2007 to 2022 using intraday rebalancing and neural network optimization.
- Rank space, driven by a single factor, exhibits a more stable market structure with stronger mean-reversion properties than name space.

---

## Updates on Mean-Variance and Mean-ETL Optimization in Portfolio Selection

**Authors:**
BP Shao, JB Guerard Jr, G Xu - Annals of Operations Research (2024)
Tudor Investment Corporation

**Results and Key Findings**

Robust regression with composite analyst forecast variables generates significant active returns, even after accounting for transaction costs.

- MV and Mean-ETL optimization produce statistically significant active returns, validated through data-mining correction tests.

---

## Extracting Alpha from Financial Analyst Networks

**Authors:**
D Gorduza, Y Kong, X Dong, S Zohren - arXiv:2410.20597 (2024)
University of Oxford

**Results and Key Findings**

Graph Attention Networks (GAT) applied to analyst coverage networks significantly enhance trading strategy performance.

- The GAT model achieves an annualized return of 29.44% and Sharpe ratio of 4.06, outperforming traditional approaches.
- Captures complex nonlinear relationships between companies through simultaneous analysis of firm features and network structure.

---

## Forecasting Equity Premiums at High Risk Levels and Risk Prices

**Authors:**
N Bansal, C Stivers - Financial Management (2024)
University of Louisville

**Results and Key Findings**

VIX and sentiment indices effectively predict U.S. equity premiums with robust forecasting power across different market environments.

- Equity premiums decline when market sentiment is high (low-risk periods) and surge sharply when VIX exceeds the 80-85th percentile (high-risk periods).
- Adjusted R-squared reaches 19% and 29% at 6-month and 12-month horizons respectively.

---

## Dynamic Portfolio Optimization via Global-in-time Neural Networks

**Authors:**
PM van Staden, PA Forsyth, Y Li - Applied Mathematical Finance (2024)
University of Waterloo

**Results and Key Findings**

Proposes a dynamic programming-free, global-in-time neural network model for portfolio optimization that outperforms traditional methods.

- Provides a more flexible and efficient optimization approach for complex financial problems without requiring dynamic programming.

---

## Linear Strategies for Nonlinear Price Impact

**Authors:**
Brokmann X, Itkin D, Muhle-Karbe J, Schmidt P
Mathematical Finance (2024)
Qube Research and Technologies, Imperial College London, LSE

**Results and Key Findings**

For nonlinear price impact, linear trading strategies optimized for quadratic costs approximate optimal performance with less than 2% loss.

---

## No Tick Too Small: Universal Modeling of Small-tick Limit Order Books

**Authors:**
K Jain, JF Muzy, J Kochems, E Bacry - arXiv:2410.08744 (2024)
UCL, University of Oxford

**Results and Key Findings**

Proposes a universal Hawkes Process model for simulating LOB dynamics across different tick sizes.

- Analyzes high-frequency data for 15 stocks classified by tick size, revealing key characteristic differences in bid-ask spreads, price movements, and liquidity distributions.

---

## Multi-task Dynamic Pricing in Credit Markets Using Contextual Information

**Authors:**
A Javanmard, J Ji, R Xu - arXiv:2410.14839 (2024)
NYU, USC

**Results and Key Findings**

The TSMT algorithm leverages structural similarity between securities to improve pricing accuracy beyond individual or pooled approaches.

---

## Do Maker-Taker Limit Order Subsidies Improve Market Outcomes?

**Authors:**
Y Lin, PL Swan, FHB Harris - Journal of Banking & Finance (2024)
UNSW, Wake Forest University

**Results and Key Findings**

Maker-Taker subsidies improve market efficiency but increase trading costs; removing subsidies worsens market quality.

---

## Optimal Execution Under Deterministic Time-varying Liquidity

**Authors:**
G Palmari, F Lillo, Z Eisler - arXiv:2410.04867 (2024)
Imperial College London, University of Bologna

**Results and Key Findings**

Optimal execution problems under time-varying liquidity have well-defined solutions and avoid price manipulation under certain conditions.

---

## Simulation and Analysis of Sparse Order Books: Applications in Intraday Electricity Markets

**Authors:**
P Bergault, E Cogneville - arXiv:2410.06839 (2024)
Universite Paris Dauphine-PSL, EDF R&D

**Results and Key Findings**

Non-homogeneous Poisson process models effectively simulate order flow in low-liquidity markets.

---

## The Impact of Liquidity on Spoofing Feasibility

**Authors:**
A Gu, Y Wang, C Mascioli, M Chakraborty, R Savani - 2024
University of Michigan, University of Liverpool

**Results and Key Findings**

High market liquidity reduces the effectiveness of spoofing, suggesting that maintaining adequate liquidity naturally deters market manipulation.

---

## Inventory, Market Making, and OTC Market Liquidity

**Authors:**
A Cohen, M Kargar, B Lester, PO Weill - Journal of Economic Theory (2024)
Federal Reserve Bank of Philadelphia, UCLA

**Results and Key Findings**

Models dealer inventory costs and regulatory impacts within a search-theoretic framework, exploring OTC market liquidity and welfare effects.

---

## Realized Volatility Forecasting with Spillover Effects: A GNN Perspective

**Authors:**
C Zhang, X Pu, M Cucuringu, X Dong - International Journal of Forecasting (2024)
Oxford-Man Institute, Alan Turing Institute, HKUST(GZ)

**Results and Key Findings**

GNN-based models for multivariate realized volatility prediction incorporate spillover effects and significantly improve forecasting accuracy, especially for short-term (intra-week) horizons.

---

## Fast Deep Hedging with Second-order Optimization

**Authors:**
K Mueller, A Akkari, L Gonon, B Wood - arXiv:2410.22568 (2024)
Imperial College London, J.P. Morgan

**Results and Key Findings**

The KFAC second-order optimization method accelerates deep hedging training by 75%, converging faster in high-curvature loss regions.

---

## Global Equity Volatility Forecasting via Graph Signal Processing

**Authors:**
Z Chi, J Gao, C Wang - arXiv:2410.22706 (2024)
The University of Sydney

**Results and Key Findings**

GSPHAR integrates graph signal processing with HAR models, using graph Fourier transforms and learnable convolutional filters to improve multi-market volatility forecasting.

---

## Hedging with Perpetual Derivatives: Trinomial Option Pricing and Implied Parameter Surfaces

**Authors:**
J Gnawali, WB Lindquist, ST Rachev - arXiv:2410.04748 (2024)
Texas Tech University

**Results and Key Findings**

Proposes trinomial tree model pricing methods that simultaneously estimate risk-neutral and real-world parameters, including implied volatility, mean, risk-free rate, and probability distribution parameters.

---

## Modeling Monthly Average VIX with the Log Heston Model

**Authors:**
J Park, A Sarantsev - arXiv:2410.22471 (2024)
University of Michigan, University of Nevada Reno

**Results and Key Findings**

Taking the logarithm of VIX and applying the Heston model produces normalized monthly index returns closer to Gaussian i.i.d., improving volatility and return modeling accuracy.

---

## GARCH-Informed Neural Networks for Financial Volatility Forecasting

**Authors:**
Z Xu, J Liechty, S Benthall, N Skar-Gislinge - arXiv:2024
Carnegie Mellon University, NYU

**Results and Key Findings**

GINN combines GARCH patterns with LSTM advantages, outperforming traditional GARCH and GAS models across multiple global market indices.

---

## Drivers of Credit Bond Market Liquidity in China

**Authors:**
J Mo, MG Subrahmanyam - The Journal of Finance and Data Science (2024)
NYU, NYU Shanghai

**Results and Key Findings**

Analysis of the 2010-2019 Chinese credit bond market reveals significant liquidity variations across markets and instruments, influenced by policy interventions and macroeconomic conditions.

---

## AI and Big Holdings Data: New Opportunities for Central Banks

**Authors:**
X Gabaix, RSJ Koijen, R Richmond, M Yogo - 2024 - bis.org
Harvard, NYU Stern

**Results and Key Findings**

Combining asset demand systems with AI and large-scale holdings data provides central banks with deeper insights into financial stability and policy intervention.

---

## GMM Estimation with Brownian Kernels and Income Inequality Measurement

**Authors:**
JS Cho, PCB Phillips - 2024
Yale University, Yonsei University

**Results and Key Findings**

Introduces Brownian motion and Brownian bridge kernels into infinite-dimensional GMM estimation for income inequality analysis, proposing a new U-test.

---

## Taming the Curse of Dimensionality: Quantitative Economics with Deep Learning

**Authors:**
J Fernandez-Villaverde, G Nuno, J Perla - 2024 - nber.org

**Results and Key Findings**

Deep neural networks can overcome the curse of dimensionality in solving high-dimensional dynamic equilibrium models, improving computational efficiency in economics.

---

## Negative Mean Output Gaps and Symmetry Bias in Statistical Filters

**Authors:**
S Aiyar, S Voigts - IMF Economic Review (2024)
IMF, Johns Hopkins University

**Results and Key Findings**

Symmetry bias causes standard filters to underestimate potential output during deep recessions, leading to weaker policy responses and larger output losses.

- In the deepest 25% of recessions, symmetry bias adds an extra one-third to output losses.

---

## Stylized Facts of Money Markets: Empirical Analysis of Euro Area Data

**Authors:**
VL Coz, N Allaire, M Benzaquen, D Challet - arXiv:2024
Ecole Polytechnique, European Central Bank

**Results and Key Findings**

LCR regulation drives increases in "evergreen repos," making euro area interbank networks denser, more stable, and more oriented toward secured lending.

---

## A Minimalist Model of Money Creation Under Regulatory Constraints

**Authors:**
VL Coz, M Benzaquen, D Challet - arXiv:2410.18145 (2024)
Ecole Polytechnique, CentraleSupelec

**Results and Key Findings**

An agent-based model studying bank liquidity management under regulatory constraints reveals how asymmetric responses to payment shocks create excess liquidity in money markets.

---

## Can Competition Increase Factor Investing Profits?

**Authors:**
V DeMiguel, A Martin-Utrera - Management Science (2024)
London Business School, Iowa State University

**Results and Key Findings**

Competition reduces profits from the same factor strategy, but when competitors exploit different factors, multi-factor diversification can boost returns.

---

## Conditional Margin Call Forecasting with Dynamic Graph Neural Networks

**Authors:**
M Citterio, M D'Errico, G Visentin - arXiv:2410.23275 (2024)
European Central Bank, ETH Zurich

**Results and Key Findings**

A novel DGNN architecture accurately predicts net variation margin (NVM) demands up to 21 days ahead, providing forward-looking tools for systemic risk monitoring.

---

## Time Series Foundation Models for Value-at-Risk

**Authors:**
A Goel, P Pasricha, J Kanniainen - arXiv:2410.11773 (2024)
Tampere University, IIT Ropar

**Results and Key Findings**

Fine-tuned TimesFM (Google's pre-trained time series foundation model) outperforms traditional econometric models for VaR estimation across multiple confidence levels.

---

## Model Validation Practices in Banking: A Structured Approach

**Authors:**
A Sudjianto, A Zhang - arXiv:2410.13877 (2024)
Wells Fargo

**Results and Key Findings**

Provides a comprehensive, structured framework for model validation in banking, emphasizing conceptual soundness, outcome analysis, and ongoing monitoring.

---

## Drivers of Liquidity in Decentralized Exchanges: Evidence from Uniswap

**Authors:**
BZ Zhu, D Liu, X Wan, G Liao, CC Moallemi - arXiv:2024
Columbia University, Uniswap Labs

**Results and Key Findings**

Identifies core factors driving Uniswap v3 liquidity, including gas fees, token returns, and volatility, while introducing new metrics for granular analysis.

---

## AgileRate: Bringing Adaptability and Robustness to DeFi Lending Markets

**Authors:**
M Bastankhah, V Nadkarni, X Wang - arXiv:2024
UIUC, Princeton University

**Results and Key Findings**

AgileRate's adaptive interest rate controller (using RLS algorithms) substantially improves lending utilization rates and reduces liquidation risk, outperforming static models.

---

## XForecast: Evaluating Natural Language Explanations for Time Series Forecasting

**Authors:**
T Aksu, C Liu, A Saha, S Tan, C Xiong - arXiv:2024
NUS, Salesforce Research

**Results and Key Findings**

Proposes new evaluation metrics for natural language explanations of time series forecasts, finding that numerical reasoning ability matters more than model size.

---

## Prediction Intervals for Multi-step Time Series Forecasting with Online Conformal Inference

**Authors:**
X Wang, RJ Hyndman - arXiv:2410.13115 (2024)
Monash University

**Results and Key Findings**

The AcMCP method accounts for autocorrelation in multi-step forecast errors under non-stationary AR processes, providing more effective prediction intervals with distribution-free coverage guarantees.

---

## Frontier Research Beyond the Curated List

The following are noteworthy papers beyond the curated selection, organized by topic:

**AI and LLMs in Financial Analysis and Trading**

1. GPT-Signal: Generative AI for Semi-automated Feature Engineering in the Alpha Research Process
2. Generative AI in Financial Reporting
3. Aligning LLMs with Human Instructions and Stock Market Feedback in Financial Sentiment Analysis
4. CustomizedFinGPT Search Agents Using Foundation Models
5. Large Language Models in Economics
6. The macroeconomic implications of the Gen-AI economy
7. What Role Does AI Play In Modern Financial Transactions?
8. Efficient Training of Neural Stochastic Differential Equations by Matching Finite Dimensional Distributions
9. Generation of synthetic financial time series by diffusion models
10. Financial Time Series Forecasting Based on Adversarial Training and Dynamic Weight Design
11. A scoping review of ChatGPT research in accounting and finance
12. Opportunities and Challenges of Generative-AI in Finance
13. Multiple Objectives Escaping Bird Search Optimization and Its application in Stock Market Prediction Based on Transformer Model
14. FinTeamExperts: Role Specialized MOEs For Financial Analysis
15. Financemath: Knowledge-intensive math reasoning in finance domains
16. Deep Learning in Finance: A Survey of Applications and Techniques
17. Natural language processing in finance: A survey
18. FLAG: Financial Long Document Classification via AMR-based GNN
19. The Local Effects of Artificial Intelligence Labor Investments: Evidence from the Municipal Bond Market
20. Enhancing LLM Trading Performance with Fact-Subjectivity Aware Reasoning
21. The Role of Artificial Intelligence in Investment Decision-Making: Opportunities and Risks for Financial Institutions
22. From Facts to Insights: A Study on the Generation and Evaluation of Analytical Reports for Deciphering Earnings Calls
23. Temporal Relational Reasoning of Large Language Models for Detecting Stock Portfolio Crashes
24. GraphVAE: Unveiling Dynamic Stock Relationships with Variational Autoencoder-based Factor Modeling
25. Mapping Hong Kong's Financial Ecosystem: A Network Analysis of the SFC's Licensed Professionals and Institutions
26. FAMMA: A Benchmark for Financial Domain Multilingual Multimodal Question Answering
27. Exploiting Risk-Aversion and Size-dependent fees in FX Trading with Fitted Natural Actor-Critic
28. Distilling Analysis from Generative Models for Investment Decisions
29. Large Legislative Models: Towards Efficient AI Policymaking in Economic Simulations
30. The effect of ESG divergence on the financial performance of Hong Kong-listed firms: an artificial neural network approach
31. A comparative analysis of SHAP, LIME, ANCHORS, and DICE for interpreting a dense neural network in Credit Card Fraud Detection
32. Hierarchical Reinforced Trader (HRT): A Bi-Level Approach for Optimizing Stock Selection and Execution
33. The Perks and Perils of Machine Learning in Business and Economic Research
34. Decrypting Corporate Speak: GPT-Assisted Measurement of Facts and Tones in Earnings Calls
35. TraderTalk: An LLM Behavioural ABM applied to Simulating Human Bilateral Trading Interactions
36. Enhancing Compliance And Kyc Processes Through Ai, Ocr, And Automation: A Costeffective Approach

**Portfolio Strategy and Market Prediction**

37. Deep Learning Methods for S Shaped Utility Maximisation with a Random Reference Point
38. Two-fund separation under hyperbolically distributed returns and concave utility function
39. Robust forward investment and consumption under drift and volatility uncertainties: A randomization approach
40. Clustering Digital Assets Using Path Signatures: Application to Portfolio Construction
41. Machine Learning for Real-Time Portfolio Rebalancing: A Novel Approach to Financial Optimization
42. Time evaluation of portfolio for asymmetrically informed traders
43. Conformal Predictive Portfolio Selection
44. Predicting the stock market prices using a machine learning-based framework during crisis periods
45. MFB: A Generalized Multimodal Fusion Approach for Bitcoin Price Prediction Using Time-Lagged Sentiment and Indicator Features
46. Kendall Correlation Coefficients for Portfolio Optimization
47. Delegated portfolio management with random default
48. Deep prediction on financial market sequence for enhancing economic policies
49. Economic Theory and Machine Learning Integration in Asset Pricing and Portfolio Optimization: A Bibliometric Analysis and Conceptual Framework
50. Generalized Distribution Prediction for Asset Returns
51. Unlocking predictive potential: the frequency-domain approach to equity premium forecasting
52. Improving out-of-sample forecasts of stock price indexes with forecast reconciliation and clustering
53. A Comparative Analysis of Deep Learning and Traditional Statistics for Stock Price and Return Forecasting
54. A Fully Analog Pipeline for Portfolio Optimization

**Electronic Financial Markets and LOB**

55. Reinforcement Learning in Non-Markov Market-Making
56. Double Auctions: Formalization and Automated Checkers
57. A Financial Market Simulation Environment for Trading Agents Using Deep Reinforcement Learning
58. Price impact and long-term profitability of energy storage
59. Information Externalities, Free Riding, and Optimal Exploration in the UK Oil Industry

**Derivatives Modeling and Volatility**

60. Graph-Based Methods for Forecasting Realized Covariances
61. Discrete approximation of risk-based prices under volatility uncertainty
62. A second order finite volume IMEX Runge-Kutta scheme for two dimensional PDEs in finance
63. No arbitrage and the existence of ACLMMs in general diffusion models
64. Numerical analysis of American option pricing in a two-asset jump-diffusion model
65. European Option Pricing in Regime Switching Framework via Physics-Informed Residual Learning
66. Efficient calibration of the shifted square-root diffusion model to credit default swap spreads using asymptotic approximations
67. A Data Driven Study on Fractional Black-Scholes-Merton Equation Using Physics Informed Neural Network
68. Automated Volatility Forecasting
69. Exploiting News Analytics for Volatility Forecasting
70. Multi-model transfer function approach tuned by PSO for predicting stock market implied volatility explained by uncertainty indexes
71. KANOP: A Data-Efficient Option Pricing Model using Kolmogorov-Arnold Networks
72. Forecasting Day-Ahead Eurusd Tail Risk: Leveraging Machine Learning and the Volatility Surface
73. Exact Simulation of Quadratic Intensity Models

**Financial Markets and Macroeconomics**

74. Mean field equilibrium asset pricing model under partial observation: An exponential quadratic Gaussian approach
75. Responsible Investing under Climate Change Uncertainty
76. Fractional Moments by the Moment-Generating Function
77. Distributionally Robust Instrumental Variables Estimation
78. Macroeconomic Impacts of ETS Revenue Allocation: A Post-Keynesian Analysis of Decarbonization Strategies in the EU
79. Note on Bubbles Attached to Real Assets
80. A Run on Fossil Fuel? Climate Change and Transition Risk
81. Dynamic treatment effect of capital controls on macroeconomic and financial stability in emerging market economies
82. Heterogeneous Economies and Micro Data
83. How Do Electoral Votes, Presidential Approval, and Consumer Sentiment Respond to Economic Indicators?
84. A Hierarchical-Dealer-Centric Model of FX Swap Valuation
85. Is Capital Structure Irrelevant with ESG Investors?
86. Alternative Finance in the International Business Context: A Review and Future Research
87. Dynamic graphical models: Theory, structure and counterfactual forecasting
88. The Hallin-Liska criterion through the lens of the random matrix theory
89. The effects of climate change-related risks on banks: A literature review
90. Machine Learning Debiasing with Conditional Moment Restrictions: An Application to LATE
91. Reforming the IMF Surcharge Rate Policy to Avoid Procyclical Lending
92. Econometrics of Insurance with Multidimensional Types
93. TimeBridge: Non-Stationarity Matters for Long-term Time Series Forecasting
94. EXPRESS: Addressing Endogeneity Using a Two-stage Copula Generated Regressor Approach
95. Empirical Insights into Financial Development and Climate Policy Uncertainty Paving the Path for Energy Diversification in the US
96. Managerial Overextrapolation: Who and When

**Quantitative Risk Management**

97. First order Martingale model risk and semi-static hedging
98. Optimal mutual insurance against systematic longevity risk
99. Corporate Non-Disclosure Disputes: Equilibrium Settlements with a Probabilistic Burden of Proof
100. Risk Aggregation and Allocation in the Presence of Systematic Risk via Stable Laws
101. Applications of the Second-Order Esscher Pricing in Risk Management
102. Worst-case values of target semi-variances with applications to robust portfolio selection
103. Machine learning technique to compute climate risk in finance
104. A dealers funding liquidity risk and its money market trades in the 2007/08 crisis
105. Cryptocurrencies and Systemic Risk. The Spillover Effects Between Cryptocurrency and Financial Markets
106. Skew Index: a machine learning forecasting approach
107. Continuous Risk Factor Models: Analyzing Asset Correlations through Energy Distance
108. Quantum Monte Carlo Integration for Simulation-Based Optimisation
109. Tail risk and uncertainty in financial markets
110. Stochastic Loss Reserving: Dependence and Estimation
111. Examination of Bitcoin Hedging, Diversification and Safe-Haven Ability During Financial Crisis
112. Measuring Market Risk in Asset Management
113. Computing Systemic Risk Measures with Graph Neural Networks
114. A Spatio-Temporal Machine Learning Model for Mortgage Credit Risk: Default Probabilities and Loan Portfolios
115. Forecasting VaR and Returns Distribution Using the Real-Time GARCH Models with Standardized Two-Sided Lindley Distribution
116. The Analytics of Robust Satisficing: Predict, Optimize, Satisfice, Then Fortify
117. Risk parity portfolio optimization under heavy-tailed returns and dynamic correlations
118. Are causal effect estimations enough for optimal recommendations under multi-treatment scenarios?
119. A One-Step Approach for Determining the Optimal Aggregate Capital Reserve and Allocation
120. On the mean-field limit of diffusive games through the master equation: extreme value analysis

**Decentralized Finance (DeFi)**

121. The Rise of Decentralised Finance (DeFi)
122. Lightning Network Economics: Topology
123. Competitive dynamics between decentralized and centralized finance lending markets
124. Ormer: A Manipulation-resistant and Gas-efficient Blockchain Pricing Oracle for DeFi
125. Improving DeFi Mechanisms with Dynamic Games and Optimal Control: A Case Study in Stablecoins
126. Security Perceptions of Users in Stablecoins: Advantages and Risks within the Cryptocurrency Ecosystem

**Time Series Forecasting**

127. HiMTM: Hierarchical Multi-Scale Masked Time Series Modeling with Self-Distillation for Long-Term Forecasting
128. FlexTSF: A Universal Forecasting Model for Time Series with Variable Regularities
129. Novel Bayesian algorithms for ARFIMA long-memory processes: a comparison between MCMC and ABC approaches
130. Recurrent Neural Goodness-of-Fit Test for Time Series
131. xLSTM-Mixer: Multivariate Time Series Forecasting by Mixing via Scalar Memories
132. Context is Key: A Benchmark for Forecasting with Essential Textual Information
133. Graph Neural Flows for Unveiling Systemic Interactions Among Irregularly Sampled Time Series
134. TimeMixer++: A General Time Series Pattern Machine for Universal Predictive Analysis
135. Timer-XL: Long-Context Transformers for Unified Time Series Forecasting
136. Inferring Latent Graphs from Stationary Signals Using a Graphical Autoregressive Model
137. Metadata Matters for Time Series: Informative Forecasting with Transformers
138. Learning Pattern-Specific Experts for Time Series Forecasting Under Patch-level Distribution Shift
139. GIFT-Eval: A Benchmark For General Time Series Forecasting Model Evaluation
140. Advancing Multivariate Time Series Anomaly Detection: A Comprehensive Benchmark with Real-World Data from Alibaba Cloud
141. Diffusion Auto-regressive Transformer for Effective Self-supervised Time Series Forecasting
142. LLM-Mixer: Multiscale Mixing in LLMs for Time Series Forecasting
143. LLM-TS Integrator: Integrating LLM for Enhanced Time Series Modeling
144. Scalable Signature-Based Distribution Regression via Reference Sets
145. Robustness Auditing for Linear Regression: To Singularity and Beyond
146. On Anticompetitive Third-Degree Price Discrimination

---

*The above represents the October 2024 curated and extended index of quantitative finance papers, covering AI, LLMs, portfolio optimization, derivatives pricing, risk management, DeFi, macroeconomics, and time series forecasting -- providing a comprehensive reference for researchers, practitioners, and policymakers.*

## About LLMQuant

LLMQuant is a cutting-edge community of researchers and practitioners from the world's leading universities and quantitative finance firms, dedicated to exploring the intersection of artificial intelligence (AI) and quantitative finance (Quant). Our team members come from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other top institutions, with external advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and leading proprietary trading firms.
