![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# What Is a Uniform Distribution?
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

In statistics, a uniform distribution is a type of probability distribution in which all outcomes are equally likely. A probability distribution helps you determine the likelihood of future events.

For example, when drawing from a deck of cards, the chances of pulling a heart, club, diamond, or spade are equal, so a uniform distribution is expected. Flipping a coin is another example: the probability of getting heads or tails is the same.

A uniform distribution can be visualized as a horizontal straight line. For a coin flip, where the probability of heads or tails is each 50% (p = 0.50), the graph would show the y-axis at 0.50.

### Key Takeaways

- A uniform distribution is a probability distribution in which all outcomes are equally likely.
- In a discrete uniform distribution, outcomes are discrete and have the same probability.
- In a continuous uniform distribution, outcomes are continuous and infinite.
- In a normal distribution, data near the mean occurs more frequently than data far from the mean.
- A uniform distribution can be plotted on a graph.

## Understanding Uniform Distributions

There are two types of uniform distributions: discrete and continuous.

The possible results of rolling a die provide an example of a discrete uniform distribution. The possible outcomes are 1, 2, 3, 4, 5, or 6 -- you cannot roll a 2.3, 4.7, or 5.5. Therefore, rolling a die generates a discrete distribution with p = 1/6 for each outcome. There are only 6 possible return values, with nothing in between, and the possibilities are finite.

By contrast, a continuous uniform distribution has infinitely many possible outcomes. An idealized random number generator can be thought of as a continuous uniform distribution. In such a distribution, every point between 0.0 and 1.0 has an equal chance of appearing, and the number of points within this interval is infinite.

Several other important continuous distributions exist, such as the normal distribution, chi-square distribution, and Student's t-distribution.

There are also several data-generating or data-analysis functions associated with distributions that help explain variables and their variance within a dataset. These functions include the probability density function, cumulative density function, and moment-generating function.

**Tip:** The term "discrete" in statistics refers to a variable with single, countable, and finite possible values.

## Visualizing Uniform Distributions

A distribution is a simple way to visualize a set of data. It can be displayed as a graph or a list, showing which values of a random variable have higher or lower probabilities of occurring. A uniform distribution is perhaps the simplest of all probability distributions.

In a uniform distribution, every possible value has the same probability of occurring. When displayed as a bar or line chart, this distribution has the same height for each potential outcome. In this way, it looks like a rectangle and is sometimes called a rectangular distribution.

Consider drawing a particular suit from a deck of cards. The chance of pulling a heart is the same as pulling a spade -- both are 1/4, or 25%.

Rolling a die produces one of the numbers 1, 2, 3, 4, 5, or 6. Since there are only 6 possible outcomes, the probability of rolling any one of them is 16.67% (1/6). When plotted on a graph, each possible outcome appears on the x-axis with its probability on the y-axis.

## Example of a Uniform Distribution

A standard deck of cards has 52 cards in four suits: hearts, diamonds, clubs, and spades. Each suit contains an A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, and K. The deck also includes 2 jokers, but for this example we will ignore the jokers and face cards, focusing only on number cards in each suit. This leaves 40 cards, forming a discrete dataset.

Suppose you want to know the probability of drawing the 2 of hearts from the modified deck. The probability is 1/40 or 2.5%. Each card is unique, so the likelihood of drawing any particular card is the same.

Now consider the probability of drawing a heart. This probability is significantly higher because we are now looking only at suits. Since there are only four suits, drawing a heart has a probability of 1/4 or 25%.

**Note:** Plotting the results of a single die roll produces a discrete uniform distribution, while plotting the results (mean) of many die rolls produces a normal distribution.

## Uniform Distribution vs. Normal Distribution

Some of the most common probability distributions include:

- Discrete uniform distribution
- Binomial distribution
- Continuous uniform distribution
- Normal distribution
- Exponential distribution

Perhaps the most familiar and widely used is the normal distribution, often depicted as a bell curve. Normal distributions show how continuous data is distributed, concentrating most of the data around the mean or average.

In a normal distribution, the area under the curve equals 1, and 68.27% of all data falls within one standard deviation of the mean; 95.45% falls within two standard deviations; and approximately 99.73% falls within three standard deviations. As data points move further from the mean, their frequency decreases.

A discrete uniform distribution shows that variables in a range have the same probability of occurrence. There is no variation in possible outcomes, and the data is discrete rather than continuous. Its shape resembles a rectangle rather than the bell curve of a normal distribution. Nevertheless, the area under the graph still equals 1.

## What Is a Uniform Distribution?

A uniform distribution is a probability distribution indicating that the outcomes in a discrete dataset are equally likely for each value.

## What Is the Formula for a Uniform Distribution?

The formula for a discrete uniform distribution is:

$$ \begin{aligned}&P_x = \frac{ 1 }{ n } \\&\textbf{where:} \\&P_x = \text{Probability of a discrete value} \\&n = \text{Number of values in the range} \\\end{aligned} $$

## Is a Uniform Distribution Normal?

No, a uniform distribution is not normal. A normal distribution describes how data is distributed around the mean, indicating that a variable is more likely to occur near the mean than far from it. In a normal distribution, probabilities are not uniform, whereas in a uniform distribution, all outcomes are equally likely.

## What Is the Expectation of a Uniform Distribution?

The expectation of a uniform distribution is that all possible outcomes have the same probability. The probability of one variable is the same as that of any other.

## Summary

A uniform distribution is one of several types of probability distributions in statistics. It is a distribution in which all possible outcomes are finite and equally probable. For example, rolling a single die can produce only six possible outcomes, each with a probability of 1/6.

## References

[1] National Institute of Standards and Technology. "[What Do We Mean by "Normal" Data?](https://www.itl.nist.gov/div898/handbook/pmc/section5/pmc51.htm)"

## About LLMQuant

LLMQuant is a cutting-edge community composed of professionals from top global universities and the quantitative finance industry, dedicated to exploring the limitless possibilities at the intersection of artificial intelligence (AI) and quantitative finance (Quant). Our team members hail from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other prestigious institutions, with external advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and leading proprietary trading firms.
