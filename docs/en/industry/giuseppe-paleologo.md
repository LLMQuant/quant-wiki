This article features interviews with two industry heavyweights: buy-side veteran Giuseppe Paleologo and sell-side leader Nick Baltas, centered around three "Multi" themes -- Multi-Asset, Multi-Strategy Portfolios, and Multi-Manager Hedge Funds.

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

* Giuseppe Paleologo has previously served in **Risk and Quantitative Analysis** at **Citadel**, as Head of Enterprise Risk at **Millennium**, and most recently as **Head of Risk Management** at **HRT**.

* Nick Baltas is currently a **Managing Director at Goldman Sachs**, heading Cross-Asset Delta One, Commodities, and Equity Strategy Research & Structuring.

## Interview with Giuseppe Paleologo, Head of Risk Management at HRT

The conversation begins with a discussion of what quantitative researchers actually do within multi-manager hedge funds. In a semi-support role alongside fundamental portfolio managers (PMs), Gappy explains how **portfolio manager coverage**, **factor hedging**, and **internal alpha capture** work together to maximize the firm's P&L.

The interview then delves into the broader domains of **factor research** and **portfolio construction**, with Gappy sharing some firmly held views on factor design and application. Topics covered include:

* **Returns versus characteristics**
* **Blending and integrating alpha signals**
* **Single-period versus multi-period optimization**
* **Linear versus nonlinear models**

### 1. Can you briefly introduce your background?

**Answer:**
I am currently on gardening leave. Previously, I worked in **Risk and Quantitative Analysis** at **Citadel**, served as **Head of Enterprise Risk** at **Millennium**, and most recently was **Head of Risk Management** at **HRT**.

---

### 2. What were your responsibilities as a Quantitative Researcher across these firms?

**Answer:**
I have alternated between two roles: quantitative researcher and risk management advisor. I liken the quant researcher role to playing offense on a football team, while risk management is the defense. My job is to ensure the firm's risk profile aligns with the partners' risk tolerance, to understand each strategy in detail, and to prevent worst-case scenarios -- or at least make them survivable.

---

### 3. Can you explain what "Portfolio Manager Coverage" entails?

**Answer:**
PM coverage involves evaluating whether portfolio managers are taking appropriate levels of risk and conducting performance attribution analysis. This goes beyond standard attribution to include advanced performance analysis and solving customized problems, such as adjustments to factor models.

---

### 4. Hedge funds sometimes exhibit extreme P&L distributions. How do you explain this?

**Answer:**
When P&L outcomes are very large or very small, the distribution of stock contributions tends to be highly uneven -- a small number of stocks generate disproportionate impact on P&L. This phenomenon, known as "fat tails," exists not only within an individual PM's portfolio but also across multiple PMs on a hedge fund platform.

---

### 5. How do you approach hedging strategies, particularly momentum risk hedging?

**Answer:**
Hedging strategies vary depending on the portfolio type -- equities or derivatives. Typically, the firm creates a hedging account with an overlay portfolio that makes the overall position more desirable from a risk perspective. When the number of PMs is large enough, momentum risk becomes very pronounced and must be actively hedged.

---

### 6. How does the quantitative research team help portfolio managers generate alpha?

**Answer:**
The quant research team's role is to design sound incentive structures that motivate PMs to generate more alpha. The challenge for successful hedge funds is not simply maintaining a high Sharpe ratio while earning modest profits, but earning substantially more while keeping the Sharpe ratio high.

---

### 7. What are your views on returns versus characteristics in factor models?

**Answer:**
Characteristics are superior to returns as the foundation for constructing factors because they offer greater explanatory power, a finding well validated in empirical data. Many hedge funds develop customized factor models to meet their specific needs. Off-the-shelf factor models tend to fail commercially because customization is essential.

---

### 8. Crowding is a fascinating phenomenon. How do you view its impact on hedge funds?

**Answer:**
Crowding is not a typical factor because it is an endogenous event rather than a recurring external phenomenon. Nonetheless, hedge funds must pay close attention to it, as crowding can trigger liquidity spirals and events similar to the "quant quake."

---

### 9. Can quantitative strategies be applied to asset classes beyond equities?

**Answer:**
Quantitative strategies are by no means limited to equities. They have broad applicability across other asset classes, including foreign exchange and commodities. The principles underlying factor models translate across different markets.

---

### 10. What do you see as the most fertile areas for future quantitative research?

**Answer:**
Despite factor models having existed for decades, many areas remain underexplored -- particularly agent-based modeling. This approach is critical for understanding crowding effects in financial markets.

---

### 11. What books or perspectives on risk management do you find most valuable?

**Answer:**
I am particularly fond of Aaron Brown's *Red-Blooded Risk*. The book argues that a good risk manager should not only alert PMs when they are taking too much risk, but also encourage them to take more risk when appropriate, striking the right balance between risk and reward.

---

## Interview with Nick Baltas, Managing Director at Goldman Sachs, Head of Cross-Asset Delta One, Commodities, and Equity Strategy Research & Structuring

The discussion begins with how Nick Baltas leverages a broad toolkit of systematic strategies to address client needs. As head of cross-asset strategy research and structuring at Goldman Sachs, Nick explains how **strategy selection**, **cross-asset investing**, and **client utility functions** play critical roles in constructing multi-asset portfolios.

First, we explore how Nick uses his extensive systematic strategy toolkit to solve the problems faced by asset owners.

Second, we discuss Nick's research on **cross-asset skewness** -- a topic rarely addressed in cross-asset strategies. Nick authored one of the definitive papers in this area and provides numerous nuanced insights on implementing skewness strategies.

We then delve into the broader field of **cross-asset risk premia** and **portfolio construction**, where Nick shares his distinctive perspectives on systematic strategy design. Topics include:

* **Taxonomy of systematic strategies**
* **Defensive versus return-enhancing strategies**
* **Trend-following and skewness strategies**
* **Signal blending versus strategy blending**

Finally, Nick shares his views on **building multi-strategy portfolios**, combining theoretical frameworks with practical considerations for meeting client objectives.

---

### 1. How did you start your career? What is your background?

**Nick Baltas:**
I am from Greece, where I studied electronic and computer engineering. I then moved to London for my master's degree, followed by a PhD. During my doctoral studies, I gradually shifted from engineering to financial economics, researching equity momentum, correlation risk, and trend-following strategies. After completing my PhD, I worked briefly at a hedge fund before moving into investment banking, focusing on quantitative research for multi-asset portfolios. I currently lead cross-asset strategy research at Goldman Sachs.

---

### 2. You frequently reference the client "utility function." Can you explain this concept and its role in systematic investing?

**Nick Baltas:**
The utility function is a key tool for understanding client investment objectives. Different client types -- sovereign wealth funds, pension funds, family offices -- have different needs. Some seek defensive portfolios to protect assets from market downturns; others prioritize returns and are willing to accept greater risk. By understanding a client's utility function, we can tailor systematic investment solutions to their specific goals.

---

### 3. How do you match systematic strategies to different utility functions?

**Nick Baltas:**
We classify strategies into four categories: contractual hedging strategies, statistical hedging strategies, diversifying risk premia strategies, and return-enhancing strategies. Contractual hedging strategies include buying put options and constructing collar structures -- primarily for managing sudden, short-term market dislocations. Statistical hedging strategies focus on longer-term trends, such as the market environments of 2008 and 2022. Diversifying risk premia strategies generally do not add downside risk, while return-enhancing strategies may accept more risk in exchange for higher returns. Proper categorization enables us to better serve each client's needs.

---

### 4. How do crowding effects and capacity constraints impact systematic strategy performance?

**Nick Baltas:**
Capacity risk is our primary concern when constructing systematic portfolios. It has two dimensions: position capacity and trading capacity. Position capacity determines how quickly we can exit the market when needed, while trading capacity governs how much market liquidity we consume in daily operations. We manage this through daily trading volume controls and dynamic constraints to avoid materially impacting the market. Notably, crowding is not inherently negative -- for some strategies, crowding is actually a necessary condition for the strategy to function.

---

### 5. How do you combine different signals and strategies in multi-asset portfolios?

**Nick Baltas:**
There is a significant difference between combining signals and combining strategies. Signal combination means blending different signals before optimization, while strategy combination involves building each strategy independently and then merging them. In trend-following strategies, we use risk budgeting to allocate risk; in carry strategies, the focus is on finding the optimal blend through different market signals. Ultimately, we want both strategies to complement rather than cancel each other, improving the combined portfolio's performance.

---

### 6. Why do you prefer risk budgeting in cross-asset strategies?

**Nick Baltas:**
I favor risk budgeting to manage risk across different assets and strategies. This approach ensures each market receives equal risk weighting within the portfolio, preventing high-volatility assets from disproportionately influencing overall performance. For trend-following strategies, risk budgeting is particularly effective because it dynamically adjusts position sizes as market volatility changes, automatically calibrating risk exposure to optimize overall results.

---

### 7. You mentioned that philosophical design principles matter in portfolio construction. Can you elaborate?

**Nick Baltas:**
I believe certain design principles should always be followed in portfolio construction, even when they do not produce visible effects in backtests. For example, setting concentration risk limits -- capping the maximum risk exposure to any single market. This constraint may not significantly impact backtest results, but in live trading it protects the portfolio during market dislocations by preventing excessive exposure to any one market. While such design principles may not directly improve backtest performance, they are essential for sound risk management.

---

### 8. How do you view the different risk premia strategies in cross-asset investing?

**Nick Baltas:**
Each strategy has unique characteristics and use cases. Trend-following is generally considered defensive because it performs well during market downturns. Carry strategies depend on time-series and cross-market yield differentials and may underperform during risk events. Skewness strategies are contrarian signals that typically emerge after significant market selloffs. Combining different strategies gives a portfolio broader risk management coverage and return potential -- the specific mix depends on each client's utility function.

---

### 9. What areas are you currently most interested in?

**Nick Baltas:**
I have recently become fascinated by sleep science, particularly a book called *Why We Sleep*. It explores why humans need to spend so much time sleeping and explains how sleep affects brain function, memory, and learning. For me, sleep is a truly intriguing research area -- and one that is highly relevant to daily life.

---
