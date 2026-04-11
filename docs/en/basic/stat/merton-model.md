![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# What Is the Merton Model?
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

The Merton model is a mathematical formula that stock analysts and commercial loan officers can use to assess a corporation's credit default risk. Named after economist Robert C. Merton, who proposed it in 1974, the model evaluates a company's structural credit risk by treating the company's equity as a call option on its assets.

### Key Takeaways

- In 1974, economist Robert C. Merton proposed a model for assessing credit risk by modeling a company's equity as a call option on its assets.
- Today, the Merton model is used by stock analysts, commercial loan officers, and others.
- Merton, along with fellow economist Myron S. Scholes, was awarded the Nobel Prize in Economics in 1997 for this work.

## The Merton Model Formula

$$ \begin{aligned} &E=V_tN\left(d_1\right)-Ke^{-r\Delta{T}}N\left(d_2\right)\\ &\textbf{where:}\\ &d_1=\frac{\ln{\frac{V_t}{K}}+\left(r+\frac{\sigma_v^2}{2}\right)\Delta{T}}{\sigma_v\sqrt{\Delta{T}}}\\ &\text{and}\\ &d_2=d_1-\sigma_v\sqrt{\Delta{T}}\\ &\text{E = Theoretical value of the company's equity}\\ &V_t=\text{Value of the company's assets at time t}\\ &\text{K = Value of the company's debt}\\ &\text{t = Current time period}\\ &\text{T = Future time period}\\ &\text{r = Risk-free interest rate}\\ &\text{N = Cumulative standard normal distribution}\\ &\text{e = Exponential term}\left(\text{i.e., }2.7183...\right)\\ &\sigma=\text{Standard deviation of stock returns}\\ \end{aligned} $$

## What the Merton Model Can Tell Us

The Merton model makes it easier to value a company and helps analysts assess whether a company can maintain solvency by analyzing the maturity dates and totals of its debt.

The model calculates the theoretical pricing of European put and call options without accounting for dividends paid during the life of the option. However, the model can be adjusted to incorporate dividends by calculating the ex-dividend date value of the underlying stock.

The Merton model makes the following fundamental assumptions:

- All options are European options, exercisable only at expiration.
- No dividends are paid.
- Market movements are unpredictable (efficient markets).
- No commissions are included.
- The underlying stock's volatility and the risk-free rate are constant.
- Returns on the underlying stock are normally distributed.

Variables considered in the formula include the option's strike price, the current underlying price, the risk-free interest rate, and the time until expiration.

## History of the Merton Model

Robert C. Merton is a distinguished American economist and Nobel laureate who purchased his first stock at age 10. He earned a bachelor's degree in engineering from Columbia University, a master's degree in applied mathematics from the California Institute of Technology, and a Ph.D. in economics from MIT, where he later became a professor.

During his time at MIT, Merton and fellow economists Fischer Black and Myron S. Scholes were working on problems related to options pricing and assisting one another. Black and Scholes published their seminal paper, "The Pricing of Options and Corporate Liabilities," in 1973. Merton published "On the Pricing of Corporate Debt: The Risk Structure of Interest Rates" the following year, describing what came to be known as the Merton model.

Merton and Scholes were awarded the Nobel Prize in Economics in 1997 (Black had passed away and was ineligible). The prize committee recognized them for developing "a pioneering formula for the valuation of stock options. Their methodology has paved the way for economic valuations in many areas and has also generated new types of financial instruments, facilitating more efficient risk management in society."

Their most famous collaboration is now commonly known as the Black-Scholes-Merton model.

## What Is a Call Option?

A call option is a contract that allows the buyer to purchase a stock or other financial asset at a specified price before a certain date.

## What Is the Difference Between European and American Options?

European options can only be exercised on the expiration date, while American options can be exercised at any time before expiration.

## What Is the Risk-Free Rate?

The risk-free rate is the theoretical rate of return on an investment carrying zero risk. It is theoretical because no investment is entirely without risk, although some carry risk that is near zero.

## Summary

The Merton model is a mathematical formula developed by economist Robert C. Merton that assesses a company's structural credit risk by treating its equity as a call option on its assets. The model is commonly used by stock analysts and commercial loan officers to evaluate the credit default risk a business may face.

## About LLMQuant

LLMQuant is a cutting-edge community composed of professionals from top global universities and the quantitative finance industry, dedicated to exploring the limitless possibilities at the intersection of artificial intelligence (AI) and quantitative finance (Quant). Our team members hail from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other prestigious institutions, with external advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and leading proprietary trading firms.
