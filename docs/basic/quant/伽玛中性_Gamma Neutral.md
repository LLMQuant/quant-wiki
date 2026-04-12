![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# 什么是伽玛中性？
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

伽玛中性期权头寸是指已对基础证券的大幅波动进行了免疫的期权头寸。实现伽玛中性头寸是一种管理期权交易风险的方法，通过建立一个在基础证券上涨或下跌时，其德尔塔的变化率接近于零的资产组合。这被称作伽玛对冲。因此，伽玛中性投资组合对二阶时间价格敏感性有对冲效应。

伽玛是“期权希腊字母”之一，其他还有德尔塔、罗、希腊和维加。这些希腊字母用于评估期权投资组合中的不同风险类型。[1]

### 关键要点

- 伽玛中性投资组合是一个期权头寸，即使基础证券大幅波动，其德尔塔也不会发生变化。
- 伽玛中性是通过向投资组合中添加额外的期权合约来实现的，通常与当前头寸形成对比，这一过程被称为伽玛对冲。
- 德尔塔-伽玛对冲通常用于通过创建一个同时为德尔塔中性和伽玛中性的头寸来锁定利润。

## 理解伽玛中性

期权投资组合的方向风险可以通过德尔塔对冲进行管理，从而创建一个德尔塔中性或方向上不明确的投资组合。问题在于，随着基础证券价格的变化，期权的德尔塔本身也会发生变化，这意味着德尔塔中性头寸可能会获得或失去德尔塔，从而变成一个方向性投机，尤其是在基础证券大幅波动时。伽玛对冲试图中和德尔塔的这种变化。

可以通过持有抵消伽玛值的头寸来创建伽玛中性投资组合。这有助于减少因市场价格和条件变化而导致的波动。然而，伽玛中性投资组合仍然面临风险。例如，如果用于建立投资组合的假设被证明是错误的，原本应为中性的头寸可能实际上会变得风险显著。此外，随着价格变化和时间推移，头寸需要重新平衡。

伽玛中性期权策略可以用于建立新证券头寸或调整现有头寸。目标是使用一组期权将总体伽玛值尽量保持在接近零的水平。接近零的值意味着当基础证券价格波动时，德尔塔值不应发生变化。

需要注意的是，如果目标是实现一个持久的德尔塔中性策略，通常会采用德尔塔-伽玛对冲。但交易者也可能希望维持一个特定的德尔塔头寸，此时其德尔塔可能为正（或负）但保持伽玛中性。

锁定利润是伽玛中性头寸的一种常见用途。如果预计将出现高波动期，而期权交易头寸目前已经获得良好的利润，那么与其通过卖出头寸来锁定利润并不再获取进一步的收益，不如采用德尔塔中性或伽玛中性对冲来有效地锁定这些利润。

## 伽玛中性与德尔塔中性

简单的德尔塔对冲可以通过购买看涨期权并同时卖出一定数量的基础股票来创建。如果股票价格保持不变但波动性上升，交易者可能会获利，除非时间价值的侵蚀摧毁了这些利润。交易者可以向策略中添加一个不同执行价格的空头看涨期权，以抵消时间价值的衰减并防范德尔塔的巨大波动。将第二个看涨期权添加到头寸中就是伽玛对冲。

随着基础股票价格的上涨和下跌，投资者如果希望保持头寸中性，可以买入或卖出股票。这可能会增加交易的波动性和成本。德尔塔和伽玛对冲并不一定要完全中性，交易者可以根据时间调整他们所承担的正或负伽玛的程度。

## 参考文献

[1] TD Ameritrade. "[Stock Options Greeks: Gamma Explained](https://tickertape.tdameritrade.com/trading/trading-stock-options-gamma-17718)."

## 伽玛中性的数学基础

### 伽玛的定义与计算

伽玛（Gamma，$\Gamma$）是期权价格对标的资产价格的二阶偏导数：

$$\Gamma = \frac{\partial^2 C}{\partial S^2} = \frac{\partial \Delta}{\partial S}$$

在Black-Scholes模型中，欧式期权的伽玛公式为：

$$\Gamma = \frac{N'(d_1)}{S \sigma \sqrt{T}}$$

其中 $N'(d_1) = \frac{1}{\sqrt{2\pi}} e^{-d_1^2/2}$ 为标准正态分布的概率密度函数，$d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}$。

### 伽玛中性条件

投资组合的总伽玛为各头寸伽玛的加权和。伽玛中性要求：

$$\Gamma_{portfolio} = \sum_{i=1}^{n} w_i \cdot \Gamma_i = 0$$

其中 $w_i$ 为第 $i$ 个期权头寸的数量（正数为多头，负数为空头），$\Gamma_i$ 为对应单份期权的伽玛值。

### Delta-Gamma展开

组合价值变化的二阶Taylor展开为：

$$\Delta V \approx \Delta \cdot \delta S + \frac{1}{2} \Gamma \cdot (\delta S)^2 + \Theta \cdot \delta t$$

当 $\Gamma = 0$ 时，组合价值变化近似为线性函数，消除了标的价格大幅波动带来的非线性风险。

## 详细交易实例

**案例：构建伽玛中性组合**

假设交易者持有以下头寸（标的股票价格 $S = \$100$，无风险利率 $r = 5\%$，波动率 $\sigma = 25\%$）：

- **初始头寸**：多头100份行权价$100的看涨期权（30天到期）
  - 单份 $\Gamma_1 = 0.0398$，总伽玛 = $100 \times 0.0398 = 3.98$
  - 单份 $\Delta_1 = 0.536$，总Delta = $100 \times 0.536 = 53.6$

**目标**：通过卖出行权价$105的看涨期权来实现伽玛中性。

- 行权价$105看涨期权的单份 $\Gamma_2 = 0.0312$

需要卖出的合约数量：

$$n = \frac{\Gamma_{portfolio}}{\Gamma_2} = \frac{3.98}{0.0312} \approx 128 \text{份}$$

- 卖出128份$105看涨期权后的总伽玛：$3.98 - 128 \times 0.0312 = 3.98 - 3.99 \approx 0$
- 新增Delta变化：$-128 \times 0.354 = -45.3$
- 调整后组合Delta：$53.6 - 45.3 = 8.3$

最后做空约8股标的股票使Delta也接近零，实现Delta-Gamma双中性。

**情景分析**（隔日价格变动）：

| 股价变动 | 未对冲组合P&L | 伽玛中性组合P&L |
|---------|-------------|---------------|
| -$5 | -$1,780 | -$120 |
| -$2 | -$580 | -$35 |
| +$0 | $0 | $0 |
| +$2 | +$650 | +$40 |
| +$5 | +$1,950 | +$105 |

可以看出，伽玛中性组合在大幅波动中的损益显著平坦化。

## 量化应用

```python
import numpy as np
from scipy.stats import norm

class GammaNeutralPortfolio:
    """伽玛中性组合构建与管理"""
    
    @staticmethod
    def bs_greeks(S, K, T, r, sigma, option_type='call'):
        """计算Black-Scholes希腊字母"""
        if T <= 0:
            delta = 1.0 if S > K else 0.0
            return {'delta': delta, 'gamma': 0, 'theta': 0, 'vega': 0}
        
        d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
        d2 = d1 - sigma*np.sqrt(T)
        
        gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
        vega = S * norm.pdf(d1) * np.sqrt(T)
        
        if option_type == 'call':
            delta = norm.cdf(d1)
            theta = (-S * norm.pdf(d1) * sigma / (2*np.sqrt(T)) 
                     - r * K * np.exp(-r*T) * norm.cdf(d2))
        else:
            delta = norm.cdf(d1) - 1
            theta = (-S * norm.pdf(d1) * sigma / (2*np.sqrt(T)) 
                     + r * K * np.exp(-r*T) * norm.cdf(-d2))
        
        return {'delta': delta, 'gamma': gamma, 'theta': theta, 'vega': vega}
    
    def build_gamma_neutral(self, positions: list, hedge_option: dict, 
                             S: float, r: float, sigma: float) -> dict:
        """
        构建伽玛中性组合
        
        Parameters:
            positions: [{'K': float, 'T': float, 'qty': int, 'type': str}, ...]
            hedge_option: {'K': float, 'T': float, 'type': str}  用于对冲的期权
            S: 标的价格
            r: 无风险利率
            sigma: 波动率
        
        Returns:
            对冲方案详情
        """
        # 计算现有组合的总伽玛和Delta
        total_gamma = 0
        total_delta = 0
        
        for pos in positions:
            greeks = self.bs_greeks(S, pos['K'], pos['T'], r, sigma, pos['type'])
            total_gamma += pos['qty'] * greeks['gamma']
            total_delta += pos['qty'] * greeks['delta']
        
        # 计算对冲期权的伽玛
        hedge_greeks = self.bs_greeks(
            S, hedge_option['K'], hedge_option['T'], r, sigma, hedge_option['type']
        )
        
        # 需要的对冲期权数量（取整）
        hedge_qty = -int(round(total_gamma / hedge_greeks['gamma']))
        
        # 对冲后的组合希腊字母
        final_gamma = total_gamma + hedge_qty * hedge_greeks['gamma']
        final_delta = total_delta + hedge_qty * hedge_greeks['delta']
        
        # 需要的标的股票数量来消除Delta
        stock_hedge = -int(round(final_delta))
        
        return {
            'original_gamma': round(total_gamma, 4),
            'original_delta': round(total_delta, 4),
            'hedge_option_qty': hedge_qty,
            'hedge_option_strike': hedge_option['K'],
            'stock_hedge_qty': stock_hedge,
            'final_gamma': round(final_gamma, 6),
            'final_delta': round(final_delta + stock_hedge, 4)
        }
    
    def simulate_pnl(self, S, positions, hedge_qty, hedge_K, hedge_T,
                     stock_qty, r, sigma, price_range=0.1, steps=50):
        """
        模拟不同价格下的组合P&L
        """
        price_changes = np.linspace(-price_range * S, price_range * S, steps)
        pnl_hedged = []
        pnl_unhedged = []
        
        for dS in price_changes:
            new_S = S + dS
            pnl_h = 0
            pnl_u = 0
            
            # 原始头寸P&L
            for pos in positions:
                old_price = max(self.bs_greeks(S, pos['K'], pos['T'], r, sigma)['delta'] * S, 0)
                # 使用BS定价
                d1 = (np.log(new_S/pos['K']) + (r + 0.5*sigma**2)*pos['T']) / (sigma*np.sqrt(pos['T']))
                d2 = d1 - sigma*np.sqrt(pos['T'])
                new_call = new_S * norm.cdf(d1) - pos['K']*np.exp(-r*pos['T'])*norm.cdf(d2)
                d1_old = (np.log(S/pos['K']) + (r + 0.5*sigma**2)*pos['T']) / (sigma*np.sqrt(pos['T']))
                d2_old = d1_old - sigma*np.sqrt(pos['T'])
                old_call = S * norm.cdf(d1_old) - pos['K']*np.exp(-r*pos['T'])*norm.cdf(d2_old)
                
                pnl_h += pos['qty'] * (new_call - old_call)
                pnl_u += pos['qty'] * (new_call - old_call)
            
            # 对冲期权P&L
            d1_h = (np.log(new_S/hedge_K) + (r + 0.5*sigma**2)*hedge_T) / (sigma*np.sqrt(hedge_T))
            d2_h = d1_h - sigma*np.sqrt(hedge_T)
            new_hedge = new_S * norm.cdf(d1_h) - hedge_K*np.exp(-r*hedge_T)*norm.cdf(d2_h)
            d1_h0 = (np.log(S/hedge_K) + (r + 0.5*sigma**2)*hedge_T) / (sigma*np.sqrt(hedge_T))
            d2_h0 = d1_h0 - sigma*np.sqrt(hedge_T)
            old_hedge = S * norm.cdf(d1_h0) - hedge_K*np.exp(-r*hedge_T)*norm.cdf(d2_h0)
            
            pnl_h += hedge_qty * (new_hedge - old_hedge)
            
            # 股票对冲P&L
            pnl_h += stock_qty * dS
            
            pnl_hedged.append(pnl_h)
            pnl_unhedged.append(pnl_u)
        
        return price_changes, pnl_hedged, pnl_unhedged


# 使用示例
portfolio = GammaNeutralPortfolio()

# 初始头寸：多头100份ATM看涨期权
positions = [{'K': 100, 'T': 30/252, 'qty': 100, 'type': 'call'}]

# 用行权价105的看涨期权对冲
hedge_option = {'K': 105, 'T': 30/252, 'type': 'call'}

result = portfolio.build_gamma_neutral(
    positions, hedge_option, S=100, r=0.05, sigma=0.25
)

print(f"原始组合 Gamma: {result['original_gamma']}")
print(f"原始组合 Delta: {result['original_delta']}")
print(f"对冲期权数量: {result['hedge_option_qty']}份 (K={result['hedge_option_strike']})")
print(f"股票对冲: {result['stock_hedge_qty']}股")
print(f"最终 Gamma: {result['final_gamma']}")
print(f"最终 Delta: {result['final_delta']}")
```

## 伽玛中性的实务考量

1. **再平衡频率**：由于伽玛本身随标的价格和时间变化，伽玛中性需要定期再平衡。在高伽玛环境（如临近到期的ATM期权）下，可能需要每日甚至日内多次调整。

2. **伽玛与Theta的权衡**：伽玛中性组合通常以牺牲Theta收入为代价。做多伽玛意味着每天损失时间价值（$\Theta < 0$），而做空伽玛则每天获得时间价值但面临跳空风险。

3. **交易成本约束**：频繁的再平衡会产生显著的交易成本。实务中常采用"伽玛带"（Gamma Band）方法：仅当组合伽玛偏离零超过预设阈值时才进行调整。

## 关于LLMQuant
LLMQuant是由一群来自世界顶尖高校和量化金融从业人员组成的前沿社区，致力于探索人工智能（AI）与量化（Quant）领域的无限可能。我们的团队成员来自剑桥大学、牛津大学、哈佛大学、苏黎世联邦理工学院、北京大学、中科大等世界知名高校，外部顾问来自Microsoft、HSBC、Citadel、Man Group、Citi、Jump Trading、国内顶尖私募等一流企业。