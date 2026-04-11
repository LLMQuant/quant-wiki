![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# What Is the Coefficient of Variation (CV)?
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

The coefficient of variation (CV) is a statistical measure of the relative dispersion of data points around the mean in a data set. It represents the ratio of the standard deviation to the mean and is a useful statistic for comparing the degree of variation across different data sets, even when the means differ substantially.

### Key Takeaways

- The coefficient of variation (CV) is a statistical measure of the relative dispersion of data points around the mean in a data set.
- It represents the ratio of the standard deviation to the mean.
- The CV can be used to compare the degree of variation across different data sets, even when the means differ substantially.
- In finance, the CV allows investors to determine how much volatility, or risk, is assumed relative to the expected return on an investment.
- The lower the ratio of standard deviation to mean return, the better the risk-return tradeoff.

## Understanding the Coefficient of Variation (CV)

The coefficient of variation shows the extent of variability in a sample relative to the population mean.

In finance, the CV allows investors to determine how much volatility, or risk, is assumed relative to the expected return. Ideally, a CV formula that yields a lower ratio of standard deviation to mean return indicates a better risk-return tradeoff. [1]

CVs are most commonly used to analyze dispersion around the mean, but quartile, quintile, or decile CVs can also be used to understand variation around the median or, for example, the 10th percentile.

**Important:** The CV formula or calculation can be used to determine the deviation between the historical mean price and the current price performance of a stock, commodity, or bond relative to other assets.

## Coefficient of Variation (CV) Formula

The formula for calculating the coefficient of variation is: [2]

$$ \begin{aligned} &\text{CV} = \frac { \sigma }{ \mu } \\ &\textbf{where:} \\ &\sigma = \text{standard deviation} \\ &\mu = \text{mean} \\ \end{aligned} $$

To calculate the CV for a sample, the formula is:

$$ CV = s/x * 100 $$

**Tip:** Multiplying the coefficient by 100 is an optional step that yields a percentage rather than a decimal.

The CV formula can be executed in Excel by first using the standard deviation function for the data set. Next, calculate the mean using the appropriate Excel function. Since the CV is the standard deviation divided by the mean, simply divide the cell containing the standard deviation by the cell containing the mean.

## Coefficient of Variation (CV) vs. Standard Deviation

Standard deviation is a statistic that measures the dispersion of a data set relative to its mean. It is used to determine the spread of values within a single data set rather than to compare across different units.

The coefficient of variation is used when comparing two or more data sets. The CV is the ratio of the standard deviation to the mean, and because it is independent of the unit of measurement, it can be used to compare data sets with different units or widely varying means.

In short, standard deviation measures how far the average value is from the mean, while the coefficient of variation measures the ratio of the standard deviation to the mean. [2]

## Advantages and Disadvantages of the CV

The coefficient of variation can be useful when comparing data sets with different units or widely varying means. [3]

This includes using risk/return ratios to select investments. For example, a risk-averse investor may want to consider assets with a historically low degree of volatility relative to the overall market or their industry. Conversely, a risk-seeking investor may look to invest in assets with a historically high degree of volatility.

When the mean is close to zero, the CV becomes very sensitive to small changes in the mean. A notable drawback, using the example above, is that if the expected return in the denominator is negative or zero, the CV could be misleading. [3]

If the expected return in the denominator of the CV formula is negative or zero, the result may be misleading. [3]

## How Is the Coefficient of Variation (CV) Used?

The CV is used across many different fields, including chemistry, engineering, physics, economics, and neuroscience.

Beyond helping select investments using risk/return ratios, economists also use it to measure economic inequality. Outside of finance, it is commonly used to audit the precision of specific processes and achieve optimal balance.

## CV Example for Selecting Investments

For example, consider a risk-averse investor who wishes to invest in an exchange-traded fund (ETF) -- a basket of securities that tracks a broad market index. The investor selects the SPDR S&P 500 ETF (SPY), the Invesco QQQ ETF (QQQ), and the iShares Russell 2000 ETF (IWM). The investor then analyzes the ETFs' returns and volatility over the past 15 years and assumes that their returns may be similar to their long-term averages.

For illustrative purposes, the following 15-year historical information is used:

- If the SPDR S&P 500 ETF has an average annual return of 5.47% and a standard deviation of 14.68%, SPY's CV is 2.68.
- If the Invesco QQQ ETF has an average annual return of 6.88% and a standard deviation of 21.31%, QQQ's CV is 3.10.
- If the iShares Russell 2000 ETF has an average annual return of 7.16% and a standard deviation of 19.46%, IWM's CV is 2.72.

Based on these approximate figures, the investor could invest in either the SPDR S&P 500 ETF or the iShares Russell 2000 ETF, as they have roughly similar risk/return ratios that indicate a better risk-return tradeoff than the Invesco QQQ ETF.

## What Does the Coefficient of Variation Tell Us?

The coefficient of variation (CV) indicates the size of the standard deviation relative to its mean. The higher the CV, the greater the dispersion around the mean. [2]

## What Is Considered a Good Coefficient of Variation?

It depends on what you are examining and comparing. There is no universally "good" set value. However, in general, a lower CV is usually preferable, as it indicates that data values are more tightly distributed relative to the mean.

## How Is the Coefficient of Variation Calculated?

To calculate the CV, first find the mean, then the sum of squares, and then compute the standard deviation. With this information, calculate the CV by dividing the standard deviation by the mean. [2]

## The Bottom Line

The coefficient of variation is a straightforward way to compare the degree of variation across different data sets. It can be applied to almost anything, including the process of selecting suitable investments.

In general, a higher CV indicates greater variability in the group, while a lower value suggests the opposite.

## References

[1] JoVE. "[JoVE Core Statistics; Chapter 4, Measures of Variation; 4.7: Coefficient of Variation](https://www.jove.com/science-education/13224/coefficient-of-variation)."

[2] Penn State, Eberly College of Science. "[STAT 500: Applied Statistics; 1.5.3 -- Measures of Variability](https://online.stat.psu.edu/stat500/lesson/1/1.5/1.5.3)."

[3] UCLA, Advanced Research Computing: Statistical Methods and Data Analytics. "[FAQ: What Is the Coefficient of Variation?](https://stats.oarc.ucla.edu/other/mult-pkg/faq/general/faq-what-is-the-coefficient-of-variation/)"
