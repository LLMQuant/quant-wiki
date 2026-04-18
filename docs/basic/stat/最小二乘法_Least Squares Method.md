![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

# 什么是最小二乘法？

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

最小二乘法是一种数学回归分析方法，用于确定一组数据的最佳拟合线，直观展示数据点之间的关系。每个数据点代表一个已知自变量与一个未知因变量之间的关系。统计学家和交易者常用这种方法来识别交易机会和趋势。

### 关键要点

- 最小二乘法是一种统计程序，用于找到数据点的最佳拟合。
- 该方法通过最小化数据点与拟合曲线之间偏差或残差的总和来工作。
- 最小二乘回归用于预测因变量的行为。
- 最小二乘法为研究数据点之间最佳拟合线的定位提供了整体 rationale。
- 交易者和分析师可以利用最小二乘法识别交易机会及经济或金融趋势。

## 理解最小二乘法

最小二乘法是一种回归分析形式，为研究的数据点之间最佳拟合线的定位提供了整体依据。它以一组使用两个变量的数据点开始，这些数据点绘制在以x轴和y轴为基础的图表上。交易者和分析师可以将此作为工具，以准确识别市场中的牛市和熊市趋势以及潜在交易机会。

此方法最常用的应用有时称为线性或普通线性回归。它旨在创建一条直线，该直线最小化由于相关方程结果而产生的误差平方和，例如，观察值与基于该模型预期值之间差异产生的平方残差。

例如，分析师可能使用最小二乘法生成一条最佳拟合线，以解释自变量与因变量之间的潜在关系。根据最小二乘法确定的最佳拟合线的方程展示了数据点之间的关系。

如果数据表现出两个变量之间的倾斜关系，将产生一条最小二乘回归线。这条线最小化数据点到回归线的竖直距离。"最小二乘"的名称来源于其所造成的误差平方和最小，也称为方差。另一方面，非线性最小二乘问题没有封闭解，通常通过迭代求解。

**重要提示：** 在回归分析中，因变量在竖直的y轴上表示，而自变量在水平的x轴上表示。这些分类形成最佳拟合线的方程，该方程由最小二乘法确定。

## 最小二乘法的数学推导

最小二乘法的核心目标是找到参数 $\beta_0$（截距）和 $\beta_1$（斜率），使得残差平方和（RSS）最小：

$$ RSS = \sum_{i=1}^{n}(y_i - \hat{y}_i)^2 = \sum_{i=1}^{n}(y_i - \beta_0 - \beta_1 x_i)^2 $$

对 $\beta_0$ 和 $\beta_1$ 分别求偏导并令其等于零：

$$ \frac{\partial RSS}{\partial \beta_0} = -2\sum_{i=1}^{n}(y_i - \beta_0 - \beta_1 x_i) = 0 $$

$$ \frac{\partial RSS}{\partial \beta_1} = -2\sum_{i=1}^{n}x_i(y_i - \beta_0 - \beta_1 x_i) = 0 $$

解这个方程组，得到正规方程（Normal Equations）的解：

$$ \hat{\beta}_1 = \frac{n\sum x_i y_i - \sum x_i \sum y_i}{n\sum x_i^2 - (\sum x_i)^2} = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sum(x_i - \bar{x})^2} $$

$$ \hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x} $$

其中 $\bar{x}$ 和 $\bar{y}$ 分别为 $x$ 和 $y$ 的样本均值。

### 矩阵形式（多元情形）

对于多元线性回归 $\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\epsilon}$，最小二乘解的矩阵形式为：

$$ \hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y} $$

这要求 $\mathbf{X}^T\mathbf{X}$ 是可逆的（即自变量之间不存在完全的线性相关）。当存在多重共线性时，$\mathbf{X}^T\mathbf{X}$ 接近奇异，参数估计将变得不稳定。

### 参数估计的统计性质

在经典假设下，OLS估计量具有以下优良性质（Gauss-Markov定理）：

1. **无偏性**：$E[\hat{\boldsymbol{\beta}}] = \boldsymbol{\beta}$
2. **最优性**：在所有线性无偏估计量中，OLS估计量的方差最小（BLUE: Best Linear Unbiased Estimator）
3. **一致性**：随着样本量增大，$\hat{\boldsymbol{\beta}}$ 趋近于真实值 $\boldsymbol{\beta}$

参数的标准误为：

$$ SE(\hat{\beta}_1) = \sqrt{\frac{\hat{\sigma}^2}{\sum(x_i - \bar{x})^2}} $$

其中 $\hat{\sigma}^2 = \frac{RSS}{n-2}$ 为残差方差的无偏估计。

## 最小二乘法的优缺点

使用最小二乘法找出最佳拟合线是最有效的方法。但交易者和分析师可能会遇到一些问题，因为这并不是万无一失的方法。以下列出了使用此方法的一些优缺点。

使用该方法的主要优点之一是它易于应用和理解。这是因为它只使用两个变量（一个在x轴上，一个在y轴上），并突出了它们之间的最佳关系。

投资者和分析师可以通过分析过去的表现来使用最小二乘法，并对未来经济和股市趋势做出预测。因此，它可以作为决策工具。

最小二乘法的主要缺陷在于所使用的数据。它只能突出两个变量之间的关系，因此不考虑其他变量。如果存在任何离群值，结果将发生偏差。

#### 优点

- 易于应用和理解
- 突出两个变量之间的关系
- 可用于预测未来表现
- 具有坚实的数学理论支撑（Gauss-Markov定理）
- 在经典假设满足时是最优的线性无偏估计

#### 缺点

- 仅突出两个变量之间的关系（简单线性回归情形）
- 不考虑离群值，对异常值极为敏感
- 假设误差方差恒定（同方差性），违反时估计效率降低
- 假设误差服从正态分布，实际金融数据常具有厚尾特征

**注意：** 最佳拟合线的方程可以由计算机软件模型确定，这些模型包括分析的输出摘要，其中的系数和摘要输出解释了被测试变量之间的依赖关系。

### 最小二乘法的变体与扩展

当经典OLS的假设不满足时，可使用以下变体：

| 方法 | 适用场景 | 核心思想 |
|------|---------|---------|
| 加权最小二乘法（WLS） | 异方差性 | 对不同观测赋予不同权重 |
| 广义最小二乘法（GLS） | 误差相关或异方差 | 利用误差协方差矩阵校正 |
| 岭回归（Ridge Regression） | 多重共线性 | 添加 $L_2$ 正则化项 $\lambda\|\boldsymbol{\beta}\|_2^2$ |
| LASSO回归 | 变量选择 + 正则化 | 添加 $L_1$ 正则化项 $\lambda\|\boldsymbol{\beta}\|_1$ |
| 弹性网络（Elastic Net） | 兼顾Ridge和LASSO | 同时使用 $L_1$ 和 $L_2$ 正则化 |
| 稳健回归（Robust Regression） | 存在离群值 | 使用Huber损失等替代平方损失 |

## Python 实战：最小二乘法

以下是使用 Python 实现最小二乘法的完整示例，包括手动推导和库函数两种方式：

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 生成示例数据：股票收益率与指数收益率
np.random.seed(42)
n = 50
index_returns = np.random.normal(0.001, 0.02, n)  # 指数日收益率
stock_returns = 0.5 + 1.2 * index_returns + np.random.normal(0, 0.01, n)  # Beta=1.2

# ===== 手动实现最小二乘法 =====
x = index_returns
y = stock_returns
x_mean = np.mean(x)
y_mean = np.mean(y)

# 计算斜率和截距
beta_1 = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
beta_0 = y_mean - beta_1 * x_mean

print(f"手动计算:")
print(f"  截距 (β₀) = {beta_0:.6f}")
print(f"  斜率 (β₁) = {beta_1:.4f}")

# 计算 R²
y_pred = beta_0 + beta_1 * x
SS_res = np.sum((y - y_pred) ** 2)
SS_tot = np.sum((y - y_mean) ** 2)
R2 = 1 - SS_res / SS_tot
print(f"  R² = {R2:.4f}")

# 计算标准误
sigma2 = SS_res / (n - 2)
SE_beta1 = np.sqrt(sigma2 / np.sum((x - x_mean) ** 2))
t_stat = beta_1 / SE_beta1
print(f"  β₁ 标准误 = {SE_beta1:.4f}")
print(f"  t 统计量 = {t_stat:.4f}")

# ===== 使用 sklearn =====
model = LinearRegression()
model.fit(x.reshape(-1, 1), y)
print(f"\nsklearn 计算:")
print(f"  截距 = {model.intercept_:.6f}")
print(f"  斜率 = {model.coef_[0]:.4f}")

# ===== 可视化 =====
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 左图：回归拟合
axes[0].scatter(x, y, alpha=0.6, label='数据点')
x_line = np.linspace(x.min(), x.max(), 100)
axes[0].plot(x_line, beta_0 + beta_1 * x_line, 'r-', linewidth=2,
             label=f'OLS拟合线: y={beta_0:.4f}+{beta_1:.2f}x')
axes[0].set_xlabel('指数收益率')
axes[0].set_ylabel('股票收益率')
axes[0].set_title(f'最小二乘回归 (R²={R2:.3f})')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# 右图：残差分析
residuals = y - y_pred
axes[1].scatter(y_pred, residuals, alpha=0.6)
axes[1].axhline(y=0, color='r', linestyle='--')
axes[1].set_xlabel('预测值')
axes[1].set_ylabel('残差')
axes[1].set_title('残差图（检验同方差性）')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

### 岭回归与LASSO的Python实现

```python
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from sklearn.preprocessing import StandardScaler

# 生成多元数据（含共线性）
np.random.seed(42)
n = 100
X = np.random.randn(n, 5)
X[:, 4] = X[:, 0] * 0.9 + np.random.randn(n) * 0.1  # 构造共线性
y = 3 * X[:, 0] + 2 * X[:, 1] - 1.5 * X[:, 2] + np.random.randn(n) * 0.5

# 标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# OLS、Ridge、LASSO 对比
models = {
    'OLS': LinearRegression(),
    'Ridge (α=1.0)': Ridge(alpha=1.0),
    'LASSO (α=0.1)': Lasso(alpha=0.1),
    'ElasticNet': ElasticNet(alpha=0.1, l1_ratio=0.5)
}

print("各模型系数对比:")
print(f"{'模型':<20} {'β₁':>8} {'β₂':>8} {'β₃':>8} {'β₄':>8} {'β₅':>8}")
print("-" * 60)
for name, model in models.items():
    model.fit(X_scaled, y)
    coefs = model.coef_
    print(f"{name:<20} {coefs[0]:>8.3f} {coefs[1]:>8.3f} {coefs[2]:>8.3f} "
          f"{coefs[3]:>8.3f} {coefs[4]:>8.3f}")
```

## 最小二乘法的示例

以下是一个假设的例子，展示最小二乘法如何工作。假设有一位分析师希望测试一家公司的股票收益与该股票为组成部分的指数收益之间的关系。在这个例子中，分析师试图测试股票收益对指数收益的依赖性。

为实现这一目标，所有收益都绘制在图表上。指数收益被指定为自变量，而股票收益为因变量。最佳拟合线为分析师提供了一条显示因变量与自变量之间关系的线。

### 手算示例

假设我们有以下5个数据点：

| 指数收益 (x) | 股票收益 (y) |
|-------------|-------------|
| 1% | 1.5% |
| 2% | 2.8% |
| 3% | 3.2% |
| 4% | 4.9% |
| 5% | 5.1% |

**计算步骤**：

1. 计算均值：$\bar{x} = 3$，$\bar{y} = 3.5$
2. 计算 $\sum(x_i - \bar{x})(y_i - \bar{y}) = (-2)(-2) + (-1)(-0.7) + (0)(-0.3) + (1)(1.4) + (2)(1.6) = 4 + 0.7 + 0 + 1.4 + 3.2 = 9.3$
3. 计算 $\sum(x_i - \bar{x})^2 = 4 + 1 + 0 + 1 + 4 = 10$
4. 斜率：$\hat{\beta}_1 = 9.3 / 10 = 0.93$
5. 截距：$\hat{\beta}_0 = 3.5 - 0.93 \times 3 = 0.71$

因此，回归方程为 $\hat{y} = 0.71 + 0.93x$，意味着指数每上涨1%，该股票预期上涨约0.93%（即Beta约为0.93）。

## 最小二乘法是什么？

最小二乘法是一种数学技术，使分析师能够确定绘制数据点图表时最适合的曲线。它被广泛用于简化散点图的解释，并与回归分析相关联。如今，最小二乘法通常作为大多数统计软件程序的一部分使用。

## 最小二乘法在金融中的应用

最小二乘法被广泛应用于包括金融和投资在内的多个领域。对于金融分析师而言，该方法可以帮助量化两个或多个变量之间的关系，例如股票的股价与每股收益（EPS）之间的关系。通过进行这种类型的分析，投资者通常试图预测股票价格或其他因素的未来趋势。

**金融领域的具体应用**：

- **Beta系数估计**：通过回归股票收益率对市场收益率，计算CAPM模型中的Beta值。
- **因子模型校准**：使用OLS拟合Fama-French多因子模型的因子载荷。
- **收益率曲线拟合**：通过最小二乘法拟合Nelson-Siegel模型参数。
- **对冲比率计算**：通过回归分析确定期货对冲的最优比率。
- **时间序列预测**：在ARIMA等模型中，参数估计的核心步骤之一就是最小二乘法。

## 最小二乘法的一个例子

考虑一位投资者是否应该投资于一家金矿公司的情况。投资者可能希望了解该公司的股价对黄金市场价格变化的敏感性。为了研究这一点，投资者可以使用最小二乘法在散点图上绘制这两个变量之间的关系。该分析可以帮助投资者预测在黄金价格任何给定的上涨或下跌情况下，股票价格可能上升或下降的程度。

## 谁首次发现最小二乘法？

尽管最小二乘法的发明者仍有争议，德国数学家卡尔·弗里德里希·高斯声称他在1795年发明了这一理论。[1] 法国数学家阿德里安-马里·勒让德于1805年首次发表了该方法。高斯随后在1809年的著作中详细阐述了这一方法，并将其与正态分布理论相结合，奠定了现代回归分析的基础。

## 结论

交易者和分析师有许多工具可用来预测市场和经济的未来表现。最小二乘法是一种回归分析形式，许多技术分析师使用它来识别交易机会和市场趋势。它使用两个变量绘制在图表上，以展示它们之间的关系。

作为量化金融的基石方法，最小二乘法不仅是理解更复杂统计模型（如广义线性模型、时间序列模型、机器学习回归算法）的基础，也是日常数据分析和策略研发中最常用的工具之一。深入理解其数学原理、统计性质和适用条件，对于量化从业者而言至关重要。

## 参考文献

[1] Stigler M., Stephen. "Gauss and the Invention of Least Squares," The Annals of Statistics, vol. 9, no, 3, May 1982, Page 465.

## 关于LLMQuant
LLMQuant是由一群来自世界顶尖高校和量化金融从业人员组成的前沿社区，致力于探索人工智能（AI）与量化（Quant）领域的无限可能。我们的团队成员来自剑桥大学、牛津大学、哈佛大学、苏黎世联邦理工学院、北京大学、中科大等世界知名高校，外部顾问来自Microsoft、HSBC、Citadel、Man Group、Citi、Jump Trading、国内顶尖私募等一流企业。