![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# Internal Training Program | Cambridge LLMQuant and Peking University QTA Joint Training Program Now Open
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

The joint internal training program organized by **Cambridge University LLMQuant** and the **Peking University Quantitative Trading Association** is now live. This program is designed to help students interested in quantitative trading, machine learning, and derivatives deepen their knowledge through hands-on learning. Whether you are a complete beginner or an experienced researcher, there is content tailored for you.

## About LLMQuant

LLMQuant originated at Cambridge University and is a cutting-edge community of professionals from the world's leading universities and quantitative finance practitioners, dedicated to exploring the intersection of artificial intelligence (AI) and quantitative finance (Quant). Our team members come from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other prestigious institutions, with external advisors from Microsoft, HSBC, Jump Trading, Man Group, and leading proprietary trading firms.

## Training Partner

![](https://fastly.jsdelivr.net/gh/bucketio/img14@main/2024/09/04/1725457918602-9850222e-1dce-4d0a-98db-f5783681eb37.jpg)

The Peking University Quantitative Trading Association (QTA) is an academic society focused on quantitative trading and one of the most influential quant-focused student organizations at Peking University.

## Supporting Organization

![](https://fastly.jsdelivr.net/gh/bucketio/img0@main/2024/09/04/1725457918597-d07a6531-b5a1-4bd9-8568-0e4ea34d0701.png)

The Cambridge University Algorithmic Trading Society (CUATS) is the most influential quantitative trading student organization at Cambridge, with partners including Jane Street, Citadel, Optiver, SIG, DRW, and others.

## Program Highlights

The program covers multiple tracks including **multi-factor models**, **machine learning**, and **derivatives**, exploring key theories and applications in quantitative trading. Each module is led by an experienced team of mentors, combining **theoretical instruction** with **hands-on projects** to maximize learning in the shortest time. The program concludes with three practical projects from **industry mentors**, giving participants exposure to the day-to-day work in quantitative finance.

## Multi-Factor Model Track

### Overview

Multi-factor models form the foundation of quantitative trading research. This module aims to help community members build a deep understanding of market structure, become familiar with the multi-factor research workflow, and independently design and optimize factors.

### Curriculum

1. **Theoretical Study**: Read "Factor Investing," the latest research reports, and academic papers to develop a comprehensive understanding of multi-factor models.
2. **Practical Research**: Master the complete factor research workflow, covering factor replication, construction, and improvement. Mentors provide specific research topics to help you discover high-performing factors.

Whether you are a beginner or an advanced researcher, our mentor team will help you grow rapidly and go deep into factor research.

## Machine Learning Track

### Overview

This module focuses on the application of machine learning in quantitative trading, combining the latest ML techniques with financial data analysis to explore the potential of machine learning in processing unstructured data.

# Curriculum

### 1. Machine Learning Pairs Trading Strategy

This strategy improves upon traditional pairs trading by using machine learning to pair stocks with similar returns and company characteristics. By identifying these pairs and betting on mean reversion, the strategy profits when stocks deviate from historical relationships. Agglomerative clustering is used to find optimal pairs, with monthly rebalancing.

- **Assets**: Common stocks listed on NYSE, AMEX, NASDAQ
- **Trading Logic**: Long underperforming stocks and short outperforming stocks within groups sharing similar characteristics and historical returns.
- **Rationale**: Stocks that have historically moved together are expected to revert to the mean when they diverge. Incorporating company characteristics improves pair selection and enhances returns.
- **Rebalancing**: Monthly

### 2. Predicting Earnings Surprises with Machine Learning

Instead of relying on a single earnings estimate, this strategy predicts the entire earnings distribution. By estimating the probability that a company will beat or miss analyst expectations, it helps traders make better decisions. Non-parametric machine learning models are used for precise predictions.

- **Assets**: US-listed stocks
- **Trading Logic**: Long companies with a high predicted probability of positive earnings surprises; short those with low probability.
- **Rationale**: Predicting the earnings distribution provides better insight into future stock performance, particularly around earnings events.
- **Rebalancing**: Quarterly (around earnings announcements)

### 3. Predicting Option Returns with Machine Learning

This strategy uses machine learning to predict option returns by identifying mispriced options through a comprehensive feature set including liquidity and volatility measures, then constructing long-short portfolios based on predicted returns.

- **Assets**: US equity options
- **Trading Logic**: Long options with strong predicted returns and short those with weak predicted returns, based on features including implied volatility and liquidity.
- **Rationale**: By analyzing extensive options and stock characteristic data, machine learning can uncover option mispricings and arbitrage opportunities.
- **Rebalancing**: Monthly (dynamically adjusted based on market conditions)

### 4. Building Factor Portfolios with Machine Learning

This strategy uses machine learning to analyze hundreds of stock characteristics and construct a portfolio that outperforms traditional factor models. Its key advantage is the ability to dynamically adapt to changing market conditions, particularly across different phases of the credit cycle.

- **Assets**: US-listed stocks
- **Trading Logic**: Long predicted winners and short predicted losers based on machine learning models that identify the dominant return-driving factors.
- **Rationale**: The factors driving stock returns change over time; machine learning captures these shifts, producing better portfolio performance than static factor models.
- **Rebalancing**: Monthly

### 5. Assessing Company Quality with Machine Learning

This strategy uses machine learning to more accurately evaluate company quality by analyzing financial data, helping investors and stakeholders make better decisions and identify high-quality companies likely to outperform.

- **Assets**: US-listed stocks
- **Trading Logic**: Long undervalued high-quality companies based on ML-predicted quality scores.
- **Rationale**: Machine learning can more accurately assess company quality through granular financial data analysis, enabling better predictions of future performance.
- **Rebalancing**: Annually

### 6. Predicting Intraday Returns with Machine Learning

This strategy uses LSTM models to predict the direction of intraday stock returns. By observing past intraday prices, the model attempts to execute profitable trades within the trading day, though recent backtests indicate room for improvement.

- **Assets**: S&P 500 stocks
- **Trading Logic**: Using LSTM predictions, long the top 10 stocks expected to perform best intraday and short the bottom 10.
- **Rationale**: Past intraday price movements can help predict future intraday returns, providing profitable short-term trading opportunities.
- **Rebalancing**: Intraday

This track is ideal for students interested in machine learning, especially those who want to learn through hands-on programming practice.

## Derivatives Track

### Overview

If you are interested in options and other derivatives and want to apply them to personal trading strategies, this module is for you. We will guide you through a deep understanding of option pricing models and hedging strategies.

### Curriculum

1. **Theoretical Study**:
   - Option fundamentals: The Black-Scholes model and its applications
   - Dynamic analysis of the Greeks
   - Volatility surfaces and stochastic volatility models
   - Pricing implementation for exotic options
2. **Practical Projects**: Combine numerical methods with derivatives strategies to build backtesting systems and perform optimization testing.

This track is particularly well-suited for students interested in derivatives trading and complex financial instruments. A programming foundation is recommended.

---

## LLMQuant Mini-Projects

# 1. Option Pricing Project

### Project Overview

This project provides an in-depth exploration of option pricing models and their application in hedging strategies. It includes programming and mathematical exercises designed to help Cambridge LLMQuant and Peking University QTA members understand different approaches to option pricing and their practical applications.

### Key Topics

1. **Black-Scholes Option Pricing Model**
   - Including Ito calculus exercises
2. **Discretization of Stochastic Differential Equations and Monte Carlo Option Pricing**
   - Using numerical methods to simulate option prices
3. **Dynamic Hedging Strategies Based on Market Sensitivities**
   - Including delta, gamma, and vega applications
4. **Dupire Model and Heston Model**
   - Two important volatility models
5. **FFT-Based Option Pricing Models**
   - Carr and Madan model
6. **Introduction to Exotic Options**
   - Such as barrier options
7. **Practical Applications in Algorithmic Trading Strategies**

# 2. Limit Order Book Project

### Project Overview

This project focuses on limit order books and their role in market microstructure, exploring how exchanges match orders and how various algorithms and order types are implemented. The project is primarily programming-focused with minimal mathematical content.

### Key Topics

1. **Limit Order Book Concepts**
   - Covering limit orders and market orders
   - Implementing a price-time priority order book
   - Exploring order cancellation and market manipulation strategies (e.g., spoofing)
2. **Matching Algorithms**
   - Implementing pro-rata matching algorithms, extending to include top-of-book priority and Liquidity Market Makers (LMMs)
   - Adding additional order types (market orders, stop orders, iceberg orders, etc.)
3. **Fair Price of an Asset**
   - Calculating mid-price and weighted versions
   - Markov model-based microprice
   - Heuristic methods using Level 2 market data
4. **Extensions**
   - Using deep learning to predict future order book states and execute trades

# 3. Implied Volatility and Volatility Surface Project

### Project Overview

This project covers how to calculate implied volatility, construct volatility surfaces, and apply them in trading strategies. It includes extensive programming and mathematical exercises; Cambridge LLMQuant and Peking University QTA members will learn how to work with real market data and analyze volatility.

### Key Topics

1. **Volatility Surface Concepts**
   - Introduction to the Black-Scholes pricing model
   - Definition of implied volatility and conditions for its existence
2. **Obtaining Option Chain Data**
   - Using the yfinance library to retrieve option chain data
   - Organizing option chain information into pandas DataFrames
3. **Computing Implied Volatility**
   - Analytical solutions for implied volatility in special cases
   - Computing implied volatility using bisection and Newton-Raphson methods
   - Extension using Brent's method
4. **Interpolation and Plotting the Volatility Surface**
   - Ensuring the volatility surface is arbitrage-free
   - Using linear interpolation and cubic spline interpolation to construct the surface
5. **Properties of the Volatility Surface**
   - Discussion of skew, smile, and term structure
   - Typical volatility surface shapes across different markets
6. **Practical Applications**
   - FX market straddle trading
   - Predicting option returns through the volatility term structure

---

## How to Apply

This training program is open to Cambridge LLMQuant community members and Peking University Quantitative Trading Association members. No extensive quantitative experience is required. The LLMQuant community is now **open to external participants**. To join future internal courses and lectures, scan the QR code below to apply for LLMQuant membership. Including your resume will expedite the application process.

Apply now by scanning the QR code!

---
