![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# What Is a P-Value?
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

In statistics, a p-value is defined as the probability of obtaining results at least as extreme as the observed results, assuming the null hypothesis is true.

The p-value serves as an alternative to rejection regions, providing the smallest significance level at which the null hypothesis can be rejected. A smaller p-value indicates stronger evidence in favor of the alternative hypothesis.

Government agencies frequently use p-values to bolster the credibility of research and reports. For example, the U.S. Census Bureau requires that any analysis with a p-value greater than 0.10 be accompanied by a statement indicating that the difference is not statistically different from zero. The Bureau also maintains standards specifying which p-values are acceptable for various publications. [1]

### Key Takeaways

- A p-value is a statistical measure used to validate a hypothesis against observed data.
- It quantifies the probability of obtaining the observed results under the assumption that the null hypothesis is true.
- The lower the p-value, the greater the statistical significance of the observed difference.
- A p-value of 0.05 or less is generally considered statistically significant.
- P-values can serve as an alternative or supplement to pre-selected confidence levels in hypothesis testing.

## Understanding P-Values

P-values are typically determined using p-value tables, spreadsheets, or statistical software. These calculations are based on the assumed or known probability distribution of the specific statistic being tested. The sample size determines the reliability of the observed data and directly affects the accuracy of the p-value calculation. The p-value is derived from the deviation between the observed value and a chosen reference value, taking into account the probability distribution of the statistic -- the greater the difference between the two values, the smaller the corresponding p-value.

Mathematically, the p-value is calculated using integral calculus. It represents the area under the probability distribution curve for all values of the statistic that are at least as far from the reference value as the observed value is, relative to the total area under the curve. Standard deviation, which quantifies the dispersion of data points from the mean, plays an important role in this calculation.

The computation of the p-value varies depending on the type of test performed. Three test types describe different positions on the probability distribution curve: left-tailed tests, right-tailed tests, and two-tailed tests. In each case, degrees of freedom play a crucial role in determining the shape of the distribution and, consequently, the calculation of the p-value.

In essence, the greater the difference between two observed values, the less likely that difference is attributable to simple random chance -- and this is reflected in a lower p-value.

## The P-Value Approach to Hypothesis Testing

The p-value approach uses the calculated probability to determine whether there is evidence to reject the null hypothesis. This determination relies heavily on the test statistic, which summarizes the sample information relevant to the hypothesis being tested. The null hypothesis (also called the conjecture) is the initial claim about a population or data-generating process. The alternative hypothesis states that the population parameter differs from the value specified in the conjecture.

In practice, a significance level is declared in advance to determine how small the p-value must be in order to reject the null hypothesis. Because different researchers may use different significance levels when examining the same question, readers can sometimes find it difficult to compare results across studies. P-values offer a solution to this problem.

**Important:** Even a low p-value does not constitute definitive proof of statistical significance, because the possibility remains that the observed data are a chance result. Only repeated experiments or studies can confirm whether a relationship is truly statistically significant.

For example, suppose a study comparing the returns of two specific assets is conducted by different researchers using the same data but different significance levels. These researchers could reach opposite conclusions about whether the assets differ.

If one researcher uses a 90% confidence level and the other requires 95% confidence to reject the null hypothesis, and the p-value of the observed difference is 0.08 (corresponding to a 92% confidence level), then the first researcher would find a statistically significant difference between the two assets, while the second would not.

To avoid this problem, researchers can report the p-value of the hypothesis test and allow readers to interpret the statistical significance for themselves. This is known as the p-value approach to hypothesis testing. Independent observers can note the p-value and decide for themselves whether it represents a statistically significant difference.

## Example of a P-Value

An investor claims that their portfolio performs equivalently to the S&P 500 index. To test this, the investor conducts a two-tailed test.

The null hypothesis states that the portfolio's returns are equivalent to the S&P 500's returns over a specified period. The alternative hypothesis states that the portfolio's returns are not equivalent. If the investor were conducting a one-tailed test, the alternative hypothesis would state that the portfolio's returns are either less than or greater than those of the S&P 500.

The p-value approach does not necessarily use a pre-selected confidence level at which to reject the null hypothesis. Instead, it provides a measure of how much evidence exists against the null hypothesis. The smaller the p-value, the stronger the evidence against it.

If the investor finds a p-value of 0.001, there is strong evidence against the null hypothesis, and the investor can confidently conclude that the portfolio's returns are not equivalent to those of the S&P 500.

While this does not provide an exact threshold for acceptance or rejection of the null hypothesis, it offers a practical advantage: the p-value approach provides a straightforward way to compare the relative confidence an investor can have when choosing among multiple investments or portfolios benchmarked against the S&P 500.

For example, given two portfolios A and B whose performances differ from the S&P 500 with p-values of 0.10 and 0.01 respectively, the investor can be more confident that Portfolio B, with the lower p-value, will consistently show different results.

## Is a P-Value of 0.05 Significant?

A p-value less than 0.05 is generally considered statistically significant, in which case the null hypothesis should be rejected. A p-value greater than 0.05 means the deviation from the null hypothesis is not statistically significant, and the null hypothesis is not rejected.

## What Does a P-Value of 0.001 Mean?

A p-value of 0.001 indicates that if the null hypothesis being tested were indeed true, there would be a one-in-a-thousand chance of observing results at least as extreme as those actually obtained. This leads the observer to reject the null hypothesis because either a highly rare data outcome has been observed, or the null hypothesis is incorrect.

## How Can P-Values Be Used to Compare Two Different Results?

If you have two different results -- one with a p-value of 0.04 and another with a p-value of 0.06 -- the result with a p-value of 0.04 would be considered more statistically significant. Beyond this simplified example, you could compare a p-value of 0.04 with one of 0.001. Both are statistically significant, but the 0.001 result provides much stronger evidence against the null hypothesis than the 0.04 result.

## The Bottom Line

The p-value is used to measure the significance of observed data. When researchers identify an apparent relationship between two variables, there is always a possibility that this correlation is merely coincidental. The p-value calculation helps determine whether the observed relationship could plausibly have arisen by chance.

## References

[1] U.S. Census Bureau. "[Statistical Quality Standard E1: Analyzing Data](https://www.census.gov/about/policies/quality/standards/standarde1.html)."
