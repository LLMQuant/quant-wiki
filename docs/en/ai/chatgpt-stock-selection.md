![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

# Still Writing Papers by Hand in 2025? How to Use ChatGPT to Auto-Generate Academic Papers on Stock Research

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

2025 is poised to be the year AI is widely applied in finance and quantitative investing. This guide, based on the paper **"AI-Powered (Finance) Scholarship"** by **Novy-Marx & Velikov (2024)**, explains how large language models (LLMs) can automate academic research production -- from data mining to paper writing. We also incorporate mathematical formulas and discuss the technology's applications and implications for financial research, particularly in stock return prediction.

## 1. Background and Motivation

### 1.1 Large Language Models and Academic Research

In traditional academic research, the cycle of exploration, hypothesis formation, paper writing, and peer review demands enormous time and effort. With the rise of **ChatGPT, Claude**, and other LLMs, AI is transforming this process:

1. **Automated Idea Generation**: LLMs' generative capabilities can mine large bodies of literature or data to surface potential research directions.
2. **Accelerated Paper Writing**: LLMs can rapidly produce paper drafts, abstracts, and supplementary text based on specific prompts.
3. **Data Mining and Result Interpretation**: After "screening" effective signals from large-scale data, LLMs can automatically assign plausible economic theories to explain those signals.

However, this automation also introduces new challenges, such as the risk of **HARKing** (Hypothesizing After Results are Known) at industrial scale. The paper emphasizes that the technology can both "enhance research efficiency" and be "misused."

### 1.2 Stock Return Prediction and "Anomaly" Research

In finance, finding "signals" or "factors" that predict cross-sectional stock returns is a classic and important pursuit. Since the Fama-French three-factor and five-factor models, hundreds or even thousands of "anomalies" have been identified.

- **What is an "anomaly"?** A statistically significant excess return pattern that cannot easily be explained by traditional risk factors under the Efficient Market Hypothesis (EMH).
- **Common approaches**: Combining accounting variables from financial statements (balance sheets, income statements, etc.) through ratios, differences, and other transformations, then testing their predictive power for future returns using portfolio sorts or regressions.

Since a vast number of candidate signals creates **multiple testing** and **data snooping** risks, rigorous statistical methods are needed to control the false discovery rate -- such as Fama-MacBeth cross-sectional regressions and FDR (False Discovery Rate) corrections. **Novy-Marx & Velikov (2024)** introduced a systematic approach called **"Assaying Anomalies"** that subjects mined factors to layered filtering and evaluation.

---

## 2. Automated Research Pipeline Overview

The paper describes a complete "automated research production line" covering:

1. **Large-scale signal mining**
2. **Statistical significance and robustness testing**
3. **Automated hypothesis generation, signal naming, and full paper writing using LLMs**

Below we detail each stage, including mathematical formulas for deeper understanding.

---

### 2.1 Large-scale Signal Mining

The research begins by extracting **31,460** candidate accounting signals from the **COMPUSTAT** database, each derived from different combinations or differences of accounting variables. For example:

- **Ratio-based signals**:
  $$
  \text{Signal}_{i,t} = \frac{\text{AccountingVar1}_{i,t}}{\text{AccountingVar2}_{i,t}}
  $$

- **Difference-based signals**:
  $$
  \text{Signal}_{i,t} = \frac{\text{AccountingVar1}_{i,t} - \text{AccountingVar1}_{i,t-1}}{\text{AccountingVar2}_{i,t-1}}
  $$

Here $i$ denotes the firm and $t$ denotes time (typically annual or quarterly). After filtering for duplicates, severe missing data, and other quality issues, the initial 31,460 signals are reduced to **17,074** candidates.

---

### 2.2 Statistical Significance and Robustness Testing

To avoid a flood of false positives, each signal is subjected to multiple evaluation methods:

1. **Portfolio Sort Tests**
   - Stocks are sorted into groups (e.g., quintiles or deciles) based on signal values, and the return differences across groups are examined.
   - The traditional **t-statistic** tests whether group return differences are significant:
     $$
     t = \frac{\overline{r}_\text{High} - \overline{r}_\text{Low}}{\sqrt{\mathrm{Var}\bigl(\overline{r}_\text{High} - \overline{r}_\text{Low}\bigr)}}
     $$

2. **Factor Model Regressions**
   - Excess returns are regressed on multiple factors (e.g., the Fama-French 6-factor model) to determine whether the signal retains statistical significance after controlling for known risk factors:
     $$
     r_{i,t} - r_{f,t}
     = \alpha
       + \beta_1 \cdot \text{MKT}_{t}
       + \beta_2 \cdot \text{SMB}_{t}
       + \cdots
       + \beta_6 \cdot \text{Factor6}_{t}
       + \epsilon_{i,t}
     $$
   - If the estimated $\alpha$ remains significantly positive or negative, the signal contains incremental information.

3. **The "Assaying Anomalies" Protocol**
   - **Novy-Marx & Velikov (2024)** developed a systematic "assay" process that compares each signal against hundreds of existing anomalies in the literature, subjecting it to rigorous robustness tests and differentiation from similar signals.

Ultimately, very few signals pass all tests -- only **96** survive. These are considered genuinely promising for predicting cross-sectional returns.

---

### 2.3 Automated Paper Generation Using LLMs

Building on the 96 "surviving" signals, the researchers use **GPT-3.5-turbo** or **Claude 3.5-Sonnet** to automatically write papers. The process includes:

1. **Naming System**
   - The LLM is prompted to generate academic-sounding signal names such as *Operating Liquidity Margin* or *Tax Efficiency*, avoiding generic terms like "ratio" or "difference."

2. **Paper Body Generation**
   - Following pre-designed prompts, LLMs generate complete paper text including **abstract, introduction, data and methods, results, and conclusions**.
   - The introduction section automatically constructs theoretical motivation, occasionally citing real literature with appropriate embellishment.

3. **Large-scale Batch Production**
   - For each signal, three complete paper versions are generated (each with different theoretical angles), totaling **288 papers**. The entire process takes minimal time -- an unimaginable "paper production line" by traditional standards.

While demonstrating AI's potential, this also highlights the risk of **"industrialized HARKing"** -- writing rationalized explanations after observing significant results while neglecting genuine economic mechanisms.

---

## 3. Key Findings and Implications

### 3.1 Efficiency and Scale

- **Extreme efficiency**: Traditional academic papers take months or years; with AI automation, once data mining and statistical analysis are complete, generation takes only minutes to produce papers at scale.
- **Potential for abuse**: Without quality oversight, this method could flood the literature with low-quality or highly repetitive papers, severely straining the traditional peer review system.

### 3.2 Researcher Reputation and Peer Review

- **Reputation mechanisms**: Researchers build academic influence through sustained, high-quality work. Short-term quantity-over-quality approaches are unlikely to yield genuine academic standing.
- **Peer review under pressure**: When large volumes of "automated papers" flood journals, editors and reviewers face an enormous burden of distinction. How to quickly assess paper quality and prevent fabricated or circular citations becomes a new challenge.

### 3.3 The Evolution of the Hypothesis-Empirical Paradigm

- In the traditional paradigm, researchers typically propose hypotheses grounded in economic principles, then test them empirically. The current flow -- "mine data to discover patterns first, then have AI create hypotheses" -- is becoming increasingly prevalent.
- **Does this violate the scientific method?** In practice, many important discoveries throughout history were not preceded by complete theories. The real question is: **how to ensure that post-hoc hypotheses are not merely "hindsight wisdom" but possess genuine predictive or generalizable power.**

---

## 4. Mathematical Example: Evaluating "Automated Hypotheses"

Suppose we evaluate an automatically generated signal
$$
\text{SIGNAL}_{i,t-1}
$$
on next-period returns
$$
r_{i,t}
$$
within a standard Fama-MacBeth regression framework:

$$
r_{i,t}
= \alpha_t
+ \beta_t \cdot \text{SIGNAL}_{i,t-1}
+ \gamma_t \cdot \mathbf{X}_{i,t-1}
+ \epsilon_{i,t},
$$

where
$$
\mathbf{X}_{i,t-1}
$$
is a set of control variables or classical factors (e.g., SIZE, BM, MOM, RMW, CMA).

1. **Cross-sectional regressions**: For each period $t$, run a cross-sectional regression to obtain a series of

$$
\hat{\beta}_t
$$.
2. **Time-series mean and variance**:
   $$
   \overline{\beta} = \frac{1}{T}\sum_{t=1}^{T} \hat{\beta}_t,
   \quad
   SE(\overline{\beta}) = \sqrt{\frac{1}{T(T-1)}\sum_{t=1}^{T} \Bigl(\hat{\beta}_t - \overline{\beta}\Bigr)^2}.
   $$

If
$$
\overline{\beta}
$$
is significantly greater than zero with a significant t-statistic, the signal is considered to have predictive power for cross-sectional returns.

However, if
$$
\text{SIGNAL}_{i,t-1}
$$
was discovered through blind data mining among tens of thousands of variables, multiple testing corrections should be applied; otherwise, the false positive probability may be understated. This concern is amplified in the context of AI-driven mass paper production, making **dual scrutiny of statistical significance and economic interpretation** essential.

---

## 5. Risks and Prospects

1. **Academic Integrity**:
   - Large-scale automated paper generation could lead to **widespread fabricated citations** or **citation manipulation**, undermining quality and originality assessment.
   - Systems for **citation identification and verification** -- similar to plagiarism detection or database cross-referencing -- are needed to reduce the harm of LLM "hallucinated citations."

2. **Peer Review Reform**:
   - Clearer **review standards** may be needed, such as requiring authors (or AI) to **submit searchable data and code** with papers for rapid replication and verification.
   - Higher standards for **economic mechanism innovation** -- not just statistical significance -- should be enforced.

3. **Future Research Directions**:
   - As **LLMs** continue to evolve, researchers can integrate **automated verification modules** -- such as automatic reference authentication and theory consistency checks.
   - Developing "AI research laboratories" for finance -- providing end-to-end services from large-scale data cleaning and factor detection to paper formatting -- but with stricter oversight and review mechanisms.

---

## 6. Conclusion

**Novy-Marx & Velikov (2024)** demonstrate a new landscape for AI in financial research:
- Large-scale mining of accounting data can screen tens of thousands of candidate signals in short order;
- New testing protocols and multi-factor models separate genuine signals from noise;
- "Surviving" signals are then fed to LLMs for mass generation of "academic papers," complete with abstract economic theory and motivation.

While delivering a **quantum leap** in research efficiency, this also poses serious challenges to **academic integrity**, **research quality**, and **peer review**. Machines can help us "discover" and "explain" anomalies faster, but only the human academic community can determine which discoveries and explanations truly advance the frontier of financial knowledge.

Going forward, academia may need to establish new standards that balance research efficiency with scholarly rigor. At this pivotal moment of transition, it is essential to affirm a core principle: **embracing technology must not mean abandoning the pursuit of academic truth and research quality**.

---

## References

- Chen, A. Y., Lopez-Lira, A. & Zimmermann, T. (2024). *Does peer-reviewed research help predict stock returns? Working Paper.*
- Fama, E. F. & French, K. R. (2018). *Choosing factors.* Journal of Financial Economics, 128(2), 234-252.
- Kerr, N. L. (1998). *HARKing: Hypothesizing After the Results are Known.* Personality and Social Psychology Review, 2(3), 196-217.
- Novy-Marx, R. & Velikov, M. (2024). *Assaying Anomalies.* Working Paper.
- Yan, X. & Zheng, L. (2017). *Fundamental analysis and the cross-section of stock returns: A data-mining approach.* The Review of Financial Studies, 30(4), 1382-1423.

For more details and access to the original paper and **code**, join the **LLMQuant community**.

## About LLMQuant

LLMQuant is a cutting-edge community of researchers and practitioners from the world's leading universities and quantitative finance firms, dedicated to exploring the intersection of artificial intelligence (AI) and quantitative finance (Quant). Our team members come from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other top institutions, with external advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and leading proprietary trading firms.
