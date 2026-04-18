![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# 什么是多空股权？
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

多空股权是一种投资策略，旨在对预计升值的股票建立多头头寸，对预计贬值的股票建立空头头寸。多空股权策略寻求在获取多头头寸的股票涨幅收益的同时，降低市场风险，以及从空头头寸的价格下跌中获利。尽管并不总是如此，但该策略通常应该在净收益上保持盈利。

多空股权是一种流动性较高的替代策略，受对冲基金的青睐，其中许多基金采用市场中性策略，即多头和空头头寸的资金量相等。

### 关键要点

- 多空股权是一种投资策略，旨在对被低估的股票建立多头头寸，同时对被高估的股票卖出空头。
- 多空股权旨在通过利用被认为是低估和高估的证券之间的盈利机会，增强传统的单边多头投资。
- 多空股权通常被对冲基金使用，后者往往持有相对多头偏向，例如一个130/30策略，其中多头敞口为资产管理规模的130%，空头敞口为30%。

## 多空股权是如何运作的

多空股权通过利用预期价格变动中的潜在上涨和下跌利润机会来运作。该策略识别并对被认为相对被低估的股票建立多头头寸，同时对被认为被高估的股票进行空头交易。

虽然许多对冲基金也采用多空股权策略并持有多头偏向（例如130/30，其中多头敞口为130%，空头敞口为30%），但相对较少的对冲基金在其多空策略中采用空头偏向。因为从历史上看，发掘盈利的空头想法通常比多头想法更具挑战性。

多空股权策略可以在多个方面相互区分——按市场地理（发达经济体、新兴市场、欧洲等）、行业（能源、科技等）、投资理念（价值或成长）等进行划分。

一个具有广泛任务的多空股权策略的例子可能是全球股票成长基金，而一个相对狭窄任务的例子可能是新兴市场医疗保健基金。

## 多空股权与股权市场中性

多空股权基金与股权市场中性（EMN）基金的主要区别在于，后者试图通过在具有相似特征的股票中建立多头和空头来利用股价差异。

EMN策略试图保持其多头和空头持仓的总值大致相等，这有助于降低整体风险。为了维持多头和空头之间的等价性，股权市场中性基金必须在市场趋势建立和加强时进行再平衡。

因此，当其他多空对冲基金在市场趋势中让利润运行并甚至进行杠杆放大时，股权市场中性基金则积极地收缩收益并增加相对头寸的规模。当市场不可避免地再次转向时，股权市场中性基金会再次削减应获利的头寸，转向更多处于亏损状态的投资组合。

采用股权市场中性策略的对冲基金通常面向那些希望寻找能够超越债券而不承担更高风险和高回报的激进基金的机构投资者。

## 多空股权示例：配对交易

多空模型的一种常见变体是“配对交易”，其涉及对一个股票的多头头寸与另一个同一行业股票的空头头寸进行抵消。

例如，技术领域的投资者可能在微软上建立多头头寸，并用英特尔的空头头寸进行抵消。如果投资者以每股33美元的价格购买1,000股微软，同时英特尔交易价格为22美元，则此配对交易的空头部分将涉及购买1,500股英特尔，以使多头和空头头寸的金额相等。

这种多空策略的理想情况是微软升值而英特尔贬值。如果微软上涨至35美元而英特尔下跌至21美元，则该策略的整体利润将为3,500美元。即使英特尔上涨至23美元——因为通常推动某个特定行业股票上涨或下跌的因素是相似的——该策略仍会以500美元获利，尽管利润较少。

为了应对同一行业内股票一般趋向共同上涨或下跌的事实，多空策略通常倾向于在多头和空头部分使用不同的行业。例如，如果利率上升，对冲基金可能会做空对利率敏感的行业，如公用事业，同时在防御性行业如医疗保健上持有多头。

## 多空股权的数学框架

### 组合收益分解

多空股权组合的收益可以分解为：

$$R_{portfolio} = \beta_{net} \cdot R_{market} + \alpha_{long} + \alpha_{short} + \epsilon$$

其中：
- $\beta_{net} = \beta_{long} - \beta_{short}$ 为净Beta敞口
- $\alpha_{long}$ 为多头部分的选股超额收益
- $\alpha_{short}$ 为空头部分的选股超额收益
- $\epsilon$ 为残差项

对于130/30策略，假设多头总敞口为组合净值的130%，空头为30%，净敞口为100%：

$$R_{130/30} = 1.3 \times R_{long} - 0.3 \times R_{short}$$

### 信息比率与最优敞口

组合的信息比率（IR）衡量风险调整后的超额收益：

$$IR = \frac{E[R_{portfolio} - R_{benchmark}]}{\sigma(R_{portfolio} - R_{benchmark})}$$

Grinold和Kahn的基本法则（Fundamental Law of Active Management）表明：

$$IR \approx IC \times \sqrt{BR}$$

其中 $IC$ 为信息系数（预测能力），$BR$ 为广度（独立投注数量）。多空策略通过增加空头投注，有效提高了 $BR$，从而提高 $IR$。

## 详细交易实例

**案例：因子驱动的多空组合**

假设一位基金经理管理1亿美元的130/30多空组合，基于价值和动量因子进行选股。

**多头部分（$1.3亿敞口）**：

| 股票 | 权重 | 买入价 | 预期收益 | Beta |
|------|------|--------|---------|------|
| 贵州茅台 | 15% | ¥1,800 | +12% | 0.75 |
| 宁德时代 | 12% | ¥210 | +15% | 1.20 |
| 招商银行 | 10% | ¥35 | +8% | 0.85 |
| 其他20只股票 | 93% | — | +10% (均值) | 1.05 |

**空头部分（$3,000万敞口）**：

| 股票 | 权重 | 做空价 | 预期跌幅 | Beta |
|------|------|--------|---------|------|
| 某过度炒作概念股A | 8% | ¥45 | -20% | 1.80 |
| 某业绩下滑股B | 7% | ¥28 | -15% | 1.10 |
| 某高估值股C | 8% | ¥120 | -12% | 1.30 |
| 其他5只空头 | 7% | — | -10% (均值) | 1.25 |

**组合净Beta**：$1.3 \times 1.05 - 0.3 \times 1.35 = 1.365 - 0.405 = 0.96$

**预期年化收益**（假设市场收益8%）：

$$R = 0.96 \times 8\% + 1.3 \times 2\% + 0.3 \times 3\% = 7.68\% + 2.6\% + 0.9\% = 11.18\%$$

其中2%为多头alpha，3%为空头alpha（做空下跌股票带来的收益）。

## 量化应用

```python
import numpy as np
from dataclasses import dataclass

@dataclass
class Stock:
    ticker: str
    expected_return: float  # 预期收益率
    beta: float
    volatility: float
    sector: str

class LongShortEquity:
    """多空股权策略构建与分析"""
    
    def __init__(self, gross_long=1.3, gross_short=0.3, capital=1e8):
        """
        Parameters:
            gross_long: 多头总敞口占比（如1.3表示130%）
            gross_short: 空头总敞口占比（如0.3表示30%）
            capital: 总资本
        """
        self.gross_long = gross_long
        self.gross_short = gross_short
        self.capital = capital
    
    def rank_stocks(self, stocks: list, factors: dict) -> list:
        """
        基于多因子模型对股票排序
        factors: {'value': weight, 'momentum': weight, 'quality': weight}
        """
        scored = []
        for stock in stocks:
            # 简化的因子评分（实际应使用真实因子数据）
            composite = (
                factors.get('value', 0) * np.random.normal(0, 1) +
                factors.get('momentum', 0) * np.random.normal(0, 1) +
                factors.get('quality', 0) * np.random.normal(0, 1)
            )
            scored.append((stock, composite))
        
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored
    
    def construct_portfolio(self, ranked_stocks: list, 
                            n_long: int = 30, n_short: int = 10) -> dict:
        """
        构建多空组合
        做多评分最高的n_long只，做空评分最低的n_short只
        """
        longs = ranked_stocks[:n_long]
        shorts = ranked_stocks[-n_short:]
        
        # 等权分配（可替换为优化权重）
        long_weight = self.gross_long / n_long
        short_weight = self.gross_short / n_short
        
        portfolio = {
            'long': [(s.ticker, long_weight, s.beta) for s, _ in longs],
            'short': [(s.ticker, short_weight, s.beta) for s, _ in shorts],
        }
        
        # 计算组合特征
        net_beta = (sum(w * b for _, w, b in portfolio['long']) - 
                    sum(w * b for _, w, b in portfolio['short']))
        gross_exposure = self.gross_long + self.gross_short
        net_exposure = self.gross_long - self.gross_short
        
        portfolio['metrics'] = {
            'net_beta': round(net_beta, 3),
            'gross_exposure': f"{gross_exposure:.0%}",
            'net_exposure': f"{net_exposure:.0%}",
            'long_count': n_long,
            'short_count': n_short
        }
        
        return portfolio
    
    def simulate_returns(self, portfolio: dict, market_returns: np.ndarray,
                         alpha_long: float = 0.02, alpha_short: float = 0.03,
                         idio_vol: float = 0.15) -> dict:
        """
        模拟多空组合收益序列
        
        Parameters:
            market_returns: 市场日收益率序列
            alpha_long: 多头年化alpha
            alpha_short: 空头年化alpha
            idio_vol: 个股特异性波动率
        """
        n_days = len(market_returns)
        net_beta = portfolio['metrics']['net_beta']
        
        daily_alpha_l = alpha_long / 252
        daily_alpha_s = alpha_short / 252
        daily_idio = idio_vol / np.sqrt(252)
        
        portfolio_returns = []
        for mkt_ret in market_returns:
            # 多头收益 = beta * market + alpha + noise
            long_ret = (self.gross_long * 
                       (net_beta / self.gross_long * mkt_ret + daily_alpha_l + 
                        daily_idio * np.random.normal() * 0.5))
            
            # 空头收益 = -beta * market + alpha + noise
            short_ret = (self.gross_short * 
                        (daily_alpha_s - 0.3 * mkt_ret + 
                         daily_idio * np.random.normal() * 0.5))
            
            portfolio_returns.append(long_ret + short_ret)
        
        returns = np.array(portfolio_returns)
        cumulative = np.cumprod(1 + returns) - 1
        
        # 性能指标
        ann_return = np.mean(returns) * 252
        ann_vol = np.std(returns) * np.sqrt(252)
        sharpe = ann_return / ann_vol if ann_vol > 0 else 0
        
        # 最大回撤
        wealth = np.cumprod(1 + returns)
        peak = np.maximum.accumulate(wealth)
        drawdown = (peak - wealth) / peak
        max_dd = np.max(drawdown)
        
        return {
            'annual_return': f"{ann_return:.2%}",
            'annual_volatility': f"{ann_vol:.2%}",
            'sharpe_ratio': f"{sharpe:.2f}",
            'max_drawdown': f"{max_dd:.2%}",
            'cumulative_return': f"{cumulative[-1]:.2%}",
            'win_rate': f"{np.mean(returns > 0):.1%}"
        }


# 使用示例
np.random.seed(42)

# 生成模拟股票池
sectors = ['科技', '金融', '消费', '医药', '能源', '工业']
stocks = [
    Stock(f"STOCK_{i:03d}", 
          np.random.normal(0.08, 0.15), 
          np.random.uniform(0.5, 1.8),
          np.random.uniform(0.15, 0.45),
          np.random.choice(sectors))
    for i in range(200)
]

# 构建策略
strategy = LongShortEquity(gross_long=1.3, gross_short=0.3, capital=1e8)

# 因子排序
factors = {'value': 0.4, 'momentum': 0.35, 'quality': 0.25}
ranked = strategy.rank_stocks(stocks, factors)

# 构建组合
portfolio = strategy.construct_portfolio(ranked, n_long=40, n_short=15)
print(f"组合特征: {portfolio['metrics']}")

# 模拟2年收益
market_rets = np.random.normal(0.0003, 0.012, 504)  # 约8%年化收益
perf = strategy.simulate_returns(portfolio, market_rets)
print(f"策略表现:")
for k, v in perf.items():
    print(f"  {k}: {v}")
```

## 风险管理要点

| 风险类型 | 描述 | 管理方法 |
|---------|------|---------|
| 空头挤压（Short Squeeze） | 被做空的股票突然大幅上涨 | 分散空头头寸，单只空头不超过组合3% |
| 借券风险 | 无法续借被做空的股票 | 维持充足的借券来源，避免做空流通盘过小的股票 |
| 因子拥挤 | 过多基金追逐相同因子导致收益衰减 | 监控因子拥挤度指标，适时调整因子权重 |
| 杠杆风险 | 130/30结构放大了亏损 | 动态调整总敞口，在高波动环境降低杠杆 |
| 相关性风险 | 多空头寸的相关性突然变化 | 定期检验多空头寸的相关性结构 |

## 关于LLMQuant
LLMQuant是由一群来自世界顶尖高校和量化金融从业人员组成的前沿社区，致力于探索人工智能（AI）与量化（Quant）领域的无限可能。我们的团队成员来自剑桥大学、牛津大学、哈佛大学、苏黎世联邦理工学院、北京大学、中科大等世界知名高校，外部顾问来自Microsoft、HSBC、Citadel、Man Group、Citi、Jump Trading、国内顶尖私募等一流企业。