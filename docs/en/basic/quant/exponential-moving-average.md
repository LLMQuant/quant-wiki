![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# What Is an Exponential Moving Average (EMA)?
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)
An exponential moving average (EMA) is a type of weighted moving average (MA) that assigns greater weight and significance to the most recent data points. It is also referred to as an exponentially weighted moving average. Compared to a simple moving average (SMA), which assigns equal weight to all observations in the period, the EMA reacts more significantly to recent price changes.

### Key Takeaways

- The EMA is a moving average that places greater weight on the most recent data points.
- Like all moving averages, this technical indicator is used to generate buy and sell signals based on crossovers and divergences from the historical average.
- Traders commonly use several EMA lengths, such as 10-day, 50-day, and 200-day moving averages.

## Exponential Moving Average (EMA) Formula

$$ \begin{aligned} &\begin{aligned} EMA_{\text{today}}=&\left(\text{Value}_{\text{today}}\ast\left(\frac{\text{Smoothing}}{1+\text{Days}}\right)\right)\\ &+EMA_{\text{yesterday}}\ast\left(1-\left(\frac{\text{Smoothing}}{1+\text{Days}}\right)\right)\end{aligned}\\ &\textbf{where:}\\ &EMA=\text{Exponential Moving Average} \end{aligned} $$

While there are many possible choices for the smoothing factor, the most common is:

- Smoothing = 2

This gives greater weight to the most recent observation. As the smoothing factor increases, the influence of recent observations on the EMA grows accordingly.

## Calculating the EMA

Calculating the EMA requires one more observation than the SMA. Suppose you want to use 20 days as the number of observations for the EMA. You must wait until the 20th day to obtain the SMA. On the 21st day, you can then use the prior day's SMA as the first EMA for the previous day.

The SMA calculation is straightforward. It is simply the sum of the stock's closing prices over the period divided by the number of observations. For example, a 20-day SMA is the sum of the closing prices over the past 20 trading days divided by 20.

Next, you calculate the multiplier for smoothing (weighting) the EMA, which typically follows the formula: [2 / (number of observations + 1)]. For a 20-day moving average, the multiplier would be [2 / (20 + 1)] = 0.0952.

Finally, the following formula is used to calculate the current EMA:

- EMA = Closing Price x Multiplier + EMA (previous day) x (1 - Multiplier)

The EMA assigns higher weight to recent prices, while the SMA assigns equal weight to all values. The weighting applied to the most recent price is greater for a shorter-period EMA than for a longer-period EMA. For example, an 18.18% multiplier is applied to the most recent price data for a 10-period EMA, while only a 9.52% weighting applies to a 20-period EMA.

Slight variations of the EMA can also be computed using the open, high, low, or median price instead of the closing price.

## What Does the EMA Tell You?

The 12-day and 26-day exponential moving averages are among the most commonly cited and analyzed short-term averages. The 12-day and 26-day EMAs are used to create indicators such as the moving average convergence divergence (MACD) and the percentage price oscillator (PPO). In general, the 50-day and 200-day EMAs are used as indicators of long-term trends. When a stock price crosses its 200-day moving average, it is typically regarded as a technical signal that a reversal has occurred.

Traders who employ technical analysis find moving averages very useful and insightful when applied correctly. However, they also recognize that these signals can be misleading when used improperly or misinterpreted. All moving averages commonly used in technical analysis are lagging indicators.

Therefore, conclusions drawn from applying a moving average to a particular market chart should serve to confirm a market move or indicate its strength. Often, by the time a moving average indicator line has shifted to reflect a significant move in the market, the optimal point of entry has already passed.

The EMA does help to mitigate the negative impact of lag to some degree. Because the EMA calculation places more weight on recent data, it "hugs" the price action more closely and reacts more quickly. This is particularly desirable when using an EMA to generate a trading entry signal.

Like all moving average indicators, the EMA is better suited for trending markets. When the market is in a strong and sustained uptrend, the EMA indicator line will also show an uptrend, and vice versa. A vigilant trader pays attention to both the direction of the EMA line and the rate of change from one bar to the next. For example, suppose a strong uptrend's price action begins to flatten and reverse. From an opportunity cost perspective, it might be time to switch to a more bullish investment.

## Examples of How to Use the EMA

The EMA is commonly used in conjunction with other indicators to confirm significant market moves and gauge their validity. For traders who operate on intraday and fast-moving markets, the EMA is especially applicable. Traders often use the EMA to determine a trading bias. If the EMA on a daily chart shows a strong upward trend, an intraday trader's strategy might be to trade only on the long side.

## Difference Between EMA and SMA

The major difference between the EMA and SMA is the sensitivity each one shows to changes in the data used in its calculation.

Specifically, the EMA gives a higher weighting to recent prices, while the SMA assigns equal weight to all values. The two averages are similar in that they are interpreted in the same manner and are both commonly used by technical traders to smooth out price fluctuations.

Since the EMA places a higher weight on recent data than on older data, it is more responsive to the latest price changes than the SMA. This makes the EMA's results more timely, which explains why many traders prefer it.

## Limitations of the EMA

It is not clear whether more emphasis should be placed on the most recent days in the period. Many traders believe that new data better reflects the current trend of the security. At the same time, others feel that overemphasizing recent dates introduces a bias that leads to more false signals.

Similarly, the EMA relies entirely on historical data. Many economists believe that markets are efficient, meaning that current market prices already reflect all available information. If markets are indeed efficient, using historical data should not provide any insight into the future direction of asset prices.

## What Is a Good Exponential Moving Average?

Longer-day EMAs (e.g., 50-day and 200-day) tend to be used more by long-term investors, while short-term investors tend to use 8-day and 20-day EMAs.

## Is the Exponential Moving Average Better Than the Simple Moving Average?

The EMA places more emphasis on recent price movements, which means it tends to respond to price changes more quickly than the SMA.

## How Do You Interpret the Exponential Moving Average?

Investors generally view a rising EMA as support for price action and a falling EMA as resistance. Based on this interpretation, investors look for buying opportunities when the price is near a rising EMA and selling opportunities when the price is near a falling EMA.
