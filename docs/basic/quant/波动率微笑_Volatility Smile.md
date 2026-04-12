![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# 什么是波动率微笑？
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

波动率微笑是一种常见的图形，通过绘制相同标的资产和到期日期的一组期权的行使价格与隐含波动率，可以得到这种图形。波动率微笑之所以得名，是因为它的形状像一张笑脸。当期权的标的资产更加虚值（OTM）或实值（ITM）时，隐含波动率上升，而相对于平值（ATM）期权，隐含波动率较低。并非所有期权都有波动率微笑。

### 关键要点

- 当在不同的行使价格下，期权的到期日和标的资产相同时，隐含波动率的图形往往呈现微笑形状。
- 微笑曲线表明，实值（ITM）或虚值（OTM）期权的隐含波动率最高。
- 隐含波动率最低的期权，其行使价格通常接近平值（ATM）或在平值附近。
- 并非所有期权都会出现隐含波动率微笑。短期期权和与货币相关的期权更可能出现波动率微笑。
- 单个期权的隐含波动率也可能随着其走向更实值或虚值而呈现波动率微笑。
- 虽然隐含波动率是期权定价的一个因素，但并不是唯一因素。交易者还需关注其他影响期权价格和波动率的因素。

## 波动率微笑传达了什么？

波动率微笑是由于隐含波动率随着标的资产走向实值或虚值而变化所形成的。期权越是实值或虚值，其隐含波动率通常越高，而在平值期权下，隐含波动率往往最低。

波动率微笑并不符合布莱克-斯科尔斯模型（Black-Scholes model），该模型是用于定价期权及其他衍生品的主要公式之一。布莱克-斯科尔斯模型预测，当针对不同的行使价格绘制隐含波动率曲线时，曲线将是平坦的。根据该模型，所有在同一天到期、具有相同标的资产的期权，其隐含波动率应是一致的，无论行使价格如何。然而，在现实中情况并非如此。

自1987年股市崩盘后，波动率微笑开始在期权定价中出现。此前，美国市场并未出现这种现象，这表明市场结构更符合布莱克-斯科尔斯模型的预测。1987年后，交易者意识到极端事件可能会发生，市场也存在显著的偏斜。因此，在现实中，隐含波动率会随着期权走向更实值或虚值而增加或减少。

此外，波动率微笑的存在显示，实值和虚值期权的需求通常超过平值期权。需求驱动价格，从而影响隐含波动率。这部分可以归因于上面提到的原因。极端事件可能导致期权价格发生显著波动，大幅波动的可能性被纳入隐含波动率的计算中。

## 波动率微笑的使用示例

在比较相同标的资产和到期日但行使价格不同的各类期权时，可以观察到波动率微笑。若对不同的行使价格绘制隐含波动率，则可能出现U形。U形并不总是与上述图形一样完美。

要粗略估计某个期权是否呈现U形，可以查看一个列出各行使价格隐含波动率的期权链。如果该期权呈U形，则ITM和OTM的期权应具有大致相同的隐含波动率。行使价格越是远离平值，其隐含波动率就越高，而处于平值附近的期权则有最低的隐含波动率。如果情况并非如此，则该期权并不符合波动率微笑的特征。

单个期权的隐含波动率也可以随着标的资产价格的波动而绘制出时间序列图。当价格往内或往外移动时，隐含波动率可能呈现某种U形。

这在寻找隐含波动率较低的期权时很有用。在这种情况下，可以选择接近平值的期权。如果希望寻找更高的隐含波动率，则应选择更为实值或虚值的期权。不过，请记住，随着标的资产价格靠近或远离行使价格，这将影响隐含波动率。因此，维持一个特定隐含波动率的期权组合将需要不断调整。

并非所有期权都有波动率微笑。在使用波动率微笑来帮助交易决策之前，务必检查该期权的隐含波动率是否真的符合这一模型。

## 波动率微笑与波动率偏斜/微笑的区别

虽然短期期权和外汇期权更倾向于符合波动率微笑，但指数期权和长期股权期权则往往更倾向于与波动率偏斜相一致。偏斜/微笑表明，实值或虚值期权的隐含波动率可能更高。

## 使用波动率微笑的局限性

首先，确定交易的期权是否真正符合波动率微笑非常重要。波动率微笑是某些期权可能符合的模型，但隐含波动率也可能更加符合反向或正向的偏斜/微笑。

此外，由于其他市场因素（例如供求关系），波动率微笑（如果适用）可能不会是一个干净的U形（或微笑）。它可能具有基本的U形，但可能很不平坦，某些期权的隐含波动率可能比该模型预期的高或低。

波动率微笑突显了交易者在寻找更高或更低隐含波动率时应关注的方向，但在做出期权交易决策时，还需考虑其他许多因素。

## 参考文献

[1] Luca Benzoni, Pierre Collin-Dufresne, and Robert S. Goldstein. “[Explaining Asset Pricing Puzzles Associated with the 1987 Market Crash](http://pages.stern.nyu.edu/~dbackus/GE_asset_pricing/BCDG%2087%20crash%20Jan%2010.PDF),” Page 1. Journal of Financial Economics, September 2011.

## 波动率微笑的数学解释

### Black-Scholes模型的局限

Black-Scholes模型假设标的资产价格服从几何布朗运动：

$$dS = \mu S \, dt + \sigma S \, dW_t$$

其中波动率 $\sigma$ 为常数。该假设意味着对数收益率服从正态分布：

$$\ln\left(\frac{S_T}{S_0}\right) \sim N\left(\left(\mu - \frac{\sigma^2}{2}\right)T, \sigma^2 T\right)$$

然而，实际市场中对数收益率呈现**负偏态**和**肥尾**特征（峰度 > 3），导致深度OTM看跌期权和深度OTM看涨期权的市场价格高于BS模型预测，因此反推出的隐含波动率呈现”微笑”形状。

### 隐含波动率曲面

完整的隐含波动率不仅是行权价的函数，还是到期时间的函数，形成一个二维曲面 $\sigma_{IV}(K, T)$。

对于固定到期日 $T$，隐含波动率关于行权价的常用参数化形式包括：

**二次多项式近似**：

$$\sigma_{IV}(K) \approx a + b \cdot \left(\frac{K - S}{S}\right) + c \cdot \left(\frac{K - S}{S}\right)^2$$

其中 $a$ 为ATM波动率水平，$b$ 控制偏斜（skew），$c$ 控制曲率（微笑程度）。

**SVI参数化（Stochastic Volatility Inspired）**：

$$w(k) = a + b\left(\rho(k - m) + \sqrt{(k - m)^2 + \sigma^2}\right)$$

其中 $w = \sigma_{IV}^2 T$ 为总隐含方差，$k = \ln(K/F)$ 为对数moneyness，参数 $\{a, b, \rho, m, \sigma\}$ 通过拟合市场数据确定。

### 风险中性概率分布

Breeden-Litzenberger公式将隐含波动率曲面与风险中性概率密度联系起来：

$$f_{RN}(S_T = K) = e^{rT} \frac{\partial^2 C}{\partial K^2}\bigg|_{K}$$

波动率微笑意味着风险中性分布具有比正态分布更厚的尾部，反映市场对极端事件赋予了更高的概率。

## 详细交易实例

**案例一：利用波动率微笑的蝶式价差**

假设SPX指数在4,500点，30天期权的隐含波动率如下：

| 行权价 | Moneyness | IV | BS价格 | 市场价格 |
|--------|-----------|-----|--------|---------|
| 4,200 | -6.7% | 22.5% | $8.20 | $12.50 |
| 4,350 | -3.3% | 18.8% | $22.40 | $24.80 |
| 4,500 (ATM) | 0% | 16.2% | $45.30 | $45.30 |
| 4,650 | +3.3% | 17.5% | $12.80 | $14.20 |
| 4,800 | +6.7% | 19.8% | $3.10 | $5.40 |

交易者观察到左侧偏斜（OTM看跌IV偏高），认为偏斜过度，构建看跌蝶式价差：

- 买入1份$4,200看跌（$12.50）
- 卖出2份$4,350看跌（$24.80 × 2 = $49.60）
- 买入1份$4,500看跌（$45.30）

净成本：$12.50 - $49.60 + $45.30 = $8.20

最大利润：$(4,350 - 4,200) - $8.20 = $141.80（指数到期时恰好在$4,350时）

**案例二：波动率偏斜交易（Risk Reversal）**

当交易者认为下行偏斜过度时：

- 卖出1份25-delta OTM看跌（高IV，收取较多权利金）
- 买入1份25-delta OTM看涨（较低IV，支付较少权利金）

例如：卖出$4,200看跌收取$12.50，买入$4,800看涨支付$5.40
净收入：$7.10（零成本或正收入的方向性交易）

## 量化应用

```python
import numpy as np
from scipy.stats import norm
from scipy.optimize import minimize, brentq

class VolatilitySmileAnalyzer:
    “””波动率微笑分析与交易工具”””
    
    @staticmethod
    def bs_call(S, K, T, r, sigma):
        “””Black-Scholes看涨期权定价”””
        if T <= 0 or sigma <= 0:
            return max(S - K * np.exp(-r * T), 0)
        d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
        d2 = d1 - sigma*np.sqrt(T)
        return S * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)
    
    @staticmethod
    def implied_vol(market_price, S, K, T, r, option_type='call'):
        “””二分法求隐含波动率”””
        if option_type == 'put':
            # 通过Put-Call Parity转换
            market_price = market_price + S - K * np.exp(-r * T)
        
        def obj(sigma):
            return VolatilitySmileAnalyzer.bs_call(S, K, T, r, sigma) - market_price
        
        try:
            return brentq(obj, 0.001, 5.0)
        except ValueError:
            return np.nan
    
    def fit_svi(self, strikes, ivs, S, T):
        “””
        拟合SVI参数化模型
        w(k) = a + b * (rho*(k-m) + sqrt((k-m)^2 + sigma^2))
        “””
        k = np.log(strikes / S)  # log-moneyness
        w = ivs**2 * T  # total implied variance
        
        def svi(params, k):
            a, b, rho, m, sig = params
            return a + b * (rho * (k - m) + np.sqrt((k - m)**2 + sig**2))
        
        def objective(params):
            pred = svi(params, k)
            return np.sum((pred - w)**2)
        
        # 初始猜测
        x0 = [np.mean(w), 0.1, -0.3, 0, 0.1]
        bounds = [(0, None), (0, None), (-0.99, 0.99), (-1, 1), (0.001, None)]
        
        result = minimize(objective, x0, bounds=bounds, method='L-BFGS-B')
        
        params = result.x
        fitted_w = svi(params, k)
        fitted_iv = np.sqrt(fitted_w / T)
        
        return {
            'params': {'a': params[0], 'b': params[1], 'rho': params[2], 
                       'm': params[3], 'sigma': params[4]},
            'fitted_iv': fitted_iv,
            'residuals': ivs - fitted_iv,
            'rmse': np.sqrt(np.mean((ivs - fitted_iv)**2))
        }
    
    def compute_skew_metrics(self, strikes, ivs, S):
        “””计算波动率偏斜的关键指标”””
        # 找到ATM隐含波动率
        atm_idx = np.argmin(np.abs(strikes - S))
        atm_iv = ivs[atm_idx]
        
        # 25-delta偏斜（近似）
        otm_put_idx = np.argmin(np.abs(strikes - S * 0.95))  # ~25-delta put
        otm_call_idx = np.argmin(np.abs(strikes - S * 1.05))  # ~25-delta call
        
        skew_25d = ivs[otm_put_idx] - ivs[otm_call_idx]
        
        # 蝶式（微笑曲率）
        butterfly = (ivs[otm_put_idx] + ivs[otm_call_idx]) / 2 - atm_iv
        
        # 偏斜斜率（每1% moneyness的IV变化）
        moneyness = (strikes - S) / S
        slope_idx = (moneyness > -0.10) & (moneyness < 0.10)
        if np.sum(slope_idx) > 2:
            coeffs = np.polyfit(moneyness[slope_idx], ivs[slope_idx], 1)
            skew_slope = coeffs[0]  # IV per unit moneyness
        else:
            skew_slope = np.nan
        
        return {
            'atm_iv': f”{atm_iv:.2%}”,
            'skew_25d': f”{skew_25d:.2%}”,
            'butterfly_25d': f”{butterfly:.2%}”,
            'skew_slope': f”{skew_slope:.4f}” if not np.isnan(skew_slope) else “N/A”
        }
    
    def risk_neutral_density(self, strikes, ivs, S, T, r, dK=0.5):
        “””
        通过Breeden-Litzenberger公式提取风险中性概率密度
        “””
        prices = np.array([
            self.bs_call(S, K, T, r, iv) for K, iv in zip(strikes, ivs)
        ])
        
        # 数值二阶导数
        density = []
        valid_strikes = []
        
        for i in range(1, len(strikes) - 1):
            d2C = (prices[i+1] - 2*prices[i] + prices[i-1]) / (
                (strikes[i+1] - strikes[i]) * (strikes[i] - strikes[i-1]))
            density.append(np.exp(r * T) * d2C)
            valid_strikes.append(strikes[i])
        
        return np.array(valid_strikes), np.array(density)
    
    def smile_trading_signals(self, current_skew, hist_skews, 
                               current_butterfly, hist_butterflies):
        “””
        基于波动率微笑的交易信号
        “””
        skew_z = (current_skew - np.mean(hist_skews)) / np.std(hist_skews)
        bfly_z = (current_butterfly - np.mean(hist_butterflies)) / np.std(hist_butterflies)
        
        signals = []
        
        if skew_z > 2:
            signals.append({
                'trade': '卖出偏斜（Risk Reversal）',
                'action': '卖OTM Put + 买OTM Call',
                'rationale': f'偏斜Z-score={skew_z:.1f}，处于历史极高水平'
            })
        elif skew_z < -2:
            signals.append({
                'trade': '买入偏斜',
                'action': '买OTM Put + 卖OTM Call',
                'rationale': f'偏斜Z-score={skew_z:.1f}，下行保护被低估'
            })
        
        if bfly_z > 2:
            signals.append({
                'trade': '卖出蝶式',
                'action': '卖出Iron Butterfly',
                'rationale': f'微笑曲率Z-score={bfly_z:.1f}，尾部期权定价偏高'
            })
        elif bfly_z < -2:
            signals.append({
                'trade': '买入蝶式',
                'action': '买入Iron Butterfly',
                'rationale': f'微笑曲率Z-score={bfly_z:.1f}，尾部保护便宜'
            })
        
        if not signals:
            signals.append({'trade': '无信号', 'action': '观望', 
                           'rationale': '偏斜和曲率均在正常范围内'})
        
        return signals


# 使用示例
analyzer = VolatilitySmileAnalyzer()

# 构建模拟的波动率微笑数据
S = 4500  # SPX指数
T = 30/252
r = 0.05

strikes = np.arange(4050, 4951, 50)
# 模拟微笑形状：ATM最低，两侧上升，左侧更陡
moneyness = (strikes - S) / S
true_ivs = 0.16 + 0.15 * moneyness**2 - 0.08 * moneyness + \
           0.01 * np.random.normal(size=len(strikes))
true_ivs = np.maximum(true_ivs, 0.05)

# 1. 偏斜分析
print(“=== 波动率微笑分析 ===”)
metrics = analyzer.compute_skew_metrics(strikes, true_ivs, S)
for k, v in metrics.items():
    print(f”  {k}: {v}”)

# 2. SVI拟合
print(“\n=== SVI模型拟合 ===”)
svi_result = analyzer.fit_svi(strikes, true_ivs, S, T)
print(f”SVI参数: {svi_result['params']}”)
print(f”拟合RMSE: {svi_result['rmse']:.4f}”)

# 3. 风险中性概率密度
print(“\n=== 风险中性密度 ===”)
rn_strikes, rn_density = analyzer.risk_neutral_density(
    strikes, true_ivs, S, T, r
)
peak_idx = np.argmax(rn_density)
print(f”概率密度峰值: K=${rn_strikes[peak_idx]:.0f}”)
print(f”左尾概率 (S<4200): {np.sum(rn_density[rn_strikes<4200]) * 50:.2%}”)
print(f”右尾概率 (S>4800): {np.sum(rn_density[rn_strikes>4800]) * 50:.2%}”)

# 4. 交易信号
print(“\n=== 交易信号 ===”)
np.random.seed(42)
hist_skews = np.random.normal(0.05, 0.015, 252)
hist_bfly = np.random.normal(0.02, 0.008, 252)

current_skew = float(metrics['skew_25d'].strip('%')) / 100
signals = analyzer.smile_trading_signals(
    current_skew, hist_skews, 0.035, hist_bfly
)
for sig in signals:
    print(f”  交易: {sig['trade']}”)
    print(f”  操作: {sig['action']}”)
    print(f”  理由: {sig['rationale']}”)
```

## 波动率微笑的实务要点

1. **偏斜的信息含量**：股指期权的偏斜反映了市场对下行风险的定价。偏斜急剧陡峭化通常发生在市场恐慌时期（如VIX飙升时），此时OTM看跌期权需求激增。偏斜的绝对水平和变化速度都是重要的市场情绪指标。

2. **期限结构效应**：短期期权通常展现更明显的微笑/偏斜，因为短期内跳跃风险的影响更大。随着到期时间延长，微笑趋于平坦化，这是因为中心极限定理使得长期收益分布更接近正态。

3. **做市商的角色**：期权做市商通过波动率曲面的校准和动态对冲来管理复杂的风险簿。他们持续根据供需动态调整各行权价的隐含波动率报价，是波动率微笑形成和维持的核心参与者。

4. **模型选择**：精确拟合波动率微笑需要超越BS模型。常用的替代模型包括：
   - **局部波动率模型**（Dupire）：$\sigma = \sigma(S, t)$
   - **随机波动率模型**（Heston）：波动率本身服从随机过程
   - **跳跃扩散模型**（Merton）：在扩散过程中加入泊松跳跃
   - **SABR模型**：利率衍生品市场的标准模型

## 关于LLMQuant
LLMQuant是由一群来自世界顶尖高校和量化金融从业人员组成的前沿社区，致力于探索人工智能（AI）与量化（Quant）领域的无限可能。我们的团队成员来自剑桥大学、牛津大学、哈佛大学、苏黎世联邦理工学院、北京大学、中科大等世界知名高校，外部顾问来自Microsoft、HSBC、Citadel、Man Group、Citi、Jump Trading、国内顶尖私募等一流企业。