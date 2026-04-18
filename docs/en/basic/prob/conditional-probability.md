![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# What Is Conditional Probability?
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

Conditional probability is a fundamental concept in probability theory that deals with the likelihood of an event occurring given that another event has already taken place.

It involves two or more related events and poses the question: "If we know event A has occurred, what is the chance that event B will occur?" Conditional probability is calculated by multiplying the probability of the preceding event by the updated probability of the subsequent (conditional) event.

### Key Takeaways

- Conditional probability refers to the likelihood that an outcome (A) will occur given that another event (B) has already occurred.
- It is typically written as "A given B": P(A|B), indicating that the probability of A depends on the occurrence of B.
- Conditional probability contrasts with unconditional (or marginal) probability.
- Probability can be categorized as conditional, marginal (the base probability of a single event independent of others), and joint (the probability of two events occurring simultaneously).
- Bayes' theorem is a mathematical formula that can be used to calculate conditional probabilities involving uncertain events.

## Understanding Conditional Probability

Conditional probability measures the likelihood of a particular outcome (A) based on the occurrence of some prior event (B).

If the occurrence of one event does not affect the probability of the other, the two events are called independent. However, if the occurrence (or non-occurrence) of one event affects the likelihood of the other, the events are dependent.

An example of dependent events is a company's stock price rising after reporting earnings that exceed expectations.

If events are independent, then the probability of event B is unaffected by whether event A occurs. For example, the rise in Apple's stock price has no connection to a decline in wheat prices.

Conditional probability is typically expressed as "A given B," written as P(A|B).

- Conditional probability contrasts with unconditional probability, also called marginal probability, which measures the likelihood of a single event occurring without regard to any other events. Conditional probability, by contrast, determines the likelihood of an event given that another event has occurred, linking the two together.
- The probability of independent events has no such interrelation; it examines the probability of an event in isolation, since the event is considered independent.
- Joint probability is the likelihood of two events occurring simultaneously. From these concepts, Bayes' theorem emerges, providing a way to mathematically reverse conditional probabilities. If you know the probability of event B given event A, you can compute the conditional probability of A given B.

Overall, while marginal and joint probabilities measure the likelihoods of individual and paired events, conditional probability captures the sequential relationships and dependencies between events.

**Note:** Conditional probability is widely applied in insurance, economics, politics, and various branches of mathematics.

## Conditional Probability Formula

$$ P(B|A) = P(A \text{ and } B) / P(A) $$

Or equivalently:

$$ P(B|A) = P(A\cap B) / P(A) $$

where:

P = Probability

A = Event A

B = Event B

**Important:** Unconditional probability, also called marginal probability, measures the chance of something occurring without consideration of any prior or external events. Since it ignores new information, it remains constant.

## Examples of Conditional Probability

### Example 1: Colored Balls

Step 1: Understand the scenario

You have a bag containing six red balls, three blue balls, and one green ball -- ten balls in total.

Step 2: Identify the events

- Event A: Drawing a red ball from the bag
- Event B: Drawing a ball that is not green

Step 3: Calculate the probability of Event B: P(B)

Event B is drawing a ball that is not green. Of the 10 balls, 9 are not green (6 red and 3 blue).

$$ P(B) = \text{(non-green balls)} / \text{(total balls)} = 9/10 $$

Step 4: Identify the intersection of Events A and B: P(A $\cap$ B)

The intersection involves drawing a ball that is both red and not green. Since all red balls are non-green, the intersection is simply drawing a red ball.

Step 5: Calculate the intersection probability: P(A $\cap$ B)

$$ P(A\cap B) = \text{(red balls)} / \text{(total balls)} = 6/10 = 3/5 $$

Step 6: Calculate the conditional probability: P(A|B)

Using the conditional probability formula P(A|B) -- the probability of drawing a red ball given the ball is not green:

$$ P(A|B) = P(A\cap B)/P(B) = (3/5)/(9/10) = 2/3 $$

Result: The conditional probability of drawing a red ball, given the ball drawn is not green, is 2/3.

### Example 2: Fair Six-Sided Die

Step 1: Understand the scenario

You have a fair six-sided die. You want to determine the probability of rolling an even number given that the number rolled is greater than 4.

Step 2: Identify the events

The sample space is {1, 2, 3, 4, 5, 6}. Define two events:

- Event A: Rolling an even number, meaning {2, 4, 6}.
- Event B: Rolling a number greater than 4, meaning {5, 6}.

Step 3: Calculate the probability of each event

P(A) is the probability of rolling an even number. Three of six outcomes are even: {2, 4, 6}. Thus, P(A) = 3/6 = 1/2.

P(B) is the probability of rolling a number greater than 4. Two of six outcomes qualify: {5, 6}. Thus, P(B) = 2/6 = 1/3.

Step 4: Identify the intersection of Events A and B

The intersection consists of outcomes satisfying both conditions. Only one outcome is both even and greater than 4: rolling a 6.

Step 5: Calculate the intersection probability

P(A $\cap$ B) is the probability of rolling a 6, since 6 is the only outcome that is both even and greater than 4. So P(A $\cap$ B) = 1/6.

Step 6: Calculate the conditional probability: P(B|A)

$$ P(B|A) = P(A\cap B) / P(A) $$

Substituting:

$$ P(B|A) = (1/6)/(1/2) = 1/3 $$

Result: Given that the number rolled is even, the probability that it is greater than 4 is 1/3.

### Example 3: University Admission, Scholarship, and Stipend

Step 1: Understand the scenario

A student wants to know their chances of being admitted to a university, then receiving a scholarship, and then receiving a stipend for books, meals, and housing.

Step 2: Identify the events

- Event A: Being admitted to the university.
- Event B: Receiving a scholarship after admission.
- Event C: Receiving a stipend for books, meals, and housing after receiving the scholarship.

Step 3: Calculate the probability of admission (Event A)

The university admits 100 out of every 1,000 applicants. Thus, P(A) = 100/1000 = 0.10, or 10%.

Step 4: Determine the probability of a scholarship given admission: P(B|A)

Among admitted students, 10 out of every 500 receive a scholarship:

$$ P(B|A) = 10/500 = 0.02 = 2\% $$

Step 5: Calculate the probability of admission and scholarship

$$ P(A\cap B) = P(A)\times P(B|A) = 0.1\times 0.02 = 0.002 = 0.2\% $$

Step 6: Determine the probability of a stipend given the scholarship: P(C|B)

Among scholarship recipients, 50% also receive the stipend. Thus, P(C|B) = 0.5 = 50%.

Step 7: Calculate the combined probability

$$ P(A\cap B\cap C) = P(A)\times P(B|A)\times P(C|B) = 0.1\times 0.02\times 0.5 = 0.001 = 0.1\% $$

This step-by-step analysis demonstrates how basic probability formulas and conditional probability can be used to calculate the probability of each scenario.

## Conditional Probability vs. Joint and Marginal Probability

Let us distinguish conditional probability from other types of probability using a standard deck of cards. Define two events:

- Event A: Drawing a four.
- Event B: Drawing a red card.

A standard deck has 52 cards across four suits (hearts, diamonds, clubs, spades). Hearts and diamonds are red; clubs and spades are black. Each suit has 13 cards.

The deck contains 26 red cards (13 hearts and 13 diamonds). The probability of drawing a red card is P(B) = 26/52 = 1/2.

Among the red cards, there is one four of hearts and one four of diamonds. Given a red card has been drawn, the conditional probability it is a four is:

$$ P(A|B) = \text{(red fours)} / \text{(total red cards)} = 2/26 = 1/13 $$

**Marginal probability** P(A) is the probability of Event A occurring on its own, without considering any other events.

Since Event A is drawing a four, P(A) is calculated by dividing the number of fours by the total number of cards:

$$ P(A) = 4/52 = 1/13 $$

**Joint probability** is the likelihood of two or more events occurring simultaneously, expressed as P(A $\cap$ B).

Using the same events, the joint probability of drawing a card that is both a four and red is:

$$ P(A\cap B) = 2/52 = 1/26 $$

## Bayes' Theorem and Conditional Probability

Bayes' theorem is used to calculate conditional probabilities when dealing with uncertain events. In investing, it can be applied to update the probability estimates of market outcomes after receiving new relevant data.

For example, suppose you want to know the probability that the S&P 500 will deliver a positive annual return given initial gross domestic product (GDP) data. You would first apply Bayes' theorem, considering the index's historical returns, to form a preliminary estimate of economic expansion.

You would then revise this preliminary probability using the latest GDP forecasts. This provides a more refined probability assessment that integrates all available evidence as the year progresses.

Although somewhat complex mathematically, Bayes' theorem is quite logical. If an investor discovers new economic information relevant to potential market returns, it is rational to incorporate that data for a more precise calculation.

This statistical technique was developed by the 18th-century English clergyman Thomas Bayes and remains central to financial modeling and other fields requiring predictions under uncertainty.

**Note:** Bayes' theorem is well suited for machine learning and is widely used in that field.

## What Is a Conditional Probability Calculator?

A conditional probability calculator is an online tool that computes conditional probabilities. It takes the probabilities of the first and second events as inputs, saving users from performing the calculations manually.

## What Is the Difference Between Probability and Conditional Probability?

Probability concerns the likelihood of a single event occurring. Conditional probability concerns the relationship between two events -- specifically, it is the probability of a second event occurring given that the first event has already occurred.

## What Is Prior Probability?

Prior probability is the probability of an event occurring before any data is collected. It is determined by prior beliefs. In Bayesian statistical inference, the prior probability is a key component, as it can be revised mathematically to produce a posterior probability.

## What Is Compound Probability?

Compound probability determines the likelihood of two independent events both occurring. It is calculated by multiplying the probability of the first event by the probability of the second event. The most common example is flipping a coin twice and determining whether the second result matches the first.

## Conclusion

Conditional probability examines the likelihood of an event occurring based on the probability of a preceding event. The second event depends on the first.

For example, we might want to know the probability that a particular stock will rise given that its sector index has increased. The conditional probability calculation accounts for both the likelihood of the first event (the stock price rising) and the overlap between the two events.
