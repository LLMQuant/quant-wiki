![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# What Is Gamma Hedging?
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

Gamma hedging is a trading strategy designed to keep the delta of an options position stable -- typically delta-neutral -- as the underlying asset's price changes. It is used to reduce the risk created by sharp upward or downward moves in the underlying security, particularly in the final days before expiration.

The gamma of an options position represents the rate of change of the option's delta for each one-point move in the underlying asset's price. Gamma is a key measure of the convexity of a derivative's value relative to the underlying. By comparison, a delta hedge alone only mitigates the impact of small price changes on the option's price.

### Key Takeaways

- Gamma hedging is a sophisticated options strategy used to reduce an options position's exposure to large moves in the underlying security.
- Gamma hedging also protects against rapid price changes that can occur as expiration approaches.
- Gamma hedging is often used in conjunction with delta hedging.

## How Gamma Hedging Works

A gamma-neutral options position is one that has been immunized against large moves in the underlying security. Achieving gamma neutrality is a risk management approach that constructs a portfolio whose delta's rate of change is near zero, regardless of whether the underlying rises or falls. This process is called gamma hedging. A gamma-neutral portfolio is thereby hedged against second-order time-price sensitivity.

Gamma hedging involves adding additional option contracts to a portfolio, typically opposite to the current position. For example, if a position holds a large number of calls, the trader might add a small put position to offset an unexpected price decline over the next 24 to 48 hours, or sell a carefully selected quantity of calls at a different strike price. Gamma hedging is a sophisticated activity that requires careful calculation to execute properly.

## Gamma and Delta

Gamma is a standard Greek-letter variable originating from the Black-Scholes model, the first widely recognized formula for options pricing. Within this framework, two variables help traders understand how option prices change as the underlying security's price moves: delta and gamma.

Delta tells a trader how much the option's price is expected to change for a small move -- specifically a $1 move -- in the underlying stock or asset.

Gamma refers to the rate of change of an option's delta as the underlying stock or asset price changes. In essence, gamma is the rate of change of the rate of change of the option's price. Some traders also think of gamma as the expected change resulting from two consecutive $1 moves in the underlying. Adding gamma to delta gives the expected change from a $2 move in the underlying security.

## Delta-Gamma Hedging

Delta-gamma hedging is an options strategy that combines both delta and gamma hedges to mitigate risk from changes in both the underlying asset and in delta itself. Delta hedging alone protects a position from small changes in the underlying. However, larger moves will alter the hedge (change the delta), leaving the position exposed. By adding a gamma hedge, the delta hedge remains intact.

When implementing delta-gamma hedging, an investor needs to create new hedges as the underlying asset's delta changes. The number of underlying shares bought or sold varies depending on whether the underlying price is rising or falling, and by how much.

A trader seeking to maintain a delta-hedged or delta-neutral position is typically making a trade whose value changes little with small short-term price fluctuations. Such a trade is often a bet on volatility -- that is, a bet that demand for that security's options will increase or decrease significantly in the future. Yet even delta hedging cannot fully protect an options trader on the day before expiration. On that day, because so little time remains before expiration, even normal price fluctuations in the underlying security can cause significant price changes in the option. Delta hedging alone is therefore insufficient.

Gamma hedging supplements a delta-hedging strategy to protect the trader against larger-than-expected changes, or to protect the entire portfolio -- especially when time value has almost entirely decayed -- against rapid price changes in the option.

**Important:** While traders in many cases seek a delta-gamma hedge that is delta-neutral, they may alternatively wish to maintain a specific delta position -- which could be positive or negative -- while simultaneously maintaining gamma neutrality.

## Gamma Hedging vs. Delta Hedging

As described above, delta hedging and gamma hedging are often used together. A simple delta hedge can be created by purchasing call options while simultaneously shorting a corresponding number of shares of the underlying stock. If the stock price remains unchanged but volatility rises, the trader may profit -- unless time-value decay erodes those gains. Adding a short call at a different strike price offsets time-value decay and protects against a large shift in delta; adding that second call to the position constitutes a gamma hedge.

As the underlying stock's value rises and falls, an investor can buy or sell shares to keep the position neutral. This may increase the volatility and costs of the trade. Delta and gamma hedging do not need to be perfectly neutral; traders can adjust the degree of positive or negative gamma exposure over time.

## About LLMQuant
LLMQuant is a cutting-edge community composed of professionals from world-leading universities and the quantitative finance industry, dedicated to exploring the frontiers of artificial intelligence (AI) and quantitative (Quant) research. Our team members hail from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other top institutions, with external advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and leading proprietary trading firms.
