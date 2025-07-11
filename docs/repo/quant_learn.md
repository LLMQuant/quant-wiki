# 量化百宝箱

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

本列表由[LLMQuant社区](https://llmquant.com/)整理, 我们收集一份关于**系统化交易（量化交易）策略**的资源清单，包括论文、软件、书籍、文章，帮助大家寻找、开发并运行此类策略。

<!-- omit in toc -->
### 你能在这里找到什么？

- [97 个库和包](#libraries-and-packages)，支持量化研究与实盘交易
- [696 条策略](#strategies)，来自机构与学术界的量化策略
- [23 个视频](#videos) 高质量量化学习视频
- [14种编程语言](../repo/quant_repo.md) 基于不同编程语言的量化框架
- [研究成果复现](../repo/reproduce.md) 代码复现经典研究成果
- 同时还有一些有价值的 [博客](#blogs) 与 [课程](#courses)

## 目录

- [库和包](#libraries-and-packages)
  - [回测和实盘交易](#backtesting-and-live-trading)
    - [通用 - 事件驱动框架](#general---event-driven-frameworks)  
    - [通用 - 向量化框架](#general---vector-based-frameworks)
    - [加密货币](#cryptocurrencies)
  - [交易机器人](#trading-bots)
  - [分析工具](#analytics)
    - [指标](#indicators)
    - [指标计算](#metrics-computation)
    - [优化](#optimization)
    - [定价](#pricing)
    - [风险](#risk)
  - [券商API](#broker-apis)
  - [数据源](#data-sources)
    - [通用](#general)
    - [加密货币](#cryptocurrencies-1)
  - [数据科学](#data-science)
  - [数据库](#databases)
  - [图计算](#graph-computation)
  - [机器学习](#machine-learning)
  - [时间序列分析](#timeseries-analysis)
  - [可视化](#visualization)
- [策略](#strategies)
  - [债券、商品、货币、股票](#bonds-commodities-currencies-equities)
  - [债券、商品、股票、REITs](#bonds-commodities-equities-reits)
  - [债券、股票](#bonds-equities)
  - [债券、股票、REITs](#bonds-equities-reits)
  - [商品](#commodities)
  - [加密货币](#cryptos)
  - [货币](#currencies)
  - [股票](#equities)
- [量化视频](#videos)
- [量化博客](#blogs)
- [量化课程](#courses)
- [14种编程语言的量化框架](../repo/quant_repo.md)
- [研究成果复现](../repo/reproduce.md)

---

# Libraries and packages

*下列 **97 个库与包**可用于实现交易机器人、回测器、技术指标工具、定价器等。每个库按照其使用的编程语言分类，并根据项目在 GitHub 上的人气（Star 数）从高到低排列。*

## Backtesting and Live Trading

### General - Event Driven Frameworks

| 仓库 (Repository) | 描述 (Description) | Stars | 使用语言 |
|------------------|--------------------|-------|----------|
| [vnpy](https://github.com/vnpy/vnpy) | 基于 Python 的开源量化交易系统开发框架，2015 年 1 月正式发布，从零成长为一个功能完善的量化交易平台 | ![GitHub stars](https://badgen.net/github/stars/vnpy/vnpy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [zipline](https://github.com/quantopian/zipline) | 一个 Pythonic 的算法交易库。基于事件驱动模型进行回测 | ![GitHub stars](https://badgen.net/github/stars/quantopian/zipline) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [backtrader](https://github.com/mementum/backtrader) | 事件驱动的 Python 回测库，用于交易策略 | ![GitHub stars](https://badgen.net/github/stars/mementum/backtrader) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [QUANTAXIS](https://github.com/QUANTAXIS/QUANTAXIS) | QUANTAXIS 支持任务调度、分布式部署的股票/期货/期权/港股/加密货币数据、回测、模拟、交易、可视化和多账户的纯本地量化解决方案 | ![GitHub stars](https://badgen.net/github/stars/QUANTAXIS/QUANTAXIS) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [QuantConnect](https://github.com/QuantConnect/Lean) | QuantConnect 提供的 Lean 算法交易引擎（Python、C#） | ![GitHub stars](https://badgen.net/github/stars/QuantConnect/Lean) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Rqalpha](https://github.com/ricequant/rqalpha) | 一个可扩展、可替换的 Python 算法回测 & 交易框架，支持多种金融产品 | ![GitHub stars](https://badgen.net/github/stars/ricequant/rqalpha) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [finmarketpy](https://github.com/cuemacro/finmarketpy) | 一个 Python 库，用于回测交易策略与分析金融市场（前身名为 pythalesians） | ![GitHub stars](https://badgen.net/github/stars/cuemacro/finmarketpy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [backtesting.py](https://github.com/kernc/backtesting.py) | 在历史数据上推断交易策略可行性的 Python 回测框架。相比现有替代品更轻量、快速、易用、直观、交互性强 | ![GitHub stars](https://badgen.net/github/stars/kernc/backtesting.py) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [zvt](https://github.com/zvtvz/zvt) | 模块化量化框架 | ![GitHub stars](https://badgen.net/github/stars/zvtvz/zvt) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [WonderTrader](https://github.com/wondertrader/wondertrader) | WonderTrader——量化研发交易的一体化框架 | ![GitHub stars](https://badgen.net/github/stars/wondertrader/wondertrader) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [nautilus_trader](https://github.com/nautechsystems/nautilus_trader) | 一个高性能算法交易平台与事件驱动的回测框架 | ![GitHub stars](https://badgen.net/github/stars/nautechsystems/nautilus_trader) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [PandoraTrader](https://github.com/pegasusTrader/PandoraTrader) | 基于 C++ 开发的高频量化交易平台，支持多种交易 API 且跨平台 | ![GitHub stars](https://badgen.net/github/stars/pegasusTrader/PandoraTrader) | ![made-with-c++](https://img.shields.io/badge/Made%20with-c++-1f425f.svg) |
| [HFTBacktest](https://github.com/nkaz001/hftbacktest) | 在 Python + Numba 下进行高精度 HFT 数据回测 | ![GitHub stars](https://badgen.net/github/stars/nkaz001/hftbacktest) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [aat](https://github.com/AsyncAlgoTrading/aat) | 异步、事件驱动的 Python 算法交易策略框架，可选 C++ 加速，支持多交易所实盘交易 | ![GitHub stars](https://badgen.net/github/stars/AsyncAlgoTrading/aat) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [sdoosa-algo-trade-python](https://github.com/sreenivasdoosa/sdoosa-algo-trade-python) | 主要面向量化交易初学者，使用 Python 练手自编交易算法 | ![GitHub stars](https://badgen.net/github/stars/sreenivasdoosa/sdoosa-algo-trade-python) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [lumibot](https://github.com/Lumiwealth/lumibot) | 一个非常简单但有用的回测与示例化实盘交易框架（速度略慢） | ![GitHub stars](https://badgen.net/github/stars/Lumiwealth/lumibot) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [quanttrader](https://github.com/letianzj/quanttrader) | 基于事件的 Python 回测与实盘交易框架，类似 backtesting.py | ![GitHub stars](https://badgen.net/github/stars/letianzj/quanttrader) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [gobacktest](https://github.com/gobacktest/gobacktest) | 使用 Go 语言实现的事件驱动回测框架 | ![GitHub stars](https://badgen.net/github/stars/gobacktest/gobacktest) | ![made-with-go](https://img.shields.io/badge/Made%20with-Go-1f425f.svg) |
| [FlashFunk](https://github.com/HFQR/FlashFunk) | 用 Rust 编写的高性能运行时 | ![GitHub stars](https://badgen.net/github/stars/HFQR/FlashFunk) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |

### General - Vector Based Frameworks

| 仓库 | 描述 | Stars | 使用语言 |
|------|------|-------|----------|
| [vectorbt](https://github.com/polakowo/vectorbt) | 完全基于 pandas 和 NumPy，并使用 Numba 加速的回测工具，可在高速和规模化前提下测试成千上万策略 | ![GitHub stars](https://badgen.net/github/stars/polakowo/vectorbt) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [pysystemtrade](https://github.com/robcarver17/pysystemtrade) | 《Systematic Trading》作者 Rob Carver 提供的 Python 系统化交易实现 | ![GitHub stars](https://badgen.net/github/stars/robcarver17/pysystemtrade) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [bt](https://github.com/pmorissette/bt) | 基于 Python 的灵活回测库，使用类似树形的策略结构 | ![GitHub stars](https://badgen.net/github/stars/pmorissette/bt) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

### Cryptocurrencies

| 仓库 | 描述 | Stars | 使用语言 |
|------|------|-------|----------|
| [Freqtrade](https://github.com/freqtrade/freqtrade) | 一个使用 Python 编写的免费开源加密货币交易机器人，支持各大交易所并可通过 Telegram 控制，提供回测、可视化和资金管理，支持机器学习优化策略 | ![GitHub stars](https://badgen.net/github/stars/freqtrade/freqtrade) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Jesse](https://github.com/jesse-ai/jesse) | 旨在简化交易策略研究与开发的高级加密货币交易框架 | ![GitHub stars](https://badgen.net/github/stars/jesse-ai/jesse) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [OctoBot](https://github.com/Drakkar-Software/OctoBot) | 支持技术分析、套利与社交化交易等功能的加密货币交易机器人，配备高级 Web 界面 | ![GitHub stars](https://badgen.net/github/stars/Drakkar-Software/OctoBot) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Kelp](https://github.com/stellar/kelp) | Stellar DEX 与 100+ 中心化交易所的免费开源交易机器人 | ![GitHub stars](https://badgen.net/github/stars/stellar/kelp) | ![made-with-go](https://img.shields.io/badge/Made%20with-Go-1f425f.svg) |
| [openlimits](https://github.com/nash-io/openlimits) | Rust 编写的高性能加密货币交易 API，支持多交易所并带有多语言封装 | ![GitHub stars](https://badgen.net/github/stars/nash-io/openlimits) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [bTrader](https://github.com/gabriel-milan/btrader) | Binance 三角套利交易机器人 | ![GitHub stars](https://badgen.net/github/stars/gabriel-milan/btrader) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [crypto-crawler-rs](https://github.com/crypto-crawler/crypto-crawler-rs) | 从加密货币交易所收集订单簿与交易消息 | ![GitHub stars](https://badgen.net/github/stars/crypto-crawler/crypto-crawler-rs) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [Hummingbot](https://github.com/CoinAlpha/hummingbot) | 一款专注于市场做市（market making）的加密货币交易客户端 | ![GitHub stars](https://badgen.net/github/stars/CoinAlpha/hummingbot) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [cryptotrader-core](https://github.com/monomadic/cryptotrader-core) | Rust 中的加密货币交易所 REST API 客户端，简易易用 | ![GitHub stars](https://badgen.net/github/stars/monomadic/cryptotrader-core) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |

## Trading bots

*交易机器人与 alpha 模型，有些项目可能已过时或无人维护。*

| 仓库 | 描述 | Stars | 使用语言 |
|------|------|-------|----------|
| [Blackbird](https://github.com/butor/blackbird) | Blackbird 比特币跨平台套利机器人：做多/做空的市场中性策略 | ![GitHub stars](https://badgen.net/github/stars/butor/blackbird) | ![made-with-c++](https://img.shields.io/badge/Made%20with-c++-1f425f.svg) |
| [bitcoin-arbitrage](https://github.com/maxme/bitcoin-arbitrage) | 比特币套利机会探测器 | ![GitHub stars](https://badgen.net/github/stars/maxme/bitcoin-arbitrage) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [ThetaGang](https://github.com/brndnmtthws/thetagang) | 针对 IBKR 的收租策略 (theta) 机器人 | ![GitHub stars](https://badgen.net/github/stars/brndnmtthws/thetagang) | ![made-with-typescript](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [czsc](https://github.com/waditu/czsc) | 「缠中说禅」技术分析工具；缠论；股票/期货/Quant/量化交易 | ![GitHub stars](https://badgen.net/github/stars/waditu/czsc) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [R2 Bitcoin Arbitrager](https://github.com/bitrinjani/r2) | 基于 Node.js + TypeScript 的自动化比特币套利交易系统 | ![GitHub stars](https://badgen.net/github/stars/bitrinjani/r2) | ![made-with-typescript](https://img.shields.io/badge/Made%20with-TypeScript-1f425f.svg) |
| [analyzingalpha](https://github.com/leosmigel/analyzingalpha) | 一些简单交易策略的实现 | ![GitHub stars](https://badgen.net/github/stars/leosmigel/analyzingalpha) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [PyTrendFollow](https://github.com/chrism2671/PyTrendFollow) | 使用趋势跟随方法进行系统化期货交易 | ![GitHub stars](https://badgen.net/github/stars/chrism2671/PyTrendFollow) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

## Analytics

### Indicators

*预测未来价格运动的指标库。*

| 仓库 | 描述 | Stars | 使用语言 |
|------|------|-------|----------|
| [ta-lib](https://github.com/mrjbq7/ta-lib) | 对金融市场数据进行技术分析 | ![GitHub stars](https://badgen.net/github/stars/mrjbq7/ta-lib) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [go-tart](https://github.com/iamjinlei/go-tart) | Go 语言版本的 [ta-lib](https://github.com/mrjbq7/ta-lib)，支持流式更新 | ![GitHub stars](https://badgen.net/github/stars/iamjinlei/go-tart) | ![made-with-go](https://img.shields.io/badge/Made%20with-go-1f425f.svg) |
| [pandas-ta](https://github.com/twopirllc/pandas-ta) | Pandas 技术分析扩展（Pandas TA），包含 130+ 技术指标与 60 多种 TA-Lib K 线形态 | ![GitHub stars](https://badgen.net/github/stars/twopirllc/pandas-ta) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [finta](https://github.com/peerchemist/finta) | 常见金融技术指标的 Pandas 实现 | ![GitHub stars](https://badgen.net/github/stars/peerchemist/finta) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [ta-rust](https://github.com/greyblake/ta-rs) | Rust 语言的技术分析库 | ![GitHub stars](https://badgen.net/github/stars/greyblake/ta-rs) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |

### Metrics computation

*计算各种金融指标的库。*

| 仓库 | 描述 | Stars | 使用语言 |
|------|------|-------|----------|
| [quantstats](https://github.com/ranaroussi/quantstats) | 为量化研究提供投资组合分析的 Python 库 | ![GitHub stars](https://badgen.net/github/stars/ranaroussi/quantstats) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [ffn](https://github.com/pmorissette/ffn) | 一个 Python 金融函数库 | ![GitHub stars](https://badgen.net/github/stars/pmorissette/ffn) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

### Optimization

| 仓库 | 描述 | Stars | 使用语言 |
|------|------|-------|----------|
| [PyPortfolioOpt](https://github.com/robertmartin8/PyPortfolioOpt) | Python 中的投资组合优化，包括传统有效前沿、Black-Litterman、层次化风险平价等 | ![GitHub stars](https://badgen.net/github/stars/robertmartin8/PyPortfolioOpt) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Riskfolio-Lib](https://github.com/dcajasn/Riskfolio-Lib) | Python 投资组合优化与量化资产配置库 | ![GitHub stars](https://badgen.net/github/stars/dcajasn/Riskfolio-Lib) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [empyrial](https://github.com/ssantoshp/Empyrial) | 由 Python 编写的开源量化投资库，2021 年 3 月正式发布，面向金融机构和个人 | ![GitHub stars](https://badgen.net/github/stars/ssantoshp/Empyrial) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Deepdow](https://github.com/jankrepl/deepdow) | 结合投资组合优化和深度学习的 Python 库，旨在探索可在一次前向传播中完成权重分配的网络 | ![GitHub stars](https://badgen.net/github/stars/jankrepl/deepdow) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [spectre](https://github.com/Heerozh/spectre) | Python 中的投资组合优化与量化资产配置 | ![GitHub stars](https://badgen.net/github/stars/Heerozh/spectre) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

### Pricing

| 仓库 | 描述 | Stars | 使用语言 |
|------|------|-------|----------|
| [tf-quant-finance](https://github.com/google/tf-quant-finance) | Google 推出的基于 TensorFlow 的高性能量化金融库 | ![GitHub stars](https://badgen.net/github/stars/google/tf-quant-finance) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [FinancePy](https://github.com/domokane/FinancePy) | 一个 Python 金融库，专注于金融衍生品的定价与风险管理，包括固定收益、股票、外汇和信用衍生品 | ![GitHub stars](https://badgen.net/github/stars/domokane/FinancePy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [PyQL](https://github.com/enthought/pyql) | 著名定价库 QuantLib 的 Python 封装 | ![GitHub stars](https://badgen.net/github/stars/enthought/pyql) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

### Risk

| 仓库 | 描述 | Stars | 使用语言 |
|------|------|-------|----------|
| [pyfolio](https://github.com/quantopian/pyfolio) | Python 中的投资组合与风险分析工具 | ![GitHub stars](https://badgen.net/github/stars/quantopian/pyfolio) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

## Broker APIs

| 仓库 | 描述 | Stars | 使用语言 |
|------|------|-------|----------|
| [ccxt](https://github.com/ccxt/ccxt) | 一个同时支持 JavaScript、Python、PHP 的加密货币交易 API，整合了超过 100 家比特币或山寨币交易所 | ![GitHub stars](https://badgen.net/github/stars/ccxt/ccxt) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Ib_insync](https://github.com/erdewit/ib_insync) | 适用于 Interactive Brokers 的 Python 同步/异步框架 | ![GitHub stars](https://badgen.net/github/stars/erdewit/ib_insync) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Coinnect](https://github.com/hugues31/coinnect) | Rust 库，为主要加密货币交易所（REST API）提供完整访问 | ![GitHub stars](https://badgen.net/github/stars/hugues31/coinnect) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [PENDAX](https://github.com/CompendiumFi/PENDAX-SDK) | 针对 FTX、FTXUS、OKX、Bybit 等交易所的 JavaScript SDK，支持交易、数据与 WebSocket | ![GitHub stars](https://badgen.net/github/stars/CompendiumFi/PENDAX-SDK) | ![made-with-javascript](https://img.shields.io/badge/Made%20with-Javascript-1f425f.svg) |

## Data Sources

### General

| 仓库 | 描述 | Stars | 使用语言 |
|------|------|-------|----------|
| [OpenBB Terminal](https://github.com/OpenBB-finance/OpenBBTerminal) | 人人都能使用、随时随地进行投资研究的终端 | ![GitHub stars](https://badgen.net/github/stars/OpenBB-finance/OpenBBTerminal) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [TuShare](https://github.com/waditu/tushare) | 一个获取中国股票历史数据的工具 | ![GitHub stars](https://badgen.net/github/stars/waditu/tushare) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [yfinance](https://github.com/ranaroussi/yfinance) | 提供多线程、Pythonic 的方式下载 Yahoo!Ⓡ Finance 市场数据 | ![GitHub stars](https://badgen.net/github/stars/ranaroussi/yfinance) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [AkShare](https://github.com/akfamily/akshare) | 一个优雅而简单的 Python 金融数据接口库，为人类而生！ | ![GitHub stars](https://badgen.net/github/stars/akfamily/akshare) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [pandas-datareader](https://github.com/pydata/pandas-datareader) | 可获取远程数据的 Pandas 扩展，兼容多个 Pandas 版本 | ![GitHub stars](https://badgen.net/github/stars/pydata/pandas-datareader) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Quandl](https://github.com/quandl/quandl-python) | 从数百个发布者处获取数百万金融与经济数据集，只需一个免费 API | ![GitHub stars](https://badgen.net/github/stars/quandl/quandl-python) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [findatapy](https://github.com/cuemacro/findatapy) | 提供易用的 Python API，可从 Quandl、Bloomberg、Yahoo、Google 等多种源统一下载市场数据 | ![GitHub stars](https://badgen.net/github/stars/cuemacro/findatapy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Investpy](https://github.com/alvarobartt/investpy) | 从 Investing.com 中提取金融数据的 Python 工具 | ![GitHub stars](https://badgen.net/github/stars/alvarobartt/investpy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Fundamental Analysis Data](https://github.com/JerBouma/FundamentalAnalysis) | 全面的基础面分析包，可收集 20 年的公司简介、财务报表、比率与股票数据，覆盖 2 万家以上公司 | ![GitHub stars](https://badgen.net/github/stars/JerBouma/FundamentalAnalysis) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Wallstreet](https://github.com/mcdallas/wallstreet) | 实时股票与期权工具 | ![GitHub stars](https://badgen.net/github/stars/mcdallas/wallstreet) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

### Cryptocurrencies

| 仓库 | 描述 | Stars | 使用语言 |
|------|------|-------|----------|
| [Cryptofeed](https://github.com/bmoscon/cryptofeed) | 使用 asyncio 获取加密货币交易所 WebSocket 数据（订单簿、交易流） | ![GitHub stars](https://badgen.net/github/stars/bmoscon/cryptofeed) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Gekko-Datasets](https://github.com/xFFFFF/Gekko-Datasets) | Gekko 交易机器人数据集，可下载并使用 SQLite 格式的历史文件 | ![GitHub stars](https://badgen.net/github/stars/xFFFFF/Gekko-Datasets) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [CryptoInscriber](https://github.com/Optixal/CryptoInscriber) | 加密货币实时历史交易数据记录器，可从任意交易所下载历史交易数据 | ![GitHub stars](https://badgen.net/github/stars/Optixal/CryptoInscriber) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Crypto Lake](https://github.com/crypto-lake/lake-api) | 高频订单簿 & 交易数据，用于加密货币领域 | ![GitHub stars](https://badgen.net/github/stars/crypto-lake/lake-api) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

## Data Science

| 仓库 | 描述 | Stars | 使用语言 |
|------|------|-------|----------|
| [TensorFlow](https://github.com/tensorflow/tensorflow) | Python 中的基础科学计算算法集合 | ![GitHub stars](https://badgen.net/github/stars/tensorflow/tensorflow) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Pytorch](https://github.com/pytorch/pytorch) | Python 中的张量与动态神经网络（GPU 加速） | ![GitHub stars](https://badgen.net/github/stars/pytorch/pytorch) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Keras](https://github.com/keras-team/keras) | 对人类最友好的深度学习 Python 库 | ![GitHub stars](https://badgen.net/github/stars/keras-team/keras) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Scikit-learn](https://github.com/scikit-learn/scikit-learn) | Python 中的机器学习库 | ![GitHub stars](https://badgen.net/github/stars/scikit-learn/scikit-learn) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Pandas](https://github.com/pandas-dev/pandas) | 强大灵活的数据分析/操作库，为 Python 提供了类似 R 的 data.frame、统计函数等 | ![GitHub stars](https://badgen.net/github/stars/pandas-dev/pandas) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Numpy](https://github.com/numpy/numpy) | Python 科学计算的基础包 | ![GitHub stars](https://badgen.net/github/stars/numpy/numpy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Scipy](https://github.com/scipy/scipy) | Python 科学计算所需的基础算法 | ![GitHub stars](https://badgen.net/github/stars/scipy/scipy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [PyMC](https://github.com/pymc-devs/pymc) | Python 中的概率编程：基于 Aesara 的贝叶斯建模和概率机器学习 | ![GitHub stars](https://badgen.net/github/stars/pymc-devs/pymc) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Cvxpy](https://github.com/cvxpy/cvxpy) | Python 内嵌式的凸优化建模语言 | ![GitHub stars](https://badgen.net/github/stars/cvxpy/cvxpy) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

## Databases

| 仓库 | 描述 | Stars | 使用语言 |
|------|------|-------|----------|
| [Marketstore](https://github.com/alpacahq/marketstore) | 面向金融时序数据的 DataFrame 服务器 | ![GitHub stars](https://badgen.net/github/stars/alpacahq/marketstore) | ![made-with-go](https://img.shields.io/badge/Made%20with-Go-1f425f.svg) |
| [Tectonicdb](https://github.com/0b01/tectonicdb) | 一款快速、高度压缩、可独立运行的数据库和流式协议，用于订单簿 Tick 数据 | ![GitHub stars](https://badgen.net/github/stars/0b01/tectonicdb) | ![made-with-rust](https://img.shields.io/badge/Made%20with-Rust-1f425f.svg) |
| [ArcticDB (Man Group)](https://github.com/man-group/arcticdb) | 高性能数据存储库，适用于时序和逐笔交易数据 | ![GitHub stars](https://badgen.net/github/stars/man-group/ArcticDB) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Timeplus Proton](https://github.com/timeplus-io/proton) | 一款基于 ClickHouse 开发的高性能批流一体数据库，提供列式存储，流式增量计算，毫秒级推送和自定义函数，适用于基于 SQL 的复杂事件处理，因子计算和回测 | ![GitHub stars](https://badgen.net/github/stars/timeplus-io/proton) | ![made-with-cpp](https://img.shields.io/badge/Made%20with-C%2B%2B-1f425f.svg) |

## Graph Computation

| 仓库 | 描述 | Stars | 使用语言 |
|------|------|-------|----------|
| [Ray](https://github.com/ray-project/ray) | 一个开源框架，提供简单通用的 API 用于构建分布式应用 | ![GitHub stars](https://badgen.net/github/stars/ray-project/ray) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Dask](https://github.com/dask/dask) | Python 中的并行计算库，使用与 Pandas 类似的 API 进行任务调度 | ![GitHub stars](https://badgen.net/github/stars/dask/dask) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Incremental (JaneStreet)](https://github.com/janestreet/incremental) | Incremental 库可根据输入的变化高效更新复杂计算，灵感来自 Umut Acar 等关于自适应计算的研究 | ![GitHub stars](https://badgen.net/github/stars/janestreet/incremental) | ![made-with-ocaml](https://img.shields.io/badge/Made%20with-Ocaml-1f425f.svg) |
| [Man MDF](https://github.com/man-group/mdf) | Python 数据流编程工具包 | ![GitHub stars](https://badgen.net/github/stars/man-group/mdf) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [GraphKit](https://github.com/yahoo/graphkit) | 一个轻量级 Python 模块，用于创建并运行有序的计算图 | ![GitHub stars](https://badgen.net/github/stars/yahoo/graphkit) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Tributary](https://github.com/timkpaine/tributary) | Python 中的流式响应式与数据流图 | ![GitHub stars](https://badgen.net/github/stars/timkpaine/tributary) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

## Machine Learning

| 仓库 | 描述 | Stars | 使用语言 |
|------|------|-------|----------|
| [QLib (Microsoft)](https://github.com/microsoft/qlib) | 面向人工智能的量化投资平台，助力研究和落地 AI 技术在量化投资中的潜力，已有越来越多的前沿量化研究工作在此发布 | ![GitHub stars](https://badgen.net/github/stars/microsoft/qlib) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [FinRL](https://github.com/AI4Finance-Foundation/FinRL) | 首个展示深度强化学习在量化金融中巨大潜力的开源框架 | ![GitHub stars](https://badgen.net/github/stars/AI4Finance-Foundation/FinRL) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [MlFinLab (Hudson & Thames)](https://github.com/hudson-and-thames/mlfinlab) | 助力投资组合经理和交易员利用机器学习力量的工具，提供可复现、可解释且易用的模块 | ![GitHub stars](https://badgen.net/github/stars/hudson-and-thames/mlfinlab) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [TradingGym](https://github.com/Yvictor/TradingGym) | 一个用于训练强化学习智能体或简单规则算法的交易与回测环境 | ![GitHub stars](https://badgen.net/github/stars/Yvictor/TradingGym) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [Stock Trading Bot using Deep Q-Learning](https://github.com/pskrunner14/trading-bot) | 使用深度 Q-Learning 的股票交易机器人 | ![GitHub stars](https://badgen.net/github/stars/pskrunner14/trading-bot) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

## TimeSeries Analysis

| 仓库 | 描述 | Stars | 使用语言 |
|------|------|-------|----------|
| [Facebook Prophet](https://github.com/facebook/prophet) | 面向时间序列数据的高质量预测工具，适用于多重季节性且可线性或非线性增长 | ![GitHub stars](https://badgen.net/github/stars/facebook/prophet) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [statsmodels](https://github.com/statsmodels/statsmodels) | Python 模块，可进行数据探索、统计模型估计与统计检验 | ![GitHub stars](https://badgen.net/github/stars/statsmodels/statsmodels) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [tsfresh](https://github.com/blue-yonder/tsfresh) | 自动提取时间序列中的相关特征 | ![GitHub stars](https://badgen.net/github/stars/blue-yonder/tsfresh) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [pmdarima](https://github.com/alkaline-ml/pmdarima) | 在 Python 中填补时间序列分析空白的统计库，包括 R 语言中 auto.arima 的等价功能 | ![GitHub stars](https://badgen.net/github/stars/alkaline-ml/pmdarima) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

## Visualization

| 仓库 | 描述 | Stars | 使用语言 |
|------|------|-------|----------|
| [D-Tale (Man Group)](https://github.com/man-group/dtale) | 将 Flask 后端与 React 前端结合，可轻松查看与分析 Pandas 数据结构 | ![GitHub stars](https://badgen.net/github/stars/man-group/dtale) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [mplfinance](https://github.com/matplotlib/mplfinance) | 基于 Matplotlib 的金融市场数据可视化 | ![GitHub stars](https://badgen.net/github/stars/matplotlib/mplfinance) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |
| [btplotting](https://github.com/happydasch/btplotting) | 为 backtrader 的回测、优化结果和实时数据提供可视化 | ![GitHub stars](https://badgen.net/github/stars/happydasch/btplotting) | ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) |

---

# Strategies

## Bonds, commodities, currencies, equities

| 标题 | Sharpe 比率 | 波动率 | 调仓频率 | 实现 | 来源 |
|------|------------|--------|---------|------|------|
| Time Series Momentum Effect | `0.576` | `20.5%` | `Monthly` | [QuantConnect](./static/strategies/time-series-momentum-effect.py) | [Paper](https://pages.stern.nyu.edu/~lpederse/papers/TimeSeriesMomentum.pdf) |
| Short Term Reversal with Futures | `-0.05` | `12.3%` | `Weekly` | [QuantConnect](./static/strategies/asset-class-momentum-rotational-system.py) | [Paper](https://ideas.repec.org/a/eee/jbfina/v28y2004i6p1337-1361.html) |

## Bonds, commodities, equities, REITs

| 标题 | Sharpe 比率 | 波动率 | 调仓频率 | 实现 | 来源 |
|------|------------|--------|---------|------|------|
| Asset Class Trend-Following | `0.502` | `10.4%` | `Monthly` | [QuantConnect](./static/strategies/asset-class-trend-following.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=962461) |
| Momentum Asset Allocation Strategy | `0.321` | `11%` | `Monthly` | [QuantConnect](./static/strategies/asset-class-trend-following.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1585517) |

## Bonds, equities

| 标题 | Sharpe 比率 | 波动率 | 调仓频率 | 实现 | 来源 |
|------|------------|--------|---------|------|------|
| Paired Switching | `0.691` | `9.5%` | `Quarterly` | [QuantConnect](./static/strategies/paired-switching.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1917044) |
| FED Model | `0.369` | `14.3%` | `Monthly` | [QuantConnect](./static/strategies/fed-model.py) | [Paper](https://www.researchgate.net/publication/228267011_The_FED_Model_and_Expected_Asset_Returns) |

## Bonds, equities, REITs

| 标题 | Sharpe 比率 | 波动率 | 调仓频率 | 实现 | 来源 |
|------|------------|--------|---------|------|------|
| Value and Momentum Factors across Asset Classes | `0.155` | `9.8%` | `Monthly` | [QuantConnect](./static/strategies/value-and-momentum-factors-across-asset-classes.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1079975) |

## Commodities

| 标题 | Sharpe 比率 | 波动率 | 调仓频率 | 实现 | 来源 |
|------|------------|--------|---------|------|------|
| Skewness Effect in Commodities | `0.482` | `17.7%` | `Monthly` | [QuantConnect](./static/strategies/skewness-effect-in-commodities.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2671165) |
| Return Asymmetry Effect in Commodity Futures | `0.239` | `13.4%` | `Monthly` | [QuantConnect](./static/strategies/return-asymmetry-effect-in-commodity-futures.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3918896) |
| Momentum Effect in Commodities | `0.14` | `20.3%` | `Monthly` | [QuantConnect](./static/strategies/momentum-effect-in-commodities.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=702281) |
| Term Structure Effect in Commodities | `0.128` | `23.1%` | `Monthly` | [QuantConnect](./static/strategies/term-structure-effect-in-commodities.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1127213) |
| Trading WTI/BRENT Spread | `-0.199` | `11.6%` | `Daily` | [QuantConnect](./static/strategies/trading-wti-brent-spread.py) | [Paper](https://link.springer.com/article/10.1057/jdhf.2009.24) |

## Cryptos

| 标题 | Sharpe 比率 | 波动率 | 调仓频率 | 实现 | 来源 |
|------|------------|--------|---------|------|------|
| Overnight Seasonality in Bitcoin | `0.892` | `20.8%` | `Intraday` | [QuantConnect](./static/strategies/intraday-seasonality-in-bitcoin.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4081000) |
| Rebalancing Premium in Cryptocurrencies | `0.698` | `27.5%` | `Daily` | [QuantConnect](./static/strategies/rebalancing-premium-in-cryptocurrencies.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3982120) |

## Currencies

| 标题 | Sharpe 比率 | 波动率 | 调仓频率 | 实现 | 来源 |
|------|------------|--------|---------|------|------|
| FX Carry Trade | `0.254` | `7.8%` | `Monthly` | [QuantConnect](./static/strategies/fx-carry-trade.py) | [Paper](http://globalmarkets.db.com/new/docs/dbCurrencyReturns_March2009.pdf) |
| Dollar Carry Trade | `0.113` | `5.8%` | `Monthly` | [QuantConnect](./static/strategies/dollar-carry-trade.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1541230) |
| Currency Momentum Factor | `-0.01` | `6.7%` | `Monthly` | [QuantConnect](./static/strategies/currency-momentum-factor.py) | [Paper](http://globalmarkets.db.com/new/docs/dbCurrencyReturns_March2009.pdf) |
| Currency Value Factor – PPP Strategy | `-0.103` | `5%` | `Quarterly` | [QuantConnect](./static/strategies/currency-value-factor-ppp-strategy.py) | [Paper](http://globalmarkets.db.com/new/docs/dbCurrencyReturns_March2009.pdf) |

## Equities

| 标题 | Sharpe 比率 | 波动率 | 调仓频率 | 实现 | 来源 |
|------|------------|--------|---------|------|------|
| Asset Growth Effect | `0.835` | `10.2%` | `Yearly` | [QuantConnect](./static/strategies/asset-growth-effect.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1335524) |
| Short Term Reversal Effect in Stocks | `0.816` | `21.4%` | `Weekly` | [QuantConnect](./static/strategies/short-term-reversal-in-stocks.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1605049) |
| Reversal During Earnings-Announcements | `0.785` | `25.7%` | `Daily` | [QuantConnect](./static/strategies/reversal-during-earnings-announcements.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2275982) |
| Size Factor – Small Capitalization Stocks Premium | `0.747` | `11.1%` | `Yearly` | [QuantConnect](./static/strategies/small-capitalization-stocks-premium-anomaly.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3177539) |
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
| Sector Momentum – Rotational System | `0.401` | `14.1%` | `Monthly` | [QuantConnect](./static/strategies/sector-momentum-rotational-system.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1585517) |
| Combining Smart Factors Momentum and Market Portfolio | `0.388` | `8.2%` | `Monthly` | [QuantConnect](./static/strategies/combining-smart-factors-momentum-and-market-portfolio.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3745517) |
| Momentum and Reversal Combined with Volatility Effect in Stocks | `0.375` | `17%` | `Monthly` | [QuantConnect](./static/strategies/momentum-and-reversal-combined-with-volatility-effect-in-stocks.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1679464) |
| Market Sentiment and an Overnight Anomaly | `0.369` | `3.6%` | `Daily` | [QuantConnect](./static/strategies/market-sentiment-and-an-overnight-anomaly.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3829582) |
| January Barometer | `0.365` | `7.4%` | `Monthly` | [QuantConnect](./static/strategies/january-barometer.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1436516) |
| R&D Expenditures and Stock Returns | `0.354` | `8.1%` | `Yearly` | [QuantConnect](./static/strategies/rd-expenditures-and-stock-returns.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=227564) |
| Value Factor – CAPE Effect within Countries | `0.351` | `20.2%` | `Yearly` | [QuantConnect](./static/strategies/value-factor-effect-within-countries.py) | [Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2129474) |
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
| Short Interest Effect – Long-Short Version | `0.079` | `6.6%` | `Monthly` | [QuantConnect](./static/strategies/short-interest-effect-long-short-version.py) | [Paper](https://www.semanticscholar.org/paper/Why-Do-Short-Interest-Levels-Predict-Stock-Returns-Boehmer-Erturk/06418ef437dc7156229532a97d0f8392373eb297?p2df) |
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

| 标题 | Likes |
|------|-------|
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

| 博客标题 |
|---------|
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

| 课程标题 |
|---------|
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
