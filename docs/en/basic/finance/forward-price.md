![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# What Is the Forward Price?
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

The forward price is the predetermined delivery price agreed upon by the buyer and seller in a forward contract for an underlying commodity, currency, or financial asset, to be paid on a specified future date. At the inception of a forward contract, the forward price makes the value of the contract zero, but changes in the price of the underlying asset will cause the forward to take on either a positive or negative value.

The forward price is determined by the following formula:

$$ \begin{aligned} &F_0 = S_0 \times e^{rT} \\ \end{aligned} $$

## Fundamentals of the Forward Price

The forward price is based on the current spot price of the underlying asset, plus any carrying costs such as interest, storage costs, foregone interest, and other expenses including opportunity costs.

Although the contract has no intrinsic value at inception, over time the contract may gain or lose value. Offsetting positions in a forward contract are equivalent to a zero-sum game. For example, if one investor takes a long position in a pork belly futures contract and another investor takes a short position in the same contract, any gains in the long position will equal the losses that the second investor incurs from the short position. By initially setting the value of the contract to zero, both parties are on equal footing at the inception of the contract.

### Key Takeaways

- The forward price is the price at which a seller delivers an underlying asset, financial derivative, or currency to the buyer of a forward contract at a predetermined date.
- The forward price is roughly equal to the spot price plus associated carrying costs such as storage costs, interest rates, etc.
- Investors may wish to lock in a forward price to hedge against the risk of future market volatility.
- The downside of locking in a forward price is that the value of the asset may move unfavorably for the investor.

## Forward Price Calculation Example

When the underlying asset in a forward contract does not pay any dividends, the forward price can be calculated using the following formula:

$$ \begin{aligned} &F = S \times e ^ { (r \times t) } \\ &\textbf{where:} \\ &F = \text{the contract's forward price} \\ &S = \text{the underlying asset's current spot price} \\ &e = \text{the mathematical irrational constant approximated by 2.7183} \\ &r = \text{the risk-free rate that applies to the life of the forward contract} \\ &t = \text{the delivery date in years} \\ \end{aligned} $$

For example, assume a security is currently trading at $100 per unit. An investor wants to enter into a forward contract that expires in one year. The current annual risk-free interest rate is 6%. Using the above formula, the forward price is calculated as:

$$ \begin{aligned} &F = \$100 \times e ^ { (0.06 \times 1) } = \$106.18 \\ \end{aligned} $$

If there are carrying costs, those are added into the formula:

$$ \begin{aligned} &F = S \times e ^ { (r + q) \times t } \\ \end{aligned} $$

Here, q is the carrying cost.

If the underlying asset pays dividends over the life of the contract, the formula for the forward price is:

$$ \begin{aligned} &F = ( S - D ) \times e ^ { ( r \times t ) } \\ \end{aligned} $$

Here, D equals the sum of each dividend's present value, given as:

$$ \begin{aligned} D =& \ \text{PV}(d(1)) + \text{PV}(d(2)) + \cdots + \text{PV}(d(x)) \\ =& \ d(1) \times e ^ {- ( r \times t(1) ) } + d(2) \times e ^ { - ( r \times t(2) ) } + \cdots + \\ \phantom{=}& \ d(x) \times e ^ { - ( r \times t(x) ) } \\ \end{aligned} $$

Using the example above, assume the security pays a $0.50 dividend every three months. First, the present value of each dividend is calculated:

$$ \begin{aligned} &\text{PV}(d(1)) = \$0.5 \times e ^ { - ( 0.06 \times \frac { 3 }{ 12 } ) } = \$0.493 \\ \end{aligned} $$

$$ \begin{aligned} &\text{PV}(d(2)) = \$0.5 \times e ^ { - ( 0.06 \times \frac { 6 }{ 12 } ) } = \$0.485 \\ \end{aligned} $$

$$ \begin{aligned} &\text{PV}(d(3)) = \$0.5 \times e ^ { - ( 0.06 \times \frac { 9 }{ 12 } ) } = \$0.478 \\ \end{aligned} $$

$$ \begin{aligned} &\text{PV}(d(4)) = \$0.5 \times e ^ { - ( 0.06 \times \frac { 12 }{ 12 } ) } = \$0.471 \\ \end{aligned} $$

The sum of these present values is $1.927. This amount is then substituted into the dividend-adjusted forward price formula:

$$ \begin{aligned} &F = ( \$100 - \$1.927 ) \times e ^ { ( 0.06 \times 1 ) } = \$104.14 \\ \end{aligned} $$

## What Is the Difference Between the Forward Price and the Spot Price?

Investors may wish to lock in a forward price to hedge against the risk of future market volatility. For example, a farmer may wish to enter into a forward wheat contract before harvest to guard against a potential price decline caused by an abundant crop or other factors.

## What Are the Disadvantages of Locking In a Forward Price?

The primary disadvantage of locking in a forward price is that the value of the asset may move unfavorably for the investor, resulting in a loss compared to what they would have received by selling at the spot price upon delivery. Additionally, longer-dated forward contracts increase the risk of non-payment or default.

## What Are the Main Factors Affecting an Asset's Forward Price?

Investors determine the forward price of an asset based on its current spot price plus carrying costs such as storage, transportation, opportunity costs, and foregone interest. Generally, carrying costs are higher for forward contracts with longer maturities.

## Conclusion

The forward price is the price agreed upon by the buyer and seller in a forward contract for the future delivery of an asset. Such contracts have zero value at inception, because market conditions have not yet changed. Investors determine the forward price by adding the underlying asset's spot price to the carrying costs. Using a forward price in a futures contract provides a hedge against market volatility, but it can also be a double-edged sword if the asset's value moves against the investor.
