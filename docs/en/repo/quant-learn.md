# The Quant Toolbox

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

This list is curated by the [LLMQuant community](https://llmquant.com/). We have compiled a comprehensive resource directory for **systematic trading (quantitative trading) strategies**, including papers, software, books, and articles to help you discover, develop, and run such strategies.

<!-- omit in toc -->
### What Will You Find Here?

- [97 libraries and packages](#libraries-and-packages) supporting quantitative research and live trading
- [696 strategies](#strategies) from institutional and academic sources
- [23 videos](#videos) of high-quality quantitative learning content
- [14 programming languages](../repo/quant-repo.md) with quant frameworks in each
- [Research reproduction](../repo/reproduce.md) code that reproduces classic research results
- Plus valuable [blogs](#blogs) and [courses](#courses)

## Table of Contents

- [Libraries and Packages](#libraries-and-packages)
  - [Backtesting and Live Trading](#backtesting-and-live-trading)
    - [General - Event Driven Frameworks](#general---event-driven-frameworks)
    - [General - Vector Based Frameworks](#general---vector-based-frameworks)
    - [Cryptocurrencies](#cryptocurrencies)
  - [Trading Bots](#trading-bots)
  - [Analytics](#analytics)
    - [Indicators](#indicators)
    - [Metrics Computation](#metrics-computation)
    - [Optimization](#optimization)
    - [Pricing](#pricing)
    - [Risk](#risk)
  - [Broker APIs](#broker-apis)
  - [Data Sources](#data-sources)
    - [General](#general)
    - [Cryptocurrencies](#cryptocurrencies-1)
  - [Data Science](#data-science)
  - [Databases](#databases)
  - [Graph Computation](#graph-computation)
  - [Machine Learning](#machine-learning)
  - [TimeSeries Analysis](#timeseries-analysis)
  - [Visualization](#visualization)
- [Strategies](#strategies)
  - [Bonds, Commodities, Currencies, Equities](#bonds-commodities-currencies-equities)
  - [Bonds, Commodities, Equities, REITs](#bonds-commodities-equities-reits)
  - [Bonds, Equities](#bonds-equities)
  - [Bonds, Equities, REITs](#bonds-equities-reits)
  - [Commodities](#commodities)
  - [Cryptos](#cryptos)
  - [Currencies](#currencies)
  - [Equities](#equities)
- [Videos](#videos)
- [Blogs](#blogs)
- [Courses](#courses)
- [Quant Frameworks in 14 Languages](../repo/quant-repo.md)
- [Research Reproduction](../repo/reproduce.md)

---

# Libraries and Packages

*The following **97 libraries and packages** can be used to build trading bots, backtesting engines, technical indicator tools, pricers, and more. Each library is categorized by programming language and sorted by GitHub stars (descending).*

## Backtesting and Live Trading

### General - Event Driven Frameworks

| Repository | Description | Stars | Language |
|-----------|-------------|-------|----------|
| [vnpy](https://github.com/vnpy/vnpy) | An open-source quantitative trading system development framework built on Python, first released in January 2015 and grown into a full-featured quantitative trading platform | ![GitHub stars](https://badgen.net/github/stars/vnpy/vnpy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [zipline](https://github.com/quantopian/zipline) | A Pythonic algorithmic trading library with an event-driven backtesting model | ![GitHub stars](https://badgen.net/github/stars/quantopian/zipline) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [backtrader](https://github.com/mementum/backtrader) | An event-driven Python backtesting library for trading strategies | ![GitHub stars](https://badgen.net/github/stars/mementum/backtrader) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [QUANTAXIS](https://github.com/QUANTAXIS/QUANTAXIS) | A fully local quantitative solution supporting task scheduling, distributed deployment for stocks/futures/options/HK stocks/crypto data, backtesting, simulation, trading, visualization, and multi-account management | ![GitHub stars](https://badgen.net/github/stars/QUANTAXIS/QUANTAXIS) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [QuantConnect](https://github.com/QuantConnect/Lean) | The Lean algorithmic trading engine by QuantConnect (Python, C#) | ![GitHub stars](https://badgen.net/github/stars/QuantConnect/Lean) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Rqalpha](https://github.com/ricequant/rqalpha) | An extensible, replaceable Python algorithmic backtesting & trading framework supporting multiple financial instruments | ![GitHub stars](https://badgen.net/github/stars/ricequant/rqalpha) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [finmarketpy](https://github.com/cuemacro/finmarketpy) | A Python library for backtesting trading strategies and analyzing financial markets (formerly pythalesians) | ![GitHub stars](https://badgen.net/github/stars/cuemacro/finmarketpy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [backtesting.py](https://github.com/kernc/backtesting.py) | A Python backtesting framework for inferring the viability of trading strategies on historical data -- lighter, faster, more user-friendly, and more interactive than existing alternatives | ![GitHub stars](https://badgen.net/github/stars/kernc/backtesting.py) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [zvt](https://github.com/zvtvz/zvt) | A modular quantitative framework | ![GitHub stars](https://badgen.net/github/stars/zvtvz/zvt) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [WonderTrader](https://github.com/wondertrader/wondertrader) | WonderTrader -- an all-in-one framework for quantitative research and trading | ![GitHub stars](https://badgen.net/github/stars/wondertrader/wondertrader) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [nautilus_trader](https://github.com/nautechsystems/nautilus_trader) | A high-performance algorithmic trading platform and event-driven backtesting framework | ![GitHub stars](https://badgen.net/github/stars/nautechsystems/nautilus_trader) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [PandoraTrader](https://github.com/pegasusTrader/PandoraTrader) | A C++ high-frequency quantitative trading platform supporting multiple trading APIs and cross-platform deployment | ![GitHub stars](https://badgen.net/github/stars/pegasusTrader/PandoraTrader) | ![made-with-c++](https://img.shields.io/badge/Made%20with-c++-1f425f.svg) |
| [HFTBacktest](https://github.com/nkaz001/hftbacktest) | High-precision HFT data backtesting in Python + Numba | ![GitHub stars](https://badgen.net/github/stars/nkaz001/hftbacktest) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [aat](https://github.com/AsyncAlgoTrading/aat) | An asynchronous, event-driven Python framework for algorithmic trading strategies with optional C++ acceleration and multi-exchange live trading support | ![GitHub stars](https://badgen.net/github/stars/AsyncAlgoTrading/aat) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [sdoosa-algo-trade-python](https://github.com/sreenivasdoosa/sdoosa-algo-trade-python) | Primarily aimed at quantitative trading beginners, using Python to practice writing trading algorithms | ![GitHub stars](https://badgen.net/github/stars/sreenivasdoosa/sdoosa-algo-trade-python) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [lumibot](https://github.com/Lumiwealth/lumibot) | A simple but useful backtesting and sample live trading framework (slightly slower performance) | ![GitHub stars](https://badgen.net/github/stars/Lumiwealth/lumibot) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [quanttrader](https://github.com/letianzj/quanttrader) | An event-driven Python backtesting and live trading framework, similar to backtesting.py | ![GitHub stars](https://badgen.net/github/stars/letianzj/quanttrader) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [gobacktest](https://github.com/gobacktest/gobacktest) | An event-driven backtesting framework implemented in Go | ![GitHub stars](https://badgen.net/github/stars/gobacktest/gobacktest) | ![made-with-go](https://img.shields.io/badge/Made%20with-Go-1f425f.svg) |
| [FlashFunk](https://github.com/HFQR/FlashFunk) | A high-performance runtime written in Rust | ![GitHub stars](https://badgen.net/github/stars/HFQR/FlashFunk) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |

### General - Vector Based Frameworks

| Repository | Description | Stars | Language |
|-----------|-------------|-------|----------|
| [vectorbt](https://github.com/polakowo/vectorbt) | A backtesting tool built entirely on pandas and NumPy with Numba acceleration, capable of testing thousands of strategies at high speed and scale | ![GitHub stars](https://badgen.net/github/stars/polakowo/vectorbt) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [pysystemtrade](https://github.com/robcarver17/pysystemtrade) | Rob Carver's Python systematic trading implementation from his book *Systematic Trading* | ![GitHub stars](https://badgen.net/github/stars/robcarver17/pysystemtrade) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [bt](https://github.com/pmorissette/bt) | A flexible Python backtesting library using a tree-like strategy structure | ![GitHub stars](https://badgen.net/github/stars/pmorissette/bt) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

### Cryptocurrencies

| Repository | Description | Stars | Language |
|-----------|-------------|-------|----------|
| [Freqtrade](https://github.com/freqtrade/freqtrade) | A free, open-source crypto trading bot written in Python, supporting major exchanges with Telegram control, backtesting, visualization, money management, and ML-optimized strategies | ![GitHub stars](https://badgen.net/github/stars/freqtrade/freqtrade) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Jesse](https://github.com/jesse-ai/jesse) | An advanced crypto trading framework designed to simplify strategy research and development | ![GitHub stars](https://badgen.net/github/stars/jesse-ai/jesse) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [OctoBot](https://github.com/Drakkar-Software/OctoBot) | A crypto trading bot supporting technical analysis, arbitrage, and social trading with an advanced web interface | ![GitHub stars](https://badgen.net/github/stars/Drakkar-Software/OctoBot) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Kelp](https://github.com/stellar/kelp) | A free, open-source trading bot for the Stellar DEX and 100+ centralized exchanges | ![GitHub stars](https://badgen.net/github/stars/stellar/kelp) | ![made-with-go](https://img.shields.io/badge/Made%20with-Go-1f425f.svg) |
| [openlimits](https://github.com/nash-io/openlimits) | A high-performance Rust crypto trading API supporting multiple exchanges with multi-language bindings | ![GitHub stars](https://badgen.net/github/stars/nash-io/openlimits) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [bTrader](https://github.com/gabriel-milan/btrader) | A Binance triangular arbitrage trading bot | ![GitHub stars](https://badgen.net/github/stars/gabriel-milan/btrader) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [crypto-crawler-rs](https://github.com/crypto-crawler/crypto-crawler-rs) | Collects order book and trade messages from cryptocurrency exchanges | ![GitHub stars](https://badgen.net/github/stars/crypto-crawler/crypto-crawler-rs) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [Hummingbot](https://github.com/CoinAlpha/hummingbot) | A crypto trading client focused on market making | ![GitHub stars](https://badgen.net/github/stars/CoinAlpha/hummingbot) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [cryptotrader-core](https://github.com/monomadic/cryptotrader-core) | A simple, easy-to-use crypto exchange REST API client in Rust | ![GitHub stars](https://badgen.net/github/stars/monomadic/cryptotrader-core) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |

## Trading Bots

*Trading bots and alpha models. Some projects may be outdated or unmaintained.*

| Repository | Description | Stars | Language |
|-----------|-------------|-------|----------|
| [Blackbird](https://github.com/butor/blackbird) | Blackbird Bitcoin cross-exchange arbitrage bot: a market-neutral long/short strategy | ![GitHub stars](https://badgen.net/github/stars/butor/blackbird) | ![made-with-c++](https://img.shields.io/badge/Made%20with-c++-1f425f.svg) |
| [bitcoin-arbitrage](https://github.com/maxme/bitcoin-arbitrage) | A Bitcoin arbitrage opportunity detector | ![GitHub stars](https://badgen.net/github/stars/maxme/bitcoin-arbitrage) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [ThetaGang](https://github.com/brndnmtthws/thetagang) | A theta (premium-selling) strategy bot for IBKR | ![GitHub stars](https://badgen.net/github/stars/brndnmtthws/thetagang) | ![made-with-typescript](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [czsc](https://github.com/waditu/czsc) | Technical analysis toolkit based on "Chan Theory"; stocks/futures/quant trading | ![GitHub stars](https://badgen.net/github/stars/waditu/czsc) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [R2 Bitcoin Arbitrager](https://github.com/bitrinjani/r2) | An automated Bitcoin arbitrage trading system built with Node.js + TypeScript | ![GitHub stars](https://badgen.net/github/stars/bitrinjani/r2) | ![made-with-typescript](https://img.shields.io/badge/Made%20with-TypeScript-1f425f.svg) |
| [analyzingalpha](https://github.com/leosmigel/analyzingalpha) | Implementations of simple trading strategies | ![GitHub stars](https://badgen.net/github/stars/leosmigel/analyzingalpha) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [PyTrendFollow](https://github.com/chrism2671/PyTrendFollow) | Systematic futures trading using trend-following methods | ![GitHub stars](https://badgen.net/github/stars/chrism2671/PyTrendFollow) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

## Analytics

### Indicators

*Libraries for indicators that forecast future price movements.*

| Repository | Description | Stars | Language |
|-----------|-------------|-------|----------|
| [ta-lib](https://github.com/mrjbq7/ta-lib) | Technical analysis of financial market data | ![GitHub stars](https://badgen.net/github/stars/mrjbq7/ta-lib) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [go-tart](https://github.com/iamjinlei/go-tart) | A Go implementation of [ta-lib](https://github.com/mrjbq7/ta-lib) with streaming update support | ![GitHub stars](https://badgen.net/github/stars/iamjinlei/go-tart) | ![made-with-go](https://img.shields.io/badge/Made%20with-go-1f425f.svg) |
| [pandas-ta](https://github.com/twopirllc/pandas-ta) | Pandas Technical Analysis extension with 130+ indicators and 60+ TA-Lib candlestick patterns | ![GitHub stars](https://badgen.net/github/stars/twopirllc/pandas-ta) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [finta](https://github.com/peerchemist/finta) | Common financial technical indicators implemented in Pandas | ![GitHub stars](https://badgen.net/github/stars/peerchemist/finta) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [ta-rust](https://github.com/greyblake/ta-rs) | A technical analysis library for Rust | ![GitHub stars](https://badgen.net/github/stars/greyblake/ta-rs) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |

### Metrics Computation

*Libraries for computing various financial metrics.*

| Repository | Description | Stars | Language |
|-----------|-------------|-------|----------|
| [quantstats](https://github.com/ranaroussi/quantstats) | A Python library for portfolio analytics in quantitative research | ![GitHub stars](https://badgen.net/github/stars/ranaroussi/quantstats) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [ffn](https://github.com/pmorissette/ffn) | A Python financial functions library | ![GitHub stars](https://badgen.net/github/stars/pmorissette/ffn) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

### Optimization

| Repository | Description | Stars | Language |
|-----------|-------------|-------|----------|
| [PyPortfolioOpt](https://github.com/robertmartin8/PyPortfolioOpt) | Portfolio optimization in Python, including classical efficient frontier, Black-Litterman, Hierarchical Risk Parity, and more | ![GitHub stars](https://badgen.net/github/stars/robertmartin8/PyPortfolioOpt) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Riskfolio-Lib](https://github.com/dcajasn/Riskfolio-Lib) | A Python library for portfolio optimization and quantitative asset allocation | ![GitHub stars](https://badgen.net/github/stars/dcajasn/Riskfolio-Lib) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [empyrial](https://github.com/ssantoshp/Empyrial) | An open-source Python quantitative investment library for financial institutions and individuals, released March 2021 | ![GitHub stars](https://badgen.net/github/stars/ssantoshp/Empyrial) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Deepdow](https://github.com/jankrepl/deepdow) | A Python library combining portfolio optimization with deep learning, exploring networks that perform weight allocation in a single forward pass | ![GitHub stars](https://badgen.net/github/stars/jankrepl/deepdow) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [spectre](https://github.com/Heerozh/spectre) | Portfolio optimization and quantitative asset allocation in Python | ![GitHub stars](https://badgen.net/github/stars/Heerozh/spectre) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

### Pricing

| Repository | Description | Stars | Language |
|-----------|-------------|-------|----------|
| [tf-quant-finance](https://github.com/google/tf-quant-finance) | Google's high-performance TensorFlow-based quantitative finance library | ![GitHub stars](https://badgen.net/github/stars/google/tf-quant-finance) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [FinancePy](https://github.com/domokane/FinancePy) | A Python finance library focused on pricing and risk management of financial derivatives, including fixed income, equity, FX, and credit | ![GitHub stars](https://badgen.net/github/stars/domokane/FinancePy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [PyQL](https://github.com/enthought/pyql) | Python bindings for the QuantLib pricing library | ![GitHub stars](https://badgen.net/github/stars/enthought/pyql) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

### Risk

| Repository | Description | Stars | Language |
|-----------|-------------|-------|----------|
| [pyfolio](https://github.com/quantopian/pyfolio) | Portfolio and risk analytics in Python | ![GitHub stars](https://badgen.net/github/stars/quantopian/pyfolio) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

## Broker APIs

| Repository | Description | Stars | Language |
|-----------|-------------|-------|----------|
| [ccxt](https://github.com/ccxt/ccxt) | A cryptocurrency trading API supporting JavaScript, Python, and PHP, integrating 100+ exchanges | ![GitHub stars](https://badgen.net/github/stars/ccxt/ccxt) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Ib_insync](https://github.com/erdewit/ib_insync) | A Python sync/async framework for Interactive Brokers | ![GitHub stars](https://badgen.net/github/stars/erdewit/ib_insync) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Coinnect](https://github.com/hugues31/coinnect) | A Rust library providing full REST API access to major crypto exchanges | ![GitHub stars](https://badgen.net/github/stars/hugues31/coinnect) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [PENDAX](https://github.com/CompendiumFi/PENDAX-SDK) | A JavaScript SDK for FTX, FTXUS, OKX, Bybit, and other exchanges, supporting trading, data, and WebSocket | ![GitHub stars](https://badgen.net/github/stars/CompendiumFi/PENDAX-SDK) | ![made-with-javascript](https://img.shields.io/badge/Made%20with-Javascript-1f425f.svg) |

## Data Sources

### General

| Repository | Description | Stars | Language |
|-----------|-------------|-------|----------|
| [OpenBB Terminal](https://github.com/OpenBB-finance/OpenBBTerminal) | Investment research for everyone, anywhere | ![GitHub stars](https://badgen.net/github/stars/OpenBB-finance/OpenBBTerminal) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [TuShare](https://github.com/waditu/tushare) | A tool for obtaining Chinese stock historical data | ![GitHub stars](https://badgen.net/github/stars/waditu/tushare) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [yfinance](https://github.com/ranaroussi/yfinance) | Multi-threaded, Pythonic way to download Yahoo! Finance market data | ![GitHub stars](https://badgen.net/github/stars/ranaroussi/yfinance) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [AkShare](https://github.com/akfamily/akshare) | An elegant and simple Python financial data interface library -- built for humans! | ![GitHub stars](https://badgen.net/github/stars/akfamily/akshare) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [pandas-datareader](https://github.com/pydata/pandas-datareader) | A Pandas extension for fetching remote data, compatible with multiple Pandas versions | ![GitHub stars](https://badgen.net/github/stars/pydata/pandas-datareader) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Quandl](https://github.com/quandl/quandl-python) | Access millions of financial and economic datasets from hundreds of publishers with a single free API | ![GitHub stars](https://badgen.net/github/stars/quandl/quandl-python) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [findatapy](https://github.com/cuemacro/findatapy) | An easy-to-use Python API for downloading market data from Quandl, Bloomberg, Yahoo, Google, and more | ![GitHub stars](https://badgen.net/github/stars/cuemacro/findatapy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Investpy](https://github.com/alvarobartt/investpy) | A Python tool for extracting financial data from Investing.com | ![GitHub stars](https://badgen.net/github/stars/alvarobartt/investpy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Fundamental Analysis Data](https://github.com/JerBouma/FundamentalAnalysis) | A comprehensive fundamental analysis package with 20 years of company profiles, financial statements, ratios, and stock data for 20,000+ companies | ![GitHub stars](https://badgen.net/github/stars/JerBouma/FundamentalAnalysis) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Wallstreet](https://github.com/mcdallas/wallstreet) | Real-time stock and option data | ![GitHub stars](https://badgen.net/github/stars/mcdallas/wallstreet) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

### Cryptocurrencies

| Repository | Description | Stars | Language |
|-----------|-------------|-------|----------|
| [Cryptofeed](https://github.com/bmoscon/cryptofeed) | Asyncio-based crypto exchange WebSocket data collection (order books, trade feeds) | ![GitHub stars](https://badgen.net/github/stars/bmoscon/cryptofeed) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Gekko-Datasets](https://github.com/xFFFFF/Gekko-Datasets) | Gekko trading bot datasets with downloadable SQLite historical files | ![GitHub stars](https://badgen.net/github/stars/xFFFFF/Gekko-Datasets) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [CryptoInscriber](https://github.com/Optixal/CryptoInscriber) | A real-time crypto historical trade data recorder for any exchange | ![GitHub stars](https://badgen.net/github/stars/Optixal/CryptoInscriber) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Crypto Lake](https://github.com/crypto-lake/lake-api) | High-frequency order book & trade data for crypto | ![GitHub stars](https://badgen.net/github/stars/crypto-lake/lake-api) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

## Data Science

| Repository | Description | Stars | Language |
|-----------|-------------|-------|----------|
| [TensorFlow](https://github.com/tensorflow/tensorflow) | An open-source platform for machine learning | ![GitHub stars](https://badgen.net/github/stars/tensorflow/tensorflow) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Pytorch](https://github.com/pytorch/pytorch) | Tensors and dynamic neural networks in Python with GPU acceleration | ![GitHub stars](https://badgen.net/github/stars/pytorch/pytorch) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Keras](https://github.com/keras-team/keras) | Deep learning for humans | ![GitHub stars](https://badgen.net/github/stars/keras-team/keras) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Scikit-learn](https://github.com/scikit-learn/scikit-learn) | Machine learning in Python | ![GitHub stars](https://badgen.net/github/stars/scikit-learn/scikit-learn) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Pandas](https://github.com/pandas-dev/pandas) | Powerful, flexible data analysis and manipulation library for Python | ![GitHub stars](https://badgen.net/github/stars/pandas-dev/pandas) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Numpy](https://github.com/numpy/numpy) | The fundamental package for scientific computing with Python | ![GitHub stars](https://badgen.net/github/stars/numpy/numpy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Scipy](https://github.com/scipy/scipy) | Fundamental algorithms for scientific computing in Python | ![GitHub stars](https://badgen.net/github/stars/scipy/scipy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [PyMC](https://github.com/pymc-devs/pymc) | Probabilistic programming in Python: Bayesian modeling and probabilistic ML powered by Aesara | ![GitHub stars](https://badgen.net/github/stars/pymc-devs/pymc) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Cvxpy](https://github.com/cvxpy/cvxpy) | An embedded convex optimization modeling language for Python | ![GitHub stars](https://badgen.net/github/stars/cvxpy/cvxpy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

## Databases

| Repository | Description | Stars | Language |
|-----------|-------------|-------|----------|
| [Marketstore](https://github.com/alpacahq/marketstore) | A DataFrame server for financial time-series data | ![GitHub stars](https://badgen.net/github/stars/alpacahq/marketstore) | ![made-with-go](https://img.shields.io/badge/Made%20with-Go-1f425f.svg) |
| [Tectonicdb](https://github.com/0b01/tectonicdb) | A fast, highly compressed, standalone database and streaming protocol for order book tick data | ![GitHub stars](https://badgen.net/github/stars/0b01/tectonicdb) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [ArcticDB (Man Group)](https://github.com/man-group/arcticdb) | High-performance data store for time-series and tick data | ![GitHub stars](https://badgen.net/github/stars/man-group/ArcticDB) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Timeplus Proton](https://github.com/timeplus-io/proton) | A high-performance streaming-batch unified database built on ClickHouse, with columnar storage, incremental computation, millisecond-level push, and UDFs -- ideal for SQL-based complex event processing, factor computation, and backtesting | ![GitHub stars](https://badgen.net/github/stars/timeplus-io/proton) | ![made-with-cpp](https://img.shields.io/badge/Made%20with-C%2B%2B-1f425f.svg) |

## Graph Computation

| Repository | Description | Stars | Language |
|-----------|-------------|-------|----------|
| [Ray](https://github.com/ray-project/ray) | An open-source framework providing simple, universal APIs for building distributed applications | ![GitHub stars](https://badgen.net/github/stars/ray-project/ray) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Dask](https://github.com/dask/dask) | A parallel computing library in Python with a Pandas-like API for task scheduling | ![GitHub stars](https://badgen.net/github/stars/dask/dask) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Incremental (JaneStreet)](https://github.com/janestreet/incremental) | A library for efficiently updating complex computations based on input changes, inspired by Umut Acar's work on self-adjusting computation | ![GitHub stars](https://badgen.net/github/stars/janestreet/incremental) | ![made-with-ocaml](https://img.shields.io/badge/Made%20with-Ocaml-1f425f.svg) |
| [Man MDF](https://github.com/man-group/mdf) | A Python dataflow programming toolkit | ![GitHub stars](https://badgen.net/github/stars/man-group/mdf) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [GraphKit](https://github.com/yahoo/graphkit) | A lightweight Python module for creating and running ordered computation graphs | ![GitHub stars](https://badgen.net/github/stars/yahoo/graphkit) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Tributary](https://github.com/timkpaine/tributary) | Streaming reactive and dataflow graphs in Python | ![GitHub stars](https://badgen.net/github/stars/timkpaine/tributary) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

## Machine Learning

| Repository | Description | Stars | Language |
|-----------|-------------|-------|----------|
| [QLib (Microsoft)](https://github.com/microsoft/qlib) | An AI-oriented quantitative investment platform to empower research and deployment of AI technologies in quantitative investing | ![GitHub stars](https://badgen.net/github/stars/microsoft/qlib) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [FinRL](https://github.com/AI4Finance-Foundation/FinRL) | The first open-source framework demonstrating the great potential of deep reinforcement learning in quantitative finance | ![GitHub stars](https://badgen.net/github/stars/AI4Finance-Foundation/FinRL) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [MlFinLab (Hudson & Thames)](https://github.com/hudson-and-thames/mlfinlab) | Tools to help portfolio managers and traders leverage machine learning, providing reproducible, interpretable, and easy-to-use modules | ![GitHub stars](https://badgen.net/github/stars/hudson-and-thames/mlfinlab) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [TradingGym](https://github.com/Yvictor/TradingGym) | A trading and backtesting environment for training reinforcement learning agents or simple rule-based algorithms | ![GitHub stars](https://badgen.net/github/stars/Yvictor/TradingGym) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Stock Trading Bot using Deep Q-Learning](https://github.com/pskrunner14/trading-bot) | A stock trading bot using Deep Q-Learning | ![GitHub stars](https://badgen.net/github/stars/pskrunner14/trading-bot) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

## TimeSeries Analysis

| Repository | Description | Stars | Language |
|-----------|-------------|-------|----------|
| [Facebook Prophet](https://github.com/facebook/prophet) | A high-quality forecasting tool for time-series data with multiple seasonality and linear or non-linear growth | ![GitHub stars](https://badgen.net/github/stars/facebook/prophet) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [statsmodels](https://github.com/statsmodels/statsmodels) | A Python module for data exploration, statistical model estimation, and statistical tests | ![GitHub stars](https://badgen.net/github/stars/statsmodels/statsmodels) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [tsfresh](https://github.com/blue-yonder/tsfresh) | Automatic extraction of relevant features from time series | ![GitHub stars](https://badgen.net/github/stars/blue-yonder/tsfresh) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [pmdarima](https://github.com/alkaline-ml/pmdarima) | A statistical library that bridges the gap in Python time-series analysis, including an equivalent of R's auto.arima | ![GitHub stars](https://badgen.net/github/stars/alkaline-ml/pmdarima) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

## Visualization

| Repository | Description | Stars | Language |
|-----------|-------------|-------|----------|
| [D-Tale (Man Group)](https://github.com/man-group/dtale) | Combines a Flask backend with a React frontend for easy viewing and analysis of Pandas data structures | ![GitHub stars](https://badgen.net/github/stars/man-group/dtale) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [mplfinance](https://github.com/matplotlib/mplfinance) | Financial market data visualization using Matplotlib | ![GitHub stars](https://badgen.net/github/stars/matplotlib/mplfinance) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [btplotting](https://github.com/happydasch/btplotting) | Visualization for backtrader backtesting, optimization results, and live data | ![GitHub stars](https://badgen.net/github/stars/happydasch/btplotting) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

---

# Strategies

## Bonds, Commodities, Currencies, Equities

| Title | Sharpe Ratio | Volatility | Rebalancing | Implementation | Source |
|-------|-------------|-----------|-------------|---------------|--------|
| Time Series Momentum Effect | `0.576` | `20.5%` | `Monthly` | [QuantConnect](./static/strategies/time-series-momentum-effect.py) | [Paper](https://pages.stern.nyu.edu/~lpederse/papers/TimeSeriesMomentum.pdf) |
| Short Term Reversal with Futures | `-0.05` | `12.3%` | `Weekly` | [QuantConnect](./static/strategies/asset-class-momentum-rotational-system.py) | [Paper](https://ideas.repec.org/a/eee/jbfina/v28y2004i6p1337-1361.html) |

## Bonds, Commodities, Equities, REITs

| Title | Sharpe Ratio | Volatility | Rebalancing | Implementation | Source |
|-------|-------------|-----------|-------------|---------------|--------|
| Asset Class Trend-Following | `0.502` | `10.4%` | `Monthly` | [QuantConnect](./static/strategies/asset-class-trend-following.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=962461) |
| Momentum Asset Allocation Strategy | `0.321` | `11%` | `Monthly` | [QuantConnect](./static/strategies/asset-class-trend-following.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1585517) |

## Bonds, Equities

| Title | Sharpe Ratio | Volatility | Rebalancing | Implementation | Source |
|-------|-------------|-----------|-------------|---------------|--------|
| Paired Switching | `0.691` | `9.5%` | `Quarterly` | [QuantConnect](./static/strategies/paired-switching.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1917044) |
| FED Model | `0.369` | `14.3%` | `Monthly` | [QuantConnect](./static/strategies/fed-model.py) | [Paper](https://www.researchgate.net/publication/228267011_The_FED_Model_and_Expected_Asset_Returns) |

## Bonds, Equities, REITs

| Title | Sharpe Ratio | Volatility | Rebalancing | Implementation | Source |
|-------|-------------|-----------|-------------|---------------|--------|
| Value and Momentum Factors across Asset Classes | `0.155` | `9.8%` | `Monthly` | [QuantConnect](./static/strategies/value-and-momentum-factors-across-asset-classes.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1079975) |

## Commodities

| Title | Sharpe Ratio | Volatility | Rebalancing | Implementation | Source |
|-------|-------------|-----------|-------------|---------------|--------|
| Skewness Effect in Commodities | `0.482` | `17.7%` | `Monthly` | [QuantConnect](./static/strategies/skewness-effect-in-commodities.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2671165) |
| Return Asymmetry Effect in Commodity Futures | `0.239` | `13.4%` | `Monthly` | [QuantConnect](./static/strategies/return-asymmetry-effect-in-commodity-futures.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3918896) |
| Momentum Effect in Commodities | `0.14` | `20.3%` | `Monthly` | [QuantConnect](./static/strategies/momentum-effect-in-commodities.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=702281) |
| Term Structure Effect in Commodities | `0.128` | `23.1%` | `Monthly` | [QuantConnect](./static/strategies/term-structure-effect-in-commodities.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1127213) |
| Trading WTI/BRENT Spread | `-0.199` | `11.6%` | `Daily` | [QuantConnect](./static/strategies/trading-wti-brent-spread.py) | [Paper](https://link.springer.com/article/10.1057/jdhf.2009.24) |

## Cryptos

| Title | Sharpe Ratio | Volatility | Rebalancing | Implementation | Source |
|-------|-------------|-----------|-------------|---------------|--------|
| Overnight Seasonality in Bitcoin | `0.892` | `20.8%` | `Intraday` | [QuantConnect](./static/strategies/intraday-seasonality-in-bitcoin.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4081000) |
| Rebalancing Premium in Cryptocurrencies | `0.698` | `27.5%` | `Daily` | [QuantConnect](./static/strategies/rebalancing-premium-in-cryptocurrencies.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3982120) |

## Currencies

| Title | Sharpe Ratio | Volatility | Rebalancing | Implementation | Source |
|-------|-------------|-----------|-------------|---------------|--------|
| FX Carry Trade | `0.254` | `7.8%` | `Monthly` | [QuantConnect](./static/strategies/fx-carry-trade.py) | [Paper](http://globalmarkets.db.com/new/docs/dbCurrencyReturns_March2009.pdf) |
| Dollar Carry Trade | `0.113` | `5.8%` | `Monthly` | [QuantConnect](./static/strategies/dollar-carry-trade.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1541230) |
| Currency Momentum Factor | `-0.01` | `6.7%` | `Monthly` | [QuantConnect](./static/strategies/currency-momentum-factor.py) | [Paper](http://globalmarkets.db.com/new/docs/dbCurrencyReturns_March2009.pdf) |
| Currency Value Factor -- PPP Strategy | `-0.103` | `5%` | `Quarterly` | [QuantConnect](./static/strategies/currency-value-factor-ppp-strategy.py) | [Paper](http://globalmarkets.db.com/new/docs/dbCurrencyReturns_March2009.pdf) |

## Equities

| Title | Sharpe Ratio | Volatility | Rebalancing | Implementation | Source |
|-------|-------------|-----------|-------------|---------------|--------|
| Asset Growth Effect | `0.835` | `10.2%` | `Yearly` | [QuantConnect](./static/strategies/asset-growth-effect.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1335524) |
| Short Term Reversal Effect in Stocks | `0.816` | `21.4%` | `Weekly` | [QuantConnect](./static/strategies/short-term-reversal-in-stocks.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1605049) |
| Reversal During Earnings-Announcements | `0.785` | `25.7%` | `Daily` | [QuantConnect](./static/strategies/reversal-during-earnings-announcements.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2275982) |
| Size Factor -- Small Capitalization Stocks Premium | `0.747` | `11.1%` | `Yearly` | [QuantConnect](./static/strategies/small-capitalization-stocks-premium-anomaly.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3177539) |
| Low Volatility Factor Effect in Stocks | `0.717` | `11.5%` | `Monthly` | [QuantConnect](./static/strategies/low-volatility-factor-effect-in-stocks.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=980865) |
| How to Use Lexical Density of Company Filings | `0.688` | `10.4%` | `Monthly` | [QuantConnect](./static/strategies/how-to-use-lexical-density-of-company-filings.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3921091) |
| Volatility Risk Premium Effect | `0.637` | `13.2%` | `Monthly` | [QuantConnect](./static/strategies/volatility-risk-premium-effect.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=189840) |
| Pairs Trading with Stocks | `0.634` | `8.5%` | `Daily` |  | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=141615) |
| Crude Oil Predicts Equity Returns | `0.599` | `11.5%` | `Monthly` | [QuantConnect](./static/strategies/crude-oil-predicts-equity-returns.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=460500) |
| Betting Against Beta Factor in Stocks | `0.594` | `18.9%` | `Monthly` | [QuantConnect](./static/strategies/betting-against-beta-factor-in-stocks.py) | [Paper](https://pages.stern.nyu.edu/~lpederse/papers/BettingAgainstBeta.pdf) |
| Trend-following Effect in Stocks | `0.569` | `15.2%` | `Daily` | [QuantConnect](./static/strategies/trend-following-effect-in-stocks.py) | [Paper](https://www.cis.upenn.edu/~mkearns/finread/trend.pdf) |
| ESG Factor Momentum Strategy | `0.559` | `21.8%` | `Monthly` | [QuantConnect](./static/strategies/esg-factor-momentum-strategy.py) | [Paper](https://www.semanticscholar.org/paper/Can-ESG-Add-Alpha-An-Analysis-of-ESG-Tilt-and-Nagy-Kassam/64f77da4f8ce5906a73ffe4e9eec7c49c0960acc) |
| Value (Book-to-Market) Factor | `0.526` | `11.9%` | `Monthly` | [QuantConnect](./static/strategies/value-book-to-market-factor.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2595747) |
| Soccer Clubs' Stocks Arbitrage | `0.515` | `14.2%` | `Daily` | [QuantConnect](./static/strategies/soccer-clubs-stocks-arbitrage.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1343685) |
| Synthetic Lending Rates Predict Subsequent Market Return | `0.494` | `13.7%` | `Daily` | [QuantConnect](./static/strategies/synthetic-lending-rates-predict-subsequent-market-return.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3976307) |
| Option-Expiration Week Effect | `0.452` | `5%` | `Weekly` | [QuantConnect](./static/strategies/option-expiration-week-effect.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1571786) |
| Dispersion Trading | `0.432` | `8.1%` | `Monthly` | [QuantConnect](./static/strategies/dispersion-trading.py) | [Paper](https://www.academia.edu/16327015/EQUILIBRIUM_INDEX_AND_SINGLE_STOCK_VOLATILITY_RISK_PREMIA) |
| Momentum in Mutual Fund Returns | `0.414` | `13.6%` | `Quarterly` | [QuantConnect](./static/strategies/momentum-in-mutual-fund-returns.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1462408) |
| Sector Momentum -- Rotational System | `0.401` | `14.1%` | `Monthly` | [QuantConnect](./static/strategies/sector-momentum-rotational-system.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1585517) |
| Combining Smart Factors Momentum and Market Portfolio | `0.388` | `8.2%` | `Monthly` | [QuantConnect](./static/strategies/combining-smart-factors-momentum-and-market-portfolio.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3745517) |
| Momentum and Reversal Combined with Volatility Effect in Stocks | `0.375` | `17%` | `Monthly` | [QuantConnect](./static/strategies/momentum-and-reversal-combined-with-volatility-effect-in-stocks.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1679464) |
| Market Sentiment and an Overnight Anomaly | `0.369` | `3.6%` | `Daily` | [QuantConnect](./static/strategies/market-sentiment-and-an-overnight-anomaly.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3829582) |
| January Barometer | `0.365` | `7.4%` | `Monthly` | [QuantConnect](./static/strategies/january-barometer.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1436516) |
| R&D Expenditures and Stock Returns | `0.354` | `8.1%` | `Yearly` | [QuantConnect](./static/strategies/rd-expenditures-and-stock-returns.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=227564) |
| Value Factor -- CAPE Effect within Countries | `0.351` | `20.2%` | `Yearly` | [QuantConnect](./static/strategies/value-factor-effect-within-countries.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2129474) |
| 12 Month Cycle in Cross-Section of Stocks Returns | `0.34` | `43.7%` | `Monthly` | [QuantConnect](./static/strategies/12-month-cycle-in-cross-section-of-stocks-returns.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=687022) |
| Turn of the Month in Equity Indexes | `0.305` | `7.2%` | `Daily` | [QuantConnect](./static/strategies/turn-of-the-month-in-equity-indexes.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=917884) |
| Payday Anomaly | `0.269` | `3.8%` | `Daily` | [QuantConnect](./static/strategies/payday-anomaly.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3257064) |
| Pairs Trading with Country ETFs | `0.257` | `5.7%` | `Daily` | [QuantConnect](./static/strategies/pairs-trading-with-country-etfs.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1958546) |
| Residual Momentum Factor | `0.24` | `9.7%` | `Monthly` | [QuantConnect](./static/strategies/residual-momentum-factor.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2319861) |
| Earnings Announcement Premium | `0.192` | `3.7%` | `Monthly` | [QuantConnect](./static/strategies/earnings-announcement-premium.py) | [Paper](https://www.nber.org/system/files/working_papers/w13090/w13090.pdf) |
| ROA Effect within Stocks | `0.155` | `8.7%` | `Monthly` | [QuantConnect](./static/strategies/roa-effect-within-stocks.py) | [Paper](https://static1.squarespace.com/static/5e6033a4ea02d801f37e15bb/t/5f61583e88f43b7d5b7196b5/1600215105801/Chen_Zhang_JF.pdf) |
| 52-Weeks High Effect in Stocks | `0.153` | `19%` | `Monthly` | [QuantConnect](./static/strategies/52-weeks-high-effect-in-stocks.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1787378) |
| Combining Fundamental FSCORE and Equity Short-Term Reversals | `0.153` | `17.6%` | `Monthly` | [QuantConnect](./static/strategies/combining-fundamental-fscore-and-equity-short-term-reversals.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3097420) |
| Betting Against Beta Factor in International Equities | `0.142` | `9.1%` | `Monthly` | [QuantConnect](./static/strategies/betting-against-beta-factor-in-country-equity-indexes.py) | [Paper](https://pages.stern.nyu.edu/~lpederse/papers/BettingAgainstBeta.pdf) |
| Consistent Momentum Strategy | `0.128` | `28.8%` | `6 Months` | [QuantConnect](./static/strategies/consistent-momentum-strategy.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2652592) |
| Short Interest Effect -- Long-Short Version | `0.079` | `6.6%` | `Monthly` | [QuantConnect](./static/strategies/short-interest-effect-long-short-version.py) | [Paper](https://www.semanticscholar.org/paper/Why-Do-Short-Interest-Levels-Predict-Stock-Returns-Boehmer-Erturk/06418ef437dc7156229532a97d0f8392373eb297?p2df) |
| Momentum Factor Combined with Asset Growth Effect | `0.058` | `25.1%` | `Monthly` | [QuantConnect](./static/strategies/momentum-factor-combined-with-asset-growth-effect.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1684767) |
| Momentum Factor Effect in Stocks | `-0.008` | `21.8%` | `Monthly` | [QuantConnect](./static/strategies/momentum-factor-effect-in-stocks.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2435323) |
| Momentum Factor and Style Rotation Effect | `-0.056` | `10%` | `Monthly` | [QuantConnect](./static/strategies/momentum-factor-and-style-rotation-effect.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1276815) |
| Earnings Announcements Combined with Stock Repurchases | `-0.16` | `0.1%` | `Daily` | [QuantConnect](./static/strategies/earnings-announcements-combined-with-stock-repurchases.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2589966) |
| Earnings Quality Factor | `-0.18` | `28.7%` | `Yearly` | [QuantConnect](./static/strategies/earnings-quality-factor.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2179247) |
| Accrual Anomaly | `-0.272` | `13.7%` | `Yearly` | [QuantConnect](./static/strategies/accrual-anomaly.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=546108) |
| ESG, Price Momentum and Stochastic Optimization | `N/A` | `N/A` | `Monthly` |  | [Paper](https://quantpedia.com/strategies/esg-price-momentum-and-stochastic-optimization/) |
| The Positive Similarity of Company Filings and Stock Returns | `N/A` | `N/A` | `Monthly` |  | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3690461) |

---

# Videos

| Title | Likes |
|-------|-------|
| [Krish Naik - Machine learning tutorials and their Application in Stock Prediction](https://www.youtube.com/watch?v=H6du_pfuznE) | ![](https://badgen.net/badge/likes/6.3k/blue) |
| [QuantInsti Youtube - webinars about Machine Learning for trading](https://www.youtube.com/user/quantinsti/search?query=machine+learning) | ![](https://badgen.net/badge/likes/6.1k/blue) |
| [Siraj Raval - Videos about stock market prediction using Deep Learning](https://www.youtube.com/channel/UCWN3xxRkmTPmbKwht9FuE5A/search?query=trading) | ![](https://badgen.net/badge/likes/1.7k/blue) |
| [Quantopian - Webinars about Machine Learning for trading](https://www.youtube.com/channel/UC606MUq45P3zFLa4VGKbxsg/search?query=machine+learning) | ![](https://badgen.net/badge/likes/1.5k/blue) |
| [Sentdex - Machine Learning for Forex and Stock analysis and algorithmic trading](https://www.youtube.com/watch?v=v_L9jR8P-54&list=PLQVvvaa0QuDe6ZBtkCNWNUbdaBo2vA4RO) | ![](https://badgen.net/badge/likes/1.5k/blue) |
| [QuantNews - Machine Learning for Algorithmic Trading 3 part series](https://www.youtube.com/playlist?list=PLHJACfjILJ-91qkw5YC83S6COKGscctzz) | ![](https://badgen.net/badge/likes/806/blue) |
| [Sentdex - Python programming for Finance (a few videos including Machine Learning)](https://www.youtube.com/watch?v=Z-5wNWgRJpk&index=9&list=PLQVvvaa0QuDcOdF96TBtRtuQksErCEBYZ) | ![](https://badgen.net/badge/likes/735/blue) |
| [Chat with Traders EP042 - Machine learning for algorithmic trading with Bert Mouler](https://www.youtube.com/watch?v=i8FNO8r7PaE) | ![](https://badgen.net/badge/likes/687/blue) |
| [Tucker Balch - Applying Deep Reinforcement Learning to Trading](https://www.youtube.com/watch?v=Pka0DC_P17k) | ![](https://badgen.net/badge/likes/487/blue) |
| [Ernie Chan - Machine Learning for Quantitative Trading Webinar](https://www.youtube.com/watch?v=72aEDjwGMr8&t=1023s) | ![](https://badgen.net/badge/likes/436/blue) |
| [Chat with Traders EP147 - Detective work leading to viable trading strategies with Tom Starke](https://www.youtube.com/watch?v=JjXw9Mda7eY) | ![](https://badgen.net/badge/likes/407/blue) |
| [Chat with Traders EP142 - Algo trader using automation to bypass human flaws with Bert Mouler](https://www.youtube.com/watch?v=ofL66mh6Tw0) | ![](https://badgen.net/badge/likes/316/blue) |
| [Master Thesis presentation, Uni of Essex - Analyzing the Limit Order Book, A Deep Learning Approach](https://www.youtube.com/watch?v=qxSh2VFmRGw) | ![](https://badgen.net/badge/likes/264/blue) |
| [Howard Bandy - Machine Learning Trading System Development Webinar](https://www.youtube.com/watch?v=v729evhMpYk&t=1s) | ![](https://badgen.net/badge/likes/253/blue) |
| [Chat With Traders EP131 - Trading strategies, powered by machine learning with Morgan Slade](https://www.youtube.com/watch?v=EbWbeYu8zwg) | ![](https://badgen.net/badge/likes/229/blue) |
| [Chat with Traders Quantopian 5 - Good Uses of Machine Learning in Finance with Max Margenot](https://www.youtube.com/watch?v=Zj5sXWv9SDM) | ![](https://badgen.net/badge/likes/198/blue) |
| [Hitoshi Harada, CTO at Alpaca - Deep Learning in Finance Talk](https://www.youtube.com/watch?v=FoQKCeDuPiY) | ![](https://badgen.net/badge/likes/147/blue) |
| [Better System Trader EP028 - David Aronson shares research into indicators that identify Bull and Bear markets.](https://www.youtube.com/watch?v=Q4rV0Y9NokI) | ![](https://badgen.net/badge/likes/97/blue) |
| [Prediction Machines - Deep Learning with Python in Finance Talk](https://www.youtube.com/watch?v=xvm-M-R2fZY) | ![](https://badgen.net/badge/likes/87/blue) |
| [Better System Trader EP064 - Cryptocurrencies and Machine Learning with Bert Mouler](https://www.youtube.com/watch?v=YgRTd4nLJoU) | ![](https://badgen.net/badge/likes/35/blue) |
| [Better System Trader EP023 - Portfolio manager Michael Himmel talks AI and machine learning in trading](https://www.youtube.com/watch?v=9tZjeyhfG0g) | ![](https://badgen.net/badge/likes/29/blue) |
| [Better System Trader EP082 - Machine Learning With Kris Longmore](https://www.youtube.com/watch?v=0syNgsd635M) | ![](https://badgen.net/badge/likes/18/blue) |

---

# Blogs

| Blog |
|------|
| [AAA Quants, Tom Starke Blog](http://aaaquants.com/category/blog/) |
| [AI & Systematic Trading](https://blog.paperswithbacktest.com/) |
| [Blackarbs blog](http://www.blackarbs.com/blog/) |
| [Hardikp, Hardik Patel blog](https://www.hardikp.com/) |
| [Max Dama on Automated Trading](https://bit.ly/3wVZbh9) |
| [Medallion.Club on Systematic Trading (FR)](https://medallion.club/trading-algorithmique-quantitatif-systematique/) |
| [Proof Engineering: The Algorithmic Trading Platform](https://bit.ly/3lX7zYN) |
| [Quantsportal, Jacques Joubert's Blog](http://www.quantsportal.com/blog-page/) |
| [Quantstart - Machine Learning for Trading articles](https://www.quantstart.com/articles) |
| [RobotWealth, Kris Longmore Blog](https://robotwealth.com/blog/) |

---

# Courses

| Course |
|--------|
| [AI in Finance](https://cfte.education/) |
| [AI & Systematic Trading](https://paperswithbacktest.com/course) |
| [Algorithmic Trading for Cryptocurrencies in Python](https://github.com/tudorelu/tudorials/tree/master/trading) |
| [Coursera, NYU - Guided Tour of Machine Learning in Finance](https://www.coursera.org/learn/guided-tour-machine-learning-finance) |
| [Coursera, NYU - Fundamentals of Machine Learning in Finance](https://www.coursera.org/learn/fundamentals-machine-learning-in-finance) |
| [Coursera, NYU - Reinforcement Learning in Finance](https://www.coursera.org/learn/reinforcement-learning-in-finance) |
| [Coursera, NYU - Overview of Advanced Methods for Reinforcement Learning in Finance](https://www.coursera.org/learn/advanced-methods-reinforcement-learning-finance) |
| [Hudson and Thames Quantitative Research](https://github.com/hudson-and-thames) |
| [NYU: Overview of Advanced Methods of Reinforcement Learning in Finance](https://www.coursera.org/learn/advanced-methods-reinforcement-learning-finance/home/welcome) |
| [Udacity: Artificial Intelligence for Trading](https://www.udacity.com/course/ai-for-trading--nd880) |
| [Udacity, Georgia Tech - Machine Learning for Trading](https://www.udacity.com/course/machine-learning-for-trading--ud501) |
