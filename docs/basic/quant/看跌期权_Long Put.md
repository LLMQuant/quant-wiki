![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# 什么是看跌期权？
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)
看跌期权（long put）是指买入一份看跌期权，通常是为了预期相关资产价格下跌。这里的“long”并不是指到期前的时间长度，而是指交易者以希望在未来以更高价格出售该期权的方式进行的操作。

交易者可能出于投机目的购买看跌期权，押注于相关资产价格会下跌，这将提高看跌期权的价值。看跌期权也可以用于对冲相关资产的多头头寸。如果相关资产价格下跌，看跌期权的价值随之上涨，从而帮助抵消相关资产的损失。

### 关键要点

- 看跌期权是指某人买入一份看跌期权。这本身就是一种看空市场的策略。
- 如果投资者认为某项证券的价格会下跌，他们会买入看跌期权。
- 投资者可能选择买入看跌期权，来投机价格下跌或对冲投资组合的下行风险。
- 使用看跌期权策略，因而可以限制下行风险。

## 理解看跌期权

看跌期权具有一个行权价，指看跌期权买方可以出售相关资产的价格。假设相关资产是一只股票，该期权的行权价为50美元。这意味着该看跌期权使交易者有权以50美元出售该股票，即使股票价格下跌至20美元也一样。另一方面，如果股票上涨并保持在50美元以上，该期权将变得毫无价值，因为在股票交易价格为60美元时，没有必要以50美元出售股票。

如果交易者希望行使在行权价出售相关资产的权利，他们可以行使该期权。行使期权并不是强制性的，交易者可以在到期前的任何时候通过出售期权退出。

如果是美式期权，交易者可以在到期日前行使期权，而欧式期权则只能在到期日行使。如果选择提前行使或在到期时处于实值状态，期权持有者将处于相关资产的空头头寸。

## 看跌期权策略与卖空股票

对于看空投资者来说，看跌期权可能是一种比卖空股票更具吸引力的策略。卖空股票的理论风险是无限的，因为股票价格没有上限。同时，卖空股票的盈利潜力也是有限的，因为股票无法跌破每股0美元。看跌期权与卖空股票的盈利潜力相似，因为盈利同样有限。看跌期权的价值只会在相关股票跌至零的情况下增加。看跌期权的优势在于风险仅限于为期权支付的权利金。

看跌期权的缺点是，相关资产的价格必须在期权到期日之前下跌，否则支付的金额将会损失。

要从卖空股票交易中获利，交易者在某一价格卖出股票，希望能以更低的价格买回。看跌期权也是类似的，如果相关股票下跌，那么看跌期权的价值就会增加，并可出售获利。如果行使期权，将使交易者在相关股票上处于空头头寸，交易者随后需要购买相关股票以实现交易的盈利。

## 使用看跌期权进行对冲

看跌期权也可以用于对冲多头股票头寸的不可预期的变动。这种对冲策略被称为保护性看跌（protective put）或配对看跌（married put）。

例如，假设投资者在每股25美元的价格上多头持有美国银行（Bank of America Corporation，BAC）的100股。尽管投资者对该股票长期看涨，但他们担心在接下来的一个月内股票可能会下跌。因此，投资者购买一份行权价为20美元的看跌期权，支付0.10美元（乘以100股，因为每份看跌期权代表100股），该期权将在一个月后到期。

投资者的对冲措施将损失限制在500美元，或者100股 × (25美元 - 20美元)，减去为看跌期权支付的权利金（总计10美元）。换句话说，即使美国银行在下个月跌至0美元，这位交易者最多损失510美元，因为所有20美元以下的股票损失都由看跌期权覆盖。

## 使用看跌期权的示例

假设苹果公司（Apple Inc.，AAPL）的交易价格为每股170美元，你认为在新产品发布前，价格可能会下降约10%。你决定以155美元的行权价买入10份看跌期权，支付0.45美元。你总共投入的看跌期权成本为450美元加上手续费和佣金（1,000股 × 0.45美元 = 450美元）。

如果苹果股票在到期前下跌至154美元，您的看跌期权现值为1.00美元，因为您可以行使期权，以155美元的价格做空1,000股股票，然后立刻以154美元买回以对冲。

你目前的看跌期权总值为1,000美元（减去任何费用和佣金），即（1,000股 × 1.00美元 = 1,000美元）。你在该头寸上的收益为122% = (1,000美元 - 450美元)/450美元。通过买入看跌期权，你实现的收益远高于基础股票价格的9.4%的跌幅。

相反，如果苹果股票上涨至200美元，这10份期权合约将失效，使你损失最初投入的450美元。

## 看跌期权的定价数学

### Black-Scholes看跌期权定价公式

欧式看跌期权的理论价格为：

$$P = K e^{-rT} N(-d_2) - S_0 N(-d_1)$$

其中：

$$d_1 = \frac{\ln(S_0/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}, \quad d_2 = d_1 - \sigma\sqrt{T}$$

- $S_0$：标的资产当前价格
- $K$：行权价
- $T$：距到期时间（年）
- $r$：无风险利率
- $\sigma$：波动率
- $N(\cdot)$：标准正态分布累积分布函数

### 看跌期权的希腊字母

| 希腊字母 | 公式 | 含义 | 典型值（ATM，30天） |
|---------|------|------|-----------------|
| Delta ($\Delta$) | $N(d_1) - 1$ | 价格敏感度 | -0.50 |
| Gamma ($\Gamma$) | $\frac{N'(d_1)}{S\sigma\sqrt{T}}$ | Delta变化率 | 0.04 |
| Theta ($\Theta$) | $-\frac{S N'(d_1)\sigma}{2\sqrt{T}} + rKe^{-rT}N(-d_2)$ | 时间衰减 | -0.05/天 |
| Vega ($\nu$) | $S\sqrt{T}N'(d_1)$ | 波动率敏感度 | 0.12/1%vol |

### 看跌期权的盈亏分析

到期时看跌期权的盈亏为：

$$P\&L = \max(K - S_T, 0) - P_0$$

盈亏平衡点：$S_{BE} = K - P_0$

**数值示例**：买入行权价$50的看跌期权，权利金$2.50
- 盈亏平衡点：$50 - $2.50 = $47.50
- 最大利润：$50 - $2.50 = $47.50（股票跌至$0时）
- 最大亏损：$2.50（权利金）

| 到期时股价 | 看跌期权价值 | 净盈亏 | 收益率 |
|-----------|-----------|-------|-------|
| $55 | $0 | -$2.50 | -100% |
| $50 | $0 | -$2.50 | -100% |
| $47.50 | $2.50 | $0 | 0% |
| $45 | $5.00 | +$2.50 | +100% |
| $40 | $10.00 | +$7.50 | +300% |
| $35 | $15.00 | +$12.50 | +500% |

## 高级看跌期权策略

### 看跌期权价差（Bear Put Spread）

同时买入高行权价看跌和卖出低行权价看跌，降低成本但限制收益：

- 买入$50看跌，权利金$3.00
- 卖出$45看跌，权利金$1.20
- 净成本：$1.80
- 最大利润：$5.00 - $1.80 = $3.20（股价跌至$45以下时）
- 盈亏平衡：$50 - $1.80 = $48.20

### 保护性看跌（Protective Put）的成本分析

假设持有1,000股某股票（$100/股），购买3个月期ATM看跌期权对冲：

- 看跌期权权利金：$4.50/股（波动率25%时）
- 年化对冲成本：$4.50 × 4 = $18.00/股，即18%的年化保护成本
- 实际中，可选择OTM看跌（如行权价$90）降低成本至约$1.80/股

## 量化应用

```python
import numpy as np
from scipy.stats import norm

class LongPutAnalyzer:
    """看跌期权分析与策略构建工具"""
    
    @staticmethod
    def bs_put_price(S, K, T, r, sigma):
        """Black-Scholes看跌期权定价"""
        if T <= 0:
            return max(K - S, 0)
        d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
        d2 = d1 - sigma*np.sqrt(T)
        return K * np.exp(-r*T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    
    @staticmethod
    def put_greeks(S, K, T, r, sigma):
        """计算看跌期权的希腊字母"""
        if T <= 0:
            return {'delta': -1.0 if S < K else 0.0, 
                    'gamma': 0, 'theta': 0, 'vega': 0}
        d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
        d2 = d1 - sigma*np.sqrt(T)
        
        delta = norm.cdf(d1) - 1
        gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
        theta = (-S * norm.pdf(d1) * sigma / (2*np.sqrt(T)) 
                 + r * K * np.exp(-r*T) * norm.cdf(-d2)) / 252
        vega = S * norm.pdf(d1) * np.sqrt(T) / 100
        
        return {'delta': round(delta, 4), 'gamma': round(gamma, 4),
                'theta': round(theta, 4), 'vega': round(vega, 4)}
    
    def payoff_analysis(self, S0, K, premium, n_contracts=1):
        """
        看跌期权到期盈亏分析
        """
        multiplier = 100 * n_contracts
        prices = np.linspace(S0 * 0.5, S0 * 1.5, 100)
        
        payoffs = np.maximum(K - prices, 0) * multiplier
        pnl = payoffs - premium * multiplier
        
        breakeven = K - premium
        max_profit = (K - premium) * multiplier
        max_loss = premium * multiplier
        
        return {
            'breakeven': round(breakeven, 2),
            'max_profit': round(max_profit, 2),
            'max_loss': round(max_loss, 2),
            'risk_reward_ratio': round(max_profit / max_loss, 2) if max_loss > 0 else float('inf')
        }
    
    def protective_put_analysis(self, stock_price, put_strike, put_premium, 
                                 shares, holding_days=90):
        """
        保护性看跌策略分析
        """
        total_cost = put_premium * shares
        annual_cost_pct = (put_premium / stock_price) * (365 / holding_days)
        
        # 不同情景下的组合P&L
        scenarios = {}
        for pct_change in [-0.20, -0.10, -0.05, 0, 0.05, 0.10, 0.20]:
            new_price = stock_price * (1 + pct_change)
            stock_pnl = (new_price - stock_price) * shares
            put_payoff = max(put_strike - new_price, 0) * shares
            total_pnl = stock_pnl + put_payoff - total_cost
            
            scenarios[f"{pct_change:+.0%}"] = {
                'stock_pnl': round(stock_pnl, 2),
                'put_payoff': round(put_payoff, 2),
                'net_pnl': round(total_pnl, 2)
            }
        
        max_loss = (stock_price - put_strike + put_premium) * shares
        
        return {
            'hedge_cost': round(total_cost, 2),
            'annual_cost_pct': f"{annual_cost_pct:.1%}",
            'max_loss_with_hedge': round(max_loss, 2),
            'max_loss_without_hedge': f"无限（理论上至${stock_price * shares:,.0f}）",
            'scenarios': scenarios
        }
    
    def optimal_strike_selection(self, S, T, r, sigma, budget_per_share, 
                                  min_protection_pct=0.10):
        """
        在预算约束下选择最优行权价
        """
        strikes = np.arange(S * 0.7, S * 1.01, 0.5)
        results = []
        
        for K in strikes:
            premium = self.bs_put_price(S, K, T, r, sigma)
            if premium <= budget_per_share:
                protection_pct = (S - K + premium) / S  # 无保护区间
                downside_protected = K / S  # 保护开始的价位
                leverage = (K - premium) / premium if premium > 0 else 0
                
                results.append({
                    'strike': round(K, 1),
                    'premium': round(premium, 2),
                    'protection_starts': f"{(1 - K/S):.1%} 跌幅后",
                    'max_loss_pct': f"{(S - K + premium)/S:.1%}",
                    'leverage': round(leverage, 1)
                })
        
        return results


# 使用示例
analyzer = LongPutAnalyzer()

# 1. 定价与Greeks
S, K, T, r, sigma = 170, 155, 30/252, 0.05, 0.30
price = analyzer.bs_put_price(S, K, T, r, sigma)
greeks = analyzer.put_greeks(S, K, T, r, sigma)
print(f"看跌期权价格: ${price:.2f}")
print(f"Greeks: {greeks}")

# 2. 盈亏分析
payoff = analyzer.payoff_analysis(S0=170, K=155, premium=0.45, n_contracts=10)
print(f"\n盈亏分析: {payoff}")

# 3. 保护性看跌分析
protection = analyzer.protective_put_analysis(
    stock_price=100, put_strike=95, put_premium=2.50, shares=1000
)
print(f"\n保护性看跌:")
print(f"  对冲成本: ${protection['hedge_cost']}")
print(f"  年化成本: {protection['annual_cost_pct']}")
print(f"  最大损失（有对冲）: ${protection['max_loss_with_hedge']}")
for scenario, data in protection['scenarios'].items():
    print(f"  股价变动{scenario}: 净P&L = ${data['net_pnl']:,.2f}")

# 4. 最优行权价选择
print(f"\n在$3/股预算内的行权价选择:")
options = analyzer.optimal_strike_selection(S=100, T=90/252, r=0.05, 
                                            sigma=0.25, budget_per_share=3.0)
for opt in options[-5:]:  # 显示最后5个（最接近ATM的）
    print(f"  K=${opt['strike']}: 权利金${opt['premium']}, "
          f"{opt['protection_starts']}, 杠杆={opt['leverage']}x")
```

## 看跌期权的实务考量

1. **隐含波动率对成本的影响**：高IV环境下（如财报季前），看跌期权价格显著上升。以$100股票、行权价$95、30天期限为例，IV从20%升至40%时，权利金从$0.85升至$2.45——成本增加近3倍。

2. **时间衰减的非线性**：看跌期权的Theta在最后30天加速衰减。30天期ATM看跌每天损失约$0.05，但在最后5天内每天损失可达$0.15-$0.20。

3. **滚动策略（Rolling）**：当接近到期时，交易者可将当前看跌平仓，同时买入更远到期日的同行权价看跌，延续保护。滚动成本取决于期限结构的形状。

## 关于LLMQuant
LLMQuant是由一群来自世界顶尖高校和量化金融从业人员组成的前沿社区，致力于探索人工智能（AI）与量化（Quant）领域的无限可能。我们的团队成员来自剑桥大学、牛津大学、哈佛大学、苏黎世联邦理工学院、北京大学、中科大等世界知名高校，外部顾问来自Microsoft、HSBC、Citadel、Man Group、Citi、Jump Trading、国内顶尖私募等一流企业。