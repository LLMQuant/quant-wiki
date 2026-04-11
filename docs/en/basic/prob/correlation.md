![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# What Is Correlation?
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

In the finance and investment industry, correlation is a statistic that measures the degree to which two securities move in relation to each other. Correlation is used in advanced portfolio management and is computed as the correlation coefficient, which must have a value between -1.0 and +1.0.

### Key Takeaways

- Correlation is a statistic that measures the degree to which two variables move in relation to each other.
- In finance, correlation can measure the movement of a stock relative to a benchmark index such as the S&P 500.
- Correlation is closely related to diversification -- the concept of mitigating certain types of risk by investing in uncorrelated assets.
- Correlation measures association but cannot indicate whether x causes y, whether y causes x, or whether the association is driven by a third factor.
- Correlation is most easily identified using scatter plots, particularly when variables have a nonlinear but still strong relationship.

## What Correlation Can Tell You

Correlation reveals the strength of the relationship between two variables, expressed numerically as the correlation coefficient. Correlation coefficient values range between -1.0 and 1.0.

A perfect positive correlation means the coefficient is exactly 1 -- when one security moves up or down, the other moves in lockstep in the same direction. A perfect negative correlation means two assets move in opposite directions, while a zero correlation implies no linear relationship at all.

For example, large-cap mutual funds generally have a high positive correlation with the S&P 500 index, approaching 1. Small-cap stocks tend to be positively correlated with the S&P, but to a lesser degree -- around 0.8.

However, put option prices and their underlying stock prices tend to be negatively correlated. A put option gives the owner the right (but not the obligation) to sell a specified quantity of the underlying security at a predetermined price within a specified time frame.

When the underlying stock price falls, put option contracts become more profitable. In other words, as the stock price rises, put option prices decline -- a direct, high-magnitude negative correlation.

## How to Calculate Correlation

There are several methods for calculating correlation. The most common, discussed here, is the Pearson product-moment correlation. The Pearson method measures the linear relationship between two variables and can be applied to any data set with a finite covariance matrix. Here are the steps for calculating correlation.

**Important:** To avoid complex manual calculations, consider using the CORREL function in Excel.

Using the Pearson product-moment method, the correlation coefficient r is found with the following formula:

$$\begin{aligned}
&r = \frac { n \times ( \sum (X, Y) - ( \sum (X) \times \sum (Y) ) ) }{ \sqrt { ( n \times \sum (X ^ 2) - \sum (X) ^ 2 ) \times ( n \times \sum( Y ^ 2 ) - \sum (Y) ^ 2 ) } } \\
&\textbf{where:}\\
&r=\text{correlation coefficient}\\
&n=\text{number of observations}
\end{aligned}$$

## Example of Correlation

Investment managers, traders, and analysts find calculating correlation critically important, because the risk-reduction benefits of diversification depend on this statistic. Financial spreadsheets and software can compute correlation values quickly.

As a hypothetical example, suppose an analyst needs to calculate the correlation for the following two data sets:

X: (41, 19, 23, 40, 55, 57, 33)

Y: (94, 60, 74, 71, 82, 76, 61)

Finding the correlation involves three steps. First, sum all X values to find SUM(X), sum all Y values to find SUM(Y), and multiply each X value by its corresponding Y value, then sum them to find SUM(X,Y):

SUM(X) = (41 + 19 + 23 + 40 + 55 + 57 + 33) = 268

SUM(Y) = (94 + 60 + 74 + 71 + 82 + 76 + 61) = 518

SUM(X,Y) = (41 x 94) + (19 x 60) + (23 x 74) + ... (33 x 61) = 20,391

Next, square each X value and sum them all to find SUM(X^2). Do the same for the Y values:

SUM(X^2) = (41^2) + (19^2) + (23^2) + ... (33^2) = 11,534

SUM(Y^2) = (94^2) + (60^2) + (74^2) + ... (61^2) = 39,174

With seven observations (n), the correlation coefficient r can be calculated using the formula above.

In this example, the correlation is:

r = 0.54

## Correlation and Portfolio Diversification

In investing, correlation is most significant in the context of diversified portfolios. Investors seeking to reduce risk can do so by investing in uncorrelated assets. For example, consider an investor who owns airline stocks. If the airline industry is found to have low correlation with the social media industry, the investor might choose to invest in social media stocks, knowing that a negative impact on one industry is unlikely to affect the other.

This is often the approach taken when considering cross-asset-class investments. Stocks, bonds, precious metals, real estate, cryptocurrencies, commodities, and other investment types have varying relationships with one another. While some may be highly correlated, others that are uncorrelated can serve as hedges to diversify risk.

**Note:** Risk that can be diversified away is called unsystematic risk. This type of risk is specific to a company, industry, or asset class. Investing in different assets can reduce a portfolio's correlation and reduce exposure to unsystematic risk.

## Special Considerations

Correlation is typically driven by and related to other statistical considerations. When analyzing variables statistically, correlation is commonly referenced.

In statistics, the p-value is used to indicate whether study results are statistically significant. It is possible to determine that two variables are correlated, but there may not be sufficient supporting evidence to make a strong claim. A high p-value indicates sufficient evidence to meaningfully conclude that the population correlation coefficient differs from zero.

The simplest way to visualize whether two variables are correlated is to plot them graphically in a scatter plot. Each point on the plot represents a sample item. The x-axis represents one variable being tested, while the y-axis represents the other.

The correlation coefficient between two variables is typically represented graphically as a linear line showing the relationship between them. If two variables are positively correlated, an upward-sloping linear line can be drawn on the scatter plot. If negatively correlated, a downward-sloping line can be drawn. The stronger the relationship, the closer each data point will be to the line.

Scatter plots are particularly useful when analyzing more complex data with potentially changing relationships. For example, two variables may be positively correlated up to a certain point, after which their relationship turns negative. Such nonlinear relationships may be harder to identify using formulas but easier to spot when plotted on a scatter plot.

Finally, density shading or density ellipses on scatter plots can visually depict correlation. These shaded areas show where data points are most concentrated. If the variables are correlated, the density ellipse will typically align with the direction of the linear correlation line. A more circular density ellipse with no clear direction indicates weaker correlation.

Another inherent challenge in statistics is determining whether the relationship between two variables is caused by those variables themselves. Consider the statement:

"Most basketball players are tall. Therefore, if you play basketball, you will become tall."

Clearly, this statement is incorrect. Tall individuals who recognize this advantage may be drawn to basketball because their natural physical abilities suit the sport. However, because height and basketball playing may be positively correlated, statisticians and data scientists must recognize that a strong relationship between two variables could be caused by either one.

## Limitations of Correlation

As with other aspects of statistical analysis, correlation can be misinterpreted. Even when the correlation between two variables appears strong, small sample sizes can produce unreliable results. Conversely, a small sample may indicate no correlation when the two variables are actually related.

Correlation is often distorted by outliers. Correlation only shows how one variable relates to another and may not clearly identify how individual instances or outcomes affect the coefficient.

Correlation can also be misinterpreted if the relationship between two variables is nonlinear. Identifying positive or negative correlations is straightforward, but two variables can still be related in a more complex manner.

## What Is Correlation?

Correlation is a statistical term describing the degree to which two variables move in coordination with each other. If they move in the same direction, they have a positive correlation. If they move in opposite directions, they have a negative correlation.

## Why Is Correlation Important in Finance?

Correlation plays an important role in finance because it is used to forecast future trends and manage portfolio risk. Asset correlations can be easily calculated today using various software programs and online services. Correlation, along with other statistical concepts, plays an important role in the creation and pricing of derivatives and other complex financial instruments.

## What Is an Example of How Correlation Is Used?

Correlation is a widely used concept in modern finance. For example, a trader might use historical correlations to predict whether a company's stock will rise or fall in response to changes in interest rates or commodity prices. Similarly, a portfolio manager might seek to reduce risk by ensuring that the individual assets within a portfolio are not excessively correlated with each other.

## Is Higher Correlation Better?

Investors may have preferences regarding correlation levels in their portfolios. Generally, most investors prefer lower correlations, as this reduces the risk that different assets or securities in a portfolio will be affected by similar market conditions. However, risk-seeking investors or those who wish to concentrate their capital in a specific industry may be willing to accept higher correlations in exchange for greater potential returns.
