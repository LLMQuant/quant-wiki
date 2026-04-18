![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# What Is a Z-Test?
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

A z-test is a statistical test used to determine whether two population means are different when the variance is known and the sample size is large. It can also be used to compare a single mean against a hypothesized value.

The data must approximately follow a normal distribution for the test to be valid. Parameters such as variance and standard deviation must be calculated in order to perform a z-test.

### Key Takeaways

- A z-test is a statistical test used to determine whether two population means differ when the variance is known and the sample size is large, or to compare a single mean against a hypothesized value.
- A z-test is a hypothesis test performed on data that follows a normal distribution.
- The z-statistic (or z-score) is a number representing the result of the z-test.
- Z-tests are closely related to t-tests, but t-tests are better suited when experiments involve small sample sizes.
- Z-tests assume the standard deviation is known, whereas t-tests assume it is unknown.

## Understanding Z-Tests

A z-test is a hypothesis test in which the z-statistic follows a normal distribution. Z-tests are best suited for sample sizes greater than 30 because, according to the Central Limit Theorem, the sampling distribution of the mean approximates a normal distribution as the sample size increases.

When conducting a z-test, the null and alternative hypotheses should be stated along with the significance level (alpha). The z-score (test statistic) should be calculated, and the results and conclusions should be stated clearly. The z-statistic represents how many standard deviations the score derived from the z-test is from the population mean.

Examples of tests that can be conducted as z-tests include one-sample location tests, two-sample location tests, paired difference tests, and maximum likelihood estimation. Z-tests are closely related to t-tests, but t-tests are preferred when the sample size is small. Additionally, t-tests assume the standard deviation is unknown, while z-tests assume it is known. If the population standard deviation is unknown, the sample variance is assumed to equal the population variance.

## One-Sample Z-Test Example

Suppose an investor wants to test whether the average daily return of a stock exceeds 3%. A simple random sample of 50 returns is calculated, yielding a mean of 2%. Assume the standard deviation of returns is 2.5%. The null hypothesis is that the mean equals 3%.

The alternative hypothesis is that the mean return is either greater or less than 3%. An alpha of 0.05% is selected for a two-tailed test. Consequently, there is 0.025% of the samples in each tail, and the alpha has a critical value of 1.96 or -1.96. The null hypothesis is rejected if z is greater than 1.96 or less than -1.96.

The z-value is calculated by subtracting the hypothesized mean daily return (3%) from the observed sample mean, then dividing by the standard deviation divided by the square root of the number of observations.

Therefore, the test statistic is:

The investor rejects the null hypothesis because z is less than -1.96 and concludes that the average daily return is less than 3%.

## What Is the Difference Between a T-Test and a Z-Test?

Z-tests are closely related to t-tests, but t-tests are better performed when the data consists of a small sample size (less than 30). Additionally, t-tests assume the standard deviation is unknown, while z-tests assume it is known.

## When Should a Z-Test Be Used?

A z-test can be used if the population standard deviation is known and the sample size is 30 or greater. If the population standard deviation is unknown, regardless of sample size, a t-test should be used instead.

## What Is a Z-Score?

A z-score (or z-statistic) is a number representing how many standard deviations the result from a z-test is from the population mean. Essentially, it is a numerical measurement that describes a value's relationship to the mean of a group of values. A z-score of 0 indicates the data point's score equals the mean. A z-score of 1.0 indicates the value is one standard deviation from the mean. Z-scores can be positive or negative -- positive values indicate scores above the mean, and negative values indicate scores below.

## What Is the Central Limit Theorem (CLT)?

In probability theory, the Central Limit Theorem (CLT) states that the distribution of a sample approximates a normal distribution (also known as a "bell curve") as the sample size increases, regardless of the population's distribution shape -- assuming all samples are of equal size. Sample sizes of 30 or more are considered sufficient for the CLT to accurately predict population characteristics. The accuracy of z-tests relies on the CLT holding true.

## Conclusion

Z-tests are used in hypothesis testing to evaluate whether findings or associations are statistically significant. Specifically, they test whether two means are the same (the null hypothesis). A z-test can only be used when the population standard deviation is known and the sample size is 30 data points or larger. Otherwise, a t-test should be used.
