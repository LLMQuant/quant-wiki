![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# 什么是德尔塔对冲？
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

德尔塔对冲是一种期权交易策略，旨在减少或对冲与基础资产价格变动相关的方向性风险。这一方法使用期权来抵消对单个期权持仓或整体投资组合持仓的风险。投资者试图达到德尔塔中性状态，以避免对对冲产生方向性偏差。

### 关键要点

- 德尔塔对冲是一种通过在相同基础资产上建立对冲的多头和空头头寸来实现方向中性目标的期权策略。
- 通过减少方向性风险，德尔塔对冲可以孤立期权交易者的波动变化。
- 期权头寸也可以通过基础股票的股份进行德尔塔对冲。
- 当交易者预期基础股票会出现强烈波动时，德尔塔对冲能为其带来好处，但这要求交易者不断监控并调整相关头寸。
- 可以使用德尔塔与当前期权持仓相反的期权进行对冲，以维持德尔塔中性头寸。

## 德尔塔对冲的运作原理

最基本的德尔塔对冲类型涉及购买或出售期权的投资者，通过购买或出售相应数量的股票或交易所交易基金（ETF）股份来抵消德尔塔风险。投资者可能希望通过使用德尔塔对冲策略来抵消期权或基础股票的风险。

更高级的期权策略则试图通过德尔塔中性交易策略来交易波动性。由于德尔塔对冲试图中和或减少期权价格相对于资产价格的波动，因此需要不断重新平衡对冲。德尔塔对冲是一项复杂的策略，主要用于机构交易者和投资银行。

德尔塔表示期权价值相对于基础资产市场价格变动的变化。对冲是一种投资——通常是期权——用于抵消资产的风险暴露。

**重要提示：** 德尔塔是期权合约价格变化与基础资产价值相应变动之间的比例关系。因此，如果XYZ股票的期权德尔塔为0.45，当基础股票市场价格上涨1美元时，期权的价值将上涨0.45美元，其他条件不变。

## 德尔塔的数学基础

在Black-Scholes期权定价模型中，德尔塔的精确计算公式为：

对于看涨期权：

$$ \Delta_{call} = N(d_1) $$

对于看跌期权：

$$ \Delta_{put} = N(d_1) - 1 $$

其中：

$$ d_1 = \frac{\ln(S/K) + (r + \sigma^2/2) \cdot T}{\sigma \sqrt{T}} $$

- $S$ = 标的资产当前价格
- $K$ = 行权价格
- $r$ = 无风险利率
- $\sigma$ = 波动率
- $T$ = 到期时间（年化）
- $N(\cdot)$ = 标准正态累积分布函数

假设讨论的期权以股票为基础证券。交易者希望了解期权的德尔塔，因为它可以告诉他们期权或溢价的价值将随着股票价格变动而上涨或下跌多少。每当基础价格变动1美元时，理论上期权的溢价变化就是德尔塔，而这两者之间的关系即为对冲比率。

看涨期权的德尔塔在0到1之间，而看跌期权的德尔塔则在-1到0之间。德尔塔为-0.50的看跌期权被视为价平，这意味着期权的执行价格等于基础股票的价格。相反，德尔塔为0.50的看涨期权则具有与股票价格相等的执行价格。[1]

德尔塔取决于以下情况：

- 价内或当前盈利
- 价平，即执行价格与市场价格相同
- 价外，即当前未盈利

## 德尔塔对冲中的高阶希腊值

### 伽玛（Gamma）风险

伽玛衡量德尔塔随标的价格变化的速率：

$$ \Gamma = \frac{\partial \Delta}{\partial S} = \frac{N'(d_1)}{S \sigma \sqrt{T}} $$

伽玛风险是德尔塔对冲中最重要的残余风险。当投资组合为德尔塔中性但具有较大伽玛时，标的价格的大幅变动将导致德尔塔快速偏离零，需要频繁调仓。

德尔塔对冲的盈亏（P&L）可以用Taylor展开近似：

$$ dV \approx \Delta \cdot dS + \frac{1}{2}\Gamma \cdot (dS)^2 + \Theta \cdot dt + \nu \cdot d\sigma $$

当 $\Delta = 0$（德尔塔中性）时：

$$ dV \approx \frac{1}{2}\Gamma \cdot (dS)^2 + \Theta \cdot dt + \nu \cdot d\sigma $$

这表明德尔塔中性头寸的损益主要由伽玛、Theta和Vega决定。

### Theta与Gamma的关系

对于德尔塔中性的投资组合，Black-Scholes方程给出了Theta与Gamma之间的重要关系：

$$ \Theta + \frac{1}{2}\sigma^2 S^2 \Gamma + rS\Delta = rV $$

当 $\Delta = 0$ 时：

$$ \Theta \approx -\frac{1}{2}\sigma^2 S^2 \Gamma + rV $$

这意味着正伽玛头寸必然伴随负Theta（时间衰减损失），反之亦然。这是期权市场中的基本权衡关系。

## 达到德尔塔中性

期权头寸可以通过具有与当前期权持仓相反德尔塔的期权进行对冲，以维持德尔塔中性头寸。德尔塔中性头寸的整体德尔塔为零，这最小化了期权价格相对于基础资产的波动。

例如，假设一位投资者持有一份德尔塔为0.50的看涨期权，这表明该期权为价平，并希望保持德尔塔中性头寸。投资者可以购买一份德尔塔为-0.50的价平看跌期权，以抵消正德尔塔，从而使头寸的德尔塔为零。

**注意：** 德尔塔伽玛对冲与德尔塔对冲密切相关。这是一种结合德尔塔与伽玛对冲的期权策略，以减轻基础资产和德尔塔本身变动的风险。

## 期权简要介绍

期权的价值是通过其溢价来衡量的，溢价是购买合约时支付的费用。通过持有期权，投资者或交易者可以行使其购买或出售100股基础资产的权利，但如果不盈利，他们并不需要进行此操作。购买或出售的价格称为执行价格，在购买时设定（连同到期日）。每份合约等于100股基础股票或资产。

美式期权的持有人可以在到期日之前的任何时间行使其权利。欧式期权则只允许持有人在到期日行使。此外，依赖于期权的价值，两种类型的期权持有者可以选择在到期前将合约出售给其他投资者。[2]

例如，如果一份看涨期权的执行价格为30美元，而到期时基础股票的交易价格为40美元，则期权持有人可以以较低的执行价格30美元兑换100股。如果他们选择，可以转手在公开市场以40美元出售，从而获利。获利金额为10美元减去看涨期权的溢价和进行交易的经纪费用。

看跌期权稍显复杂，但其运作与看涨期权非常相似。在此情况下，持有人预期基础资产的价值在到期之前会恶化。他们可能持有该资产在其投资组合中，或者从经纪人那里借用股份。[3]

## 使用股票进行德尔塔对冲

期权头寸还可以通过基础股票的股份进行德尔塔对冲。一股基础股票的德尔塔为1，因为股票的价值变化1美元。例如，假设一位投资者持有一份德尔塔为0.75的看涨期权。

在这种情况下，投资者可以通过卖空75股基础股票来对冲这份看涨期权。在卖空时，投资者借入股票，将这些股票以市场价出售给其他投资者，随后再以希望更低的价格买入股票归还给出借方。[4]

对冲所需的股票数量计算公式为：

$$ N_{shares} = -\Delta_{option} \times N_{contracts} \times 100 $$

例如，持有10份德尔塔为0.60的看涨期权，需要卖空的股票数量为：

$$ N_{shares} = -0.60 \times 10 \times 100 = -600 \text{ 股} $$

即卖空600股以实现德尔塔中性。

## 量化应用

### Python实现德尔塔对冲模拟

```python
import numpy as np
from scipy.stats import norm

def bs_delta(S, K, T, r, sigma, option_type='call'):
    """计算Black-Scholes德尔塔"""
    if T <= 0:
        if option_type == 'call':
            return 1.0 if S > K else 0.0
        else:
            return -1.0 if S < K else 0.0
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    
    if option_type == 'call':
        return norm.cdf(d1)
    else:
        return norm.cdf(d1) - 1


def bs_price(S, K, T, r, sigma, option_type='call'):
    """计算Black-Scholes期权价格"""
    if T <= 0:
        if option_type == 'call':
            return max(S - K, 0)
        else:
            return max(K - S, 0)
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == 'call':
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)


def simulate_delta_hedge(S0, K, T, r, sigma, n_rebalance=252, n_paths=1000):
    """
    模拟德尔塔对冲的盈亏分布
    
    Parameters
    ----------
    S0 : float       -- 初始股价
    K : float        -- 行权价
    T : float        -- 到期时间（年）
    r : float        -- 无风险利率
    sigma : float    -- 波动率
    n_rebalance : int -- 调仓次数
    n_paths : int    -- 模拟路径数
    
    Returns
    -------
    dict -- 对冲结果统计
    """
    dt = T / n_rebalance
    option_price_0 = bs_price(S0, K, T, r, sigma, 'call')
    
    pnl_list = []
    
    for _ in range(n_paths):
        # 模拟股价路径
        S = S0
        cash = option_price_0  # 卖出看涨期权收取的权利金
        shares_held = 0
        
        for i in range(n_rebalance):
            t_remaining = T - i * dt
            delta = bs_delta(S, K, t_remaining, r, sigma, 'call')
            
            # 调整对冲头寸
            shares_to_trade = delta * 100 - shares_held
            cash -= shares_to_trade * S
            shares_held += shares_to_trade
            
            # 股价变动
            Z = np.random.standard_normal()
            S = S * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)
        
        # 到期结算
        option_payoff = max(S - K, 0) * 100
        final_pnl = cash + shares_held * S - option_payoff
        pnl_list.append(final_pnl)
    
    pnl_array = np.array(pnl_list)
    
    return {
        'mean_pnl': np.mean(pnl_array),
        'std_pnl': np.std(pnl_array),
        'min_pnl': np.min(pnl_array),
        'max_pnl': np.max(pnl_array),
        'hedge_efficiency': 1 - np.std(pnl_array) / (option_price_0 * 100)
    }
```

### 调仓频率与对冲成本的权衡

在实际交易中，调仓频率的选择是一个关键决策。更频繁的调仓可以更好地维持德尔塔中性，但会产生更高的交易成本。对冲误差（Hedging Error）与调仓频率的关系可以近似为：

$$ \text{Hedging Error} \propto \frac{\Gamma \cdot S^2 \cdot \sigma^2 \cdot \Delta t}{2} $$

$$ \text{Transaction Cost} \propto \frac{c \cdot \Gamma \cdot S \cdot \sigma}{\sqrt{\Delta t}} $$

最优调仓间隔使得对冲误差与交易成本之和最小化：

$$ \Delta t^* = \left( \frac{3c}{2 \Gamma S \sigma} \right)^{2/3} $$

其中 $c$ 为每股交易成本。这一结果表明，当伽玛较大、波动率较高或交易成本较低时，应更频繁地调仓。

### 离散对冲与连续对冲的差异

Black-Scholes模型假设连续对冲，但实际交易中只能进行离散对冲。离散对冲的累计盈亏可以表示为：

$$ P\&L = \sum_{i=0}^{N-1} \frac{1}{2} \Gamma_i S_i^2 \left[ (\Delta S_i / S_i)^2 - \sigma^2 \Delta t \right] $$

这说明德尔塔对冲的损益取决于已实现波动率与隐含波动率之间的差异。如果已实现波动率高于隐含波动率，正伽玛头寸将获利；反之则亏损。

## 德尔塔对冲的优势与劣势

当交易者预期基础股票会出现强烈波动时，德尔塔对冲可以为其带来好处，但如果股票未按预期波动，则存在被过度对冲的风险。如果过度对冲的头寸需要解除，则交易成本会增加。

德尔塔对冲的一大主要缺点是必须不断监控和调整相关头寸。根据股票的波动，交易者需要频繁买卖证券，以避免出现不足或过度对冲的情况。

德尔塔对冲中涉及的交易数量可能会造成费用较高，因为在调整头寸时会产生交易费用。当通过期权进行对冲时，这尤其昂贵，因为期权可能会失去时间价值，有时交易价格低于基础股票的涨幅。

时间价值是衡量期权到期前剩余时间的指标，交易者可以在此期间赚取利润。随着时间的推移和到期日的临近，期权会失去时间价值，因为可获利的时间变少。因此，期权的时间价值影响该期权的溢价成本，因为时间价值较高的期权通常具有更高的溢价，而时间价值较低的期权则通常溢价更低。随着时间的推移，期权的价值变化，可能会导致需要更多德尔塔对冲来维持德尔塔中性策略。[5]

#### 优势

- 允许交易者对冲投资组合中不利价格变动的风险
- 短期内保护来自期权或股票头寸的利润，而无需解除长期持仓

#### 劣势

- 可能需要大量交易来不断调整德尔塔对冲，导致费用增加
- 如果德尔塔被过多抵消或市场变化出乎意料，可能会出现过度对冲的情况

## 德尔塔对冲示例

假设一位交易者希望为其在通用电气（GE）股票中的投资维持德尔塔中性头寸。投资者持有一份GE的看跌期权。一份期权代表100股GE股票。

股票大幅下跌，交易者在看跌期权上获得了利润。随后，近期事件推动股票价格上涨。然而，交易者认为这次上涨是短期事件，预计股票会重新下跌。因此，实施德尔塔对冲以保护看跌期权的收益。

GE的看跌期权德尔塔为-0.75，通常称为-75。投资者通过购买75股基础股票建立德尔塔中性头寸。以每股10美元的价格，投资者总共花费750美元购买75股GE股票。待股票近期上涨结束或事件对交易者的看跌期权持仓有利时，投资者可以解除德尔塔对冲。

## 德尔塔对冲怎么运作？

德尔塔对冲是一种涉及期权的交易策略。交易者使用它来对冲与基础资产价格变化相关的方向性风险，通常通过买卖期权并通过买卖相同数量的股票或ETF股份来抵消风险。其目标是在不对对冲产生方向性偏见的情况下，达到德尔塔中性状态。

## 可以用德尔塔来决定如何对冲期权吗？

是的，可以使用德尔塔对冲期权。为此，您必须弄清楚是应该买入还是卖出基础资产。您可以通过将德尔塔的总价值乘以相关期权合约的数量来确定德尔塔对冲的数量。将该数字乘以100即可得最终结果。

## 什么是德尔塔伽玛对冲？

德尔塔伽玛对冲是一种期权策略，与德尔塔对冲密切相关。在德尔塔伽玛对冲中，德尔塔与伽玛对冲相结合，以降低与基础资产变化相关的风险，同时也旨在减少德尔塔本身的风险。请记住，德尔塔估算衍生品价格的变化，而伽玛描述价格每变动一个点，期权德尔塔的变化率。

德尔塔伽玛对冲需要同时使用两种不同的期权合约来分别中和德尔塔和伽玛：

$$ \begin{cases} n_1 \cdot \Delta_1 + n_2 \cdot \Delta_2 + n_{stock} = 0 \\ n_1 \cdot \Gamma_1 + n_2 \cdot \Gamma_2 = 0 \end{cases} $$

求解该方程组即可确定所需的期权头寸数量。

## 总结

期权交易者拥有多种策略，以帮助减轻与这些投资相关的风险。其中之一就是德尔塔对冲。当交易者使用这一策略时，他们的目标是减少与基础资产价格变动相关的方向性风险。实现这一目标的方法是买入或卖出期权，并通过相同数量的公司股票或ETF分享抵消风险。虽然这对那些懂得如何使用这一策略的交易者来说可能是有利的，但交易者应意识到，这需要不断监控，并且可能相当昂贵。

在现代量化交易中，德尔塔对冲已高度自动化。做市商和期权交易台使用实时希腊值计算引擎，结合交易成本模型和最优调仓算法，以最小的成本维持近似德尔塔中性的状态。理解德尔塔对冲的理论基础和实践细节，是从事期权量化交易的核心能力之一。

## 参考文献

[1] Merrill. "[Delta](https://www.merrilledge.com/investment-products/options/learn-understand-delta-options)."

[2] Cbonds. "[European Option](https://cbonds.com/glossary/european-option/)."

[3] Fidelity. "[What Are Options, and How Do They Work?](https://www.fidelity.com/learning-center/smart-money/what-are-options)"

[4] Macroption. "[Delta Hedging: Calculations, Adjustments, Long vs. Short Options](https://www.macroption.com/delta-hedging/)."

[5] Macroption. "[Option Time Value](https://www.macroption.com/option-time-value/)."

## 关于LLMQuant
LLMQuant是由一群来自世界顶尖高校和量化金融从业人员组成的前沿社区，致力于探索人工智能（AI）与量化（Quant）领域的无限可能。我们的团队成员来自剑桥大学、牛津大学、哈佛大学、苏黎世联邦理工学院、北京大学、中科大等世界知名高校，外部顾问来自Microsoft、HSBC、Citadel、Man Group、Citi、Jump Trading、国内顶尖私募等一流企业。