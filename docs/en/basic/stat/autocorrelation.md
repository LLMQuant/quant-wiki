![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# What Is Autocorrelation?

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

Autocorrelation is a mathematical representation of the degree of similarity between a given time series and a lagged version of itself over successive time intervals. It is conceptually similar to the correlation between two different time series, except that autocorrelation uses the same time series twice: once in its original form and once lagged by one or more time periods.

For example, if it rains today, the data suggests that it is more likely to rain tomorrow than if today were sunny. In investing, a stock's returns may exhibit strong positive autocorrelation, meaning that if it is "up" today, it is more likely to be up tomorrow as well.

Naturally, autocorrelation can be a useful tool for traders, particularly for technical analysts.

### Key Takeaways

- Autocorrelation represents the degree of similarity between a given time series and a lagged version of itself over successive time intervals.
- Autocorrelation measures the relationship between a variable's current value and its past values.
- An autocorrelation of +1 represents a perfect positive correlation, while -1 represents a perfect negative correlation.
- Technical analysts can use autocorrelation to measure the influence of past prices on a security's future price.

## Understanding Autocorrelation

Autocorrelation can also be called lagged correlation or serial correlation, as it measures the relationship between a variable's current value and its past values.

As a very simple example, consider the five percentage values in the table below. We compare them with the same dataset shifted up by one row in the adjacent column.

| Day | % Gain or Loss | Next Day % Gain or Loss |
|-----|-------------|------------------|
| Monday | 10% | 5% |
| Tuesday | 5% | -2% |
| Wednesday | -2% | -8% |
| Thursday | -8% | -5% |
| Friday | -5% | |

Calculating autocorrelation can produce a result ranging from -1 to +1.

An autocorrelation of +1 represents a perfect positive correlation (an increase observed in one time series leads to a proportionate increase in the lagged series).

An autocorrelation of -1 represents a perfect negative correlation (an increase observed in one time series leads to a proportionate decrease in the lagged series).

Autocorrelation measures linear relationships. Even when the autocorrelation is very small, there may still be a nonlinear relationship between a time series and its lagged version.

The most common method for testing autocorrelation is the Durbin-Watson test. In simple terms, Durbin-Watson is a statistic used to detect autocorrelation through regression analysis.

Durbin-Watson test results always range from 0 to 4. Values closer to 0 indicate a greater degree of positive correlation, values closer to 4 indicate a greater degree of negative autocorrelation, and values near the middle suggest little autocorrelation.

**Correlation vs. Autocorrelation:** Correlation measures the relationship between two variables, while autocorrelation measures the relationship between a variable and its lagged values.

So why does autocorrelation matter in financial markets? Simply put, autocorrelation can be used to conduct in-depth analysis of historical price movements, which investors can then use to predict future price movements. Specifically, autocorrelation can be used to determine whether a momentum trading strategy makes sense.

## Autocorrelation in Technical Analysis

Autocorrelation is valuable for technical analysis because technical analysis is primarily concerned with trends in security prices and the relationships between them, using charting techniques. This stands in contrast to fundamental analysis, which focuses on a company's financial health or management.

Technical analysts can use autocorrelation to assess how much influence past security prices have on future prices.

Autocorrelation can help determine whether a momentum factor exists for a stock. For example, if a stock with high positive autocorrelation posts two consecutive days of strong gains, it may be reasonable to expect it to rise over the next two days as well.

## Example of Autocorrelation

Suppose Rain wants to determine whether the returns of a stock in their portfolio exhibit autocorrelation -- that is, whether the stock's returns are related to its returns in previous trading sessions.

If the returns do exhibit autocorrelation, Rain could characterize it as a momentum stock because past returns appear to influence future returns. Rain runs a regression with the prior trading session's return as the independent variable and the current return as the dependent variable. They find that the prior day's return has a positive autocorrelation of 0.8.

Since 0.8 is close to +1, past returns appear to be a very strong positive predictor of future returns for this stock.

Therefore, Rain can adjust their portfolio to take advantage of the autocorrelation, or momentum, by continuing to hold the position or accumulating more shares.

## What Is the Difference Between Autocorrelation and Multicollinearity?

Autocorrelation is the degree of correlation of a variable's values over time. Multicollinearity, on the other hand, occurs when independent variables are correlated and one can be predicted by another. An example of autocorrelation is measuring the weather in a city on June 1 versus the weather in the same city on June 5. Multicollinearity measures the correlation between two independent variables, such as a person's height and weight.

## Why Can Autocorrelation Be a Problem?

Most statistical tests assume that observations are independent of one another. In other words, the occurrence of one observation does not tell you anything about the occurrence of another. Autocorrelation is problematic for most statistical tests because it involves a lack of independence between values.

## What Are the Uses of Autocorrelation?

Autocorrelation can be applied across many disciplines but is commonly seen in technical analysis. Technical analysts evaluate securities to identify trends and predict their future performance.

## Summary

Autocorrelation is the correlation between a time series and a lagged version of itself over time. Although similar to correlation, autocorrelation uses the same time series twice. Financial analysts and traders use autocorrelation to study historical price movements and predict future trends. Technical analysts use it to determine the influence of historical security prices on future prices. While autocorrelation is a highly useful tool, it is typically used in conjunction with other statistical measures in financial analysis.

## About LLMQuant

LLMQuant is a cutting-edge community composed of professionals from top global universities and the quantitative finance industry, dedicated to exploring the limitless possibilities at the intersection of artificial intelligence (AI) and quantitative finance (Quant). Our team members hail from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other prestigious institutions, with external advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and leading proprietary trading firms.
