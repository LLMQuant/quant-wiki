![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# What Is Gamma Neutral?
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

A gamma-neutral options position is one that has been immunized against large moves in the underlying security. Achieving a gamma-neutral position is a method of managing risk in options trading by constructing a portfolio of assets whose delta's rate of change is near zero, regardless of whether the underlying rises or falls. This is known as gamma hedging. A gamma-neutral portfolio is therefore hedged against second-order time-price sensitivity.

Gamma is one of the "options Greeks," alongside delta, rho, theta, and vega. These Greeks are used to assess different types of risk in options portfolios.[1]

### Key Takeaways

- A gamma-neutral portfolio is an options position whose delta remains unchanged even when the underlying security moves significantly.
- Gamma neutrality is achieved by adding additional option contracts to a portfolio, typically in contrast to the current position -- a process known as gamma hedging.
- Delta-gamma hedging is commonly used to lock in profits by creating a position that is simultaneously delta-neutral and gamma-neutral.

## Understanding Gamma Neutral

The directional risk of an options portfolio can be managed through delta hedging, creating a delta-neutral or directionally ambiguous portfolio. The challenge is that as the underlying security's price changes, the option's delta itself shifts, meaning a delta-neutral position can gain or lose delta and become a directional bet -- especially if the underlying moves significantly. Gamma hedging seeks to neutralize this change in delta.

A gamma-neutral portfolio can be constructed by taking positions with offsetting gamma values. This helps reduce fluctuations caused by changing market prices and conditions. However, a gamma-neutral portfolio still carries risk. For example, if the assumptions used to establish the portfolio prove incorrect, a position that should be neutral may actually become risky. Furthermore, the position requires rebalancing as prices change and time passes.

Gamma-neutral options strategies can be used to create new security positions or to adjust existing ones. The goal is to use a combination of options that keeps the overall gamma value as close to zero as possible. At near-zero gamma, the delta value should not shift when the underlying security's price moves.

If the goal is to achieve a durable delta-neutral strategy, one would typically employ delta-gamma hedging. However, a trader may also want to maintain a specific delta position -- which could be positive or negative -- while remaining gamma-neutral.

Locking in profits is a common use case for gamma-neutral positions. If a period of high volatility is anticipated and an options trading position has generated a healthy profit so far, rather than selling the position to lock in gains and forgo further upside, a delta-neutral or gamma-neutral hedge can effectively preserve those profits.

## Gamma Neutral vs. Delta Neutral

A simple delta hedge can be created by purchasing call options while simultaneously shorting a corresponding number of shares of the underlying stock. If the stock price remains unchanged but volatility rises, the trader may profit -- unless time decay erodes those gains. A trader can add a short call at a different strike price to the strategy to offset time-value decay and protect against a large move in delta. Adding that second call to the position constitutes a gamma hedge.

As the underlying stock rises and falls, an investor can buy or sell shares to keep the position neutral. This can increase the volatility and costs of the trade. Delta and gamma hedging do not need to be perfectly neutral; traders can adjust how much positive or negative gamma they are exposed to over time.

## References

[1] TD Ameritrade. "[Stock Options Greeks: Gamma Explained](https://tickertape.tdameritrade.com/trading/trading-stock-options-gamma-17718)."

## About LLMQuant
LLMQuant is a cutting-edge community composed of professionals from world-leading universities and the quantitative finance industry, dedicated to exploring the frontiers of artificial intelligence (AI) and quantitative (Quant) research. Our team members hail from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other top institutions, with external advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and leading proprietary trading firms.
