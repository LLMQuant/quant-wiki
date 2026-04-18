![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# What Is Backtesting?
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)
Backtesting is a general method for assessing how well a strategy or model would have performed in the past. It evaluates the viability of a trading strategy by applying it to historical data. If the backtest yields positive results, traders and analysts may have confidence in deploying the strategy going forward.

### Key Takeaways

- Backtesting evaluates the viability of a trading strategy or pricing model by examining how it would have performed using historical data.
- The underlying premise is that any strategy that performed well in the past is likely to perform well in the future, and vice versa.
- When testing ideas on historical data, it is beneficial to reserve a time period for out-of-sample testing. If the test is successful, validating it against alternative time periods or out-of-sample data can further bolster confidence.

## Understanding Backtesting

Backtesting allows traders to simulate a trading strategy using historical data, generating results and analyzing risk and profitability before committing real capital.

A well-conducted backtest that yields positive results assures traders that the strategy is fundamentally sound and is likely to produce profits when implemented in live markets. Conversely, a backtest that yields suboptimal results will prompt traders to modify or abandon the strategy.

**Important:** Particularly complex trading strategies, such as those implemented by automated trading systems, rely heavily on backtesting to prove their worth, as they are too complex to evaluate by other means.

Any trading idea that can be quantified can be backtested. Some traders and investors may seek the expertise of a qualified programmer to develop the idea into a testable form. This typically involves coding the idea into the proprietary language supported by the trading platform.

Programmers can incorporate user-defined input variables, allowing traders to "tune" the system. For example, in a simple moving average (SMA) crossover system, the trader could input (or change) the lengths of the two moving averages used in the system. The trader could then backtest to determine which moving average lengths would have performed best on the historical data.

## The Ideal Backtesting Scenario

The ideal backtest selects sample data from a relevant time period of sufficient duration to reflect a variety of market conditions. This allows for a better assessment of whether the backtest results are a fluke or represent sound trading performance.

The historical data set must include a genuinely representative sample of stocks, including those of companies that eventually went bankrupt, were acquired, or were liquidated. Including only the historical data of stocks that still exist today will introduce survivorship bias and artificially inflate backtest returns.

A backtest should account for all trading costs, no matter how insignificant they may seem, as these can accumulate over the backtesting period and substantially affect the appearance of a strategy's profitability. Traders should ensure their backtesting software accounts for these costs.

Out-of-sample testing and forward performance testing provide further confirmation of a system's effectiveness and can reveal a system's true performance before real money is at stake. A strong correlation between backtesting, out-of-sample, and forward performance testing results is critical for determining the viability of a trading system.

## Backtesting vs. Forward Performance Testing

Forward performance testing, also known as paper trading, provides traders with another set of out-of-sample data on which to evaluate a system. Forward performance testing simulates actual trading by following the system's logic in a live market. It is called paper trading because all trades are executed on paper only -- that is, trade entries and exits along with any profit or loss are recorded, but no real trades are executed.

A crucial aspect of forward performance testing is following the system's logic precisely; otherwise, it becomes difficult, if not impossible, to accurately evaluate this step of the process. Traders should be honest about any trade entry or exit and avoid behaviors such as cherry-picking trades or rationalizing not recording a trade on paper by saying "I would never have taken that trade." If the trade would have occurred according to the system's logic, it should be documented and evaluated.

## Backtesting vs. Scenario Analysis

While backtesting uses actual historical data to test for fit or success, scenario analysis uses hypothetical data to simulate various possible outcomes. For example, scenario analysis might simulate specific changes in portfolio securities' values or key factors such as changes in interest rates.

Scenario analysis is commonly used to estimate changes in a portfolio's value in response to an adverse event and may be used to examine a theoretical worst-case scenario.

## Common Pitfalls of Backtesting

For backtesting to produce meaningful results, traders must develop and test their strategies in good faith while avoiding bias as much as possible. This means the strategy should be developed without relying on the data used for backtesting.

This is harder than it sounds. Traders typically build strategies based on historical data. They must be disciplined about testing with data sets different from those on which they trained their models. Otherwise, the backtest will produce inflated results that have no practical value.

Similarly, traders must avoid data mining -- testing a wide range of hypothetical strategies against the same data set -- which will also produce results that fail in live markets, since many invalid strategies happen to beat the market in a specific period by pure chance.

One way to compensate for the tendency toward data mining or cherry-picking is to use a strategy that succeeds in the relevant, or in-sample, time period and then backtest it with data from a different, out-of-sample time period. If in-sample and out-of-sample backtests yield similar results, they are more likely to be validated.

## About LLMQuant
LLMQuant is a cutting-edge community composed of professionals from world-leading universities and the quantitative finance industry, dedicated to exploring the frontiers of artificial intelligence (AI) and quantitative (Quant) research. Our team members hail from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other top institutions, with external advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and leading proprietary trading firms.
