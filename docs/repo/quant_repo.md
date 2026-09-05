# 基于不同编程语言的量化框架与其Github仓库

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
本列表由[LLMQuant社区](https://llmquant.com/)整理, 个精心整理、极其优秀的量化（定量金融）相关库、包及资源列表, 只供学习交流使用, 版权归原作者所有。

## 语言

- [Python](#python) - 最流行的量化金融语言，拥有丰富的数据分析、机器学习库和金融工具包
- [R](#r) - 统计分析的首选语言，在金融建模和风险分析方面有独特优势
- [Matlab](#matlab) - 在金融工程和数值计算领域广泛使用，尤其适合矩阵运算
- [Julia](#julia) - 专为高性能数值计算设计的新兴语言，在量化金融中逐渐流行
- [Java](#java) - 企业级应用的标准选择，适合构建大规模交易系统
- [JavaScript](#javascript) - 主要用于金融数据可视化和Web端交易界面开发
- [Haskell](#haskell) - 函数式编程语言，在复杂金融产品建模方面具有优势
- [Scala](#scala) - 结合了面向对象和函数式编程，适合构建高并发交易系统
- [Ruby](#ruby) - 以简洁著称，主要用于快速开发原型和小型交易系统
- [Elixir/Erlang](#elixirerlang) - 在构建容错和分布式交易系统方面表现出色
- [Golang](#golang) - 以高性能和并发特性著称，适合开发高频交易系统
- [CPP](#cpp) - 最适合开发低延迟交易系统的语言，广泛应用于高频交易
- [CSharp](#csharp) - 微软技术栈的首选，在Windows平台上开发量化交易系统的理想选择
- [Rust](#rust) - 新一代系统编程语言，在保证性能的同时提供内存安全保证
- [Frameworks](#frameworks) - 跨语言的量化金融框架，提供完整的交易和分析解决方案
- [再现研究成果、培训与书籍](#再现研究成果培训与书籍) - 学习资源和经典研究的代码实现

### 选择建议

1. **入门学习**
   - Python：最佳入门选择，学习资源丰富，生态系统完善
   - R：适合想专注于统计分析和风险建模的学习者

2. **专业开发**
   - C++：追求极致性能的高频交易系统
   - Java：企业级交易平台开发
   - Golang：现代高并发交易系统

3. **特定场景**
   - Julia：需要高性能数值计算
   - JavaScript：开发Web交易界面
   - Rust：需要兼顾性能和安全性

4. **研究导向**
   - Python/R：数据分析和策略研究
   - Matlab：金融工程研究
   - Julia：算法优化研究

### 技术栈趋势

- Python生态持续主导量化金融领域
- Julia在高性能计算领域崭露头角
- Rust在系统级开发中逐渐替代C++
- Go语言在微服务架构中应用增多

---

## Python

### 数值库与数据结构

- [numpy](https://www.numpy.org) - NumPy 是 Python 科学计算的基础包。
- [scipy](https://www.scipy.org) - SciPy（发音类似"Sigh Pie"）是基于 Python 的开源数学、科学和工程生态系统。
- [pandas](https://pandas.pydata.org) - pandas 是一个开源的、BSD 许可的库，为 Python 提供高性能、易于使用的数据结构和数据分析工具。
- [polars](https://docs.pola.rs/) - Polars 是一个用于操作结构化数据的超快 DataFrame 库。
- [quantdsl](https://github.com/johnbywater/quantdsl) - 面向金融和交易的定量分析领域专用语言。
- [statistics](https://docs.python.org/3/library/statistics.html) - Python 内置的基础统计计算库。
- [sympy](https://www.sympy.org/) - SymPy 是一个 Python 符号数学库。
- [pymc3](https://docs.pymc.io/) - Python 中的概率编程：基于 Theano 的贝叶斯建模和概率机器学习。
- [modelx](https://docs.modelx.io/) - 将电子表格重新想象为与 pandas 互操作的基于公式的对象。
- [ArcticDB](https://github.com/man-group/ArcticDB) - 面向时间序列和报价数据的高性能数据存储。

### 金融工具与定价

- [OpenBB Terminal](https://github.com/OpenBB-finance/OpenBBTerminal) - 人人可用的投资研究终端。
- [Fincept Terminal](https://github.com/Fincept-Corporation/FinceptTerminal) - 基于高级数据与 AI 的金融资产研究终端。
- [PyQL](https://github.com/enthought/pyql) - QuantLib 的 Python 移植版本。
- [pyfin](https://github.com/opendoor-labs/pyfin) - Python 中的基础期权定价。*存档项目*
- [vollib](https://github.com/vollib/vollib) - 计算期权价格、隐含波动率和希腊值的 Python 库。
- [QuantPy](https://github.com/jsmidt/QuantPy) - Python 中的定量金融框架。
- [Finance-Python](https://github.com/alpha-miner/Finance-Python) - Python 金融工具集。
- [ffn](https://github.com/pmorissette/ffn) - 金融函数库。
- [pynance](https://github.com/GriffinAustin/pynance) - 轻量级 Python 库，用于装配和分析金融数据。
- [tia](https://github.com/bpsmith/tia) - 集成与分析的工具包。
- [hasura/base-python-dash](https://platform.hasura.io/hub/projects/hasura/base-python-dash) - Hasura 快速启动，用于部署 Dash 框架。Dash 基于 Flask、Plotly.js 和 React.js，非常适用于在纯 Python 中构建数据可视化应用。
- [hasura/base-python-bokeh](https://platform.hasura.io/hub/projects/hasura/base-python-bokeh) - Hasura 快速启动，用 bokeh 库可视化数据。
- [pysabr](https://github.com/ynouri/pysabr) - SABR 模型的 Python 实现。
- [FinancePy](https://github.com/domokane/FinancePy) - 专注于定价和风险管理金融衍生品（包括固定收益、股票、外汇和信用衍生品）的 Python 库。
- [gs-quant](https://github.com/goldmansachs/gs-quant) - 高盛提供的定量金融 Python 工具箱。
- [willowtree](https://github.com/federicomariamassari/willowtree) - 对衍生品定价使用柳树格 lattice 的 Python 实现。
- [financial-engineering](https://github.com/federicomariamassari/financial-engineering) - 以 Python 进行金融工程项目的蒙特卡洛方法应用。
- [optlib](https://github.com/dbrojas/optlib) - 一款期权定价的 Python 库。
- [tf-quant-finance](https://github.com/google/tf-quant-finance) - 基于 TensorFlow 的高性能量化金融库。
- [Q-Fin](https://github.com/RomanMichaelPaolucci/Q-Fin) - 针对数学金融的 Python 库。
- [Quantsbin](https://github.com/quantsbin/Quantsbin) - 用于定价与绘制香草期权价格、希腊值等分析的工具集。
- [finoptions](https://github.com/bbcho/finoptions-dev) - 完整实现 R 包 fOptions 以及部分 fExoticOptions 的 Python 库，定价各类期权。
- [pypme](https://github.com/ymyke/pypme) - PME（Public Market Equivalent）的计算工具。
- [AbsBox](https://github.com/yellowbean/AbsBox) - Python 库，用于模拟资产支持证券（ABS）和抵押贷款支持证券（MBS）等结构化产品的现金流。
- [Intrinsic-Value-Calculator](https://github.com/akashaero/Intrinsic-Value-Calculator) - 基于贴现现金流（DCF）分析的股票内在价值计算器。
- [Kelly-Criterion](https://github.com/deltaray-io/kelly-criterion) - 使用 Kelly 公式进行投资组合头寸规模控制的 Python 实现。
- [rateslib](https://github.com/attack68/rateslib) - 用于定价债券、国债期货，以及诸如 IRS、跨货币和外汇互换等衍生品的固定收益库。
- [fypy](https://github.com/jkirkby3/fypy) - 用于研究和开发的香草及奇异期权定价库。关注在 Black-Scholes 之外的模型定价，以及市场数据的校准。

### 指标

- [pandas_talib](https://github.com/femtotrader/pandas_talib) - 基于 Pandas 实现的技术分析指标。
- [finta](https://github.com/peerchemist/finta) - 常见金融技术分析指标的 Pandas 实现。
- [Tulipy](https://github.com/cirla/tulipy) - 金融技术分析指标库（为 [tulipindicators](https://github.com/TulipCharts/tulipindicators) 提供 Python 封装）。
- [lppls](https://github.com/Boulder-Investment-Technologies/lppls) - 针对 [Log-Periodic Power Law Singularity (LPPLS)](https://en.wikipedia.org/wiki/Didier_Sornette#The_JLS_and_LPPLS_models) 模型的 Python 拟合模块。
- [talipp](https://github.com/nardew/talipp) - 针对 Python 的增量式技术分析指标库。
- [streaming_indicators](https://github.com/mr-easy/streaming_indicators) - 用于在流数据上计算技术分析指标的 Python 库。

### 交易与回测

- [skfolio](https://github.com/skfolio/skfolio) - 基于 scikit-learn 的投资组合优化 Python 库，提供统一接口与兼容 sklearn 的工具来构建、调参和交叉验证投资组合模型。
- [Investing algorithm framework](https://github.com/coding-kitties/investing-algorithm-framework) - 用于开发、回测和部署自动化交易算法的框架。
- [QSTrader](https://github.com/mhallsmoore/qstrader) - QSTrader 回测仿真引擎。
- [Blankly](https://github.com/Blankly-Finance/Blankly) - 完整集成回测、模拟交易及实时部署。
- [TA-Lib](https://github.com/mrjbq7/ta-lib) - TA-Lib (<http://ta-lib.org/>) 的 Python 封装。
- [zipline](https://github.com/quantopian/zipline) - Pythonic 的算法交易库。
- [zipline-reloaded](https://github.com/stefan-jansen/zipline-reloaded) - Zipline 的衍生版本，一个 Pythonic 算法交易库。
- [QuantSoftware Toolkit](https://github.com/QuantSoftware/QuantSoftwareToolkit) - 基于 Python 的开源软件框架，用于支持投资组合构建和管理。
- [quantitative](https://github.com/jeffrey-liang/quantitative) - 定量金融和回测库。
- [analyzer](https://github.com/llazzaro/analyzer) - 面向实时金融和回测交易策略的 Python 框架。
- [bt](https://github.com/pmorissette/bt) - 灵活的 Python 回测库。
- [backtrader](https://github.com/backtrader/backtrader) - Python 交易策略回测库。
- [pythalesians](https://github.com/thalesians/pythalesians) - Python 库，用于回测交易策略、绘制图表、无缝下载市场数据、分析市场模式等。
- [pybacktest](https://github.com/ematvey/pybacktest) - 基于 Python / pandas 的向量化回测框架，使回测更简单。
- [pyalgotrade](https://github.com/gbeced/pyalgotrade) - Python 算法交易库。
- [basana](https://github.com/gbeced/basana) - 基于 Python 异步与事件驱动的算法交易框架，专注于加密货币。
- [tradingWithPython](https://pypi.org/project/tradingWithPython/) - 一组用于量化交易的函数和类集合。
- [Pandas TA](https://github.com/twopirllc/pandas-ta) - 拥有 115+ 指标的简易 Python 3 Pandas 扩展，用于构建自定义策略。
- [ta](https://github.com/bukosabino/ta) - 使用 Pandas 的技术分析库 (Python)。
- [algobroker](https://github.com/joequant/algobroker) - 一个执行引擎，用于算法交易。
- [pysentosa](https://pypi.org/project/pysentosa/) - sentosa 交易系统的 Python API。
- [finmarketpy](https://github.com/cuemacro/finmarketpy) - 用于回测交易策略和分析金融市场的 Python 库。
- [binary-martingale](https://github.com/metaperl/binary-martingale) - 自动二元期权交易的马丁格尔策略计算机程序。
- [fooltrader](https://github.com/foolcage/fooltrader) - 使用大数据技术统一分析整个市场的项目。
- [zvt](https://github.com/zvtvz/zvt) - 使用 SQL、pandas 提供统一可扩展的方式来记录数据、计算因子、选股、回测、实时交易，并可实时清晰地可视化所有流程。
- [pylivetrader](https://github.com/alpacahq/pylivetrader) - 兼容 zipline 的实时交易库。
- [pipeline-live](https://github.com/alpacahq/pipeline-live) - 使用 IEX 数据进行实时交易的 zipline pipeline 功能。
- [zipline-extensions](https://github.com/quantrocket-llc/zipline-extensions) - Zipline 在 QuantRocket 环境下的扩展与适配。
- [moonshot](https://github.com/quantrocket-llc/moonshot) - 基于 Pandas 的向量化回测与交易引擎，适配 QuantRocket。
- [PyPortfolioOpt](https://github.com/robertmartin8/PyPortfolioOpt) - Python 中的投资组合优化，包括传统有效前沿法与高级方法。
- [Eiten](https://github.com/tradytics/eiten) - Tradytics 出品的开源工具包，包含各种投资组合算法（如最小方差组合、最大 Sharpe 比率组合、遗传算法组合等）。
- [riskparity.py](https://github.com/dppalomar/riskparity.py) - 使用 TensorFlow 2.0 的快速、可扩展风险平价投资组合设计。
- [mlfinlab](https://github.com/hudson-and-thames/mlfinlab) - 实现 Marcos Lopez de Prado 所著《Advances in Financial Machine Learning》中的相关技术（特征工程、金融数据结构、元标签）。
- [pyqstrat](https://github.com/abbass2/pyqstrat) - 快速、可扩展、透明的 Python 定量策略回测库。
- [NowTrade](https://github.com/edouardpoitras/NowTrade) - 股票和外汇市场上用于回测技术/机械策略的 Python 库。
- [pinkfish](https://github.com/fja05680/pinkfish) - 一个回测和电子表格库，用于证券分析。
- [aat](https://github.com/timkpaine/aat) - 异步算法交易引擎。
- [Backtesting.py](https://kernc.github.io/backtesting.py/) - 使用 Python 回测交易策略。
- [catalyst](https://github.com/enigmampc/catalyst) - 面向加密资产的 Python 算法交易库。
- [quantstats](https://github.com/ranaroussi/quantstats) - 面向量化研究的投资组合分析库（Python）。
- [qtpylib](https://github.com/ranaroussi/qtpylib) - Pythonic 算法交易库 <http://qtpylib.io>。
- [Quantdom](https://github.com/constverum/Quantdom) - 基于 Python 的回测交易策略与市场分析框架 [带 GUI :neckbeard:]。
- [freqtrade](https://github.com/freqtrade/freqtrade) - 免费、开源的加密货币交易机器人。
- [algorithmic-trading-with-python](https://github.com/chrisconlan/algorithmic-trading-with-python) - 《Algorithmic Trading with Python》中的示例与资源。
- [DeepDow](https://github.com/jankrepl/deepdow) - 使用深度学习进行投资组合优化。
- [Qlib](https://github.com/microsoft/qlib) - 微软推出的面向 AI 的量化投资平台。涵盖数据处理、模型训练、回测等全流程，并支持 alpha 寻找、风险建模、投资组合优化、订单执行。
- [machine-learning-for-trading](https://github.com/stefan-jansen/machine-learning-for-trading) - 《Machine Learning for Algorithmic Trading》相关代码与资源。
- [AlphaPy](https://github.com/ScottfreeLLC/AlphaPy) - 自动化机器学习 [AutoML] 库，支持 Python、scikit-learn、Keras、XGBoost、LightGBM 和 CatBoost。
- [jesse](https://github.com/jesse-ai/jesse) - 先进的加密货币交易机器人，采用 Python 编写。
- [rqalpha](https://github.com/ricequant/rqalpha) - 可扩展、可替换的 Python 算法回测 & 交易框架，支持多种金融产品。
- [FinRL-Library](https://github.com/AI4Finance-LLC/FinRL-Library) - 面向量化金融的深度强化学习库。NeurIPS 2020。
- [bulbea](https://github.com/achillesrasquinha/bulbea) - 基于深度学习的 Python 库，用于股票市场预测与建模。
- [ib_nope](https://github.com/ajhpark/ib_nope) - 基于 IBKR TWS 的 NOPE 策略自动化交易系统。
- [OctoBot](https://github.com/Drakkar-Software/OctoBot) - 开源加密货币交易机器人，支持高频、套利、技术分析和社交化交易，并提供高级 Web 界面。
- [bta-lib](https://github.com/mementum/bta-lib) - 基于 Pandas 的技术分析库，用于回测与量化分析。
- [Stock-Prediction-Models](https://github.com/huseinzol05/Stock-Prediction-Models) - 集成多种机器学习与深度学习的股票预测模型，并包含交易机器人和模拟。
- [TuneTA](https://github.com/jmrichardson/tuneta) - 通过距离相关度度量（distance correlation）来优化技术指标，与用户定义的目标特征（如次日收益）对齐。
- [AutoTrader](https://github.com/kieran-mackle/AutoTrader) - 基于 Python 的自动化交易系统开发平台，包括回测、优化和实盘交易。
- [fast-trade](https://github.com/jrmeier/fast-trade) - 专注回测可移植性和性能的交易策略回测库。
- [qf-lib](https://github.com/quarkfin/qf-lib) - 提供高质量工具用于定量金融分析，涵盖交易策略、回测等功能。
- [tda-api](https://github.com/alexgolec/tda-api) - 用于获取美股实时/历史行情及下单交易的 TDAmeritrade Python 客户端。
- [vectorbt](https://github.com/polakowo/vectorbt) - 用于回测、算法交易与研究的强大工具包。
- [ManifoldBT](https://github.com/manifoldbt/manifoldbt) - 基于 Rust 核心的高性能 Python 回测引擎：向量化信号表达式、真实成交（费用/滑点/前视偏差）、参数扫描、滚动窗口与蒙特卡洛。
- [Lean](https://github.com/QuantConnect/Lean) - QuantConnect 出品的开源 .NET/Mono/Python 算法交易引擎。
- [fast-trade](https://github.com/jrmeier/fast-trade) - 低代码回测库，基于 pandas 与技术指标。
- [pysystemtrade](https://github.com/robcarver17/pysystemtrade) - Robert Carver 开源的回测交易引擎，实现了其在《Systematic Trading》一书中阐述的策略框架，并在其[博客](https://qoppac.blogspot.com/)上进一步拓展。
- [pytrendseries](https://github.com/rafa-rod/pytrendseries) - 检测时间序列趋势、回撤、固定窗口最大回撤及"水下"时间。
- [PyLOB](https://github.com/DrAshBooth/PyLOB) - Python 编写的高性能订单簿（Limit Order Book）。
- [PyBroker](https://github.com/edtechre/pybroker) - 将机器学习用于算法交易的 Python 框架。
- [OctoBot Script](https://github.com/Drakkar-Software/OctoBot-Script) - 一个创建加密货币策略的量化框架，支持回测、优化和实盘交易。
- [hftbacktest](https://github.com/nkaz001/hftbacktest) - 高频交易与做市策略回测工具，可处理限价单、队列位置及延迟，使用逐笔交易与订单簿完整数据。
- [vnpy](https://github.com/vnpy/vnpy) - VeighNa 基于 Python 的开源量化交易系统开发框架。
- [Intelligent Trading Bot](https://github.com/asavinov/intelligent-trading-bot) - 基于机器学习和特征工程的自动交易信号生成与执行。
- [fastquant](https://github.com/enzoampil/fastquant) - 只需三行代码即可在 Python 中轻松回测投资策略。
- [nautilus_trader](https://github.com/nautechsystems/nautilus_trader) - 高性能事件驱动的回测与实盘算法交易平台。
- [YABTE](https://github.com/bsdz/yabte) - Yet Another (Python) BackTesting Engine。
- [Trading Strategy](https://github.com/tradingstrategy-ai/getting-started) - TradingStrategy.ai 是一个去中心化金融 (DeFi) 研究、回测、实盘交易及投资管理框架。
- [Hikyuu](https://github.com/fasiondog/hikyuu) - 基于 Python/C++ 的开源高性能量化框架，提供完整的交易系统组件，便于组合和复用。

### 风险分析

- [QuantLibRisks](https://github.com/auto-differentiation/QuantLib-Risks-Py) - 基于 QuantLib 的快速风险计算。
- [XAD](https://github.com/auto-differentiation/xad-py) - 自动微分 (AAD) 库。
- [pyfolio](https://github.com/quantopian/pyfolio) - 投资组合与风险分析。
- [empyrical](https://github.com/quantopian/empyrical) - 常见的金融风险与表现指标。
- [fecon235](https://github.com/rsvp/fecon235) - 金融经济学方面的计算工具，包括混合高斯模型、Boltzmann 自适应投资组合等。
- [finance](https://pypi.org/project/finance/) - 金融风险计算，着重通过类与运算符重载提升易用性。
- [qfrm](https://pypi.org/project/qfrm/) - 定量金融风险管理：面向金融工具和投资组合的 OOP 风险测量、管理与可视化工具。
- [visualize-wealth](https://github.com/benjaminmgross/visualize-wealth) - 投资组合构建与定量分析。
- [VisualPortfolio](https://github.com/wegamekinglc/VisualPortfolio) - 用于可视化投资组合表现的工具。
- [universal-portfolios](https://github.com/Marigold/universal-portfolios) - 在线投资组合选择算法的集合。
- [FinQuant](https://github.com/fmilthaler/FinQuant) - 投资组合管理、分析与优化的工具。
- [Empyrial](https://github.com/ssantoshp/Empyrial) - 投资组合风险和表现分析，以及收益预测。
- [risktools](https://github.com/bbcho/risktools-dev) - 为原油和成品油交易场景提供风险工具，部分实现 R 的 PerformanceAnalytics。
- [Riskfolio-Lib](https://github.com/dcajasn/Riskfolio-Lib) - Python 投资组合优化和量化资产配置库。
- [empyrical-reloaded](https://github.com/stefan-jansen/empyrical-reloaded) - 常见金融风险与表现指标的重制版（fork 自 [empyrical](https://github.com/quantopian/empyrical)）。
- [pyfolio-reloaded](https://github.com/stefan-jansen/pyfolio-reloaded) - 投资组合与风险分析的重制版（fork 自 [pyfolio](https://github.com/quantopian/pyfolio)）。
- [fortitudo.tech](https://github.com/fortitudo-tech/fortitudo.tech) - 使用 CVaR（条件风险价值）和熵池进行投资组合优化与压力测试的工具。

### 因子分析

- [alphalens](https://github.com/quantopian/alphalens) - 预测 alpha 因子的表现分析。
- [alphalens-reloaded](https://github.com/stefan-jansen/alphalens-reloaded) - 预测 (alpha) 股票因子的表现分析衍生版本。
- [Spectre](https://github.com/Heerozh/spectre) - GPU 加速的因子分析库与回测工具。

### 情感分析

- [Asset News Sentiment Analyzer](https://github.com/KVignesh122/AssetNewsSentimentAnalyzer) - 使用 GPT 模型进行金融资产和证券的新闻情感分析与报告生成。

### 量化研究环境

- [Jupyter Quant](https://github.com/gnzsnz/jupyter-quant) - 一个 Docker 化的 Jupyter 量化研究环境，预装了 statsmodels、pymc、arch、py_vollib、zipline-reloaded、PyPortfolioOpt 等工具。

### 时间序列

- [ARCH](https://github.com/bashtage/arch) - Python 中的 ARCH 模型。
- [statsmodels](http://statsmodels.sourceforge.net) - Python 模块，用于数据探索、统计模型估计和统计检验。
- [dynts](https://github.com/quantmind/dynts) - 时间序列分析与操作的 Python 包。
- [PyFlux](https://github.com/RJT1990/pyflux) - 针对时序模型和推断（包括频率派与贝叶斯）的 Python 库。
- [tsfresh](https://github.com/blue-yonder/tsfresh) - 自动从时间序列中提取相关特征。
- [hasura/quandl-metabase](https://platform.hasura.io/hub/projects/anirudhm/quandl-metabase-time-series) - Hasura 快速启动项目，用 Metabase 可视化 Quandl 的时序数据集。
- [Facebook Prophet](https://github.com/facebook/prophet) - 针对具有多重季节性且线性或非线性增长的时间序列数据进行高质量预测的工具。
- [tsmoothie](https://github.com/cerlymarco/tsmoothie) - 矢量化的时间序列平滑和离群值检测 Python 库。
- [pmdarima](https://github.com/alkaline-ml/pmdarima) - 一个统计库，提供类似 R 语言 auto.arima 函数的 Python 版本。
- [gluon-ts](https://github.com/awslabs/gluon-ts) - 用于概率时间序列建模的 Python 工具。
- [functime](https://github.com/functime-org/functime) - 大规模时间序列机器学习库，基于 Polars 支持并行特征提取与面板数据的预测。

### 日历

- [exchange_calendars](https://github.com/gerrymanoim/exchange_calendars) - 证券交易所交易日历集合。
- [bizdays](https://github.com/wilsonfreitas/python-bizdays) - 工作日（交易日）计算与工具集。
- [pandas_market_calendars](https://github.com/rsheftel/pandas_market_calendars) - 与 pandas 集成的交易所日历，适用于量化交易应用。

### 数据源

- [yfinance](https://github.com/ranaroussi/yfinance) - Yahoo! Finance 市场数据下载器（比 Pandas Datareader 更快）。
- [findatapy](https://github.com/cuemacro/findatapy) - 通过 Bloomberg、Quandl、Yahoo 等来源下载市场数据的 Python 库。
- [googlefinance](https://github.com/hongtaocai/googlefinance) - 从 Google Finance API 获取实时股票数据的 Python 模块。
- [yahoo-finance](https://github.com/lukaszbanasiak/yahoo-finance) - 从 Yahoo! Finance 获取股票数据的 Python 模块。
- [pandas-datareader](https://github.com/pydata/pandas-datareader) - 将诸多数据源（Google/Yahoo/FRED/OECD/Fama-French/World Bank/Eurostat 等）的数据读入 Pandas 数据结构，并带有缓存机制。
- [pandas-finance](https://github.com/davidastephens/pandas-finance) - 金融数据访问和分析的高级 API。
- [pyhoofinance](https://github.com/innes213/pyhoofinance) - 快速批量查询 Yahoo Finance 多只股票数据，并返回类型化数据以供分析。
- [yfinanceapi](https://github.com/Karthik005/yfinanceapi) - Yahoo! Finance API 的 Python 封装。
- [yql-finance](https://github.com/slawek87/yql-finance) - 利用 YQL（Yahoo Query Language）快速获取股票收盘价。
- [ystockquote](https://github.com/cgoldberg/ystockquote) - 从 Yahoo Finance 获取股票报价数据。
- [wallstreet](https://github.com/mcdallas/wallstreet) - 实时股票与期权数据。
- [stock_extractor](https://github.com/ZachLiuGIS/stock_extractor) - 通用股票数据提取工具。
- [Stockex](https://github.com/cttn/Stockex) - Yahoo! Finance API 的 Python 封装。
- [finsymbols](https://github.com/skillachie/finsymbols) - 获取标普500、AMEX、NYSE、NASDAQ 的股票符号及相关信息。
- [FRB](https://github.com/avelkoski/FRB) - FRED® API 的 Python 客户端。
- [inquisitor](https://github.com/econdb/inquisitor) - 访问 Econdb.com API 的 Python 接口。
- [yfi](https://github.com/nickelkr/yfi) - YQL（Yahoo! Query Language）库。
- [chinesestockapi](https://pypi.org/project/chinesestockapi/) - 获取中国股票价格数据的 Python API。
- [exchange](https://github.com/akarat/exchange) - 获取当前汇率。
- [ticks](https://github.com/jamescnowell/ticks) - 命令行方式获取股票数据的小工具。
- [pybbg](https://github.com/bpsmith/pybbg) - Bloomberg COM API 的 Python 接口。
- [ccy](https://github.com/lsbardel/ccy) - 货币相关 Python 模块。
- [tushare](https://pypi.org/project/tushare/) - 获取中国股票历史和实时行情数据的工具。
- [jsm](https://pypi.org/project/jsm/) - 获取日本股票市场数据。
- [cn_stock_src](https://github.com/jealous/cn_stock_src) - 从不同源获取中国股票基础数据的工具。
- [coinmarketcap](https://github.com/barnumbirr/coinmarketcap) - CoinMarketCap 的 Python API。
- [after-hours](https://github.com/datawrestler/after-hours) - 获取股票盘前盘后价格。
- [bronto-python](https://pypi.org/project/bronto-python/) - Bronto API 的 Python 封装。
- [pytdx](https://github.com/rainx/pytdx) - 通达信行情服务器的 Python 接口，用于获取中国股票实时行情。
- [pdblp](https://github.com/matthewgilbert/pdblp) - 将 pandas 与 Bloomberg Open API 集成的简单接口。
- [tiingo](https://github.com/hydrosquall/tiingo-python) - 访问 Tiingo 数据平台（包括日线价格、实时新闻）的 Python 封装。
- [iexfinance](https://github.com/addisonlynch/iexfinance) - 从 IEX 获取实时和历史股票及其他金融数据的 Python 接口。
- [pyEX](https://github.com/timkpaine/pyEX) - 针对 IEX 的 Python 接口，提供对 pandas 的支持，并可获取流式数据、收费数据、财经数据以及技术指标。
- [alpaca-trade-api](https://github.com/alpacahq/alpaca-trade-api-python) - 从 Alpaca API 获取实时/历史价格数据以及执行交易的 Python 接口。
- [metatrader5](https://pypi.org/project/MetaTrader5/) - MetaTrader 5 终端的 API 连接器。
- [akshare](https://github.com/jindaxiang/akshare) - AkShare 是一个优雅且简单的金融数据接口库，面向 Python 爱好者 <https://akshare.readthedocs.io>。
- [yahooquery](https://github.com/dpguthrie/yahooquery) - 非官方的 Yahoo Finance Python 接口。
- [investpy](https://github.com/alvarobartt/investpy) - 从 Investing.com 获取金融数据的 Python 工具！<https://investpy.readthedocs.io/>
- [yliveticker](https://github.com/yahoofinancelive/yliveticker) - 通过 Yahoo Finance websocket 获取实时市场数据流。
- [bbgbridge](https://github.com/ran404/bbgbridge) - 方便使用的 Bloomberg Desktop API Python 封装。
- [alpha_vantage](https://github.com/RomelTorres/alpha_vantage) - Alpha Vantage API 的 Python 封装，用于获取金融数据。
- [FinanceDataReader](https://github.com/FinanceData/FinanceDataReader) - 开源金融数据读取器，支持美国、韩国、日本、中国、越南等市场。
- [pystlouisfed](https://github.com/TomasKoutek/pystlouisfed) - 圣路易斯联邦储备银行 API（FRED、ALFRED、GeoFRED、FRASER）的 Python 客户端。
- [python-bcb](https://github.com/wilsonfreitas/python-bcb) - 巴西央行 web 服务的 Python 接口。
- [market-prices](https://github.com/maread99/market_prices) - 利用 [exchange-calendars](https://github.com/gerrymanoim/exchange_calendars) 的信息生成有意义的 OHLCV 数据集。
- [tardis-python](https://github.com/tardis-dev/tardis-python) - Tardis.dev 高频加密货币市场数据的 Python 封装。
- [lake-api](https://github.com/crypto-lake/lake-api) - Crypto Lake 高频加密货币市场数据的 Python 封装。
- [tessa](https://github.com/ymyke/tessa) - 用于快速获取金融资产价格（基于 yfinance 和 pycoingecko）并包含搜索和 Symbol 类。
- [pandaSDMX](https://github.com/dr-leo/pandaSDMX) - 实现 SDMX 2.1（ISO 17369:2013）的 Python 库，用于统计数据和元数据交换，广泛用于国家统计局、央行和国际组织。
- [cif](https://github.com/LenkaV/CIF) - Python 包，包含若干综合指标（composite indicators），可整合多个经济指标之间的多维关系。
- [finagg](https://github.com/theOGognf/finagg) - 提供多个免费金融 API 的 Python 实现，以及将历史数据聚合到 SQL 数据库的工具，还支持将聚合数据转化为适合分析或 AI/ML 的特征。
- [FinanceDatabase](https://github.com/JerBouma/FinanceDatabase) - 一个含有 300,000+ 证券符号的数据库，包括股票、ETF、基金、指数、货币、加密货币和货币市场。
- [Trading Strategy](https://github.com/tradingstrategy-ai/trading-strategy/) - 下载去中心化交易所和借贷协议（DeFi）的价格数据。
- [datamule-python](https://github.com/john-friedman/datamule-python) - 一个处理 SEC 数据的工具包，结合了 datamule 的端点。

### Excel 集成

- [xlwings](https://www.xlwings.org/) - 让 Excel 与 Python 融合。
- [openpyxl](https://openpyxl.readthedocs.io/en/latest/) - 读写 Excel 2007 xlsx/xlsm 文件。
- [xlrd](https://github.com/python-excel/xlrd) - 用于从 Excel 文件中提取数据的 Python 库。
- [xlsxwriter](https://xlsxwriter.readthedocs.io/) - 以 Excel 2007+ XLSX 格式写入文件。
- [xlwt](https://github.com/python-excel/xlwt) - 用于创建与 MS Excel 97/2000/XP/2003 XLS 文件兼容的电子表格。
- [DataNitro](https://datanitro.com/) - DataNitro 提供完整的 Python-Excel 集成功能，包括自定义函数（UDFs）。可下载试用，但需购买许可证。
- [xlloop](http://xlloop.sourceforge.net) - 用于在集中式服务器（函数服务器）上实现 Excel 自定义函数（UDFs）的开源框架。
- [expy](http://www.bnikolic.co.uk/expy/expy.html) - 允许在 Excel 电子表格中直接执行 Python 代码并定义新的 Excel 函数的插件。
- [pyxll](https://www.pyxll.com) - 一个 Excel 插件，只需 Python 代码即可扩展 Excel 功能。

### 可视化

- [D-Tale](https://github.com/man-group/dtale) - 针对 pandas DataFrame 和 xarray Dataset 的可视化分析工具。
- [mplfinance](https://github.com/matplotlib/mplfinance) - 基于 matplotlib 的金融数据可视化与分析工具。
- [finplot](https://github.com/highfestiva/finplot) - 高性能、易用的金融可视化工具。
- [finvizfinance](https://github.com/lit26/finvizfinance) - Finviz 数据分析的 Python 库。
- [market-analy](https://github.com/maread99/market_analy) - 使用 [market-prices](https://github.com/maread99/market_prices) 与 bqplot 进行交互式图表分析。
- [QuantInvestStrats](https://github.com/ArturSepp/QuantInvestStrats) - Quantitative Investment Strategies (QIS) 的 Python 分析库，可用于金融数据可视化与回测报告。

---

## R

### 数值库与数据结构

- [xts](https://github.com/joshuaulrich/xts) - eXtensible Time Series：为 R 中的不同时间序列类提供统一的处理方式。
- [data.table](https://github.com/Rdatatable/data.table) - data.frame 的扩展，能够对大规模数据进行快速聚合、快速有序连接，以及无需拷贝地对列进行增改删操作等。
- [sparseEigen](https://github.com/dppalomar/sparseEigen) - 稀疏主成分分析。
- [TSdbi](http://tsdbi.r-forge.r-project.org/) - 提供对时间序列数据库的通用接口。
- [tseries](https://cran.r-project.org/web/packages/tseries/index.html) - 时间序列分析与计算金融。
- [zoo](https://cran.r-project.org/web/packages/zoo/index.html) - S3 结构的规则与不规则时间序列 (Z's Ordered Observations)。
- [tis](https://cran.r-project.org/web/packages/tis/index.html) - 用于时间索引与时间索引序列的函数和 S3 类，兼容 FAME 频率。
- [tfplot](https://cran.r-project.org/web/packages/tfplot/index.html) - 快速处理与绘制时间序列数据的工具。
- [tframe](https://cran.r-project.org/web/packages/tframe/index.html) - 用于时间序列方法编程的核心函数，可与各种时间序列表示形式相对独立。

### 数据源

- [IBrokers](https://cran.r-project.org/web/packages/IBrokers/index.html) - 通过 R 访问 Interactive Brokers TWS API。
- [Rblpapi](https://github.com/Rblp/Rblpapi) - R 接口，用于访问 Bloomberg API。
- [Quandl](https://www.quandl.com/tools/r) - 将金融数据直接导入 R。
- [Rbitcoin](https://github.com/jangorecki/Rbitcoin) - 统一的加密货币交易所 API 接口（bitstamp、kraken、btce、bitmarket 等）。
- [GetTDData](https://github.com/msperlin/GetTDData) - 从 Tesouro Direto 网站下载并聚合巴西政府债券数据。
- [GetHFData](https://github.com/msperlin/GetHFData) - 从 Bovespa FTP 下载并聚合巴西金融产品的高频交易数据。
- [Reddit WallstreetBets API](https://dashboard.nbshare.io/apps/reddit/api/) - 通过 API 获取每天 r/wallstreetbets 论坛中最热门的 50 只股票及其情绪。
- [td](https://github.com/eddelbuettel/td) - 访问 twelvedata API，获取股票及（数字与常规）货币数据。
- [rbcb](https://github.com/wilsonfreitas/rbcb) - R 接口，用于访问巴西央行 web 服务。
- [rb3](https://github.com/ropensci/rb3) - 下载、解析巴西交易所（B3）数据的一系列函数。
- [simfinapi](https://github.com/matthiasgomolka/simfinapi) - 使 R 中的数据轻松访问 [SimFin](https://simfin.com/)。
- [tidyfinance](https://github.com/tidy-finance/r-tidyfinance) - 将原始金融数据转换为整洁（tidy）格式，包含日期转换、规模因子等，便于后续研究。

### 金融工具与定价

- [RQuantLib](https://github.com/eddelbuettel/rquantlib) - RQuantLib 将 GNU R 与 QuantLib 库相连接。
- [quantmod](https://cran.r-project.org/web/packages/quantmod/index.html) - 定量金融建模框架。
- [Rmetrics](https://www.rmetrics.org) - Rmetrics 是定量金融教学与培训的领先开源解决方案。
  - [fAsianOptions](https://cran.r-project.org/web/packages/fAsianOptions/index.html) - EBM 与亚洲期权估值。
  - [fAssets](https://cran.r-project.org/web/packages/fAssets/index.html) - 金融资产分析与建模。
  - [fBasics](https://cran.r-project.org/web/packages/fBasics/index.html) - 市场与基础统计。
  - [fBonds](https://cran.r-project.org/web/packages/fBonds/index.html) - 债券与利率模型。
  - [fExoticOptions](https://cran.r-project.org/web/packages/fExoticOptions/index.html) - 奇异期权估值。
  - [fOptions](https://cran.r-project.org/web/packages/fOptions/index.html) - 基础期权定价与评估。
  - [fPortfolio](https://cran.r-project.org/web/packages/fPortfolio/index.html) - 投资组合选择与优化。
- [portfolio](https://github.com/dgerlanc/portfolio) - 股票投资组合分析。
- [sparseIndexTracking](https://github.com/dppalomar/sparseIndexTracking) - 跟踪指数的投资组合设计。
- [covFactorModel](https://github.com/dppalomar/covFactorModel) - 通过因子模型估计协方差矩阵。
- [riskParityPortfolio](https://github.com/dppalomar/riskParityPortfolio) - 超快风险平价投资组合设计。
- [sde](https://cran.r-project.org/web/packages/sde/index.html) - 随机微分方程的模拟与推断。
- [YieldCurve](https://cran.r-project.org/web/packages/YieldCurve/index.html) - 利率曲线的建模与估计。
- [SmithWilsonYieldCurve](https://cran.r-project.org/web/packages/SmithWilsonYieldCurve/index.html) - 使用 Smith-Wilson 方法从 LIBOR 和 SWAP 利率构建收益曲线。
- [ycinterextra](https://cran.r-project.org/web/packages/ycinterextra/index.html) - 对收益率曲线或零息债价格进行插值与外推。
- [AmericanCallOpt](https://cran.r-project.org/web/packages/AmericanCallOpt/index.html) - 针对产生红利的标的资产进行美式看涨期权定价。
- [VarSwapPrice](https://cran.r-project.org/web/packages/VarSwapPrice/index.html) - 波动率互换（方差互换）的定价。
- [RND](https://cran.r-project.org/web/packages/RND/index.html) - 以风险中性方式提取风险分布的工具包。
- [LSMonteCarlo](https://cran.r-project.org/web/packages/LSMonteCarlo/index.html) - 用最小二乘蒙特卡洛估计美式期权。
- [OptHedging](https://cran.r-project.org/web/packages/OptHedging/index.html) - 看涨/看跌期权的价值和对冲策略估计。
- [tvm](https://cran.r-project.org/web/packages/tvm/index.html) - 时间价值函数。
- [OptionPricing](https://cran.r-project.org/web/packages/OptionPricing/index.html) - 期权定价与高效仿真算法。
- [credule](https://github.com/blenezet/credule) - 信用违约掉期（CDS）的相关函数。
- [derivmkts](https://cran.r-project.org/web/packages/derivmkts/index.html) - 《Derivatives Markets》相关函数和示例 R 代码。
- [FinCal](https://github.com/felixfan/FinCal) - 时间价值计算、时间序列分析与计算金融函数库。
- [r-quant](https://github.com/artyyouth/r-quant) - R 中进行定量金融分析的示例代码。
- [options.studies](https://github.com/taylorizing/options.studies) - 与 `options.data` 包和 shiny 一起使用的期权交易研究函数。
- [PortfolioAnalytics](https://github.com/braverock/PortfolioAnalytics) - 投资组合分析与数值优化方法。
- [fmbasics](https://github.com/imanuelcostigan/fmbasics) - 金融市场的基础构件。
- [R-fixedincome](https://github.com/wilsonfreitas/R-fixedincome) - 针对固定收益产品的 R 工具。

### 交易

- [backtest](https://cran.r-project.org/web/packages/backtest/index.html) - 针对基于投资组合的假设进行探索。
- [pa](https://cran.r-project.org/web/packages/pa/index.html) - 股票投资组合业绩归因。
- [TTR](https://github.com/joshuaulrich/TTR) - 技术交易规则。
- [QuantTools](https://quanttools.bitbucket.io/_site/index.html) - 增强的定量交易建模工具。
- [blotter](https://github.com/braverock/blotter) - 用于定义交易产品、交易、投资组合和账户的事务框架，支持多资产、多货币投资组合和模拟。

### 回测

- [quantstrat](https://github.com/braverock/quantstrat) - 面向交易系统构建和模拟的事务框架，支持多资产、多货币投资组合。

### 风险分析

- [PerformanceAnalytics](https://github.com/braverock/PerformanceAnalytics) - 用于投资组合和风险分析的计量经济学工具。

### 因子分析

- [FactorAnalytics](https://github.com/braverock/FactorAnalytics) - 针对主流三大类因子模型（基本面因子、时间序列因子、统计因子），以及组合构建、优化和风险管理的工具包。
- [Expected Returns](https://github.com/JustinMShea/ExpectedReturns) - 用 R 语言实现《Expected Returns》（Antti Ilmanen 著）中讨论的各种投资组合方法及复制示例。

### 时间序列

- [tseries](https://cran.r-project.org/web/packages/tseries/index.html) - 时间序列分析与计算金融。
- [fGarch](https://cran.r-project.org/web/packages/fGarch/index.html) - Rmetrics 中的自回归条件异方差模型。
- [timeSeries](https://cran.r-project.org/web/packages/timeSeries/index.html) - Rmetrics 中的金融时间序列对象。
- [rugarch](https://github.com/alexiosg/rugarch) - 单变量 GARCH 模型。
- [rmgarch](https://github.com/alexiosg/rmgarch) - 多变量 GARCH 模型。
- [tidypredict](https://github.com/edgararuiz/tidypredict) - 在数据库内运行预测 <https://tidypredict.netlify.com/>。
- [tidyquant](https://github.com/business-science/tidyquant) - 将金融分析引入 tidyverse。
- [timetk](https://github.com/business-science/timetk) - R 中进行时间序列分析的工具包。
- [tibbletime](https://github.com/business-science/tibbletime) - 基于 tidyverse 的时间索引扩展，让 tibble 具有时间感知功能。
- [matrixprofile](https://github.com/matrix-profile-foundation/matrixprofile) - 基于矩阵剖面结构和算法的时间序列数据挖掘库。
- [garchmodels](https://github.com/AlbertoAlmuinha/garchmodels) - 针对 GARCH 模型的 parsnip 后端实现。

### 日历

- [timeDate](https://cran.r-project.org/web/packages/timeDate/index.html) - 时间与日历对象。
- [bizdays](https://github.com/wilsonfreitas/R-bizdays) - 工作日（交易日）计算与相关工具。

---

## Matlab

### 框架

- [QUANTAXIS](https://github.com/yutiansut/quantaxis) - Matlab 版集成量化工具箱。
- [PROJ_Option_Pricing_Matlab](https://github.com/jkirkby3/PROJ_Option_Pricing_Matlab) - 量化期权定价（奇异/香草）：障碍期权、亚洲期权、欧式/美式期权、巴黎期权、回望期权、Cliquet、方差互换、Swing、远期启动期权、阶梯期权、Fader 期权等。

---

## Julia

- [Lucky.jl](https://github.com/oliviermilla/Lucky.jl) - 纯 Julia 实现的模块化、异步交易引擎。
- [QuantLib.jl](https://github.com/pazzo83/QuantLib.jl) - QuantLib 在 Julia 中的实现。
- [Ito.jl](https://github.com/aviks/Ito.jl) - Julia 语言中的定量金融包。
- [TALib.jl](https://github.com/femtotrader/TALib.jl) - TA-Lib 的 Julia 封装。
- [IncTA.jl](https://github.com/femtotrader/IncTA.jl) - Julia 增量技术分析指标。
- [Miletus.jl](https://github.com/JuliaComputing/Miletus.jl) - 一种金融合约定义、建模语言及定价框架。
- [Temporal.jl](https://github.com/dysonance/Temporal.jl) - 灵活且高效的时间序列类与方法。
- [Indicators.jl](https://github.com/dysonance/Indicators.jl) - 基于 Temporal 的金融市场技术分析与指标库。
- [Strategems.jl](https://github.com/dysonance/Strategems.jl) - 定量系统化交易策略开发与回测。
- [TimeSeries.jl](https://github.com/JuliaStats/TimeSeries.jl) - Julia 的时间序列工具包。
- [MarketTechnicals.jl](https://github.com/JuliaQuant/MarketTechnicals.jl) - 基于 TimeSeries 的金融时间序列技术分析。
- [MarketData.jl](https://github.com/JuliaQuant/MarketData.jl) - 金融市场时间序列数据。
- [TimeFrames.jl](https://github.com/femtotrader/TimeFrames.jl) - Julia 库，用于在 TimeSeries 上进行重采样。
- [DataFrames.jl](https://github.com/JuliaData/DataFrames.jl) - Julia 中的内存表格数据结构。
- [TSFrames.jl](https://github.com/xKDR/TSFrames.jl) - 基于 DataFrames.jl 处理时间序列数据。

---

## Java

- [Strata](http://strata.opengamma.io/) - 由 OpenGamma 编写的现代开源分析与市场风险库。
- [JQuantLib](https://github.com/frgomes/jquantlib) - 100% Java 编写的免费开源定量金融框架，移植自 QuantLib。
- [finmath.net](http://finmath.net) - 与数学金融相关的 Java 库及算法。
- [quantcomponents](https://github.com/lsgro/quantcomponents) - 面向定量金融与算法交易的免费 Java 组件。
- [DRIP](https://lakshmidrip.github.io/DRIP) - Fixed Income、资产配置、交易成本分析、XVA 度量库。
- [ta4j](https://github.com/ta4j/ta4j) - 技术分析的 Java 库。

---

## JavaScript

- [finance.js](https://github.com/ebradyjobory/finance.js) - 常见财务计算的 JavaScript 库。
- [portfolio-allocation](https://github.com/lequant40/portfolio_allocation_js) - 一个用于构建多资产投资组合（如债券、大宗商品、加密货币、外汇、ETF、股票等）的 JavaScript 库。
- [Ghostfolio](https://github.com/ghostfolio/ghostfolio) - 帮助跟踪股票、ETF 或加密货币等金融资产，并据此进行数据驱动的投资决策的财富管理软件。
- [IndicatorTS](https://github.com/cinar/indicatorts) - 在 TypeScript 中提供多种股票技术分析指标、策略以及回测框架。
- [chart-patterns](https://github.com/focus1691/chart-patterns) - 市场轮廓、成交量轮廓、叠加买卖不平衡和高成交量节点指标的技术分析库。
- [orderflow](https://github.com/focus1691/orderflow) - 订单流交易聚合器，用于从交易所 websocket 构建脚印 K 线。
- [ccxt](https://github.com/ccxt/ccxt) - 一个 JavaScript / Python / PHP 加密货币交易 API，支持 100+ 比特币/山寨币交易所。
- [PENDAX](https://github.com/CompendiumFi/PENDAX-SDK) - 针对 FTX、FTXUS、OKX、Bybit 等交易所的数据与交易 API 及 Websocket 的 JavaScript SDK。

#### 数据可视化

- [QUANTAXIS_Webkit](https://github.com/yutiansut/QUANTAXIS_Webkit) - 基于 QUANTAXIS 的可视化中心。

---

## Haskell

- [quantfin](https://github.com/boundedvariation/quantfin) - 纯 Haskell 实现的量化金融库。
- [Haxcel](https://github.com/MarcusRainbow/Haxcel) - Excel 的 Haskell 插件。
- [Ffinar](https://github.com/MarcusRainbow/Ffinar) - Haskell 中的金融数学库。

---

## Scala

- [QuantScale](https://github.com/choucrifahed/quantscale) - Scala 定量金融库。
- [Scala Quant](https://github.com/frankcash/Scala-Quant) - 用于处理 IFTTT 或 Google Finance 股票数据的 Scala 库。

---

## Ruby

- [Jiji](https://github.com/unageanu/jiji2) - 使用 OANDA REST API 的开源外汇算法交易框架。

---

## Elixir/Erlang

- [Tai](https://github.com/fremantle-capital/tai) - 一个开源、可组合的实时市场数据与交易执行工具集。
- [Workbench](https://github.com/fremantle-industries/workbench) - 从想法到执行——在分布式集群上管理交易业务。
- [Prop](https://github.com/fremantle-industries/prop) - 一个开放且有主见的交易平台，使用熟悉的开源库与工具进行策略研究、执行和运营。

---

## Golang

- [Kelp](https://github.com/stellar/kelp) - 开源的 Golang 算法加密交易机器人，可在中心化交易所和 Stellar DEX 上运行（支持命令行与桌面 GUI）。
- [marketstore](https://github.com/alpacahq/marketstore) - 面向金融时序数据的 DataFrame 服务器。
- [IndicatorGo](https://github.com/cinar/indicator) - Golang 模块，提供各种股票技术分析指标、策略和回测框架。

---

## CPP

- [QuantLib](https://github.com/lballabio/QuantLib) - QuantLib 项目旨在提供一个全面的定量金融软件框架。
- [QuantLibRisks](https://github.com/auto-differentiation/QuantLib-Risks-Cpp) - 使用 QuantLib 进行 C++ 快速风险计算。
- [XAD](https://github.com/auto-differentiation/xad) - 自动微分 (AAD) 库。
- [TradeFrame](https://github.com/rburkholder/trade-frame) - C++17 交易框架/库（含示例），可测试期权交易自动化策略，内含 [Option Greeks/IV](https://github.com/rburkholder/trade-frame/tree/master/lib/TFOptions) 计算库。
- [Hikyuu](https://github.com/fasiondog/hikyuu) - 基于 C++/Python 的开源高性能量化框架，用于快速分析与回测，包含完整的交易系统组件可复用。

---

## Frameworks

- [QuantLib](https://github.com/lballabio/QuantLib) - 一个全面的定量金融软件框架。
  - QuantLibRisks - [Python](https://pypi.org/project/QuantLib-Risks/) 与 [C++](https://github.com/auto-differentiation/QuantLib-Risks-Cpp) 中的基于 QuantLib 的快速风险计算。
  - XAD - [Python](https://pypi.org/project/xad/) 与 [C++](https://github.com/auto-differentiation/xad/) 的自动微分(AAD)库。
  - [JQuantLib](https://github.com/frgomes/jquantlib) - Java 移植版本。
  - [RQuantLib](https://github.com/eddelbuettel/rquantlib) - R 封装。
  - [QuantLibAddin](https://www.quantlib.org/quantlibaddin/) - Excel 支持。
  - [QuantLibXL](https://www.quantlib.org/quantlibxl/) - Excel 支持。
  - [QLNet](https://github.com/amaggiulli/qlnet) - .NET 移植版本。
  - [PyQL](https://github.com/enthought/pyql) - Python 移植版本。
  - [QuantLib.jl](https://github.com/pazzo83/QuantLib.jl) - Julia 移植版本。
  - [QuantLib-Python Documentation](https://quantlib-python-docs.readthedocs.io/) - QuantLib Python 绑定的文档。

- [TA-Lib](https://ta-lib.org) - 对金融市场数据进行技术分析。
  - [ta-lib-python](https://github.com/TA-Lib/ta-lib-python)
  - [ta-lib](https://github.com/TA-Lib/ta-lib)
- [Portfolio Optimizer](https://portfoliooptimizer.io/) - 基于 Web API 的投资组合分析与优化服务。
- XAD：针对 [Python](https://pypi.org/project/xad/) 与 [C++](https://github.com/auto-differentiation/xad/) 的自动微分（AAD）库

---

## CSharp

- [QuantConnect](https://github.com/QuantConnect/Lean) - Lean Engine 是一个开源的 C# 算法交易引擎，适用于桌面或云环境。
- [StockSharp](https://github.com/StockSharp/StockSharp) - 算法交易与量化交易开源平台，可开发涵盖股票、外汇、加密货币和期权的交易机器人。
- [TDAmeritrade.DotNetCore](https://github.com/NVentimiglia/TDAmeritrade.DotNetCore) - 免费开源的 .NET 客户端，用于集成 TD Ameritrade API 并开发自定义交易解决方案。

---

## Rust

- [QuantMath](https://github.com/MarcusRainbow/QuantMath) - 面向风险中性定价与风险管理的金融数学库。
- [Barter](https://github.com/barter-rs/barter-rs) - 用于构建事件驱动式实时交易和回测系统的开源 Rust 框架。
- [LFEST](https://github.com/MathisWellmann/lfest-rs) - 模拟永续合约交易所，可以对你的策略进行模拟交易。
- [TradeAggregation](https://github.com/MathisWellmann/trade_aggregation-rs) - 使用信息驱动规则将交易聚合到自定义周期 K 线或其他形态中。
- [SlidingFeatures](https://github.com/MathisWellmann/sliding_features-rs) - 链式树形滑动窗口，用于信号处理和技术分析。
- [RustQuant](https://github.com/avhz/RustQuant) - 用 Rust 编写的量化金融库。
- [finalytics](https://github.com/Nnamdi-sys/finalytics) - Rust 库，用于金融数据分析。

---
