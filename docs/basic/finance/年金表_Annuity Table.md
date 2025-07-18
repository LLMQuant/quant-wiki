![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# 什么是年金表？
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)
年金表是一种用于确定年金或其他结构化支付系列现值的工具。这种工具通常被会计师、精算师和其他保险人员使用，它考虑了投入年金的金额及其存在的时间，以确定应支付给年金购买者或年金领取人的金额。

任何未来年金金额的现值也可以通过金融计算器或专门设计的软件进行计算。

### 关键要点

- 年金表是用于确定年金现值的工具。
- 年金表通过将折现率应用于未来支付款项来计算年金的现值。
- 年金表使用折现率和支付期数来给出适当的因子。
- 使用年金表，您将把定期支付的金额与给定因子相乘。

## 年金表的工作原理

年金表提供一个因子，该因子基于时间和折现率（利率），通过将年金支付乘以该因子即可确定其现值。例如，如果预计利率为3%，则可使用年金表计算一项在15年内每年支付10,000美元的年金的现值。

**重要提示：** 根据货币时间价值的概念，当前一次性支付的金额比未来收到相同金额的价值更高。

今天拥有10,000美元比未来10年每年收到1,000美元更有价值，因为这笔钱可以投资以获取利息。在10年期结束时，10,000美元的现值将超过所有年度支付的总和，即使按照相同的利率进行投资。

## 年金表与年金的现值

普通年金的现值公式（与到期年金不同）如下：

$$ \begin{aligned}&\text{P} =\text{PMT}\times\frac{ 1 - (1 + r) ^ -n}{r}\\&\textbf{其中：}\\&\text{P} = \text{年金流的现值}\\&\text{PMT} =\text{每笔年金支付的金额}\\&r = \text{利率（即折现率）}\\&n = \text{支付期数}\end{aligned} $$

假设某人有机会获得一项在未来25年每年支付50,000美元的年金，折现率为6%，或者获得650,000美元的一次性付款。他需要确定更合理的选择。使用上述公式，年金的现值为：

$$ \begin{aligned}&\text{PVA} = \$50,000 \times \frac{1 - (1 + 0.06) ^ -25}{0.06} = \$639,168\\&\textbf{其中：}\\&\text{PVA}=\text{年金的现值}\end{aligned} $$

根据这些信息，从时间调整的角度来看，这项年金的价值低于10,832美元，因此该人应选择一次性支付。

请注意，这个公式适用于普通年金，支付是在每个期末进行。在上述例子中，每笔50,000美元的支付将在每年的年底进行，持续25年。对于到期年金，支付是在期初进行。若要计算到期年金的现值，则在上述公式的基础上乘以（1 + r）的因子：

$$ \begin{aligned}&\text{P} = \text{PMT} \times\left(\frac{1 - (1 + r) ^ -n}{r}\right) \times (1 + r)\end{aligned} $$

如果上述例子是一个到期年金，则其价值为：

$$ \begin{aligned}&\text{P}= \$50,000\\&\quad \times\left( \frac{1 - (1 + 0.06) ^ -25}{0.06}\right)\times (1 + 0.06) = \$677,518\end{aligned} $$

在这种情况下，该人应选择到期年金，因为其价值比一次性付款高出27,518美元。

与通过上述公式计算相比，您也可以使用年金表。年金表简化了计算，自动为公式的后一半提供一个因子。例如，普通年金表将给您一个数字（称为因子），该因子是为公式中的（1 - (1 + r) ^ - n） / r）部分预设好的。

因子的确定依赖于利率（公式中的r）和支付期数（公式中的n）。在年金表中，期数通常在左侧列出来，利率通常在顶端行列出。只需选择正确的利率和期数，便可在交集单元格找到因子。该因子随后与年金支付的美元金额相乘，以得出普通年金的现值。

以下是一个普通年金现值表的示例：

|n|1%|2%|3%|4%|5%|6%
|---|---|---|---|---|---|---|
|1|0.9901|0.9804|0.9709|0.9615|0.9524|0.9434
|2|1.9704|1.9416|1.9135|1.8861|1.8594|1.8334
|3|2.9410|2.8839|2.8286|2.7751|2.7233|2.6730
|4|3.9020|3.8077|3.7171|3.6299|3.5460|3.4651
|5|4.8534|4.7135|4.5797|4.4518|4.3295|4.2124
|10|9.4713|8.9826|8.5302|8.1109|7.7217|7.3601
|15|13.8651|12.8493|11.9380|11.1184|10.3797|9.7123
|20|18.0456|16.3514|14.8775|13.5903|12.4622|11.4699
|25|22.0232|19.5235|17.4132|15.6221|14.0939|12.7834

如果我们拿上面提到的6%利率和25年期的例子，您会发现因子= 12.7834。如果将这个年金表中的12.7834因子乘以50,000美元的支付金额，您将得到639,170美元，几乎与前面公式计算得到的639,168美元相同。数字之间的微小差异反映了年金表中的12.7834数字经过四舍五入。

对于到期年金还有一个单独的表，该表会根据第二个公式给出正确的因子。

## 什么是年金？

年金是一种保险合同，提供收入流，通常是在退休期间。年金可能是固定的、可变的或指数化的。它有两个阶段：首先是积累（储蓄）阶段，然后是支付（收入）阶段。支付可能是立即的或延迟的。

## 普通年金与到期年金之间的区别是什么？

普通年金是在年金期末生成支付，而到期年金是在支付期开始时期望或支付的年金。

## 彩票中奖者能否使用年金表？

彩票中奖者可以使用年金表来确定今天一次性领取彩票奖金，或是选择多年的分期支付哪种选择更具经济意义。然而，彩票奖金是一种相对罕见的年金形式。更常见的是，年金是一种投资类型，用于为个人提供稳定的养老金收入。

## 总结

年金表主要由会计、保险或其他金融专业人士使用，以确定年金的现值。它考虑了投入年金的金额及其存在的时长，因此便于决定应支付给年金购买者或年金领取人的金额。
## 关于LLMQuant
LLMQuant是由一群来自世界顶尖高校和量化金融从业人员组成的前沿社区，致力于探索人工智能（AI）与量化（Quant）领域的无限可能。我们的团队成员来自剑桥大学、牛津大学、哈佛大学、苏黎世联邦理工学院、北京大学、中科大等世界知名高校，外部顾问来自Microsoft、HSBC、Citadel、Man Group、Citi、Jump Trading、国内顶尖私募等一流企业。