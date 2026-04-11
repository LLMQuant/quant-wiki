# Quantitative Frameworks by Programming Language

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
This list is curated by the [LLMQuant community](https://llmquant.com/) -- a carefully compiled, outstanding collection of quantitative finance libraries, packages, and resources. For educational purposes only; all copyrights belong to the original authors.

## Languages

- [Python](#python) - The most popular language for quantitative finance, with rich data analysis, machine learning, and financial toolkits
- [R](#r) - The go-to language for statistical analysis, with unique strengths in financial modeling and risk analysis
- [Matlab](#matlab) - Widely used in financial engineering and numerical computing, especially for matrix operations
- [Julia](#julia) - An emerging language designed for high-performance numerical computing, gaining traction in quantitative finance
- [Java](#java) - The enterprise standard, suitable for building large-scale trading systems
- [JavaScript](#javascript) - Primarily used for financial data visualization and web-based trading interfaces
- [Haskell](#haskell) - A functional programming language with advantages in complex financial product modeling
- [Scala](#scala) - Combines object-oriented and functional programming, suitable for high-concurrency trading systems
- [Ruby](#ruby) - Known for its brevity, mainly used for rapid prototyping and small-scale trading systems
- [Elixir/Erlang](#elixirerlang) - Excels at building fault-tolerant and distributed trading systems
- [Golang](#golang) - Known for high performance and concurrency, ideal for developing high-frequency trading systems
- [CPP](#cpp) - The best language for low-latency trading systems, widely used in high-frequency trading
- [CSharp](#csharp) - The Microsoft ecosystem choice, ideal for developing quantitative trading systems on Windows
- [Rust](#rust) - A next-generation systems programming language that provides memory safety guarantees without sacrificing performance
- [Frameworks](#frameworks) - Cross-language quantitative finance frameworks providing complete trading and analytics solutions
- [Research Reproduction, Training and Books](#research-reproduction-training-and-books) - Learning resources and code implementations of classic research

### Recommendations

1. **Getting Started**
   - Python: Best choice for beginners, with abundant learning resources and a mature ecosystem
   - R: Ideal for those focusing on statistical analysis and risk modeling

2. **Professional Development**
   - C++: Ultra-low-latency high-frequency trading systems
   - Java: Enterprise-grade trading platform development
   - Golang: Modern high-concurrency trading systems

3. **Specialized Use Cases**
   - Julia: High-performance numerical computing
   - JavaScript: Web trading interface development
   - Rust: Combining performance with safety

4. **Research-Oriented**
   - Python/R: Data analysis and strategy research
   - Matlab: Financial engineering research
   - Julia: Algorithm optimization research

### Technology Trends

- Python continues to dominate the quantitative finance landscape
- Julia is emerging in high-performance computing
- Rust is gradually replacing C++ in systems-level development
- Go is gaining adoption in microservices architectures

---

## Python

### Numerical Libraries and Data Structures

- [numpy](https://www.numpy.org) - The fundamental package for scientific computing with Python.
- [scipy](https://www.scipy.org) - An open-source mathematics, science, and engineering ecosystem based on Python.
- [pandas](https://pandas.pydata.org) - An open-source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools.
- [polars](https://docs.pola.rs/) - A blazingly fast DataFrame library for working with structured data.
- [quantdsl](https://github.com/johnbywater/quantdsl) - A domain-specific language for quantitative analytics in finance and trading.
- [statistics](https://docs.python.org/3/library/statistics.html) - Python's built-in library for basic statistical computations.
- [sympy](https://www.sympy.org/) - A Python library for symbolic mathematics.
- [pymc3](https://docs.pymc.io/) - Probabilistic programming in Python: Bayesian modeling and probabilistic ML with Theano.
- [modelx](https://docs.modelx.io/) - Reimagine spreadsheets as formula-based objects interoperable with pandas.
- [ArcticDB](https://github.com/man-group/ArcticDB) - High-performance data store for time-series and tick data.

### Financial Instruments and Pricing

- [OpenBB Terminal](https://github.com/OpenBB-finance/OpenBBTerminal) - Investment research for everyone.
- [Fincept Terminal](https://github.com/Fincept-Corporation/FinceptTerminal) - A financial asset research terminal powered by advanced data and AI.
- [PyQL](https://github.com/enthought/pyql) - Python port of QuantLib.
- [pyfin](https://github.com/opendoor-labs/pyfin) - Basic option pricing in Python. *Archived project*
- [vollib](https://github.com/vollib/vollib) - A Python library for calculating option prices, implied volatility, and Greeks.
- [QuantPy](https://github.com/jsmidt/QuantPy) - A quantitative finance framework in Python.
- [Finance-Python](https://github.com/alpha-miner/Finance-Python) - Python finance tools collection.
- [ffn](https://github.com/pmorissette/ffn) - A financial functions library.
- [pynance](https://github.com/GriffinAustin/pynance) - A lightweight Python library for assembling and analyzing financial data.
- [tia](https://github.com/bpsmith/tia) - Toolkit for integration and analysis.
- [hasura/base-python-dash](https://platform.hasura.io/hub/projects/hasura/base-python-dash) - Hasura quickstart for deploying the Dash framework, ideal for building data visualization apps in pure Python.
- [hasura/base-python-bokeh](https://platform.hasura.io/hub/projects/hasura/base-python-bokeh) - Hasura quickstart for data visualization with the bokeh library.
- [pysabr](https://github.com/ynouri/pysabr) - Python implementation of the SABR model.
- [FinancePy](https://github.com/domokane/FinancePy) - A Python library for pricing and risk management of financial derivatives including fixed income, equity, FX, and credit.
- [gs-quant](https://github.com/goldmansachs/gs-quant) - Goldman Sachs quantitative finance Python toolkit.
- [willowtree](https://github.com/federicomariamassari/willowtree) - Python implementation of willow tree lattice for derivatives pricing.
- [financial-engineering](https://github.com/federicomariamassari/financial-engineering) - Monte Carlo methods for financial engineering projects in Python.
- [optlib](https://github.com/dbrojas/optlib) - A Python library for option pricing.
- [tf-quant-finance](https://github.com/google/tf-quant-finance) - Google's high-performance TensorFlow-based quantitative finance library.
- [Q-Fin](https://github.com/RomanMichaelPaolucci/Q-Fin) - A Python library for mathematical finance.
- [Quantsbin](https://github.com/quantsbin/Quantsbin) - Tools for pricing and plotting vanilla option prices, Greeks, and analytics.
- [finoptions](https://github.com/bbcho/finoptions-dev) - Complete Python implementation of R's fOptions and parts of fExoticOptions for pricing various option types.
- [pypme](https://github.com/ymyke/pypme) - Public Market Equivalent (PME) calculation tool.
- [AbsBox](https://github.com/yellowbean/AbsBox) - Python library for modeling cash flows of structured products such as ABS and MBS.
- [Intrinsic-Value-Calculator](https://github.com/akashaero/Intrinsic-Value-Calculator) - A stock intrinsic value calculator based on Discounted Cash Flow (DCF) analysis.
- [Kelly-Criterion](https://github.com/deltaray-io/kelly-criterion) - Kelly Criterion implementation in Python for portfolio position sizing.
- [rateslib](https://github.com/attack68/rateslib) - A fixed income library for pricing bonds, treasury futures, and derivatives such as IRS, cross-currency and FX swaps.
- [fypy](https://github.com/jkirkby3/fypy) - A vanilla and exotic option pricing library for research and development, focused on models beyond Black-Scholes and market data calibration.

### Indicators

- [pandas_talib](https://github.com/femtotrader/pandas_talib) - Technical analysis indicators implemented with Pandas.
- [finta](https://github.com/peerchemist/finta) - Common financial technical indicators implemented in Pandas.
- [Tulipy](https://github.com/cirla/tulipy) - Financial technical analysis indicator library (Python bindings for [tulipindicators](https://github.com/TulipCharts/tulipindicators)).
- [lppls](https://github.com/Boulder-Investment-Technologies/lppls) - Python module for fitting the [Log-Periodic Power Law Singularity (LPPLS)](https://en.wikipedia.org/wiki/Didier_Sornette#The_JLS_and_LPPLS_models) model.
- [talipp](https://github.com/nardew/talipp) - Incremental technical analysis indicator library for Python.
- [streaming_indicators](https://github.com/mr-easy/streaming_indicators) - A Python library for computing technical analysis indicators on streaming data.

### Trading and Backtesting

- [skfolio](https://github.com/skfolio/skfolio) - A scikit-learn-based Python library for portfolio optimization with a unified interface and sklearn-compatible tools.
- [Investing algorithm framework](https://github.com/coding-kitties/investing-algorithm-framework) - A framework for developing, backtesting, and deploying automated trading algorithms.
- [QSTrader](https://github.com/mhallsmoore/qstrader) - QSTrader backtesting simulation engine.
- [Blankly](https://github.com/Blankly-Finance/Blankly) - Full integration for backtesting, paper trading, and live deployment.
- [TA-Lib](https://github.com/mrjbq7/ta-lib) - Python wrapper for TA-Lib (<http://ta-lib.org/>).
- [zipline](https://github.com/quantopian/zipline) - Pythonic algorithmic trading library.
- [zipline-reloaded](https://github.com/stefan-jansen/zipline-reloaded) - A fork of Zipline, a Pythonic algorithmic trading library.
- [QuantSoftware Toolkit](https://github.com/QuantSoftware/QuantSoftwareToolkit) - An open-source Python framework for portfolio construction and management.
- [quantitative](https://github.com/jeffrey-liang/quantitative) - Quantitative finance and backtesting library.
- [analyzer](https://github.com/llazzaro/analyzer) - A Python framework for real-time financial and backtesting trading strategies.
- [bt](https://github.com/pmorissette/bt) - A flexible Python backtesting library.
- [backtrader](https://github.com/backtrader/backtrader) - Python backtesting library for trading strategies.
- [pythalesians](https://github.com/thalesians/pythalesians) - Python library for backtesting trading strategies, charting, downloading market data, and analyzing market patterns.
- [pybacktest](https://github.com/ematvey/pybacktest) - Vectorized backtesting framework in Python/pandas.
- [pyalgotrade](https://github.com/gbeced/pyalgotrade) - Python algorithmic trading library.
- [basana](https://github.com/gbeced/basana) - Python async and event-driven algorithmic trading framework focused on crypto.
- [tradingWithPython](https://pypi.org/project/tradingWithPython/) - A collection of functions and classes for quantitative trading.
- [Pandas TA](https://github.com/twopirllc/pandas-ta) - An easy-to-use Python 3 Pandas extension with 115+ indicators for building custom strategies.
- [ta](https://github.com/bukosabino/ta) - Technical analysis library using Pandas (Python).
- [algobroker](https://github.com/joequant/algobroker) - An execution engine for algorithmic trading.
- [pysentosa](https://pypi.org/project/pysentosa/) - Python API for the sentosa trading system.
- [finmarketpy](https://github.com/cuemacro/finmarketpy) - Python library for backtesting trading strategies and analyzing financial markets.
- [binary-martingale](https://github.com/metaperl/binary-martingale) - Automated binary options martingale strategy program.
- [fooltrader](https://github.com/foolcage/fooltrader) - A project using big data to analyze the entire market.
- [zvt](https://github.com/zvtvz/zvt) - Unified and extensible platform for recording data, computing factors, stock selection, backtesting, live trading, and visualization.
- [pylivetrader](https://github.com/alpacahq/pylivetrader) - A zipline-compatible live trading library.
- [pipeline-live](https://github.com/alpacahq/pipeline-live) - Zipline pipeline functionality for live trading with IEX data.
- [zipline-extensions](https://github.com/quantrocket-llc/zipline-extensions) - Zipline extensions and adaptations for QuantRocket.
- [moonshot](https://github.com/quantrocket-llc/moonshot) - A Pandas-based vectorized backtesting and trading engine for QuantRocket.
- [PyPortfolioOpt](https://github.com/robertmartin8/PyPortfolioOpt) - Portfolio optimization in Python, including classical and advanced methods.
- [Eiten](https://github.com/tradytics/eiten) - Open-source toolkit by Tradytics with various portfolio algorithms.
- [riskparity.py](https://github.com/dppalomar/riskparity.py) - Fast, scalable risk parity portfolio design with TensorFlow 2.0.
- [mlfinlab](https://github.com/hudson-and-thames/mlfinlab) - Implements techniques from Marcos Lopez de Prado's *Advances in Financial Machine Learning*.
- [pyqstrat](https://github.com/abbass2/pyqstrat) - Fast, extensible, transparent Python library for quantitative strategy backtesting.
- [NowTrade](https://github.com/edouardpoitras/NowTrade) - Python library for backtesting technical/mechanical strategies in stock and forex markets.
- [pinkfish](https://github.com/fja05680/pinkfish) - A backtesting and spreadsheet library for securities analysis.
- [aat](https://github.com/timkpaine/aat) - Asynchronous algorithmic trading engine.
- [Backtesting.py](https://kernc.github.io/backtesting.py/) - Backtesting trading strategies with Python.
- [catalyst](https://github.com/enigmampc/catalyst) - Python algorithmic trading library for crypto assets.
- [quantstats](https://github.com/ranaroussi/quantstats) - Portfolio analytics for quantitative research (Python).
- [qtpylib](https://github.com/ranaroussi/qtpylib) - Pythonic algorithmic trading library <http://qtpylib.io>.
- [Quantdom](https://github.com/constverum/Quantdom) - Python framework for backtesting trading strategies and market analysis [with GUI].
- [freqtrade](https://github.com/freqtrade/freqtrade) - Free, open-source crypto trading bot.
- [algorithmic-trading-with-python](https://github.com/chrisconlan/algorithmic-trading-with-python) - Resources from *Algorithmic Trading with Python*.
- [DeepDow](https://github.com/jankrepl/deepdow) - Portfolio optimization with deep learning.
- [Qlib](https://github.com/microsoft/qlib) - Microsoft's AI-oriented quantitative investment platform.
- [machine-learning-for-trading](https://github.com/stefan-jansen/machine-learning-for-trading) - Code and resources for *Machine Learning for Algorithmic Trading*.
- [AlphaPy](https://github.com/ScottfreeLLC/AlphaPy) - Automated Machine Learning [AutoML] library.
- [jesse](https://github.com/jesse-ai/jesse) - An advanced crypto trading bot written in Python.
- [rqalpha](https://github.com/ricequant/rqalpha) - An extensible Python algorithmic backtesting & trading framework.
- [FinRL-Library](https://github.com/AI4Finance-LLC/FinRL-Library) - Deep reinforcement learning library for quantitative finance. NeurIPS 2020.
- [bulbea](https://github.com/achillesrasquinha/bulbea) - Deep learning-based Python library for stock market prediction and modeling.
- [ib_nope](https://github.com/ajhpark/ib_nope) - Automated NOPE strategy trading system based on IBKR TWS.
- [OctoBot](https://github.com/Drakkar-Software/OctoBot) - Open-source crypto trading bot with advanced web interface.
- [bta-lib](https://github.com/mementum/bta-lib) - Pandas-based technical analysis library for backtesting and quantitative analysis.
- [Stock-Prediction-Models](https://github.com/huseinzol05/Stock-Prediction-Models) - Collection of ML and DL stock prediction models with trading bots and simulations.
- [TuneTA](https://github.com/jmrichardson/tuneta) - Optimize technical indicators using distance correlation against user-defined target features.
- [AutoTrader](https://github.com/kieran-mackle/AutoTrader) - Python-based automated trading system development platform.
- [fast-trade](https://github.com/jrmeier/fast-trade) - A backtesting library focused on portability and performance.
- [qf-lib](https://github.com/quarkfin/qf-lib) - High-quality tools for quantitative finance analysis.
- [tda-api](https://github.com/alexgolec/tda-api) - Python client for TDAmeritrade real-time/historical data and order execution.
- [vectorbt](https://github.com/polakowo/vectorbt) - A powerful toolkit for backtesting, algorithmic trading, and research.
- [Lean](https://github.com/QuantConnect/Lean) - QuantConnect's open-source algorithmic trading engine.
- [pysystemtrade](https://github.com/robcarver17/pysystemtrade) - Robert Carver's open-source backtesting engine implementing his *Systematic Trading* framework.
- [pytrendseries](https://github.com/rafa-rod/pytrendseries) - Detect trends, drawdowns, fixed-window maximum drawdown, and underwater periods.
- [PyLOB](https://github.com/DrAshBooth/PyLOB) - A high-performance Limit Order Book in Python.
- [PyBroker](https://github.com/edtechre/pybroker) - A Python framework for machine learning in algorithmic trading.
- [OctoBot Script](https://github.com/Drakkar-Software/OctoBot-Script) - A quantitative framework for crypto strategies with backtesting, optimization, and live trading.
- [hftbacktest](https://github.com/nkaz001/hftbacktest) - HFT and market-making backtesting tool with limit orders, queue position, and latency handling.
- [vnpy](https://github.com/vnpy/vnpy) - VeighNa open-source quantitative trading system development framework.
- [Intelligent Trading Bot](https://github.com/asavinov/intelligent-trading-bot) - ML and feature engineering-based automated trading signal generation and execution.
- [fastquant](https://github.com/enzoampil/fastquant) - Backtest investment strategies in Python with just three lines of code.
- [nautilus_trader](https://github.com/nautechsystems/nautilus_trader) - High-performance event-driven backtesting and live algorithmic trading platform.
- [YABTE](https://github.com/bsdz/yabte) - Yet Another (Python) BackTesting Engine.
- [Trading Strategy](https://github.com/tradingstrategy-ai/getting-started) - A DeFi research, backtesting, live trading, and investment management framework.
- [Hikyuu](https://github.com/fasiondog/hikyuu) - An open-source high-performance quantitative framework based on Python/C++.

### Risk Analysis

- [QuantLibRisks](https://github.com/auto-differentiation/QuantLib-Risks-Py) - Fast risk computation with QuantLib.
- [XAD](https://github.com/auto-differentiation/xad-py) - Automatic Differentiation (AAD) library.
- [pyfolio](https://github.com/quantopian/pyfolio) - Portfolio and risk analytics.
- [empyrical](https://github.com/quantopian/empyrical) - Common financial risk and performance metrics.
- [fecon235](https://github.com/rsvp/fecon235) - Computational tools for financial economics.
- [finance](https://pypi.org/project/finance/) - Financial risk calculations with emphasis on usability through classes and operator overloading.
- [qfrm](https://pypi.org/project/qfrm/) - Quantitative financial risk management: OOP tools for risk measurement, management, and visualization.
- [visualize-wealth](https://github.com/benjaminmgross/visualize-wealth) - Portfolio construction and quantitative analysis.
- [VisualPortfolio](https://github.com/wegamekinglc/VisualPortfolio) - Tools for visualizing portfolio performance.
- [universal-portfolios](https://github.com/Marigold/universal-portfolios) - A collection of online portfolio selection algorithms.
- [FinQuant](https://github.com/fmilthaler/FinQuant) - Portfolio management, analysis, and optimization tools.
- [Empyrial](https://github.com/ssantoshp/Empyrial) - Portfolio risk and performance analysis with return prediction.
- [risktools](https://github.com/bbcho/risktools-dev) - Risk tools for crude oil and refined products trading.
- [Riskfolio-Lib](https://github.com/dcajasn/Riskfolio-Lib) - Python portfolio optimization and quantitative asset allocation library.
- [empyrical-reloaded](https://github.com/stefan-jansen/empyrical-reloaded) - Reloaded fork of common financial risk and performance metrics.
- [pyfolio-reloaded](https://github.com/stefan-jansen/pyfolio-reloaded) - Reloaded fork of portfolio and risk analytics.
- [fortitudo.tech](https://github.com/fortitudo-tech/fortitudo.tech) - Portfolio optimization and stress testing with CVaR and entropy pooling.

### Factor Analysis

- [alphalens](https://github.com/quantopian/alphalens) - Performance analysis of predictive (alpha) stock factors.
- [alphalens-reloaded](https://github.com/stefan-jansen/alphalens-reloaded) - Reloaded fork for alpha factor performance analysis.
- [Spectre](https://github.com/Heerozh/spectre) - GPU-accelerated factor analysis library and backtesting tool.

### Sentiment Analysis

- [Asset News Sentiment Analyzer](https://github.com/KVignesh122/AssetNewsSentimentAnalyzer) - News sentiment analysis and reporting for financial assets using GPT models.

### Quantitative Research Environment

- [Jupyter Quant](https://github.com/gnzsnz/jupyter-quant) - A Dockerized Jupyter quantitative research environment pre-loaded with statsmodels, pymc, arch, py_vollib, zipline-reloaded, PyPortfolioOpt, and more.

### Time Series

- [ARCH](https://github.com/bashtage/arch) - ARCH models in Python.
- [statsmodels](http://statsmodels.sourceforge.net) - Python module for data exploration, statistical model estimation, and tests.
- [dynts](https://github.com/quantmind/dynts) - A Python package for time-series analysis and manipulation.
- [PyFlux](https://github.com/RJT1990/pyflux) - Python library for time-series modeling and inference (frequentist and Bayesian).
- [tsfresh](https://github.com/blue-yonder/tsfresh) - Automatic extraction of relevant features from time series.
- [hasura/quandl-metabase](https://platform.hasura.io/hub/projects/anirudhm/quandl-metabase-time-series) - Hasura quickstart for visualizing Quandl time-series datasets with Metabase.
- [Facebook Prophet](https://github.com/facebook/prophet) - High-quality forecasting for time-series data with multiple seasonality.
- [tsmoothie](https://github.com/cerlymarco/tsmoothie) - Vectorized time-series smoothing and outlier detection.
- [pmdarima](https://github.com/alkaline-ml/pmdarima) - A statistical library providing Python's equivalent of R's auto.arima.
- [gluon-ts](https://github.com/awslabs/gluon-ts) - Probabilistic time-series modeling tools.
- [functime](https://github.com/functime-org/functime) - Large-scale time-series ML library based on Polars for parallel feature extraction and panel data forecasting.

### Calendars

- [exchange_calendars](https://github.com/gerrymanoim/exchange_calendars) - Securities exchange trading calendars.
- [bizdays](https://github.com/wilsonfreitas/python-bizdays) - Business day calculations and tools.
- [pandas_market_calendars](https://github.com/rsheftel/pandas_market_calendars) - Exchange calendars integrated with pandas for quantitative trading.

### Data Sources

- [yfinance](https://github.com/ranaroussi/yfinance) - Yahoo! Finance market data downloader (faster than Pandas Datareader).
- [findatapy](https://github.com/cuemacro/findatapy) - Download market data from Bloomberg, Quandl, Yahoo, and more.
- [googlefinance](https://github.com/hongtaocai/googlefinance) - Python module for real-time stock data from Google Finance API.
- [yahoo-finance](https://github.com/lukaszbanasiak/yahoo-finance) - Python module for stock data from Yahoo! Finance.
- [pandas-datareader](https://github.com/pydata/pandas-datareader) - Read data from multiple sources into Pandas data structures with caching.
- [pandas-finance](https://github.com/davidastephens/pandas-finance) - High-level API for financial data access and analysis.
- [pyhoofinance](https://github.com/innes213/pyhoofinance) - Fast batch Yahoo Finance queries with typed data for analysis.
- [yfinanceapi](https://github.com/Karthik005/yfinanceapi) - Python wrapper for Yahoo! Finance API.
- [yql-finance](https://github.com/slawek87/yql-finance) - Fast stock closing price retrieval using YQL.
- [ystockquote](https://github.com/cgoldberg/ystockquote) - Stock quote data from Yahoo Finance.
- [wallstreet](https://github.com/mcdallas/wallstreet) - Real-time stock and option data.
- [stock_extractor](https://github.com/ZachLiuGIS/stock_extractor) - General-purpose stock data extraction tool.
- [Stockex](https://github.com/cttn/Stockex) - Python wrapper for Yahoo! Finance API.
- [finsymbols](https://github.com/skillachie/finsymbols) - Get stock symbols and info for S&P 500, AMEX, NYSE, NASDAQ.
- [FRB](https://github.com/avelkoski/FRB) - Python client for the FRED API.
- [inquisitor](https://github.com/econdb/inquisitor) - Python interface for the Econdb.com API.
- [yfi](https://github.com/nickelkr/yfi) - YQL (Yahoo! Query Language) library.
- [chinesestockapi](https://pypi.org/project/chinesestockapi/) - Python API for Chinese stock price data.
- [exchange](https://github.com/akarat/exchange) - Get current exchange rates.
- [ticks](https://github.com/jamescnowell/ticks) - Command-line stock data retrieval tool.
- [pybbg](https://github.com/bpsmith/pybbg) - Python interface for Bloomberg COM API.
- [ccy](https://github.com/lsbardel/ccy) - Python currency module.
- [tushare](https://pypi.org/project/tushare/) - Tool for obtaining Chinese stock historical and real-time data.
- [jsm](https://pypi.org/project/jsm/) - Japanese stock market data retrieval.
- [cn_stock_src](https://github.com/jealous/cn_stock_src) - Tool for obtaining Chinese stock fundamental data from various sources.
- [coinmarketcap](https://github.com/barnumbirr/coinmarketcap) - Python API for CoinMarketCap.
- [after-hours](https://github.com/datawrestler/after-hours) - Get stock pre-market and after-hours prices.
- [bronto-python](https://pypi.org/project/bronto-python/) - Python wrapper for Bronto API.
- [pytdx](https://github.com/rainx/pytdx) - Python interface for TongDaXin market data servers.
- [pdblp](https://github.com/matthewgilbert/pdblp) - Simple pandas/Bloomberg Open API integration.
- [tiingo](https://github.com/hydrosquall/tiingo-python) - Python wrapper for Tiingo data platform.
- [iexfinance](https://github.com/addisonlynch/iexfinance) - Python interface for IEX real-time and historical data.
- [pyEX](https://github.com/timkpaine/pyEX) - Python interface for IEX with pandas support and streaming data.
- [alpaca-trade-api](https://github.com/alpacahq/alpaca-trade-api-python) - Python interface for Alpaca API data and trading.
- [metatrader5](https://pypi.org/project/MetaTrader5/) - MetaTrader 5 terminal API connector.
- [akshare](https://github.com/jindaxiang/akshare) - An elegant and simple financial data interface library for Python.
- [yahooquery](https://github.com/dpguthrie/yahooquery) - Unofficial Yahoo Finance Python interface.
- [investpy](https://github.com/alvarobartt/investpy) - Python tool for extracting financial data from Investing.com.
- [yliveticker](https://github.com/yahoofinancelive/yliveticker) - Real-time market data streaming via Yahoo Finance websocket.
- [bbgbridge](https://github.com/ran404/bbgbridge) - Easy-to-use Bloomberg Desktop API Python wrapper.
- [alpha_vantage](https://github.com/RomelTorres/alpha_vantage) - Python wrapper for the Alpha Vantage API.
- [FinanceDataReader](https://github.com/FinanceData/FinanceDataReader) - Open-source financial data reader supporting US, Korean, Japanese, Chinese, Vietnamese markets.
- [pystlouisfed](https://github.com/TomasKoutek/pystlouisfed) - Python client for Federal Reserve Bank of St. Louis APIs.
- [python-bcb](https://github.com/wilsonfreitas/python-bcb) - Python interface for Brazilian Central Bank web services.
- [market-prices](https://github.com/maread99/market_prices) - Generate meaningful OHLCV datasets using exchange calendar information.
- [tardis-python](https://github.com/tardis-dev/tardis-python) - Python wrapper for Tardis.dev high-frequency crypto market data.
- [lake-api](https://github.com/crypto-lake/lake-api) - Python wrapper for Crypto Lake high-frequency market data.
- [tessa](https://github.com/ymyke/tessa) - Fast financial asset price retrieval based on yfinance and pycoingecko.
- [pandaSDMX](https://github.com/dr-leo/pandaSDMX) - Python implementation of SDMX 2.1 for statistical data exchange.
- [cif](https://github.com/LenkaV/CIF) - Python package for composite indicators integrating multi-dimensional economic relationships.
- [finagg](https://github.com/theOGognf/finagg) - Multiple free financial API implementations in Python with SQL aggregation and feature engineering.
- [FinanceDatabase](https://github.com/JerBouma/FinanceDatabase) - A database of 300,000+ symbols including stocks, ETFs, funds, indices, currencies, crypto, and money markets.
- [Trading Strategy](https://github.com/tradingstrategy-ai/trading-strategy/) - Download DeFi price data from decentralized exchanges and lending protocols.
- [datamule-python](https://github.com/john-friedman/datamule-python) - A toolkit for working with SEC data.

### Excel Integration

- [xlwings](https://www.xlwings.org/) - Make Excel fly with Python.
- [openpyxl](https://openpyxl.readthedocs.io/en/latest/) - Read/write Excel 2007 xlsx/xlsm files.
- [xlrd](https://github.com/python-excel/xlrd) - Extract data from Excel files.
- [xlsxwriter](https://xlsxwriter.readthedocs.io/) - Write Excel 2007+ XLSX files.
- [xlwt](https://github.com/python-excel/xlwt) - Create MS Excel 97/2000/XP/2003 compatible spreadsheets.
- [DataNitro](https://datanitro.com/) - Full Python-Excel integration including UDFs.
- [xlloop](http://xlloop.sourceforge.net) - Open-source framework for Excel UDFs on a centralized function server.
- [expy](http://www.bnikolic.co.uk/expy/expy.html) - Plugin for executing Python code directly in Excel spreadsheets.
- [pyxll](https://www.pyxll.com) - An Excel add-in that extends Excel with Python.

### Visualization

- [D-Tale](https://github.com/man-group/dtale) - Visual analysis tool for pandas DataFrames and xarray Datasets.
- [mplfinance](https://github.com/matplotlib/mplfinance) - Financial data visualization and analysis with matplotlib.
- [finplot](https://github.com/highfestiva/finplot) - High-performance, easy-to-use financial visualization.
- [finvizfinance](https://github.com/lit26/finvizfinance) - Finviz data analysis Python library.
- [market-analy](https://github.com/maread99/market_analy) - Interactive chart analysis using market-prices and bqplot.
- [QuantInvestStrats](https://github.com/ArturSepp/QuantInvestStrats) - QIS Python analytics library for financial data visualization and backtesting reports.

---

## R

### Numerical Libraries and Data Structures

- [xts](https://github.com/joshuaulrich/xts) - eXtensible Time Series: providing uniform handling of R time-series classes.
- [data.table](https://github.com/Rdatatable/data.table) - Extension of data.frame for fast aggregation, ordered joins, and column operations.
- [sparseEigen](https://github.com/dppalomar/sparseEigen) - Sparse principal component analysis.
- [TSdbi](http://tsdbi.r-forge.r-project.org/) - Common interface for time-series databases.
- [tseries](https://cran.r-project.org/web/packages/tseries/index.html) - Time-series analysis and computational finance.
- [zoo](https://cran.r-project.org/web/packages/zoo/index.html) - S3 infrastructure for regular and irregular time series.
- [tis](https://cran.r-project.org/web/packages/tis/index.html) - Functions and S3 classes for time indexes and time-indexed series.
- [tfplot](https://cran.r-project.org/web/packages/tfplot/index.html) - Utilities for time-series data handling and plotting.
- [tframe](https://cran.r-project.org/web/packages/tframe/index.html) - Kernel functions for time-series methods programming.

### Data Sources

- [IBrokers](https://cran.r-project.org/web/packages/IBrokers/index.html) - R interface to Interactive Brokers TWS API.
- [Rblpapi](https://github.com/Rblp/Rblpapi) - R interface to the Bloomberg API.
- [Quandl](https://www.quandl.com/tools/r) - Import financial data directly into R.
- [Rbitcoin](https://github.com/jangorecki/Rbitcoin) - Unified crypto exchange API interface for R.
- [GetTDData](https://github.com/msperlin/GetTDData) - Download and aggregate Brazilian government bond data.
- [GetHFData](https://github.com/msperlin/GetHFData) - Download and aggregate high-frequency Brazilian financial data.
- [Reddit WallstreetBets API](https://dashboard.nbshare.io/apps/reddit/api/) - API for top 50 stocks and sentiment from r/wallstreetbets.
- [td](https://github.com/eddelbuettel/td) - Access the twelvedata API for stock and currency data.
- [rbcb](https://github.com/wilsonfreitas/rbcb) - R interface for Brazilian Central Bank web services.
- [rb3](https://github.com/ropensci/rb3) - Functions for downloading and parsing Brazilian exchange (B3) data.
- [simfinapi](https://github.com/matthiasgomolka/simfinapi) - Easy access to SimFin data from R.
- [tidyfinance](https://github.com/tidy-finance/r-tidyfinance) - Convert raw financial data into tidy format for research.

### Financial Instruments and Pricing

- [RQuantLib](https://github.com/eddelbuettel/rquantlib) - Connects GNU R with the QuantLib library.
- [quantmod](https://cran.r-project.org/web/packages/quantmod/index.html) - Quantitative financial modeling framework.
- [Rmetrics](https://www.rmetrics.org) - The leading open-source solution for quantitative finance education and training.
  - [fAsianOptions](https://cran.r-project.org/web/packages/fAsianOptions/index.html) - EBM and Asian option valuation.
  - [fAssets](https://cran.r-project.org/web/packages/fAssets/index.html) - Financial asset analysis and modeling.
  - [fBasics](https://cran.r-project.org/web/packages/fBasics/index.html) - Markets and basic statistics.
  - [fBonds](https://cran.r-project.org/web/packages/fBonds/index.html) - Bonds and interest rate models.
  - [fExoticOptions](https://cran.r-project.org/web/packages/fExoticOptions/index.html) - Exotic option valuation.
  - [fOptions](https://cran.r-project.org/web/packages/fOptions/index.html) - Basic option pricing and evaluation.
  - [fPortfolio](https://cran.r-project.org/web/packages/fPortfolio/index.html) - Portfolio selection and optimization.
- [portfolio](https://github.com/dgerlanc/portfolio) - Equity portfolio analysis.
- [sparseIndexTracking](https://github.com/dppalomar/sparseIndexTracking) - Portfolio design for index tracking.
- [covFactorModel](https://github.com/dppalomar/covFactorModel) - Covariance matrix estimation through factor models.
- [riskParityPortfolio](https://github.com/dppalomar/riskParityPortfolio) - Ultra-fast risk parity portfolio design.
- [sde](https://cran.r-project.org/web/packages/sde/index.html) - Simulation and inference for stochastic differential equations.
- [YieldCurve](https://cran.r-project.org/web/packages/YieldCurve/index.html) - Yield curve modeling and estimation.
- [SmithWilsonYieldCurve](https://cran.r-project.org/web/packages/SmithWilsonYieldCurve/index.html) - Construct yield curves from LIBOR and SWAP rates using Smith-Wilson.
- [ycinterextra](https://cran.r-project.org/web/packages/ycinterextra/index.html) - Interpolation and extrapolation of yield curves.
- [AmericanCallOpt](https://cran.r-project.org/web/packages/AmericanCallOpt/index.html) - American call option pricing on dividend-paying assets.
- [VarSwapPrice](https://cran.r-project.org/web/packages/VarSwapPrice/index.html) - Variance swap pricing.
- [RND](https://cran.r-project.org/web/packages/RND/index.html) - Risk-neutral density extraction toolkit.
- [LSMonteCarlo](https://cran.r-project.org/web/packages/LSMonteCarlo/index.html) - American option pricing via least squares Monte Carlo.
- [OptHedging](https://cran.r-project.org/web/packages/OptHedging/index.html) - Option value and hedging strategy estimation.
- [tvm](https://cran.r-project.org/web/packages/tvm/index.html) - Time value of money functions.
- [OptionPricing](https://cran.r-project.org/web/packages/OptionPricing/index.html) - Option pricing and efficient simulation algorithms.
- [credule](https://github.com/blenezet/credule) - Credit default swap functions.
- [derivmkts](https://cran.r-project.org/web/packages/derivmkts/index.html) - Functions and examples from *Derivatives Markets*.
- [FinCal](https://github.com/felixfan/FinCal) - Time value calculations, time-series analysis, and computational finance.
- [r-quant](https://github.com/artyyouth/r-quant) - Example code for quantitative finance analysis in R.
- [options.studies](https://github.com/taylorizing/options.studies) - Option trading study functions.
- [PortfolioAnalytics](https://github.com/braverock/PortfolioAnalytics) - Portfolio analysis and numerical optimization methods.
- [fmbasics](https://github.com/imanuelcostigan/fmbasics) - Financial market building blocks.
- [R-fixedincome](https://github.com/wilsonfreitas/R-fixedincome) - R tools for fixed income instruments.

### Trading

- [backtest](https://cran.r-project.org/web/packages/backtest/index.html) - Explore portfolio-based hypotheses.
- [pa](https://cran.r-project.org/web/packages/pa/index.html) - Equity portfolio performance attribution.
- [TTR](https://github.com/joshuaulrich/TTR) - Technical trading rules.
- [QuantTools](https://quanttools.bitbucket.io/_site/index.html) - Enhanced quantitative trading modeling.
- [blotter](https://github.com/braverock/blotter) - Transaction framework for portfolios and accounts.

### Backtesting

- [quantstrat](https://github.com/braverock/quantstrat) - Transaction framework for building and simulating trading systems.

### Risk Analysis

- [PerformanceAnalytics](https://github.com/braverock/PerformanceAnalytics) - Econometric tools for portfolio and risk analysis.

### Factor Analysis

- [FactorAnalytics](https://github.com/braverock/FactorAnalytics) - Toolkit for fundamental, time-series, and statistical factor models.
- [Expected Returns](https://github.com/JustinMShea/ExpectedReturns) - R implementations of portfolio methods from *Expected Returns* by Antti Ilmanen.

### Time Series

- [tseries](https://cran.r-project.org/web/packages/tseries/index.html) - Time-series analysis and computational finance.
- [fGarch](https://cran.r-project.org/web/packages/fGarch/index.html) - Autoregressive conditional heteroskedastic models.
- [timeSeries](https://cran.r-project.org/web/packages/timeSeries/index.html) - Financial time-series objects.
- [rugarch](https://github.com/alexiosg/rugarch) - Univariate GARCH models.
- [rmgarch](https://github.com/alexiosg/rmgarch) - Multivariate GARCH models.
- [tidypredict](https://github.com/edgararuiz/tidypredict) - Run predictions inside databases.
- [tidyquant](https://github.com/business-science/tidyquant) - Bringing financial analysis to the tidyverse.
- [timetk](https://github.com/business-science/timetk) - Time-series analysis toolkit for R.
- [tibbletime](https://github.com/business-science/tibbletime) - Time-aware tibbles for the tidyverse.
- [matrixprofile](https://github.com/matrix-profile-foundation/matrixprofile) - Time-series data mining with matrix profiles.
- [garchmodels](https://github.com/AlbertoAlmuinha/garchmodels) - A parsnip backend for GARCH models.

### Calendars

- [timeDate](https://cran.r-project.org/web/packages/timeDate/index.html) - Time and calendar objects.
- [bizdays](https://github.com/wilsonfreitas/R-bizdays) - Business day calculations and tools.

---

## Matlab

### Frameworks

- [QUANTAXIS](https://github.com/yutiansut/quantaxis) - Matlab integrated quantitative toolbox.
- [PROJ_Option_Pricing_Matlab](https://github.com/jkirkby3/PROJ_Option_Pricing_Matlab) - Quantitative option pricing for exotic and vanilla options.

---

## Julia

- [Lucky.jl](https://github.com/oliviermilla/Lucky.jl) - A pure Julia modular, async trading engine.
- [QuantLib.jl](https://github.com/pazzo83/QuantLib.jl) - QuantLib implementation in Julia.
- [Ito.jl](https://github.com/aviks/Ito.jl) - Quantitative finance package for Julia.
- [TALib.jl](https://github.com/femtotrader/TALib.jl) - Julia wrapper for TA-Lib.
- [IncTA.jl](https://github.com/femtotrader/IncTA.jl) - Incremental technical analysis indicators for Julia.
- [Miletus.jl](https://github.com/JuliaComputing/Miletus.jl) - A financial contract definition, modeling, and pricing framework.
- [Temporal.jl](https://github.com/dysonance/Temporal.jl) - Flexible and efficient time-series class and methods.
- [Indicators.jl](https://github.com/dysonance/Indicators.jl) - Financial market technical analysis and indicators based on Temporal.
- [Strategems.jl](https://github.com/dysonance/Strategems.jl) - Quantitative systematic trading strategy development and backtesting.
- [TimeSeries.jl](https://github.com/JuliaStats/TimeSeries.jl) - Time-series toolkit for Julia.
- [MarketTechnicals.jl](https://github.com/JuliaQuant/MarketTechnicals.jl) - Financial time-series technical analysis based on TimeSeries.
- [MarketData.jl](https://github.com/JuliaQuant/MarketData.jl) - Financial market time-series data.
- [TimeFrames.jl](https://github.com/femtotrader/TimeFrames.jl) - Julia library for resampling TimeSeries.
- [DataFrames.jl](https://github.com/JuliaData/DataFrames.jl) - In-memory tabular data in Julia.
- [TSFrames.jl](https://github.com/xKDR/TSFrames.jl) - Handling time-series data based on DataFrames.jl.

---

## Java

- [Strata](http://strata.opengamma.io/) - Modern open-source analytics and market risk library by OpenGamma.
- [JQuantLib](https://github.com/frgomes/jquantlib) - Free, open-source quantitative finance framework in 100% Java.
- [finmath.net](http://finmath.net) - Java library for mathematical finance.
- [quantcomponents](https://github.com/lsgro/quantcomponents) - Free Java components for quantitative finance and algorithmic trading.
- [DRIP](https://lakshmidrip.github.io/DRIP) - Fixed income, asset allocation, transaction cost analysis, and XVA metrics.
- [ta4j](https://github.com/ta4j/ta4j) - Java library for technical analysis.

---

## JavaScript

- [finance.js](https://github.com/ebradyjobory/finance.js) - JavaScript library for common financial calculations.
- [portfolio-allocation](https://github.com/lequant40/portfolio_allocation_js) - JavaScript library for constructing multi-asset portfolios.
- [Ghostfolio](https://github.com/ghostfolio/ghostfolio) - Wealth management software for tracking financial assets and making data-driven investment decisions.
- [IndicatorTS](https://github.com/cinar/indicatorts) - TypeScript technical analysis indicators, strategies, and backtesting.
- [chart-patterns](https://github.com/focus1691/chart-patterns) - Technical analysis library for market profile, volume profile, and imbalance indicators.
- [orderflow](https://github.com/focus1691/orderflow) - Order flow trade aggregator for building footprint candles from exchange websockets.
- [ccxt](https://github.com/ccxt/ccxt) - JavaScript/Python/PHP cryptocurrency trading API for 100+ exchanges.
- [PENDAX](https://github.com/CompendiumFi/PENDAX-SDK) - JavaScript SDK for crypto exchange data, trading, and WebSocket.

#### Data Visualization

- [QUANTAXIS_Webkit](https://github.com/yutiansut/QUANTAXIS_Webkit) - Visualization center based on QUANTAXIS.

---

## Haskell

- [quantfin](https://github.com/boundedvariation/quantfin) - Pure Haskell quantitative finance library.
- [Haxcel](https://github.com/MarcusRainbow/Haxcel) - Haskell add-in for Excel.
- [Ffinar](https://github.com/MarcusRainbow/Ffinar) - Financial mathematics in Haskell.

---

## Scala

- [QuantScale](https://github.com/choucrifahed/quantscale) - Scala quantitative finance library.
- [Scala Quant](https://github.com/frankcash/Scala-Quant) - Scala library for stock data from IFTTT or Google Finance.

---

## Ruby

- [Jiji](https://github.com/unageanu/jiji2) - Open-source forex algorithmic trading framework using OANDA REST API.

---

## Elixir/Erlang

- [Tai](https://github.com/fremantle-capital/tai) - An open, composable, real-time market data and trade execution toolkit.
- [Workbench](https://github.com/fremantle-industries/workbench) - From idea to execution -- manage your trading operation across a distributed cluster.
- [Prop](https://github.com/fremantle-industries/prop) - An open, opinionated trading platform for strategy research, execution, and operations.

---

## Golang

- [Kelp](https://github.com/stellar/kelp) - Open-source Golang algo trading bot for centralized exchanges and Stellar DEX.
- [marketstore](https://github.com/alpacahq/marketstore) - DataFrame server for financial time-series data.
- [IndicatorGo](https://github.com/cinar/indicator) - Golang module with stock technical analysis indicators, strategies, and backtesting.

---

## CPP

- [QuantLib](https://github.com/lballabio/QuantLib) - A comprehensive quantitative finance software framework.
- [QuantLibRisks](https://github.com/auto-differentiation/QuantLib-Risks-Cpp) - Fast risk computation with QuantLib in C++.
- [XAD](https://github.com/auto-differentiation/xad) - Automatic Differentiation (AAD) library.
- [TradeFrame](https://github.com/rburkholder/trade-frame) - C++17 trading framework/library for testing automated options trading strategies.
- [Hikyuu](https://github.com/fasiondog/hikyuu) - Open-source high-performance quantitative framework based on C++/Python.

---

## Frameworks

- [QuantLib](https://github.com/lballabio/QuantLib) - A comprehensive quantitative finance software framework.
  - QuantLibRisks - Fast risk computation in [Python](https://pypi.org/project/QuantLib-Risks/) and [C++](https://github.com/auto-differentiation/QuantLib-Risks-Cpp).
  - XAD - Automatic Differentiation in [Python](https://pypi.org/project/xad/) and [C++](https://github.com/auto-differentiation/xad/).
  - [JQuantLib](https://github.com/frgomes/jquantlib) - Java port.
  - [RQuantLib](https://github.com/eddelbuettel/rquantlib) - R wrapper.
  - [QuantLibAddin](https://www.quantlib.org/quantlibaddin/) - Excel support.
  - [QuantLibXL](https://www.quantlib.org/quantlibxl/) - Excel support.
  - [QLNet](https://github.com/amaggiulli/qlnet) - .NET port.
  - [PyQL](https://github.com/enthought/pyql) - Python port.
  - [QuantLib.jl](https://github.com/pazzo83/QuantLib.jl) - Julia port.
  - [QuantLib-Python Documentation](https://quantlib-python-docs.readthedocs.io/) - Documentation for QuantLib Python bindings.

- [TA-Lib](https://ta-lib.org) - Technical analysis of financial market data.
  - [ta-lib-python](https://github.com/TA-Lib/ta-lib-python)
  - [ta-lib](https://github.com/TA-Lib/ta-lib)
- [Portfolio Optimizer](https://portfoliooptimizer.io/) - Web API-based portfolio analysis and optimization.
- XAD: Automatic Differentiation (AAD) for [Python](https://pypi.org/project/xad/) and [C++](https://github.com/auto-differentiation/xad/)

---

## CSharp

- [QuantConnect](https://github.com/QuantConnect/Lean) - Lean Engine is an open-source C# algorithmic trading engine for desktop or cloud.
- [StockSharp](https://github.com/StockSharp/StockSharp) - Open-source algorithmic trading and quantitative trading platform.
- [TDAmeritrade.DotNetCore](https://github.com/NVentimiglia/TDAmeritrade.DotNetCore) - Free, open-source .NET client for the TD Ameritrade API.

---

## Rust

- [QuantMath](https://github.com/MarcusRainbow/QuantMath) - Financial mathematics library for risk-neutral pricing and risk management.
- [Barter](https://github.com/barter-rs/barter-rs) - Open-source Rust framework for event-driven live trading and backtesting.
- [LFEST](https://github.com/MathisWellmann/lfest-rs) - Simulated perpetual futures exchange for paper trading strategies.
- [TradeAggregation](https://github.com/MathisWellmann/trade_aggregation-rs) - Aggregate trades into custom candles using information-driven rules.
- [SlidingFeatures](https://github.com/MathisWellmann/sliding_features-rs) - Chained tree-based sliding windows for signal processing and technical analysis.
- [RustQuant](https://github.com/avhz/RustQuant) - A quantitative finance library written in Rust.
- [finalytics](https://github.com/Nnamdi-sys/finalytics) - Rust library for financial data analysis.

---
