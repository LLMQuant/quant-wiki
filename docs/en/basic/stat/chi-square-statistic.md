![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# What Is a Chi-Square Statistic?
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

A chi-square (χ²) statistic is a test that measures how a model compares to actual observed data. The data used to compute a chi-square statistic must be random, raw, mutually exclusive, drawn from independent variables, and from a sufficiently large sample. For example, the outcomes of tossing a fair coin meet these criteria.

Chi-square tests are commonly used in hypothesis testing. The chi-square statistic compares the magnitude of any discrepancies between expected and actual results, taking into account sample size and the number of variables.

In these tests, degrees of freedom are used to determine whether a null hypothesis can be rejected based on the total number of variables and samples in the experiment. As with any statistic, the larger the sample size, the more reliable the results.

### Key Takeaways

- A chi-square (χ²) statistic measures the difference between observed and expected frequencies of a set of events or variables.
- Chi-square is particularly useful for analyzing differences in categorical variables, especially those that are nominal in nature.
- χ² depends on the size of the difference between actual and observed values, degrees of freedom, and sample size.
- χ² can be used to test whether two variables are related to or independent of each other.
- It can also be used to test the goodness of fit between an observed distribution and a theoretical frequency distribution.

## Formula for the Chi-Square Statistic

$$ \begin{aligned}&\chi^2_c = \sum \frac{(O_i - E_i)^2}{E_i} \\&\textbf{where:}\\&c=\text{Degrees of freedom}\\&O=\text{Observed value(s)}\\&E=\text{Expected value(s)}\end{aligned} $$

## What the Chi-Square Statistic Can Tell You

There are two main types of chi-square tests, which provide different information:

- **Test of independence**, which asks relational questions such as: "Is there a relationship between student gender and course selection?"
- **Goodness-of-fit test**, which asks theoretical questions such as: "How well does the coin in my hand match a theoretically fair coin?"

**Note:** Chi-square analysis is applied to categorical variables and is especially useful when those variables are nominal (i.e., where order does not matter, such as marital status or gender).

When examining student gender and course selection, a χ² test of independence can be used. To conduct this test, the researcher collects data on the two variables (gender and courses chosen), then compares the frequency at which male and female students select among the offered courses using the formula above and a χ² distribution table.

If there is no relationship between gender and course selection (i.e., they are independent), the actual frequencies with which male and female students choose each course should be roughly equal, or the proportion of males and females in each course should approximately match the proportion in the overall sample.

A χ² test of independence tells us how likely it is that random chance explains any observed differences between the actual frequencies in the data and these theoretical expectations.

As a goodness-of-fit test example, imagine a marketing team testing a new product that it believes will appeal to women over age 45. The company has product-tested with 500 potential buyers.

The marketing team has age and gender information about the test group, allowing it to construct a chi-square test showing the age and gender distribution of those who expressed willingness to purchase the product.

The results would reveal whether the most likely buyers are indeed women over 45. If testing showed that men over 45 or women aged 18 to 44 were equally likely to buy, the marketers would adjust their advertising, promotion, and placement strategy to appeal to this broader customer group.

## Example of Using the Chi-Square Statistic

Consider an imaginary coin with an equal 50/50 chance of landing heads or tails, and a real coin that you toss 100 times. If the coin is fair, it should have an equal probability of landing on either side, and the expected outcome of 100 tosses would be 50 heads and 50 tails.

In this case, χ² can tell us how the actual results of 100 coin tosses compare to the 50/50 outcome predicted by the theoretical model of a fair coin. The actual toss could come up 50/50, 60/40, or even 90/10.

The greater the deviation from 50/50, the worse the goodness of fit for this set of tosses, and the more likely the conclusion that this coin is not actually fair.

## When to Use a Chi-Square Test

A chi-square test is used to help determine whether observed results are consistent with expected results and to rule out the possibility that the observations are due to chance.

A chi-square test is appropriate when the data being analyzed comes from a random sample and the variable in question is categorical. Categorical variables include choices such as car type, race, educational attainment, gender, or a person's level of support for a political candidate (from strongly like to strongly dislike).

Such data is often collected through survey responses or questionnaires, making chi-square analysis especially useful for analyzing this type of data.

## How to Perform a Chi-Square Test

The basic steps for performing a goodness-of-fit test or test of independence are:

- Create a table of observed versus expected frequencies.
- Calculate the chi-square value using the formula.
- Find the critical chi-square value using a chi-square table or statistical software.
- Determine whether the chi-square value exceeds the critical value.
- Reject or fail to reject the null hypothesis.

## Limitations of the Chi-Square Statistic

The chi-square test is sensitive to sample size. With very large samples, relationships may appear significant when they are actually not.

Additionally, the chi-square test cannot establish whether one variable has a causal relationship with another. It can only determine whether two variables are associated.

## What Is a Chi-Square Test Used For?

Chi-square is a statistical test used to examine differences among categorical variables from a random sample to judge the goodness of fit between expected and observed results.

## Who Uses Chi-Square Analysis?

Since chi-square applies to categorical variables, it is most commonly used by researchers studying survey response data. Such research can span demographics, consumer and marketing research, political science, and economics.

## Is Chi-Square Analysis Used When the Independent Variable Is Nominal or Ordinal?

A nominal variable is a categorical variable where the numerical order may be irrelevant. For example, asking someone their favorite color produces a nominal variable. Asking someone's age, on the other hand, produces an ordinal dataset. Chi-square is best applied to nominal data.

## Summary

The chi-square statistic measures the difference between observed and expected frequencies for a set of variables. It is especially useful for analyzing differences in categorical variables, particularly those that are nominal. Two different types of chi-square tests -- the test of independence and the goodness-of-fit test -- answer different relational questions.

## About LLMQuant

LLMQuant is a cutting-edge community composed of professionals from top global universities and the quantitative finance industry, dedicated to exploring the limitless possibilities at the intersection of artificial intelligence (AI) and quantitative finance (Quant). Our team members hail from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other prestigious institutions, with external advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and leading proprietary trading firms.
