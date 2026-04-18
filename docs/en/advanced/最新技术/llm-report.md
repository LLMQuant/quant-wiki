![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

# Using Large Language Models to Uncover Hidden Bad News in Corporate Annual Reports

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

## Introduction: The Secrets Hidden in Annual Reports

**Corporate annual reports (10-K filings)** are a primary source of financial and operational information for investors. However, research from the University of Chicago Booth School of Business has found that many companies use deliberate text and paragraph ordering strategies to conceal unfavorable information. This article explores how Large Language Models (LLMs) and attention mechanisms reveal these concealment strategies, and demonstrates how AI tools can improve the efficiency of information analysis.

![](https://fastly.jsdelivr.net/gh/bucketio/img7@main/2024/12/22/1734887309221-84b023dd-771a-4cdc-8eb1-e1a3bdeb4ea9.png)

## Research Background and Core Questions

For years, market participants have attempted to understand: which annual report information truly drives stock price movements? While quantitative data (such as revenue and profit margins) is relatively straightforward, qualitative data (such as business model changes, competitive dynamics, and strategic initiatives) is typically difficult to quantify and analyze. The University of Chicago team developed a novel approach using attention-enabled LLMs to directly capture the content investors focus on most in annual reports.

The research team's core objectives were to answer the following questions:

1. **What annual report information does the market focus on?**
2. **Do companies deliberately arrange paragraph order to manipulate investor attention?**
3. **How can AI models extract key information from complex text?**

## Research Findings

### 1. Strategic Concealment of Bad News

- **Information ordering strategy**: Companies place negative information later in the Management Discussion and Analysis (MD&A) section rather than at the front of the report, reducing the visibility of adverse information.
- **Concealment conditions**: Companies with high earnings volatility, intense competitive pressure, or low profitability are more likely to adopt this concealment strategy.

### 2. Information Positioning Score: Measuring Disclosure Transparency

The research team developed an **Information Positioning Score** to measure disclosure transparency:

- **High-scoring companies**: Mature, large enterprises tend to place important information prominently, demonstrating greater transparency.
- **Low-scoring companies**: Unprofitable companies or those with volatile earnings tend to bury key information, reducing disclosure transparency.

### 3. Importance Ranking of Annual Report Sections

The model's analysis revealed which sections investors focus on most and least:

- **Most important sections**:
  - **Item 7**: Management Discussion and Analysis (MD&A)
  - **Item 8**: Financial Statements and Notes
  - **Item 1**: Business Description
  - **Item 1A**: Risk Factors
- **Least important sections**:
  - **Item 13**: Related Party Transactions
  - **Item 12**: Security Ownership
  - **Item 10**: Directors and Governance

### 4. Low Attention to ESG Content

Despite significant public discourse around ESG (Environmental, Social, and Governance) issues, the research shows that market response to ESG-related information is relatively muted, with investors focusing more on profitability, liquidity, and financial performance.

![](https://fastly.jsdelivr.net/gh/bucketio/img19@main/2024/12/22/1734887357477-30ebb089-dffb-4797-97b3-29a92d7d543c.png)

## Technical Details: How LLMs Parse Annual Reports

### 1. Data Preprocessing and Modeling

- **Dataset**: 76,929 10-K annual reports from 1996 to 2023, segmented into over 20 million paragraphs.
- **Text processing**: Charts, tables, and HTML tags were removed; text was standardized and segmented.

### 2. Attention Mechanism

The research employs the attention mechanism from the Transformer architecture to capture investor focus through the following steps:

1. **Paragraph embedding generation**: Using OpenAI's text-embedding-3-large model, each paragraph is converted into a 64-dimensional embedding vector.
2. **Dual-layer attention mechanism**:
   - First layer: Analyzes the relationship between paragraphs and context, adjusting the semantic understanding of each paragraph.
   - Second layer: Aggregates paragraph importance through weighted scoring, generating document-level importance ratings.

### 3. Portfolio Construction and Model Performance

- **Performance metrics**: Portfolios constructed based on LLM-identified important paragraphs were analyzed for market performance.
- **Model results**:
  - **Sharpe Ratio**: The LLM model achieved **1.56**, significantly outperforming the traditional Logit model's **1.08**, demonstrating AI's substantial advantage in risk-adjusted returns.

## Regulatory Implications: Enhancing Information Transparency

### Case 1: SEC S-K Regulation Modernization

- In August 2021, the SEC modernized MD&A disclosure rules, emphasizing forward-looking information and relevance.
- Post-reform, the importance score of the MD&A section increased by approximately **18.8%** relative to the financial statements section.

### Case 2: Impact of SEC Comment Letters

- Companies that received SEC comment letters saw their annual report section scores increase by an average of **10%** the following year.
- This suggests that regulatory intervention effectively improves disclosure transparency and market relevance.

## Strategic Information Positioning Analysis

The research further reveals that companies exhibit the following patterns when arranging paragraph order:

- **Positive information front-loaded**: Attracts investor attention and builds market confidence.
- **Negative information buried**: Minimizes the impact of adverse information and avoids direct investor scrutiny.

### Quantitative Framework

1. **Paragraph scoring formula**:
   - Paragraph scores are calculated using attention weights to assess information importance.
   - The relationship between paragraph position and importance is analyzed to reveal information ordering strategies.

2. **Information Positioning Score formula**:
   - Combining paragraph scores with position indices to quantify disclosure transparency:

   $$\text{Information Positioning Score} = \sum_k \left[(1 - \frac{\text{position}_k}{\text{total paragraphs}}) \times \text{importance score}_k\right]$$

   - Higher scores indicate more transparent information disclosure.

3. **Key findings**:
   - Large enterprises demonstrate greater transparency, with less concealment of negative information.
   - Companies with high earnings volatility or facing financial pressure tend to bury important content.

## Conclusions and Implications

### For Investors

LLM technology enables investors to rapidly identify key paragraphs in annual reports, improving analytical efficiency and decision quality.

### For Regulators

Well-designed regulatory measures (such as S-K reform and comment letter processes) significantly improve annual report disclosure quality and market transparency.

### For Companies

While concealing bad news may be effective in the short term, transparent disclosure builds stronger market trust and investor confidence over the long run.

> **"Not all paragraphs are equally important. Focusing on the most valuable information is key to improving information processing efficiency."**
> -- Alex Kim, Research Author
---

## About LLMQuant

LLMQuant is a cutting-edge community of professionals from the world's leading universities and quantitative finance practitioners, dedicated to exploring the intersection of artificial intelligence (AI) and quantitative finance (Quant). Our team members come from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other prestigious institutions, with external advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and leading proprietary trading firms.
