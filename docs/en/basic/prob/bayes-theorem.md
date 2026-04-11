![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# Bayes' Theorem: Understanding Conditional Probability and Information Updating
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

Bayes' theorem, named after the 18th-century British mathematician Thomas Bayes, is a mathematical formula for determining conditional probability. Conditional probability is the likelihood of an outcome occurring based on a previous outcome in similar circumstances. Bayes' theorem provides a way to revise existing predictions or theories (update probabilities) when new evidence or additional information becomes available.

In finance, Bayes' theorem can be used to assess the risk of lending money to potential borrowers. The theorem is also known as Bayes' Rule or Bayes' Law and forms the foundation of Bayesian statistics.

### Key Takeaways

- Bayes' theorem allows you to update the predicted probability of an event by incorporating new information.
- It is named after 18th-century mathematician Thomas Bayes.
- It is frequently employed in finance to calculate or update risk assessments.
- Due to the large volume of computation required, Bayes' theorem went largely unused for two centuries after its development.

## Understanding Bayes' Theorem

The applications of Bayes' theorem extend well beyond finance. For example, it can be used to assess the accuracy of medical test results by considering the general likelihood that a person has a disease and the test's overall accuracy. Bayes' theorem relies on incorporating prior probability distributions to generate posterior probabilities.

In Bayesian statistical inference, the prior probability is the probability of an event occurring before new data is collected. In other words, it represents the best rational assessment of the probability of a particular outcome based on current knowledge before an experiment is conducted.

The posterior probability is the revised probability of an event occurring after taking new information into account. It is calculated by updating the prior probability using Bayes' theorem. From a statistical perspective, the posterior probability is the probability of event A occurring given that event B has already occurred.

## Special Considerations

Bayes' theorem provides the probability of an event based on new information that is, or may be, related to that event. The formula can also be used to determine how hypothetical new information might affect the probability of an event occurring, assuming the new information turns out to be true.

For example, consider drawing a single card from a complete deck of 52 playing cards.

There are four kings in the deck, so the probability of drawing a king is 4/52, which equals 1/13, or approximately 7.69%. Now suppose it is revealed that the selected card is a face card. The conditional probability that it is a king, given it is a face card, is 4/12, or approximately 33.3%, since there are 12 face cards in the deck.

## Bayes' Theorem Formula

## Examples of Bayes' Theorem

Below are two examples of Bayes' theorem. The first shows how the formula can be derived through a stock investment example involving Amazon.com Inc. (AMZN). The second applies Bayes' theorem to drug testing.

Bayes' theorem follows simply from the axioms of conditional probability -- the probability of an event given that another event has occurred. For example, a simple probability question might be: "What is the probability that Amazon's stock price will decline?" Conditional probability takes this further: "What is the probability that AMZN's stock price will decline given that the Dow Jones Industrial Average (DJIA) has previously declined?"

The conditional probability of A given that B has occurred can be expressed as:

If A is "AMZN price declines," then P(AMZN) is the probability that AMZN declines; B is "DJIA has already declined," and P(DJIA) is the probability that the DJIA declined. The conditional probability expression reads: "The probability that AMZN declines given the DJIA has declined equals the joint probability of AMZN declining and the DJIA declining, divided by the probability of the DJIA index declining."

P(AMZN and DJIA) is the probability of both A and B occurring simultaneously. This is also equal to the probability of A occurring multiplied by the probability of B occurring given that A has occurred: P(AMZN) x P(DJIA|AMZN). The fact that these two expressions are equal leads to Bayes' theorem, expressed as:

P(AMZN) and P(DJIA) are the probabilities of Amazon and the Dow Jones declining independently of each other.

The formula explains the relationship between the probability of the hypothesis before seeing the evidence, P(AMZN), and the probability of the hypothesis after obtaining the evidence, P(AMZN|DJIA), given evidence from the Dow Jones.

As a numerical example, suppose there is a drug test that is 98% accurate -- meaning it returns a correct positive result for drug users 98% of the time and a correct negative result for non-users 98% of the time.

Next, assume that 0.5% of people use the drug. If a randomly selected person tests positive, the following calculation can be performed to determine the probability that the person actually uses the drug, using these terms:

- A = probability that the positive test result is true
- B = proportion of people who use the drug
- A x B = probability that the positive result is true
- (1 - A) x (1 - B) = probability that the negative result is true

The formula yields:

Using these values, the calculation shows:

Bayes' theorem demonstrates that even in this scenario, a person who tests positive has only a 19.76% probability of actually using the drug, while the probability of not using the drug is 80.24%.

## What Is Bayes' Rule Used For?

Bayes' rule is used to update probabilities with new conditional variables. Investment analysts use it to forecast probabilities in the stock market, but it finds applications across many other industries as well.

## Why Is Bayes' Theorem So Powerful?

Mathematically, it demonstrates that two probabilities are equivalent. Whether in statistics, investing, or other industries, this enables you to examine conditional probabilities from different angles.

## How Do You Know When to Use Bayes' Theorem?

You can use Bayes' theorem whenever you need to determine the probability of a situation occurring given the presence of other conditions that may influence its occurrence.

## Conclusion

At its simplest, Bayes' theorem takes a test result and relates it to the conditional probability of that test result given other related events. For high-probability false positives, the theorem provides a more reasoned likelihood of a particular outcome.
