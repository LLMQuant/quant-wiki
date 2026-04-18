![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# What Is Multicollinearity?
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

Multicollinearity occurs when two or more independent variables in a multiple regression model are highly correlated. When researchers or analysts attempt to determine how effectively each independent variable predicts or explains the dependent variable within a statistical model, multicollinearity can lead to skewed or misleading results.

Overall, multicollinearity causes wider confidence intervals, producing less reliable estimates of how independent variables affect the dependent variable.

In technical analysis, multicollinearity can lead to incorrect assumptions about investments. This typically happens when multiple indicators of the same type are used to analyze a stock.

### Key Takeaways

- Multicollinearity is a statistical concept where several independent variables in a model are correlated.
- Two variables are considered perfectly collinear if their correlation coefficient is +/- 1.0.
- Multicollinearity among independent variables reduces the reliability of statistical inferences.
- When analyzing investments, it is better to use different types of indicators rather than multiple indicators of the same type to avoid multicollinearity.
- Multicollinearity can reduce the reliability of results because the outcomes being compared tend to be similar.

## Understanding Multicollinearity

Statistical analysts use multiple regression models to predict the value of a specified dependent variable based on the values of two or more independent variables. The dependent variable is sometimes called the outcome, target, or criterion variable.

For example, a multiple regression model might attempt to predict stock returns based on price-to-earnings (P/E) ratios, market capitalization, or other data. The stock return is the dependent variable (outcome), while the various financial metrics serve as independent variables.

Multicollinearity in a multiple regression model indicates that the collinear independent variables are not truly independent. For instance, past performance may be related to market capitalization. Companies with strong stock performance often see increased investor confidence, driving up demand for the stock and thereby increasing its market value.

While multicollinearity does not affect the regression estimates themselves, it makes those estimates imprecise, unclear, and unreliable. Consequently, it becomes difficult to determine the individual effect of each independent variable on the dependent variable. This inflates the standard errors of some or all regression coefficients.

A statistical technique called the Variance Inflation Factor (VIF) can detect and measure the degree of collinearity in a multiple regression model. The VIF measures the degree to which the variance of an estimated regression coefficient is inflated compared to when the independent variables are not linearly related. A VIF of 1 means no correlation between variables; VIF between 1 and 5 indicates moderate correlation; and VIF between 5 and 10 indicates high correlation.

When analyzing stocks, you can detect multicollinearity by observing whether indicators produce essentially the same charts. For example, selecting two momentum indicators on a trading chart typically generates trend lines showing the same momentum.

## Causes of Multicollinearity

Multicollinearity can arise when two independent variables are highly correlated. It may also occur when an independent variable is computed from other variables in the dataset, or when two independent variables provide similar and redundant results.

If you use the same data to create two or three indicators of the same type, the result will exhibit multicollinearity, since the data and the way it is manipulated are very similar.

**Important:** Models containing multicollinearity may produce unreliable statistical inferences.

## Types of Multicollinearity

Perfect collinearity exists when there is an exact linear relationship among multiple independent variables, meaning data points fall precisely on the regression line. In technical analysis, this occurs when two indicators measuring the same metric (such as volume) are used simultaneously. If overlaid, the two would be indistinguishable.

High collinearity exists when there is some correlation among multiple independent variables, but it is not as tight as perfect collinearity. Not all data points fall on the regression line, but the data is still too closely related to be used together.

In technical analysis, highly collinear indicators typically produce very similar results.

Structural collinearity occurs when you use data to create new features. For example, if you collect data, use it for additional calculations, and then run regression on the results, those results will be correlated because they are derived from one another.

This is a common type of collinearity in investment analysis, where the same data is used to create different indicators.

Data-based collinearity is typically caused by poor experimental design or data collection processes, such as the use of observational data, where some or all variables end up being correlated.

Stock data used to create indicators is usually collected from historical prices and trading volume, so the likelihood of multicollinearity arising from improper data collection is relatively low.

## Multicollinearity in Investing

In investing, multicollinearity is a common consideration, particularly when performing technical analysis to predict future price movements of a security such as a stock or commodity future.

Market analysts want to avoid using collinear technical indicators that rely on very similar or related inputs. The issue is not the data itself but how the data is manipulated to produce results.

Analysis must therefore be based on significantly different indicators to ensure that the market is analyzed from independent analytical perspectives. For example, a momentum indicator and a trend indicator share the same underlying data, but they are not perfectly collinear and may not even be highly collinear. The two indicators produce different results based on how the data is processed.

**Note:** Most investors need not concern themselves with the data and mathematics behind indicator calculations -- understanding what multicollinearity is and how it affects analysis is sufficient.

## How to Address Multicollinearity

A common method for eliminating multicollinearity is to first identify the collinear independent variables, then remove one or more of them. In statistics, VIF calculations are typically performed to determine the degree of multicollinearity. Another approach is to collect more data under different conditions.

Noted technical analyst John Bollinger, creator of Bollinger Bands, wrote that "a cardinal rule for the successful use of technical analysis requires avoiding multicollinearity among indicators." To address this, analysts avoid using two or more technical indicators of the same type. Instead, they analyze a security using one type of indicator (such as a momentum indicator) and then perform a separate analysis using a different type (such as a trend indicator).

For example, stochastic oscillator, Relative Strength Index (RSI), and Williams %R are all momentum indicators that rely on similar inputs and are likely to produce similar results. In such cases, it is better to remove all but one indicator and use a different type of indicator that does not track the same underlying behavior.

## How Do You Deal With Multicollinearity?

To reduce multicollinearity in a statistical model, you can remove the specific variables identified as most collinear. You can also try combining or transforming the problematic variables to reduce their correlation. If that is still not feasible, modified regression models such as ridge regression, principal component regression, or partial least squares regression handle multicollinearity better. In stock analysis, the best approach is to select indicators of different types.

## What Is Multicollinearity in Regression?

Multicollinearity describes relationships among variables that cause them to be correlated with one another. Multicollinear data creates problems for analysis because the variables are not independent.

## How Do You Interpret Multicollinearity Results?

When the VIF exceeds five, the data exhibits high multicollinearity. A VIF between 1 and 5 indicates moderate correlation, while a VIF of 1 indicates no correlation. In technical analysis, indicators are often identical.

## What Is Perfect Collinearity?

Perfect collinearity exists when two independent variables in a model have an exact 1:1 correspondence. The correlation coefficient is either +1.0 or -1.0.

## Why Is Multicollinearity a Problem?

Multicollinearity is a problem because it produces regression model results that are less reliable. This occurs because wider confidence intervals (larger standard errors) can reduce the statistical significance of regression coefficients. In stock analysis, it can lead to incorrect impressions or assumptions about an investment.

## Summary

Multicollinearity exists when an independent variable is highly correlated with multiple other independent variables in a multiple regression equation. It is problematic because it makes statistical inferences unreliable. However, the Variance Inflation Factor (VIF) can provide information about which variables are redundant, allowing those with high VIF values to be removed.

When using technical analysis, multicollinearity becomes a concern because many indicators display data in the same way. To avoid this, it is best to use indicators that do not measure the same trend.

## About LLMQuant

LLMQuant is a cutting-edge community composed of professionals from top global universities and the quantitative finance industry, dedicated to exploring the limitless possibilities at the intersection of artificial intelligence (AI) and quantitative finance (Quant). Our team members hail from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other prestigious institutions, with external advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and leading proprietary trading firms.
