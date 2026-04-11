![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# What Is a T-Test?
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

A t-test is an inferential statistical method used to determine whether there is a significant difference between the means of two groups and how they are related. It is applied when the data set follows a normal distribution with unknown variance -- for example, a data set recorded from 100 coin flips.

The t-test uses a t-statistic, t-distribution values, and degrees of freedom to determine statistical significance. It is one of the most commonly used tools for hypothesis testing in statistics.

### Key Takeaways

- A t-test is an inferential statistic used to determine whether there is a statistically significant difference between the means of two variables.
- It is a widely used method for hypothesis testing in statistics.
- Computing a t-test requires three fundamental data values: the difference between the means of each data set, the standard deviation of each group, and the number of data values.
- T-tests can be either dependent (paired) or independent.

## Understanding T-Tests

A t-test compares the mean values of two data sets and determines whether they come from the same population. For instance, a sample of students from Class A and a sample of students from Class B are unlikely to have exactly the same mean and standard deviation. Similarly, samples from a placebo-controlled group and a drug-treatment group should have slightly different means and standard deviations.

Mathematically, the t-test takes a sample from each of the two sets and establishes a problem statement. It assumes a null hypothesis that the two means are equal.

Using formulas, calculated values are compared against standard values. The null hypothesis is then accepted or rejected accordingly. If the null hypothesis qualifies for rejection, this indicates that the data readings are strong and likely not due to chance.

The t-test is just one of many tests designed for this purpose. Statisticians use other tests to examine more variables and larger sample sizes. For large sample sizes, a z-test is used. Other testing options include the chi-square test and the f-test.

## Using T-Tests

Consider a pharmaceutical company testing a new drug. Following standard procedure, the drug is administered to one group of patients while a placebo is given to another group, known as the control group. The placebo serves as a benchmark against which the treatment group's response is measured.

After the drug trial, the placebo-controlled group reports an average life expectancy increase of three years, while the treatment group reports an increase of four years.

Initial observation suggests the drug is effective. However, this result could also be due to chance. A t-test can determine whether the results are statistically valid and generalizable to the broader population.

Four assumptions underlie the use of a t-test: the collected data must follow a continuous or ordinal scale (such as IQ scores), the data must be randomly selected from the population, it should produce a bell-shaped normal distribution, and there should be equal or homogeneous variance (equal standard deviations).

## T-Test Formulas

Computing a t-test requires three fundamental data values: the difference between the means of each data set (the mean difference), the standard deviation of each group, and the number of data values in each group.

This comparison helps determine whether chance accounts for the difference and whether that difference falls outside the range attributable to chance. The t-test examines whether the difference between groups represents a genuine difference in the study or is merely a random occurrence.

The t-test produces two output values: the t-value and degrees of freedom. The t-value (or t-score) is the ratio of the difference between the means of the two sample sets to the variation within the sample sets.

The numerator is the difference between the means of the two sample sets. The denominator is a measure of the dispersion or variability present within the sample sets.

The calculated t-value is then compared against a critical value obtained from a T-distribution table. A higher t-score indicates a larger difference between the two sample sets, while a smaller t-value indicates greater similarity.

**T-Score:** A larger t-score (or t-value) indicates a difference between groups, while a smaller t-score indicates similarity between groups.

Degrees of freedom refer to the values in a study that are free to vary and are essential for assessing the significance and validity of the null hypothesis. Their calculation typically depends on the number of data records available in the sample sets.

A correlated (or paired) t-test is a dependent test performed when samples consist of matched pairs of similar units, or when repeated measurements are taken. For example, the same patient might be tested both before and after receiving a specific treatment, with each patient serving as their own control.

This method also applies when samples are related or have matching characteristics, such as in comparative analyses involving children, parents, or siblings.

The formulas for computing the t-value and degrees of freedom in a paired t-test are:

$$ \begin{aligned}&T=\frac{\textit{mean}1 - \textit{mean}2}{\frac{s(\text{diff})}{\sqrt{(n)}}}\\&\textbf{where:}\\&\textit{mean}1\text{ and }\textit{mean}2=\text{the average values of each sample set}\\&s(\text{diff})=\text{the standard deviation of the differences of paired data values}\\&n=\text{the sample size (number of paired differences)}\\&n-1=\text{the degrees of freedom}\end{aligned} $$

An equal variance t-test is an independent t-test used when the number of samples in each group is the same or when the two data sets have similar variances.

The formulas for the t-value and degrees of freedom of an equal variance t-test are:

$$ \begin{aligned}&\text{T-value} = \frac{ mean1 - mean2 }{\frac {(n1 - 1) \times var1^2 + (n2 - 1) \times var2^2 }{ n1 +n2 - 2}\times \sqrt{ \frac{1}{n1} + \frac{1}{n2}} } \\&\textbf{where:}\\&mean1 \text{ and } mean2 = \text{the average values of each sample set} \\&var1 \text{ and } var2 = \text{the variance of each sample set} \\&n1 \text{ and } n2 = \text{the number of records in each sample set} \end{aligned} $$

and,

$$ \begin{aligned} &\text{Degrees of Freedom} = n1 + n2 - 2 \\ &\textbf{where:}\\ &n1 \text{ and } n2 = \text{the number of records in each sample set} \\ \end{aligned} $$

An unequal variance t-test is an independent t-test used when the number of samples in each group differs and the two data sets have different variances. This test is also known as Welch's t-test.

The formulas for the t-value and degrees of freedom of an unequal variance t-test are:

$$ \begin{aligned}&\text{T-value}=\frac{mean1-mean2}{\sqrt{\bigg(\frac{var1}{n1}{+\frac{var2}{n2}\bigg)}}}\\&\textbf{where:}\\&mean1 \text{ and } mean2 = \text{the average values of each sample set} \\&var1 \text{ and } var2 = \text{the variance of each sample set} \\&n1 \text{ and } n2 = \text{the number of records in each sample set} \end{aligned} $$

and,

$$ \begin{aligned} &\text{Degrees of Freedom} = \frac{ \left ( \frac{ var1^2 }{ n1 } + \frac{ var2^2 }{ n2 } \right )^2 }{ \frac{ \left ( \frac{ var1^2 }{ n1 } \right )^2 }{ n1 - 1 } + \frac{ \left ( \frac{ var2^2 }{ n2 } \right )^2 }{ n2 - 1}} \\ &\textbf{where:}\\ &var1 \text{ and } var2 = \text{the variance of each sample set} \\ &n1 \text{ and } n2 = \text{the number of records in each sample set} \\ \end{aligned} $$

## Which T-Test to Use?

A flowchart can help determine which t-test to use based on the characteristics of the sample sets. Key considerations include whether the sample records are similar, the number of data records in each sample set, and the variance of each sample set.

## Unequal Variance T-Test Example

Suppose diagonal measurements of paintings received at an art gallery are being analyzed. One sample group contains 10 paintings, while the other contains 20. The data sets with their corresponding means and variances are as follows:

||Set 1|Set 2
|---|---|---|
||19.7|28.3
||20.4|26.7
||19.6|20.1
||17.8|23.3
||18.5|25.2
||18.9|22.1
||18.3|17.7
||18.9|27.6
||19.5|20.6
||21.95|13.7
|||23.2
|||17.5
|||20.6
|||18
|||23.9
|||21.6
|||24.3
|||20.4
|||23.9
|||13.3
|Mean|19.4|21.6
|Variance|1.4|17.1

Although Set 2 has a higher mean than Set 1, we cannot simply conclude that the population corresponding to Set 2 has a higher mean than that of Set 1.

Is the difference from 19.4 to 21.6 due to chance alone, or does a genuine difference exist in the overall population of paintings received at the gallery? We frame the problem by assuming a null hypothesis that the means of the two sample sets are equal, and conduct a t-test to evaluate whether this hypothesis is plausible.

Since the number of data records differs (n1 = 10 and n2 = 20) and the variances also differ, the t-value and degrees of freedom are calculated using the unequal variance t-test formulas described above.

The t-value is -2.24787. Since the sign can be ignored when comparing t-values, the calculated value is 2.24787.

The degrees of freedom value is 24.38, which is rounded down to 24 as required by the formula definition.

A probability level (alpha level, significance level, p) can be specified as the acceptance criterion. In most cases, a value of 5% is assumed.

Using 24 degrees of freedom and a 5% significance level, the t-distribution table yields a critical value of 2.064. Comparing this with the calculated value of 2.247 shows that the calculated t-value exceeds the table value at the 5% significance level. Therefore, the null hypothesis of no difference between the means can be safely rejected. The population sets have inherent differences that are not attributable to chance.

## How to Use the T-Distribution Table

T-distribution tables come in one-tailed and two-tailed formats. The one-tailed version is used to evaluate situations with a fixed value or range and a clear direction (positive or negative). For example: What is the probability that the output value stays below -3? Or what is the probability of rolling more than 7 on a pair of dice? The two-tailed version is used for range-bound analyses, such as determining whether coordinates fall between -2 and +2.

## What Is an Independent T-Test?

In an independent t-test, the samples are selected independently of each other, and the data sets in the two groups do not refer to the same values. For example, 100 randomly unrelated patients might be split into two groups of 50. One group serves as the control and receives a placebo, while the other receives the prescribed treatment. This constitutes two independent sample groups that are unpaired and unrelated.

## What Does a T-Test Explain, and How Is It Used?

A t-test is a statistical test used to compare the means of two groups. It is commonly employed in hypothesis testing to determine whether a process or treatment has an effect on the population of interest, or whether two groups differ from each other.
