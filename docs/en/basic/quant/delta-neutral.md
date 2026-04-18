![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# What Is Delta Neutral?
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)
Delta neutral is a portfolio strategy that balances long and short positions so that the overall delta of the assets is zero. Options traders use delta neutral strategies to profit from implied volatility or the time decay of options. These strategies are also employed for hedging purposes. Below, we explain this strategy for both beginners and experienced traders.

### Key Takeaways

- Delta neutral is a portfolio strategy that balances positive and negative delta across multiple positions so that the overall delta sums to zero.
- A delta neutral portfolio offsets its response to market movements within a certain range, bringing the net change of the position to zero.
- Options traders use delta neutral strategies to profit from implied volatility or the time decay of options.
- Delta neutral strategies are also used for hedging purposes.

## Understanding Delta Neutral

Understanding the concept of delta is essential in options trading. Delta is one of the "Greeks" in finance, measuring the sensitivity of an option's price to changes in the price of the underlying asset. More specifically, delta measures the expected change in an option's price for every $1 move in the underlying security. For example, a call option with a delta of 0.25 and a value of $1.40 would be expected to rise to $1.65 if the underlying asset increases by $1.

A portfolio's delta can be positive, negative, or neutral, depending on the positions held:

An investor seeking delta neutrality aims to balance these deltas so that the portfolio's overall delta is zero. This balance means the portfolio will not change in value with small increases or decreases in the underlying asset's price. However, large price swings, changes in volatility, and the passage of time can still affect the portfolio's value. Achieving delta neutrality typically requires continuous adjustment, as market movements can push the delta away from zero.

## How Delta Neutral Works

A positive delta means the option's price rises when the stock price goes up and falls when the stock price drops. Conversely, a negative delta means the option's price moves inversely to the stock price. Before explaining the strategy further, let us clarify some key terms:

- **Long and short positions:** A long position means you own the asset and expect its value to increase over time. A short position means you have sold the asset short, expecting its price to decline.
- **Call and put options:** These are the two types of options contracts. A call option gives the holder the right to buy an asset at a specific price within a specific period. A put option gives the holder the right to sell an asset at a specific price within a specific period.
- **Delta values:** Long put options have deltas ranging from -1 to 0, while long call options always have deltas between 0 and +1. For the underlying asset (typically a stock), a long position always has a delta of 1, and a short position has a delta of -1. Combining negative and positive deltas can bring the overall delta to zero.

Now we can see how a delta neutral strategy works to achieve a delta of zero. Suppose you hold a long position in a stock (delta of +1). To make that position delta neutral, you could purchase a put option on the stock (with a delta ranging from -1 to 0). This is particularly evident with deep in-the-money call options. If the stock price rises by $1, the long position gains $1 (because delta is +1). However, the put option's price will decline, offsetting the gain from the long position. This ensures that the portfolio's overall value remains unchanged even if the stock price moves.

Similarly, if an option has a delta of zero and the stock rises by $1, the option's price will not increase (common with deep out-of-the-money call options). If an option has a delta of 0.5, then for every $1 increase in the underlying stock, the option's price increases by $0.50. This is because the delta (0.5) multiplied by the stock price change ($1) yields a $0.50 change in the option's price.

Suppose you hold 200 shares of Company X at $100 per share, and you believe the stock will rise over the long term. However, you are concerned about a short-term decline, so you decide to establish a delta neutral position to hedge this directional risk.

Holding 200 shares gives you a delta of +200. You need to find offsetting option contracts to produce a delta of -200.

Assume you find an at-the-money put option on Company X with a delta of -0.50. The negative sign reflects the fact that put options gain value when the underlying price falls and lose value when it rises. Since each stock option represents 100 shares of the underlying asset, buying one put option on Company X provides: -0.50 x 100 = -50 delta.

If you buy four such put options, your total delta is: 4 x 100 x -0.50 = -200.

By combining 200 shares of Company X with 4 at-the-money put options, your overall position achieves delta neutrality.

**Important:** While an initial delta hedge can establish a neutral position, the delta of the options will change as the underlying stock moves. This is known as the option's gamma. Therefore, traders who wish to maintain delta neutrality must monitor and adjust their positions to re-establish a balanced delta. This process is called dynamic hedging.

## Pros and Cons of Delta Neutral Positions

### Advantages

- Hedges against small price movements
- Allows options traders to focus on non-directional strategies
- Offers flexibility in constructing delta neutral positions

### Disadvantages

- Large sudden moves can expose directional risk due to gamma
- Monitoring and adjusting can be expensive and time-consuming

The primary benefit of a delta neutral position is its immunity to small price movements in the underlying asset, whether up or down. This strategy is about anticipating how stock prices will change without worrying about minor fluctuations.

Delta neutral traders typically seek to profit from the time decay of options (represented by the Greek letter theta) or from changes in implied volatility (the Greek letter vega), rather than focusing on directional stock movements. Since delta neutrality focuses on offsetting price movement risk, traders can concentrate on other factors that affect option value.

However, delta neutrality also means missing out on those price movements, which represents an opportunity cost for some traders. Even if you are not concerned about price changes, maintaining a delta neutral position still requires active monitoring and adjustment as the underlying asset fluctuates, which can be costly and unsuitable for inexperienced traders.

Furthermore, large sudden market movements can lead to significant losses, since the position is only neutral against small price changes. Significant and sudden market events can therefore undermine the strategy.

## How Does Delta Hedging Work?

Delta hedging minimizes directional risk associated with price changes in the underlying asset by using offsetting positions in options contracts. The typical approach is to buy or sell options that have an equal but opposite exposure to the underlying asset. In this way, gains (losses) in the underlying asset are offset by equivalent losses (gains) in the options position.

## Can You Achieve Delta Neutrality Using Call or Put Options?

Yes. If you hold shares of a stock, you can buy put options or sell call options. You can also create a delta neutral position using only options -- for example, by holding an at-the-money straddle in which you buy a call option with a delta of +0.50 and a put option with a delta of -0.50.

## How Do Options Traders Profit from Delta Neutral Positions?

Options traders can profit from delta neutral positions by selling options and collecting time decay over time. By eliminating exposure to small price fluctuations, this strategy can be optimized. Similarly, traders may bet that the volatility of the underlying asset will rise or fall in the future. A delta neutral position allows such traders to isolate the volatility factor from market direction.

## Summary

Delta neutral occurs when a trader's net position offsets market price movements, whether up or down. This is achieved by offsetting the delta of one financial instrument with the deltas of others. This balance means that small changes in the underlying asset's price have virtually no impact on the overall value of the combined position (e.g., stock plus options). The idea is that gains on one side offset losses on the other.

However, it is important to remember that delta is not static; it changes with market movements (gamma) and over time. Maintaining a delta neutral position therefore typically requires ongoing adjustments, known as dynamic hedging.

## References

[1] D. Passarelli. "[Trading Options Greeks: How Time, Volatility, and Other Pricing Factors Drive Profits](https://www.wiley.com/en-gb/Trading+Options+Greeks:+How+Time,+Volatility,+and+Other+Pricing+Factors+Drive+Profits,+2nd+Edition-p-9781118225127)." John Wiley & Sons, 2020. Pages 237-268.
