![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# What Is Covariance?
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

Covariance is a statistical tool that measures the directional relationship between the returns of two assets. A positive covariance indicates that asset returns move together, while a negative covariance means they move inversely.

Covariance can be calculated by analyzing the deviations of returns from their expected values (standard deviations from the mean) or by multiplying the correlation between two random variables by each variable's standard deviation.

### Key Takeaways

- Covariance is a statistical tool used to determine the directional relationship between two random variables.
- When two stocks tend to move in the same direction, they exhibit positive covariance; when they tend to move in opposite directions, the covariance is negative.
- Covariance differs from the correlation coefficient, which measures the strength of the associative relationship.
- Covariance is an important tool in Modern Portfolio Theory (MPT) for determining which securities to include in a portfolio.
- Risk and volatility in a portfolio can be reduced by pairing assets with negative covariance.

## Understanding Covariance

Covariance evaluates how the means of two random variables move together. For example, if Stock A's return rises when Stock B's return rises, and the same relationship holds when both stocks' returns decline, then these stocks are said to have positive covariance. In finance, covariance is used to compute diversification in securities holdings.

When an analyst has price information from selected stocks or funds, covariance can be computed using the following formula:

$$ \begin{aligned}&\text{Covariance} = \sum \frac{ ( \text{Return}_{abc} - \text{Average}_{abc} ) \times ( \text{Return}_{xyz} - \text{Average}_{xyz} ) }{ \text{Sample Size} - 1 } \\&\textbf{where:} \\&\text{Return}_{abc} = \text{Daily return of stock ABC} \\&\text{Average}_{abc} = \text{Average return of ABC over the period} \\&\text{Return}_{xyz} = \text{Daily return of stock XYZ} \\&\text{Average}_{xyz} = \text{Average return of XYZ over the period} \\&\text{Sample Size} = \text{Number of days sampled} \\\end{aligned} $$

## Types of Covariance

The covariance equation determines the direction of the relationship between two variables -- in other words, whether they tend to move in the same direction or in opposite directions. A positive or negative covariance value establishes this relationship.

A positive covariance between two variables indicates that they tend to be high or low at the same time. When Stock A is above its average, Stock B tends to be above its average as well, and vice versa. When plotted on a two-dimensional graph, data points tend to slope upward.

A negative covariance indicates an inverse relationship between the two variables. When Stock A's value falls below its average, Stock B's value tends to be above its average, and vice versa.

## Applications of Covariance

Covariance has significant applications in finance and Modern Portfolio Theory (MPT). For example, in the Capital Asset Pricing Model (CAPM), which is used to calculate the expected return of an asset, covariance serves as a key variable in the formula for beta. Beta in CAPM measures a security's volatility, or systematic risk, relative to the overall market -- a practical metric that leverages covariance to gauge an investor's risk exposure to a particular security.

Additionally, portfolio theory uses covariance to statistically reduce the overall risk of a portfolio through covariance-driven diversification, protecting it against volatility.

**Tip:** Holding financial assets with similar returns does not provide much diversification. Therefore, a diversified portfolio will typically contain a mix of financial assets with different covariances.

## Covariance vs. Variance

Covariance is related to variance, which is a statistical measure of the spread of data points in a dataset. Both variance and covariance measure how data points are distributed around a computed mean. However, variance measures the spread of data along a single axis, while covariance examines the directional relationship between two variables.

In a financial context, covariance is used to study the performance relationship between different investments. Positive covariance indicates that two assets tend to perform well simultaneously, while negative covariance suggests they tend to move in opposite directions. Investors may seek assets with negative covariance to help achieve diversification.

## Covariance vs. Correlation

Covariance is also distinct from correlation, another statistical metric commonly used to measure the relationship between two variables. While covariance measures the direction of the relationship between two variables, correlation measures the strength of that relationship. It is typically expressed through a correlation coefficient, which ranges from -1 to +1.

**Important:** While covariance measures the directional relationship between two assets, it does not indicate the strength of the relationship. The correlation coefficient is the more appropriate measure of that strength.

A correlation near +1 (positive correlation) or -1 (negative correlation) indicates a strong relationship. A coefficient near zero suggests a weak relationship between the two variables.

## Example of Covariance Calculation

The capital Greek letter sigma is used to represent the sum of all calculations. Each day's calculation must be performed and the results aggregated. For example, to calculate the covariance between two stocks, assume you have four days of stock price data using the following formula:

$$ \begin{aligned}&\text{Covariance} = \sum \frac{ ( \text{Ret}_{abc} - \text{Avg}_{abc} ) \times ( \text{Ret}_{xyz} - \text{Avg}_{xyz} ) }{ \text{Sample Size} - 1 } \\\end{aligned} $$

|Day|ABC|XYZ|
|---|---|---|
|1|1.2%|3.1%|
|2|1.8%|4.2%|
|3|2.2%|5.0%|
|4|1.5%|4.2%|

Find the average return for ABC (1.675%) and XYZ (4.125%), subtract these from the corresponding daily values, and multiply. Perform this calculation for each day:

$$ \begin{aligned}&\text{Day 1} = (1.2\% - 1.675\%) \times (3.1\% - 4.125\%) = 0.487 \\\end{aligned} $$

$$ \begin{aligned}&\text{Day 2} = (1.8\% - 1.675\%) * (4.2\% - 4.125\%) = 0.009 \\\end{aligned} $$

$$ \begin{aligned}&\text{Day 3} = (2.2\% - 1.675\%) * (5.0\% - 4.125\%) = 0.459 \\\end{aligned} $$

$$ \begin{aligned}&\text{Day 4} = (1.5\% - 1.675\%) * (4.2\% - 4.125\%) = -0.013 \\\end{aligned} $$

Sum the daily results:

$$ \begin{aligned}&0.487 + 0.009 + 0.459 - 0.013 = 0.943 \\\end{aligned} $$

The sample size is four, so subtract one from four and divide the preceding result by this number:

$$ \begin{aligned}&\frac{ 0.943 }{ 3 } = .314 \\\end{aligned} $$

The covariance for this sample is 0.314. The positive value indicates that the two stocks' returns move in the same direction.

## What Does a Covariance of Zero Mean?

A covariance of zero indicates that there is no clear directional relationship between the variables being measured. In other words, a high value in one stock is equally likely to be paired with either a high or low value in the other.

## What Is the Difference Between Covariance and Variance?

Covariance and variance are both used to measure the distribution of data points in a dataset. However, variance is typically used with a single variable and indicates how closely data points cluster around the mean. Covariance measures the directional relationship between two variables. A positive covariance means both variables tend to be high or low simultaneously; a negative covariance indicates that when one variable is high, the other tends to be low.

## What Is the Difference Between Covariance and Correlation?

Covariance measures the direction of the relationship between two variables, while correlation measures the strength of that relationship. Both covariance and correlation are positive when the variables move in the same direction and negative when they move in opposite directions. However, the correlation coefficient always ranges from -1 to +1, with extreme values indicating a strong relationship.

## How Is Covariance Calculated?

For a set of data points with two variables, covariance is measured by taking the difference between each variable and its mean. These differences are then multiplied and averaged across all data points. In mathematical notation:

Covariance = Sum[ ( Return_abc - Average_abc ) * ( Return_xyz - Average_xyz ) ] / [ Sample Size - 1 ]

## Conclusion

Covariance is an important statistical metric for comparing the relationships among multiple variables. In investing, covariance is used to identify assets that can help diversify a portfolio.

## About LLMQuant

LLMQuant is a cutting-edge community composed of professionals from top global universities and the quantitative finance industry, dedicated to exploring the limitless possibilities at the intersection of artificial intelligence (AI) and quantitative finance (Quant). Our team members hail from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other prestigious institutions, with external advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and leading proprietary trading firms.
