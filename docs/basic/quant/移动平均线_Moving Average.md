![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# 什么是移动平均线（MA）？
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)
在金融领域，移动平均线（MA）是一种常用于技术分析的股票指标。计算股票的移动平均线旨在通过创建一个不断更新的平均价格来平滑价格数据。

通过计算移动平均线，随机和短期波动对特定时间框架内股票价格的影响被减弱。简单移动平均线（SMA）利用某一时间段内价格的算术平均值，而指数移动平均线（EMA）则对近期价格赋予更大权重。

### 主要要点

- 移动平均线（MA）是常用于技术分析的股票指标。
- 移动平均线通过创建一个不断更新的平均价格，帮助平衡某一特定时期的价格数据。
- 简单移动平均线（SMA）是对过去特定天数内一组价格的算术平均值计算。
- 指数移动平均线（EMA）是加权平均，给予近期价格更大的重要性，使其对新信息更为敏感。

## 理解移动平均线（MA）

移动平均线的计算用于识别股票的趋势方向或确定其支撑和阻力水平。它是一种跟随趋势或滞后指标，因为它基于过去的价格。

移动平均线的周期越长，滞后效果越明显。200日移动平均线的滞后效果远大于20日移动平均线，因为它包含了过去200天的价格。50日和200日移动平均线的数值在投资者和交易者中广受关注，并被视为重要的交易信号。

投资者可以根据自己的交易目标选择不同长度的周期来计算移动平均线。较短的移动平均线通常用于短期交易，而较长期的移动平均线则更适合长期投资者。

尽管无法预测特定股票的未来走势，但使用技术分析和研究可以帮助做出更好的预测。上升的移动平均线表明证券处于上涨趋势，而下降的移动平均线则表明处于下跌趋势。

相似地，向上的动量通过看涨交叉确认，即短期移动平均线突破长期移动平均线。反之，向下的动量通过看跌交叉确认，即短期移动平均线跌破长期移动平均线。

## 移动平均线的类型

简单移动平均线（SMA）是通过对特定时期内一组数值的算术平均来计算的。将一组数字或股票价格相加，然后除以价格数量。计算证券简单移动平均线的公式如下：

$$ \begin{aligned} &SMA = \frac{ A_1 + A_2 + \cdots + A_n }{ n } \\ &\textbf{其中:} \\ &A = \text{第 } n \text{ 期的平均值} \\ &n = \text{时间周期的数量} \\ \end{aligned} $$

使用简单移动平均线绘制50天股票价格的图形可能如下所示：

指数移动平均线给予最近价格更多的权重，以使其更能响应新信息。要计算EMA，首先计算特定时期的简单移动平均线（SMA）。

然后计算用于加权EMA的乘数，称为"平滑因子"，其公式通常为：[2/(选择的时间周期 + 1)]。

对于20日移动平均线，乘数为[2/(20+1)]= 0.0952。平滑因子与前一个EMA结合以得出当前值。因此，EMA对近期价格赋予更高的权重，而SMA则对所有值赋予相等的权重。

$$ \begin{aligned} &EMA_t = \left [ V_t \times \left ( \frac{ s }{ 1 + d } \right ) \right ] + EMA_y \times \left [ 1 - \left ( \frac { s }{ 1 + d} \right ) \right ] \\ &\textbf{其中:}\\ &EMA_t = \text{今日EMA} \\ &V_t = \text{今日值} \\ &EMA_y = \text{昨日EMA} \\ &s = \text{平滑} \\ &d = \text{天数} \\ \end{aligned} $$

## 其他常用移动平均线类型

### 加权移动平均线（WMA）

加权移动平均线对不同时期的价格赋予线性递减的权重：

$$ WMA_n(t) = \frac{\sum_{i=0}^{n-1} (n-i) \cdot P_{t-i}}{\sum_{i=0}^{n-1} (n-i)} = \frac{\sum_{i=0}^{n-1} (n-i) \cdot P_{t-i}}{\frac{n(n+1)}{2}} $$

### 双指数移动平均线（DEMA）

DEMA 通过消除单一 EMA 的滞后性来提供更快的信号响应：

$$ DEMA_n(t) = 2 \cdot EMA_n(t) - EMA_n(EMA_n(t)) $$

### 自适应移动平均线（KAMA）

考夫曼自适应移动平均线（KAMA）根据市场噪声自动调整平滑系数：

$$ KAMA_t = KAMA_{t-1} + SC_t \cdot (P_t - KAMA_{t-1}) $$

其中 $SC_t$ 为基于效率比（Efficiency Ratio）动态计算的平滑常数。效率比定义为：

$$ ER = \frac{|P_t - P_{t-n}|}{\sum_{i=0}^{n-1}|P_{t-i} - P_{t-i-1}|}$$

ER 越接近1，表示趋势越明确，KAMA跟踪越紧密；ER越接近0，表示市场以噪声为主，KAMA变化越平缓。

## 简单移动平均线（SMA）与指数移动平均线（EMA）

EMA的计算对近期数据点赋予更大重视。因此，EMA被视为一种加权平均计算。

下图中，每种平均线使用的周期数为15，但EMA对价格变化的响应明显快于SMA。当价格上涨时，EMA的数值高于SMA，而当价格下降时，EMA的下降速度也快于SMA。这种对价格变化的敏感性是一些交易者更倾向于使用EMA的主要原因。

## 移动平均线示例

移动平均线的计算因类型不同而有所不同：SMA或EMA。以下是某个证券在15天内的收盘价格的简单移动平均线（SMA）示例：

- 第1周（5天）：20, 22, 24, 25, 23
- 第2周（5天）：26, 28, 26, 29, 27
- 第3周（5天）：28, 30, 27, 29, 28

10日移动平均线将对前10天的收盘价格进行平均，以作为第一个数据点。下一个数据点将删除最早的价格，添加第11天的价格，并重新计算平均值。

Bollinger Band技术指标通常将带宽放置在简单移动平均线的两标准差处。一般而言，向上移动至上带表示资产可能被高估，而接近下带则表明资产可能被低估。由于标准差是衡量波动性的统计指标，该指标会根据市场状况进行调整。

布林带的数学表达为：

$$ Upper = SMA_n + k \cdot \sigma_n $$
$$ Lower = SMA_n - k \cdot \sigma_n $$

其中 $k$ 通常取2，$\sigma_n$ 为 $n$ 日收盘价的标准差。

## 量化应用

### Python 实现各类移动平均线

```python
import pandas as pd
import numpy as np

def calculate_moving_averages(prices: pd.Series, window: int = 20):
    """
    计算多种移动平均线
    
    Parameters
    ----------
    prices : pd.Series -- 收盘价序列
    window : int       -- 窗口期
    
    Returns
    -------
    pd.DataFrame -- 包含各类均线的DataFrame
    """
    ma = pd.DataFrame(index=prices.index)
    ma['price'] = prices
    
    # 简单移动平均线 (SMA)
    ma['SMA'] = prices.rolling(window=window).mean()
    
    # 指数移动平均线 (EMA)
    ma['EMA'] = prices.ewm(span=window, adjust=False).mean()
    
    # 加权移动平均线 (WMA)
    weights = np.arange(1, window + 1)
    ma['WMA'] = prices.rolling(window=window).apply(
        lambda x: np.dot(x, weights) / weights.sum(), raw=True
    )
    
    # 双指数移动平均线 (DEMA)
    ema = prices.ewm(span=window, adjust=False).mean()
    ema_of_ema = ema.ewm(span=window, adjust=False).mean()
    ma['DEMA'] = 2 * ema - ema_of_ema
    
    return ma


def ma_crossover_signals(prices: pd.Series, fast: int = 10, slow: int = 30):
    """均线交叉信号生成器"""
    sma_fast = prices.rolling(window=fast).mean()
    sma_slow = prices.rolling(window=slow).mean()
    
    signals = pd.Series(0, index=prices.index)
    signals[sma_fast > sma_slow] = 1    # 多头信号
    signals[sma_fast <= sma_slow] = -1   # 空头信号
    
    # 仅保留交叉点的信号
    trades = signals.diff().fillna(0)
    return trades


def kaufman_adaptive_ma(prices: pd.Series, n: int = 10, 
                         fast_sc: int = 2, slow_sc: int = 30):
    """考夫曼自适应移动平均线（KAMA）"""
    fast_alpha = 2.0 / (fast_sc + 1)
    slow_alpha = 2.0 / (slow_sc + 1)
    
    kama = pd.Series(index=prices.index, dtype=float)
    kama.iloc[n-1] = prices.iloc[n-1]
    
    for i in range(n, len(prices)):
        direction = abs(prices.iloc[i] - prices.iloc[i-n])
        volatility = sum(abs(prices.iloc[j] - prices.iloc[j-1]) 
                        for j in range(i-n+1, i+1))
        
        if volatility == 0:
            er = 0
        else:
            er = direction / volatility
        
        sc = (er * (fast_alpha - slow_alpha) + slow_alpha) ** 2
        kama.iloc[i] = kama.iloc[i-1] + sc * (prices.iloc[i] - kama.iloc[i-1])
    
    return kama
```

### 移动平均线在因子模型中的应用

在量化多因子模型中，移动平均线常被用于构建动量因子和趋势因子：

- **均线偏离率因子**：$BIAS_n = \frac{P_t - SMA_n(t)}{SMA_n(t)}$，衡量当前价格偏离均线的程度
- **均线斜率因子**：$Slope_n = \frac{SMA_n(t) - SMA_n(t-k)}{k}$，衡量趋势的强度和方向
- **均线排列因子**：当 $SMA_5 > SMA_{10} > SMA_{20} > SMA_{60}$ 时为多头排列，反之为空头排列

### 均线系统的参数选择

在量化策略中，均线参数的选择直接影响策略表现。常见的参数组合包括：

| 策略类型 | 短期均线 | 长期均线 | 适用场景 |
|---------|---------|---------|---------|
| 超短线 | 5日 | 10日 | 日内/隔日交易 |
| 短线 | 10日 | 30日 | 波段交易 |
| 中线 | 20日 | 60日 | 中期趋势跟踪 |
| 长线 | 50日 | 200日 | 长期趋势确认 |

参数优化时应注意：过短的窗口导致过多虚假信号（高换手成本），过长的窗口导致信号严重滞后（错过行情）。可通过滚动窗口回测和信息比率（Information Ratio）来评估最优参数。

## 移动平均线表明什么？

移动平均线是一种统计数据，捕捉某一数据序列随时间变化的平均变化。在金融领域，移动平均线通常被技术分析师用于跟踪特定证券的价格趋势。移动平均线的上升趋势可能意味着证券价格或动量的上涨，而下降趋势则被视为下滑的信号。

## 移动平均线的用途是什么？

移动平均线在技术分析中广泛使用，技术分析旨在理解和利用证券与指数的价格运动模式。通常，技术分析师会利用移动平均线检测证券动量变化，例如证券价格的突然下跌。有时，他们会利用移动平均线来确认自己对潜在变化的怀疑。

## 移动平均线的例子是什么？

指数移动平均线（EMA）是一种移动平均线，对最近的交易日给予更多的权重。这种类型的移动平均线对于短期交易者可能更有用，因为对他们而言，较长期的历史数据可能相关性较低。简单移动平均线通过对一系列价格进行平均计算，同时对所有价格赋予相等的权重。

## 什么是MACD？

交易者使用移动平均收敛发散（MACD）来监视两个移动平均线之间的关系，计算方法是将26日指数移动平均线减去12日指数移动平均线：

$$ MACD(t) = EMA_{12}(t) - EMA_{26}(t) $$

MACD信号线为MACD的9日EMA：

$$ Signal(t) = EMA_9(MACD(t)) $$

MACD柱状图（Histogram）反映了MACD线与信号线之间的差异：

$$ Histogram(t) = MACD(t) - Signal(t) $$

MACD还采用信号线，帮助识别交叉点，即与MACD线绘制在同一图形上的九日指数移动平均线。

信号线用于帮助识别证券价格的趋势变化，并确认趋势的强度。当MACD为正时，短期平均值位于长期平均值之上，表明上涨动量；而当短期平均值低于长期平均值时，则表明动量向下。

在量化交易中，MACD的背离（divergence）信号尤为重要：当价格创新高但MACD未能创新高时，形成顶背离，预示趋势可能反转。

## 什么是黄金交叉？

黄金交叉是一种图表模式，其中短期移动平均线突破长期移动平均线。黄金交叉是由证券的短期移动平均线（如15日移动平均线）突破其长期移动平均线（如50日移动平均线）形成的看涨突破模式。由于长期指标影响力更大，黄金交叉预示着市场前景看好，并且往往伴随着高交易量。

## 结论

移动平均线（MA）是常用于技术分析的股票指标，通过创建一个不断更新的平均价格来平滑价格数据。上升的移动平均线表明证券处于上涨趋势，而下降的移动平均线则指示下跌趋势。

一般而言，指数移动平均线优于简单移动平均线，因为它对近期价格赋予更高的权重，并对新信息和趋势的反应更为清晰。

对于量化交易者而言，移动平均线不仅是独立的技术指标，更是构建复杂交易系统的基础组件。从简单的均线交叉策略到多因子模型中的趋势因子，移动平均线在现代量化投资中扮演着不可或缺的角色。在实际应用中，建议结合波动率调整、自适应参数等方法来增强均线系统的稳健性。

## 关于LLMQuant
LLMQuant是由一群来自世界顶尖高校和量化金融从业人员组成的前沿社区，致力于探索人工智能（AI）与量化（Quant）领域的无限可能。我们的团队成员来自剑桥大学、牛津大学、哈佛大学、苏黎世联邦理工学院、北京大学、中科大等世界知名高校，外部顾问来自Microsoft、HSBC、Citadel、Man Group、Citi、Jump Trading、国内顶尖私募等一流企业。