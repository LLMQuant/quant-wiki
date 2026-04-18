![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

# A Quantitative Trader's Perspective: Why Do Some Trading Strategies Generate Profits?

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

Understanding **why** a trading strategy is profitable is one of the most important — yet frequently overlooked — questions in finance. Whether you rely on **systematic** models or **discretionary** judgment, identifying the true source of your returns and whether you possess a genuine edge is essential for long-term survival in financial markets.

This article outlines the key theoretical foundations behind strategy profitability, covering risk premia, skewness, leverage, liquidity, behavioral biases, and more. We also examine why certain assets, portfolios, and **dynamic trading rules** can deliver consistent returns.

![](https://fastly.jsdelivr.net/gh/bucketio/img15@main/2025/01/22/1737589546535-0f621a57-2c2f-492d-ae3d-d9ef8b0a98d1.png)

## Risk Premia: The Insurance Analogy

A useful way to think about risk premia is through the lens of insurance:

- **Buying insurance**: You pay a steady stream of small premiums (frequent small losses), but receive a large payout when disaster strikes.
- **Selling insurance**: You collect premiums most of the time (frequent small gains), but face the possibility of a catastrophic loss in rare events.

Financial markets exhibit the same structure. Some participants willingly sacrifice expected return to hedge tail risk (insurance buyers), while others earn higher average returns by bearing that tail risk (insurance sellers). Assets with greater exposure to specific risk factors compensate investors through higher expected returns — this compensation is the risk premium.

### Persistent Risk Premia

Certain risk premia are available on a near-permanent basis. Equities, for example, historically deliver an **excess return** over bonds to compensate for their higher volatility and drawdown risk. Factor-based strategies — such as those exploiting **firm size** or **book-to-market ratio** (value investing) — harvest specific, well-documented risk premia. Similarly, long-duration bonds typically offer higher yields than short-duration bonds to compensate for the greater uncertainty associated with a longer lending horizon.

### Time-Varying Risk Premia

Risk premia are not static. A notable example is John Paulson's trade in 2006, when he purchased mortgage credit default swaps (CDS) at very low cost.

> In 2006, John Paulson acquired CDS contracts cheaply. The subsequent subprime crisis of 2007–2008 generated billions of dollars in returns.

More broadly, periods of market panic often present opportunities to acquire high-quality assets at depressed prices.

This type of trading logic frequently aligns with **mean reversion** — the assumption that risk premia and the associated asset prices, once pushed to extremes, will eventually revert toward fair value. However, estimating that fair value is non-trivial, and markets can remain dislocated for extended periods. Despite these challenges, the time-varying nature of risk premia remains a significant source of returns.

---

## Skewness: The Critical Dimension Beyond the Sharpe Ratio

Investors typically focus on the **Sharpe Ratio (SR)** as the primary measure of risk-adjusted performance. However, two strategies with identical Sharpe Ratios can deliver vastly different experiences if one exhibits frequent small losses with occasional large gains, while the other produces steady small gains punctuated by rare catastrophic losses. This distinction is captured by **skewness**.

### The Sharpe Ratio

The Sharpe Ratio is defined as:

$$
\text{SR} = \frac{\text{Return} - \text{Risk-Free Rate}}{\text{Standard Deviation}}
$$

> For derivatives traders, the risk-free rate has limited impact — particularly in the post-2009 low-rate environment.
> When computing the Sharpe Ratio from daily data and annualizing, a common approximation is to multiply by 16 (assuming 256 trading days per year).

The Sharpe Ratio implicitly assumes a symmetric return distribution. In practice, many assets and strategies deviate significantly from this assumption, making skewness analysis essential.

![](https://fastly.jsdelivr.net/gh/bucketio/img15@main/2025/01/22/1737589435423-6f14c563-a0ad-411d-a7c0-0e0c15e43788.png)

### Understanding Skewness

An asset whose return distribution features a heavier left tail — i.e., large losses are more probable than large gains of equal magnitude — exhibits **negative skewness**. The opposite case is **positive skewness**.

- Equities tend to display **mild negative skewness**.
- Safe-haven assets such as gold and the Swiss franc typically exhibit **positive skewness**, though less extreme than options.

**Buying insurance** is a positively skewed strategy: you incur frequent small losses (premiums) with the occasional large payoff. **Selling insurance** is negatively skewed: you earn steady income most of the time but face occasional severe drawdowns.

#### Negative Skewness vs. Positive Skewness

|                                  | Negative skew | Positive skew |
| -------------------------------- | ------------: | ------------: |
| **Mean of daily returns**        | 0.4%          | 0.4%          |
| **Sigma of daily returns**       | 6.3%          | 6.3%          |
| **Annualised Sharpe ratio**      | 1.0           | 1.0           |
| **Skew of daily returns**        | -1.0          | 1.0           |
| **Median daily return**          | 1.4%          | -0.6%         |
| **Average Gain : Average Loss**  | 0.8           | 1.4           |
| **Hit rate (% of positive days)**| 59%           | 46%           |
| **Expected annual worst daily loss** | -22%       | -10%          |
| **Expected annual best daily gain**  | 10%        | 22%           |

As the table illustrates, even when the annualized Sharpe Ratio is identical, the drawdown profile differs markedly between negatively and positively skewed strategies.

> Many investors find it psychologically intolerable to endure rare but devastating losses — which explains the persistent demand for insurance-like products. Conversely, positively skewed strategies, with their frequent small losses offset by occasional large gains, appeal to those seeking convex, high-optionality returns.

---

## Leverage: The Advantage of Being Able to Borrow

In idealized financial models, investors can freely borrow to amplify returns. In reality, most retail investors and many institutions are either unwilling or unable to employ leverage. This creates a systematic bias: **low-volatility, high-Sharpe-Ratio assets tend to be undervalued** because investors who cannot lever up prefer assets with high absolute returns — even if the risk-adjusted performance is inferior.

As a result, high-risk assets often dominate portfolios, as exemplified by the tech bubble of 1999. Those with access to leverage can, in theory, outperform over the long run by investing in high-Sharpe but low-absolute-return opportunities and scaling them up. However, leverage introduces the risk of margin calls and forced liquidation during extreme drawdowns — a "death spiral" that can wipe out years of accumulated gains in a matter of days.

> The concept of **volatility targeting** addresses how to use leverage more safely, and is discussed in subsequent sections.

---

## Liquidity and Size: Why Smaller or Alternative Assets May Offer Higher Returns

- **Liquidity premium**: Institutional investors require the ability to trade large volumes quickly, driving up the prices of highly liquid assets. Less liquid markets, by contrast, may offer a premium to compensate for the difficulty of entry and exit.
- **Size premium**: Smaller companies, with lower liquidity and less analyst coverage, have historically delivered higher returns — at the cost of greater execution difficulty and valuation uncertainty.
- **Alternative assets**: Real estate, venture capital, and other illiquid investments follow similar logic. Investors who can tolerate long lock-up periods and limited liquidity may be compensated with excess returns.

These premia fluctuate over time. For instance, mortgage-related derivatives were heavily sought after in late 2006, commanding elevated prices. Just one year later, the same instruments were virtually untradeable — offering exceptional value to those willing to step in.

---

## Forced and Non-Economic Transactions

Not all market participants trade with the objective of maximizing returns. Central banks, for example, may intervene persistently in foreign exchange markets to weaken their domestic currency, absorbing significant costs in the process.

> Switzerland and Japan have both engaged in prolonged currency interventions, which ended abruptly — triggering violent exchange rate moves.

During such periods, **carry trades** in the affected currencies can generate attractive returns — until the policy is abandoned and the resulting reversal inflicts severe losses (negative skewness).

Other examples of non-economic or forced trading include: institutional portfolio rebalancing driven by tax or regulatory deadlines, insurance companies required to purchase long-duration bonds, and fund managers liquidating positions under redemption pressure. When these forced flows are large enough, they distort market prices and create exploitable opportunities.

Similarly, **liquidity providers** earn the bid-ask spread by facilitating trades, but this is a classic **negatively skewed** strategy — a few extreme market dislocations can rapidly erase the cumulative gains from normal spread collection.

---

## Barriers to Entry, Effort, and Cost

Some strategies require substantial upfront investment or deep domain expertise. **High-frequency trading (HFT)**, for instance, demands co-located servers near exchange matching engines and ultra-low-latency software. Private equity investing involves extensive due diligence, legal structuring, and long holding periods.

The elevated costs associated with these activities mean that expected returns must be correspondingly higher to justify the investment. This does not necessarily imply that participants possess extraordinary skill — it may simply reflect the economic reality that high-cost strategies require high returns to remain viable.

---

## Behavioral Biases: Persistent Mispricings from Human Psychology

Classical finance theory explains much of the market's behavior, but real-world markets are also shaped by **cognitive and behavioral biases**.

- Short-selling restrictions in certain markets create upward price distortions.
- Investors systematically overestimate the probability of low-frequency events — a tendency visible in lottery ticket purchases, deep out-of-the-money option buying, and over-reliance on select technical indicators.
- The disposition effect — the tendency to hold losing positions too long while cutting winners too early — remains one of the most robustly documented behavioral patterns.

These psychological and institutional factors can create sustained investment opportunities. For example, simple **trend-following** rules can exploit the anchoring and disposition effects described by **prospect theory**, often generating meaningful risk-adjusted returns.

### Self-Fulfilling Prophecies

Certain technical analysis tools, such as Fibonacci retracements, lack rigorous academic support. Nonetheless, because a large number of traders act on these signals, the predicted levels often attract significant order flow — creating a self-fulfilling prophecy. Whether such effects persist in the long run remains an open question.

---

## Pure Alpha and Investment Skill: The Buffett Phenomenon

A small number of investors — Warren Buffett, John Templeton, Peter Lynch — appear to have generated returns that transcend all of the above explanations. They may be statistical outliers, or they may genuinely possess **alpha** — true investment skill and insight.

The decision-making processes of such investors are typically difficult to codify or systematize; they adapt fluidly to evolving market conditions. If you believe you belong in this category, **semi-automated** trading systems and decision-support tools can enhance execution, but the ultimate edge remains your own judgment.

---

> - The concepts discussed throughout this article — risk premia, leverage, liquidity, and behavioral biases — form foundational pillars of quantitative finance research.
> - John Paulson's CDS trade, the mechanics of the Sharpe Ratio, and central bank FX intervention are all areas of active study within the LLMQuant research community.
> - For deeper analysis and practical case studies, follow the LLMQuant community to explore the intersection of AI and quantitative finance.

## About LLMQuant

LLMQuant is a cutting-edge community founded by researchers and practitioners from the world's leading universities and quantitative finance firms, dedicated to advancing the frontier of artificial intelligence and quantitative finance. Our members hail from institutions including Cambridge, Oxford, Harvard, ETH Zurich, Peking University, and USTC, with external advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and top-tier proprietary trading firms.
