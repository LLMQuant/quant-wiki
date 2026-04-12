![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# 什么是统计显著性？

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

统计显著性是分析师所做的一项判断，涉及数据结果不单纯因偶然因素所致。统计假设检验是分析师用来作出这一判断的方法。该检验提供一个p值，即在假设结果确实由偶然因素造成的情况下，观察到与数据结果如此极端的结果的概率。

通常，p值为5%或更低被视为具有统计显著性。

### 关键要点

- 统计显著性判断两个或多个变量之间的关系是由非偶然因素造成的。
- 它用于提供证据，以评估零假设的可信度，零假设假设数据中的变动仅由随机因素造成。
- 统计假设检验用于确定数据集的结果是否具有统计显著性。
- p值为5%或更低通常被视为统计显著性。

## 理解统计显著性

统计显著性是对零假设的判断，零假设认为结果仅由随机因素造成。当p值足够小，数据集即被视为有统计显著性。

当p值较大时，结果可以用偶然因素解释，而数据被视为与零假设一致，尽管这并不证明零假设的正确性。

当p值足够小，通常为5%或更低，结果则不容易用偶然因素解释，数据被视为与零假设不一致。在这种情况下，零假设被拒绝，通常支持更系统的解释。[1]

**重要提示：** 统计显著性常用于新的药品试验、疫苗测试以及病理研究的有效性测试。这可以为投资者提供关于公司新产品发布成功率的参考。

### 显著性水平与临界值

显著性水平 $\alpha$ 是判断统计显著性的预设阈值。常用的显著性水平及对应的 Z 临界值如下：

| 显著性水平 $\alpha$ | 置信水平 | 双尾临界值 $z_{\alpha/2}$ | 单尾临界值 $z_{\alpha}$ |
|---|---|---|---|
| 0.10 | 90% | $\pm 1.645$ | 1.282 |
| 0.05 | 95% | $\pm 1.960$ | 1.645 |
| 0.01 | 99% | $\pm 2.576$ | 2.326 |
| 0.001 | 99.9% | $\pm 3.291$ | 3.090 |

判断统计显著性的等价条件：

$$
\text{统计显著} \iff p\text{-value} \leq \alpha \iff |Z_{\text{obs}}| \geq z_{\alpha/2} \text{（双尾检验）}
$$

### 效应量（Effect Size）

统计显著性只回答"差异是否存在"，而效应量则回答"差异有多大"。常用的效应量指标包括：

**Cohen's d：**

$$
d = \frac{\bar{X}_1 - \bar{X}_2}{s_p}
$$

其中 $s_p = \sqrt{\frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}}$ 为合并标准差。

Cohen 建议：$d = 0.2$ 为小效应，$d = 0.5$ 为中等效应，$d = 0.8$ 为大效应。

**在金融中，** 常用信息比率（Information Ratio）或夏普比率（Sharpe Ratio）作为效应量的度量，衡量超额收益相对于其波动性的大小。

## 统计显著性的例子

假设金融分析师亚历克斯关注是否有一些投资者提前获悉某家公司突如其来的倒闭。亚历克斯决定比较该公司倒闭前后的每日市场收益均值，以确定这两个均值之间是否存在统计显著差异。

该研究的p值为28%（>5%），这表明像观察到的差异（-0.0033至+0.0007）在仅以偶然因素作解释的情况下并不罕见。因此，数据并未提供强有力的证据证明有人提前知道该公司会倒闭。

如果p值为0.01%，远低于5%，那么在仅以偶然因素作解释的情况下，观察到的差异将十分异常。此时，亚历克斯可能决定拒绝零假设，进一步调查是否有交易者提前获知信息。

统计显著性同样用于测试新的医疗产品，包括药物、设备和疫苗。公开发布的统计显著性报告也向投资者提供有关公司新产品发布成功率的信息。

假设一家领先的糖尿病药物公司报告其新胰岛素在测试中显示出统计显著的糖尿病减少。该测试持续26周，在糖尿病患者中进行随机治疗，数据显示p值为4%。这向投资者和监管机构表明，数据确实显示糖尿病的统计显著减少。[2]

制药公司股票价格常受其新产品统计显著性公告的影响。[3]

### 数值计算示例

假设一位量化分析师检验某量化策略的月均收益率是否显著高于零：

- 样本量 $n = 48$（四年月度数据）
- 样本均值 $\bar{X} = 0.8\%$
- 样本标准差 $s = 3.2\%$

检验统计量：

$$
t = \frac{0.008 - 0}{0.032 / \sqrt{48}} = \frac{0.008}{0.00462} = 1.732
$$

对于自由度 $df = 47$ 的单尾 t 检验，$p \approx 0.045 < 0.05$，因此在 5% 显著性水平下策略收益显著大于零。

但注意，年化夏普比率为 $SR = 0.008/0.032 \times \sqrt{12} \approx 0.87$，虽然统计显著，但效应量属于中等水平，在考虑交易成本后可能不再具有经济显著性。

## 金融应用

统计显著性在量化金融领域有着至关重要的应用：

**1. 因子有效性检验：** 在构建多因子选股模型时，需要检验每个因子的收益是否具有统计显著性。通常要求因子的 t 统计量绝对值大于 2（近似对应 $p < 0.05$）。

**2. 策略回测与过拟合：** Bailey 和 Lopez de Prado 提出了"最低回测长度"（Minimum Backtest Length）的概念：

$$
\text{MinBTL} = \left(\frac{z_{\alpha/2}}{\widehat{SR} \times \sqrt{12}}\right)^2 \text{（年）}
$$

其中 $\widehat{SR}$ 为年化夏普比率。这给出了在给定夏普比率下，策略需要多长的回测才能达到统计显著。

**3. 多重检验校正：** 当同时检验 $m$ 个策略或因子时，需要调整显著性水平：

- **Bonferroni 校正：** 调整后的阈值为 $\alpha / m$
- **Holm-Bonferroni 方法：** 对 p 值排序后逐步校正
- **Benjamini-Hochberg FDR 控制：** 控制错误发现率

例如，若同时检验 100 个因子，在 $\alpha = 0.05$ 下预期有 5 个因子会因偶然而"显著"。使用 Bonferroni 校正后，单个因子的显著性阈值变为 $0.05 / 100 = 0.0005$。

### Python 代码示例

```python
import numpy as np
from scipy import stats

# 检验策略收益的统计显著性
monthly_returns = np.array([0.012, -0.005, 0.018, 0.003, 0.015, -0.008,
                            0.022, 0.007, 0.011, -0.003, 0.019, 0.006,
                            0.014, -0.001, 0.016, 0.008, 0.013, -0.004,
                            0.020, 0.005, 0.010, 0.002, 0.017, -0.006,
                            0.015, 0.009, 0.011, 0.004, 0.018, -0.002,
                            0.013, 0.007, 0.016, 0.001, 0.014, -0.003,
                            0.019, 0.006, 0.012, 0.008, 0.015, 0.003,
                            0.017, -0.001, 0.010, 0.009, 0.013, 0.005])

n = len(monthly_returns)
mean_ret = np.mean(monthly_returns)
std_ret = np.std(monthly_returns, ddof=1)

# t 检验
t_stat = mean_ret / (std_ret / np.sqrt(n))
p_value = 1 - stats.t.cdf(t_stat, df=n-1)

# 年化夏普比率
sharpe = (mean_ret / std_ret) * np.sqrt(12)

print(f"样本量: {n} 个月")
print(f"月均收益: {mean_ret:.4%}")
print(f"月标准差: {std_ret:.4%}")
print(f"t 统计量: {t_stat:.4f}")
print(f"p 值 (单尾): {p_value:.6f}")
print(f"年化夏普比率: {sharpe:.2f}")
print(f"统计显著性 (α=0.05): {'显著' if p_value < 0.05 else '不显著'}")

# 多重检验校正：Bonferroni 方法
m = 100  # 同时检验 100 个因子
p_values = np.random.uniform(0, 1, m)  # 模拟 p 值
p_values[0] = 0.001   # 假设前两个因子是真正有效的
p_values[1] = 0.0003

alpha = 0.05
bonferroni_threshold = alpha / m
significant_before = np.sum(p_values < alpha)
significant_after = np.sum(p_values < bonferroni_threshold)

print(f"\n--- 多重检验校正 ---")
print(f"校正前显著因子数: {significant_before}")
print(f"Bonferroni 校正后显著因子数: {significant_after}")
print(f"校正后显著性阈值: {bonferroni_threshold:.6f}")
```

## 统计显著性的确定方法

统计假设检验用于判断数据是否具有统计显著性，以及某一现象是否可以被解释为纯粹偶然的副产品。统计显著性是对零假设的判断，零假设认为结果仅因偶然因素而存在。拒绝零假设是数据被认为具有统计显著性的必要条件。

确定统计显著性的完整流程为：

1. 建立零假设 $H_0$ 和备择假设 $H_1$
2. 选择显著性水平 $\alpha$
3. 选择适当的检验统计量（Z、t、$\chi^2$、F 等）
4. 计算检验统计量的值
5. 确定 p 值或比较检验统计量与临界值
6. 若 $p \leq \alpha$，则结果具有统计显著性

### 统计显著性 vs 经济显著性

在量化金融中，统计显著性和经济显著性是两个不同的概念。一个策略可能在统计上显著但在经济上不显著（考虑交易成本后利润为负），反之亦然。因此，应同时评估 p 值（统计显著性）和效应量/经济影响（经济显著性）。

## 什么是p值？

p值是一种测量观察到的差异仅由随机因素造成的概率的指标。当p值足够小（5%或更低）时，结果就不易用偶然因素解释，零假设可以被拒绝。当p值较大时，数据可以被视为与零假设一致。

需要注意的是，**p 值不是零假设为真的概率**。p 值的正确解释为：在零假设为真的条件下，观察到当前或更极端结果的概率。

## 统计显著性的用途

统计显著性常用于测试新医疗产品的有效性，包括药物、设备和疫苗。公开的统计显著性报告也向投资者提供关于公司新产品发布成功情况的信息。制药公司的股票价格常因新产品统计显著性的公告而受到显著影响。[4]

在量化金融中，统计显著性还用于：

- 评估 alpha 因子和交易信号的有效性
- 进行事件研究分析（如并购公告对股价的影响）
- 验证风险模型的准确性（如 VaR 回测）
- 检验市场效率假说

## 结论

统计显著性是假设检验的结果，得出p值或两个或多个变量因为非随机原因所引起的可能性。通常情况下，p值为5%被视为界限。p值越低，数据集结果的统计显著性就越高。

这种形式的检验常用于评估药物试验，投资者，尤其是那些希望评估推出新产品公司的投资者，也将受益于此。对于量化金融从业者而言，理解统计显著性的本质、效应量的重要性以及多重检验问题，是避免"过拟合陷阱"和"p-hacking"的关键。

## 参考文献

[1] Tenny, Steven and Abdelgawad, Ibrahim. "[Statistical Significance.](https://www.ncbi.nlm.nih.gov/books/NBK459346/)" StatPearls Publishing, 2023.

[2] American Diabetes Association. "[Efficacy and Safety of Fast-Acting Aspart Compared With Insulin Aspart, Both in Combination With Insulin Degludec, in Children and Adolescents With Type 1 Diabetes: The Onset 7 Trial](https://care.diabetesjournals.org/content/42/7/1255)."

[3] Hwang, Thomas J. "[Stock Market Returns and Clinical Trial Results of Investigational Compounds: An Event Study Analysis of Large Biopharmaceutical Companies.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3737210/)" PLOS ONE, 2013.

[4] Rothenstein, Jeffrey, et al. "[Company Stock Prices Before and After Public Announcements Related to Oncology Drugs.](https://academic.oup.com/jnci/article/103/20/1507/904625)" Journal of the National Cancer Institute, vol. 103, no. 20, October 2011, pp. 1507-1512.

## 关于LLMQuant
LLMQuant是由一群来自世界顶尖高校和量化金融从业人员组成的前沿社区，致力于探索人工智能（AI）与量化（Quant）领域的无限可能。我们的团队成员来自剑桥大学、牛津大学、哈佛大学、苏黎世联邦理工学院、北京大学、中科大等世界知名高校，外部顾问来自Microsoft、HSBC、Citadel、Man Group、Citi、Jump Trading、国内顶尖私募等一流企业。
