![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# What Is the Empirical Rule?
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

The empirical rule, also known as the three-sigma rule or the 68-95-99.7 rule, is a statistical rule stating that in a normal distribution, nearly all observed data will fall within three standard deviations (denoted by the Greek letter σ) of the mean (denoted by the Greek letter μ).

Specifically, the empirical rule predicts that in a normal distribution, 68% of observations will fall within the first standard deviation (μ +/- σ), 95% within the first two standard deviations (μ +/- 2σ), and 99.7% within the first three standard deviations (μ +/- 3σ).

### Key Takeaways

- The empirical rule states that in a normal distribution, nearly all observed data will fall within three standard deviations of the mean.
- Under this rule, 68% of the data falls within one standard deviation, 95% within two standard deviations, and 99.7% within three standard deviations.
- The three-sigma limits following the empirical rule are used to set upper and lower control limits in statistical quality control charts and risk analysis.

## Understanding the Empirical Rule

The empirical rule is frequently used in statistics to forecast final outcomes. After calculating the standard deviation and before collecting complete data, the rule can serve as a rough estimate of what the forthcoming data will show.

This probability distribution can be useful as an evaluation technique because gathering appropriate data may be time-consuming or even impossible in certain situations. Such considerations are particularly relevant when firms review their quality control measures or evaluate risk exposure. For example, the commonly used risk tool Value at Risk (VaR) assumes that the probability of risk events follows a normal distribution.

The empirical rule is also used as a rough test of a distribution's "normality." If too many data points fall outside the three standard deviation boundaries, this suggests the distribution is not normal and may be skewed or follow a different distribution.

The empirical rule is also called the three-sigma rule because "three-sigma" refers to the statistical distribution of data within three standard deviations of the mean in a normal distribution (bell curve), as illustrated in the figure below.

## Empirical Rule Example

Suppose a population of animals in a zoo is known to be normally distributed. Each animal lives an average of 13.1 years (mean), with a standard deviation of 1.5 years. If someone wants to know the probability of an animal living longer than 14.6 years, they can use the empirical rule. Knowing the distribution's mean is 13.1 years, the following age ranges correspond to each standard deviation:

- One standard deviation (μ +/- σ): (13.1 - 1.5) to (13.1 + 1.5), i.e., 11.6 to 14.6
- Two standard deviations (μ +/- 2σ): 13.1 - (2 x 1.5) to 13.1 + (2 x 1.5), i.e., 10.1 to 16.1
- Three standard deviations (μ +/- 3σ): 13.1 - (3 x 1.5) to 13.1 + (3 x 1.5), i.e., 8.6 to 17.6

The person solving this problem needs to calculate the total probability of the animal living 14.6 years or longer. The empirical rule shows that 68% of the distribution lies within one standard deviation, i.e., from 11.6 to 14.6 years. Therefore, the remaining 32% of the distribution lies outside this range. Half lies above 14.6 and the other half below 11.6. Thus, the probability of the animal living longer than 14.6 is 16% (calculated as 32% divided by 2).

## The Empirical Rule in Investing

Most market data is not normally distributed, so the 68-95-99.7 rule generally does not apply directly to investing. However, many analysts still use aspects of it -- such as standard deviation -- to estimate volatility.

You can calculate the standard deviation of a portfolio, index, or other investment and use it to assess volatility. If you have access to a spreadsheet and the prices or returns of your chosen investment, calculating standard deviation is straightforward.

Market analysts generally express standard deviation in percentage terms. For example, from May 2 to June 2, 2023, the S&P 500's daily standard deviation (annualized, using daily closing prices) was 13.29%.

In a spreadsheet, you can paste returns, prices, or values, calculate the percentage change from the prior trading day, and use the standard deviation function: [1]

**Important:** Using more than one month of trading data -- such as three years or more -- yields more accurate results. The example below uses one month of daily values for the index and annualizes the standard deviation to limit table size.

To annualize the standard deviation, multiply it by the square root of the number of trading days in a year -- typically 252.

| S&P 500 Standard Deviation (Annualized)
|---|---|---|---|
||A|B|C|D
|1|Date|Close|Daily Change|Formula
|2|05/02/23|4119.58|-|-
|3|05/03/23|4090.75|-0.70%|-
|4|05/04/23|4061.22|-0.72%|-
|5|05/05/23|4136.25|1.85%|-
|6|05/08/23|4138.12|0.05%|-
|7|05/09/23|4119.17|-0.46%|-
|8|05/10/23|4137.64|0.45%|-
|9|05/11/23|4130.62|-0.17%|-
|10|05/12/23|4124.08|-0.16%|-
|11|05/15/23|4136.28|0.30%|-
|12|05/16/23|4109.9|-0.64%|-
|13|05/17/23|4158.77|1.19%|-
|14|05/18/23|4198.05|0.94%|-
|15|05/19/23|4191.98|-0.14%|-
|16|05/22/23|4192.63|0.02%|-
|17|05/23/23|4145.58|-1.12%|-
|18|05/24/23|4115.24|-0.73%|-
|19|05/25/23|4151.28|0.88%|-
|20|05/26/23|4205.45|1.30%|-
|21|05/30/23|4205.52|0.00%|-
|22|05/31/23|4179.83|-0.61%|-
|23|06/01/23|4221.02|0.99%|-
|24|06/02/23|4282.37|1.45%|-
|25|-|Daily Std Dev|0.84%|=stdev(B2:B24)
|26|-|Annualized Std Dev|13.29%|=sqrt(252)*C25

Thus, the annualized volatility based on the table data is 13.29%. The higher the standard deviation, the riskier analysts consider the investment.

Alternatively, you can find an investment's standard deviation on popular financial websites. For example, Morningstar displays three-year, five-year, and ten-year standard deviations for the S&P 500. [2]

## What Is the Empirical Rule?

In statistics, the empirical rule states that 99.7% of observed data in a normal distribution will fall within three standard deviations of the mean. Specifically, 68% of observed data will fall within one standard deviation, 95% within two standard deviations, and 97.5% within three standard deviations.

## How Is the Empirical Rule Used?

The empirical rule is applied to anticipate probable outcomes in a normal distribution. For example, a statistician can use it to estimate the percentage of cases that fall within each standard deviation. Suppose the standard deviation is 3.1 and the mean is 10. In this case, the first standard deviation would range between (10 + 3.1) = 13.1 and (10 - 3.1) = 6.9. The second standard deviation would range between 10 + (2 x 3.1) = 16.2 and 10 - (2 x 3.1) = 3.8, and so on.

## What Are the Benefits of the Empirical Rule?

The benefit of the empirical rule is that it serves as a means of forecasting data. This is especially important when dealing with large datasets and variables that are unknown.

## Summary

Analysts use the empirical rule to observe how much data within a dataset falls within specific intervals from the mean. Investment analysts can use it to estimate the volatility of a particular investment, portfolio, or fund.

## References

[1] Google Docs Editors Help. "[STDEV](https://support.google.com/docs/answer/3094054?hl=en)."

[2] Morningstar. "[S&P 500 PR](https://www.morningstar.com/indexes/spi/spx/risk)."

## About LLMQuant

LLMQuant is a cutting-edge community composed of professionals from top global universities and the quantitative finance industry, dedicated to exploring the limitless possibilities at the intersection of artificial intelligence (AI) and quantitative finance (Quant). Our team members hail from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other prestigious institutions, with external advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and leading proprietary trading firms.
