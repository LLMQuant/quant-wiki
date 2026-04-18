![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# What Is Gamma?
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)
Gamma is an options risk metric that describes the rate of change of an option's delta for each one-point move in the underlying asset's price. Delta measures how much an option's premium (price) changes for a one-point move in the underlying; gamma, in turn, measures how the rate of that price change itself shifts as the underlying fluctuates. The higher the gamma, the more volatile the option's price.

Gamma is a key measure of the convexity of a derivative's value relative to the underlying asset. It is one of the "options Greeks," used alongside delta, rho, theta, and vega to assess different types of risk in an options portfolio.

### Key Takeaways

- Gamma is the rate of change in an option's delta per one-point move in delta's price.
- It is a second-order risk factor, sometimes called the delta of delta.
- Gamma is highest when an option is at the money and lowest when it is deep in or out of the money.
- All else equal, options closer to expiration have higher gamma than longer-dated options.
- Gamma is used to gauge how a move in the underlying asset will affect an option's moneyness.
- Delta-gamma hedging can protect an options position against moves in the underlying asset.

## Understanding Gamma

Gamma is the first derivative of delta and is used to measure an option's price movement relative to its degree of being in or out of the money. It describes how delta changes as the underlying asset moves. Thus, if an option's delta is +0.40 and its gamma is 0.10, a $1 increase in the underlying price would cause the option's delta to become +0.50.

Gamma is small when the option being measured is deep in the money or deep out of the money. It is largest when the option is near or at the money. Gamma is also larger for options closer to expiration than for longer-dated options.

Gamma is an important metric because it accounts for convexity when executing hedging strategies.[1] Some portfolio managers or traders deal with portfolios of such large value that even greater precision is needed when hedging. A third-order derivative called "color" can be used. Color measures the rate of change of gamma and is important for maintaining a gamma-hedged portfolio.

**Note:** In a physics analogy, an option's delta is its "velocity," while its gamma is its "acceleration."

## What Is Gamma Used For?

Since an option's delta measure is valid only for a short period, gamma gives traders a more precise picture of how the option's delta will change over time as the underlying price moves. Delta is the change in option price relative to the change in the underlying asset's price.

As an option moves deeper into the money, gamma decreases and approaches zero, while delta approaches 1. As an option moves further out of the money, gamma also approaches zero. Gamma is highest when the price is at the money.

Calculating gamma is complex and typically requires financial software or spreadsheets to find a precise value. The following illustrates an approximate calculation: consider a call option on an underlying stock that currently has a delta of 0.40. If the stock increases by $1.00, the option would increase in value by 40 cents, and its delta would also change. After the $1 increase, suppose the option's delta is now 0.53. The difference of 0.13 in deltas can be considered an approximation of gamma.

**Important:** All long option positions have positive gamma, and all short options have negative gamma.

## Gamma Example

Suppose a stock is trading at $10 and its option has a delta of 0.5 and a gamma of 0.10. For every $1 move in the stock price, delta will be adjusted by 0.10. A $1.00 increase means the option's delta will rise to 0.60. Likewise, a $1.00 decrease will cause delta to fall to 0.40.

## How Do Traders Hedge Gamma?

Gamma hedging is a strategy that seeks to maintain a constant delta in an options position. This is achieved by buying and selling options that offset each other so that the net gamma is near zero. At that point, the position is said to be gamma-neutral. Typically, traders also want to maintain zero gamma around a delta-neutral (zero-delta) position. This is accomplished through delta-gamma hedging, where both net delta and net gamma are near zero. In such a case, the value of the options position is insulated from changes in the underlying asset's price.

## What Is a Long Gamma Strategy?

If a trader is long gamma, the delta of their options position increases as the underlying asset's price moves. For example, a long gamma position will see delta rise as the underlying price increases and delta fall as the price decreases. If the trader can sell delta as the price rises and buy delta as it falls, the long gamma exposure can produce a net profit by incentivizing a pattern of systematically buying low and selling high.

## What Is Gamma Risk?

For options positions that are short gamma, there is a risk of compounding losses from moves in the underlying price. For example, if such a position starts delta-neutral and the stock rises, it will generate increasingly negative delta for the position, meaning the option loses progressively more money as the underlying climbs. However, the risk also exists that if delta is purchased at these higher prices, the underlying may reverse direction and fall, generating long delta on the way down and compounding earlier losses.

## Conclusion

Gamma measures the rate of change of delta for each one-point increase in the underlying asset. It is a valuable tool that helps traders anticipate changes in the delta of an option or an overall position. Gamma is larger for at-the-money options and progressively decreases for both in-the-money and out-of-the-money options. Unlike delta, gamma is always positive for long calls and long puts.

## References

[1] Sheldon Natenberg. "Option Volatility Trading Strategies." John Wiley & Sons, 2012.

## About LLMQuant
LLMQuant is a cutting-edge community composed of professionals from world-leading universities and the quantitative finance industry, dedicated to exploring the frontiers of artificial intelligence (AI) and quantitative (Quant) research. Our team members hail from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other top institutions, with external advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and leading proprietary trading firms.
