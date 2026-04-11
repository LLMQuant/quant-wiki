![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# What Is the Correlation Coefficient?
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

The correlation coefficient is a statistical measure of the strength of the linear relationship between two variables. Its value ranges from -1 to 1. A coefficient of -1 describes a perfect negative (inverse) correlation -- when values in one series rise, those in the other fall, and vice versa. A coefficient of 1 indicates a perfect positive (direct) relationship. A coefficient of 0 indicates no linear relationship.

Correlation coefficients are used in science and finance to assess the degree of association between two variables, factors, or data sets. For example, since high oil prices benefit crude oil producers, one might expect the correlation between oil prices and forward returns on oil stocks to be strongly positive.

However, calculating the correlation coefficient for these variables based on market data reveals that, over longer periods, the correlation is moderate and inconsistent. [1]

### Key Takeaways

- Correlation coefficients are used to assess the strength of the association between data variables.
- The most common is the Pearson correlation coefficient, which measures the strength and direction of the linear relationship between two variables.
- Values always range from -1 (perfect inverse or negative relationship) to 1 (perfect positive relationship). Values at or near zero indicate no linear relationship or very weak correlation.
- The coefficient value needed to indicate a meaningful association depends on the specific application. Statistical significance of a correlation can be calculated from the correlation coefficient and the number of data points in the sample, assuming the population follows a normal distribution.

## Understanding Correlation Coefficients

Different types of correlation coefficients are used to assess correlation based on the properties of the data being compared. By far the most common is the Pearson coefficient (Pearson r), which measures the strength and direction of the linear relationship between two variables. The Pearson coefficient cannot assess nonlinear associations between variables, nor can it distinguish between dependent and independent variables.

The Pearson coefficient uses a mathematical formula to measure how closely the data points of two combined variables (with one series plotted on the x-axis and the corresponding values on the y-axis) align with the line of best fit. The line of best fit can be determined through regression analysis.

The farther the coefficient is from zero -- whether positive or negative -- the better the fit and the stronger the correlation. Values of -1 (negative correlation) and 1 (positive correlation) describe a perfect fit in which all data points lie on a straight line, indicating that the variables are completely correlated.

In other words, the relationship is so predictable that the value of one variable can be determined from the matching value of the other. The closer the coefficient is to zero, the weaker the correlation, until at zero no linear relationship exists at all.

The assessment of correlation strength based on coefficient values varies by application. In physics and chemistry, the coefficient should be below -0.9 or above 0.9 to be considered meaningful, whereas in the social sciences, the threshold may be as lenient as -0.5 to 0.5.

For correlation coefficients obtained from sampling, statistical significance is determined by the p-value, which is calculated from the sample size and the coefficient value.

## Correlation Coefficient Formula

To calculate the Pearson correlation coefficient, first determine the standard deviation of each variable and the covariance between them. The correlation coefficient is the covariance divided by the product of the two variables' standard deviations.

$$ \begin{aligned} &\rho_{xy} = \frac { \text{Cov} ( x, y ) }{ \sigma_x \sigma_y } \\ &\textbf{where:} \\ &\rho_{xy} = \text{Pearson product-moment correlation coefficient} \\ &\text{Cov} ( x, y ) = \text{covariance of variables } x \text{ and } y \\ &\sigma_x = \text{standard deviation of } x \\ &\sigma_y = \text{standard deviation of } y \\ \end{aligned} $$

Standard deviation measures how dispersed data is from its average. Covariance shows whether two variables tend to move in the same direction, while the correlation coefficient measures the strength of that relationship on a standardized scale from -1 to 1.

The formula above can be further expanded to:

$$ \begin{aligned}&r = \frac { n \times ( \sum (X, Y) - ( \sum (X) \times \sum (Y) ) ) }{ \sqrt { ( n \times \sum (X ^ 2) - \sum (X) ^ 2 ) \times ( n \times \sum( Y ^ 2 ) - \sum (Y) ^ 2 ) } } \\&\textbf{where:}\\&r=\text{correlation coefficient}\\&n=\text{number of observations}\end{aligned} $$

## Correlation Statistics and Investing

The correlation coefficient is particularly useful in assessing and managing investment risk. For example, modern portfolio theory holds that diversification can reduce the volatility of portfolio returns, thereby lowering risk. Correlation calculations are also a core component of factor investing -- a strategy that constructs portfolios based on factors associated with excess returns. Additionally, quantitative traders use historical correlations and correlation coefficients to forecast near-term changes in security prices.

## Limitations of the Pearson Correlation Coefficient

As the saying goes, correlation does not imply causation, and the Pearson coefficient cannot determine whether one of the correlated variables is dependent on the other.

The correlation coefficient also cannot show what proportion of the variation in the dependent variable is attributable to the independent variable. This is captured by the coefficient of determination, also known as R-squared, which is simply the square of the correlation coefficient.

The correlation coefficient does not describe the slope of the line of best fit; the slope is determined through least-squares regression analysis.

The Pearson correlation coefficient cannot be used to assess nonlinear associations or associations arising from sample data that does not follow a normal distribution. It can also be distorted by outliers -- data points far removed from the scatter plot's distribution.

These relationships can be analyzed using nonparametric methods such as the Spearman correlation coefficient, the Kendall rank correlation coefficient, or the polyserial correlation coefficient.

## Finding the Correlation Coefficient in Excel

The simplest way to calculate correlation in Excel is to enter the two data series in adjacent columns and use the built-in correlation formula.

If you want to create a correlation matrix across a range of data sets, Excel has a Data Analysis add-in under the Analysis section of the Data tab.

Select the table of returns. Check the "Labels in first row" box if your columns have headers so Excel treats them as labels. Then choose whether to output results on the same sheet or a new one.

Pressing Enter generates the correlation matrix. You can add text formatting and conditional formatting to clean up the results.

## Are R and R2 the Same?

No. R represents the Pearson correlation coefficient and is used to indicate the strength and direction of the relationship between variables. R2 represents the coefficient of determination and is used to assess the strength of the model.

## How Is the Correlation Coefficient Calculated?

The correlation coefficient is calculated by determining the covariance of the variables and then dividing that value by the product of those variables' standard deviations.

## How Is the Correlation Coefficient Used in Investing?

Correlation coefficients play a key role in portfolio risk assessment and quantitative trading strategies. For example, some portfolio managers monitor the correlation coefficients of their holdings to limit portfolio volatility and risk.

## Conclusion

The correlation coefficient describes how one variable moves relative to another. A positive correlation indicates both move in the same direction, with a value of 1 signifying a perfect positive correlation. A value of -1 signifies a perfect negative (inverse) correlation, while zero indicates no linear correlation exists.

## References

[1] DataTrek Research. "[Oil Prices/Energy Stock Correlations, Rate Expectations](https://www.datatrekresearch.com/oil-prices-energy-stock-correlations-rate-expectations/)."
