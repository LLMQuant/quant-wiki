![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# What Is Joint Probability?
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

Joint probability is a statistical measure that calculates the likelihood of two events occurring simultaneously. Put simply, it is the probability that event Y occurs at the same time as event X. For joint probability to hold, the two events must be independent of each other -- meaning no conditional relationship or mutual dependency should exist between them. Joint probability can be visualized using a Venn diagram.

### Key Takeaways

- Joint probability is a statistical measure that calculates the likelihood of two events occurring simultaneously.
- The two events must be independent of each other.
- Joint probability is also known as the intersection of two or more events.
- It differs from conditional probability, which is the probability of one event occurring given that another event has taken place.
- Venn diagrams can be used to visualize joint probability.

## Joint Probability Formula and Calculation

Joint probability can be expressed using several different notations. The following formula represents the probability of the intersection of events:

$$ \begin{aligned} & P\ \left ( X\bigcap Y \right ) \\ &\textbf{where:}\\ &X, Y = \text{two different intersecting events}\\ &P(X \text{ and } Y), P(XY) = \text{the joint probability of X and Y}\\ \end{aligned} $$

**Note:** While joint probability can help you determine the likelihood of two different events occurring simultaneously, it does not indicate how the two events influence each other.

## What Joint Probability Tells You

Probability is a field closely related to statistics that deals with the likelihood of an event or phenomenon occurring. Probability is quantified as a number between 0 and 1, where 0 represents impossibility and 1 represents certainty.

For example, the probability of drawing a red card from a deck is 1/2 = 0.5. This means there is an equal chance of drawing a red card or a black card, since each color has 26 cards. The probability is 50-50.

Joint probability measures the likelihood of two events occurring at the same time. It can only be applied when multiple observations can occur simultaneously. For instance, the joint probability of drawing a card from a standard deck that is both red and a 6 is P(6 $\cap$ red) = 2/52 = 1/26, since there are two red 6s in the deck -- the 6 of hearts and the 6 of diamonds. Because the events "red" and "6" are independent, you can also use the following formula:

$$ P(6 \cap red) = P(6) \times P(red) = 4/52 \times 26/52 = 1/26 $$

The symbol "$\cap$" in joint probability is called the intersection. The probability that event X and event Y both occur is the same as the point at which X and Y intersect. Therefore, joint probability is also known as the intersection of two or more events. A Venn diagram is one of the best visual tools for illustrating this intersection.

From the Venn diagram, the point where the two circles overlap is the intersection, containing two observations: the 6 of hearts and the 6 of diamonds.

## Joint Probability vs. Conditional Probability

Joint probability should not be confused with conditional probability, which is the probability of one event occurring given that another event has taken place. The conditional probability formula is:

$$ P(X, \text{ given } Y) \text{ or } P(X | Y) $$

This means the chance of one event depends on another event. For example, from a deck of cards, given that you drew a red card, the probability of it being a 6 is P(6|red) = 2/26 = 1/13, because there are two 6s among the 26 red cards.

Joint probability considers only the likelihood of two events occurring at the same time. Conditional probability can be used to calculate joint probability, as shown in the following formula:

$$ P(X \cap Y) = P(X|Y) \times P(Y) $$

The probability of events A and B occurring is the probability of event X occurring given event Y, multiplied by the probability of event Y. Using this formula, the joint probability of drawing a 6 and a red card is:

$$ \begin{aligned} &P(6 \cap red) = P(6|red) \times P(red) = \\ &1/13 \times 26/52 = 1/13 \times 1/2 = 1/26\\ \end{aligned} $$

Statisticians and analysts use joint probability as a tool for measuring the likelihood of two or more observable events occurring simultaneously. For example, joint probability can estimate the likelihood that Microsoft's stock price will decline at the same time as the Dow Jones Industrial Average (DJIA) drops, or that oil prices will rise when the U.S. dollar weakens.

**Important:** Joint probability depends on the two events being independent. To determine whether events are truly independent, it is important to understand whether the outcome of one event affects the other. If they influence each other, they are dependent, which leads to conditional probability. If there is no mutual influence, then you have joint probability.

## Example of Joint Probability

Here is another example to illustrate how joint probability works, using dice. We want to calculate the probability of rolling two fours. Remember that each die has six faces.

To determine the joint probability, we first need to find the probability of each individual roll:

- The chance of rolling a four on the first die is 1/6
- The chance of rolling a four on the second die is 1/6

Now we apply the joint probability formula by multiplying each individual probability:

1/6 x 1/6 = 1/36

This means the probability of rolling two fours with a pair of dice is 1/36.

## What Does Joint Probability Tell You?

Joint probability is a statistical measure that tells you the likelihood of two events occurring at the same time.

## What Are the Conditions for Joint Probability?

Certain conditions must be met for joint probability to apply. First, the two events must be able to occur simultaneously. Second, the two events must be independent -- their outcomes cannot influence each other.

## Can Joint Probability Be Greater Than 1?

No, joint probability can never be greater than 1. Joint probability values range between 0 and 1, where 0 represents the impossibility of two events occurring simultaneously and 1 represents certainty.

## Summary

Probability refers to the likelihood of an event occurring. When two variables are involved, you may encounter joint probability -- a statistical measure that tells you whether two independent events are likely to occur at the same time. For statisticians, this is an important metric for determining the relationship between two sets of variables, such as the relationship between gender and sports participation. However, it does not indicate how the two variables influence each other.
