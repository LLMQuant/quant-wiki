![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

## FinRobot: An LLM-Powered Framework for Equity Research and Valuation

In today's increasingly complex financial markets, efficient sell-side equity research demands robust automation tools. However, many existing AI solutions focus narrowly on technical indicators, lack flexible qualitative analysis capabilities, and struggle to adapt to new data in real time or assess risk accurately -- limiting their practical value in investment workflows.

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2025/01/29/1738120002722-a681f3a4-f2b3-4c73-91d7-24fe80ded644.png)

**FinRobot** is the first AI agent framework purpose-built for **equity research**. It employs a **multi-agent Chain of Thought (CoT) system** that integrates quantitative and qualitative analysis, simulating the comprehensive reasoning process of human analysts. The overall architecture consists of three functional agents:

1. **Data-CoT Agent**: Aggregates multi-source data, performing comprehensive extraction and intermediate summarization of financial statements, company announcements, and third-party databases.
2. **Concept-CoT Agent**: Conducts in-depth analysis of key financial metrics and the industry landscape, modeling the research workflow of a human analyst to produce actionable analytical conclusions.
3. **Thesis-CoT Agent**: Synthesizes the analysis into an investment recommendation report, providing data-driven insights, valuation metrics, and risk assessments in a comprehensive format.

Unlike existing automated research platforms (e.g., CapitalCube, Wright Reports), FinRobot combines **real trading value** with **institutional-grade quality**, continuously updating to reflect market developments while delivering more realistic risk assessments. The framework is open-source at: https://github.com/AI4Finance-Foundation/FinRobot

![](https://fastly.jsdelivr.net/gh/bucketio/img15@main/2025/01/22/1737589546535-0f621a57-2c2f-492d-ae3d-d9ef8b0a98d1.png)

> **Keywords**: AI-agent, Large Language Models, Equity Research, Financial Analysis, Chain of Thought

---

## 1. Introduction

**Financial analysis** is at the heart of the financial services industry, shaping a wide range of investor decisions (Abarbanell and Bushee, 1997; Greenwald et al., 2004; Penman, 2010; Berman and Knight, 2013; Subramanyam, 2014). **Equity research** is particularly critical within sell-side research departments at major investment banks and brokerages. Traditional research reports require analysts with deep quantitative modeling skills and sector expertise, making the process both time-consuming and resource-intensive.

With the rise of **artificial intelligence (AI)** and **large language models (LLMs)** (Medhat et al., 2014; Brown et al., 2020; Wu et al., 2023; Yang et al., 2023; Kim et al., 2024), the financial industry has begun exploring automated equity research. However, existing tools tend to emphasize technical analysis or simplistic models, neglecting the integration of expert judgment with substantive qualitative analysis. **FinRobot** addresses this gap through multi-agent and Chain of Thought mechanisms, combining quantitative analysis with the flexibility of subjective judgment to meet institutional-grade research depth.

**Key contributions**:

- **First multi-agent Chain of Thought (CoT) AI equity research framework**: FinRobot decomposes the research process into data processing (Data-CoT), conceptual analysis (Concept-CoT), and report generation (Thesis-CoT), simulating the analyst's reasoning chain.
- **Integration of subjective judgment, real-time data, and novel evaluation metrics**: FinRobot features real-time data pipelines and multidimensional report quality evaluation (Accuracy, Logicality, Storytelling).
- **Open-source platform to democratize financial AI**: FinRobot's open-source codebase encourages collaboration between the finance and AI communities.

---

## 2. Related Work

### 2.1 LLMs and Financial Applications
Large language models (LLMs), with their powerful natural language understanding and generation capabilities, are playing an increasingly important role in **financial analysis**, including **sentiment analysis** (Medhat et al., 2014; Huang et al., 2023; Zhang et al., 2023) and **market prediction** (Henrique et al., 2019; Nabipour et al., 2020; Kumar et al., 2022; Jiang, 2021). However, LLMs often lack real-time data access and domain-specific knowledge, making them insufficient for demanding real-time equity research. This project directly addresses that pain point.

### 2.2 AI Agents and Chain of Thought in Financial Analysis
Multi-agent collaboration frameworks have brought greater efficiency to financial decision-making, with systems like FinAgent (Zhang et al., 2024) and FinMem (Yu et al., 2023) leveraging real-time market data to support trading strategies. Meanwhile, **Chain-of-Thought (CoT)** prompting simulates human step-by-step reasoning, significantly improving analytical quality (Wei et al., 2022; Kim et al., 2024). FinRobot builds on this foundation with a CoT framework specifically designed for sell-side research, achieving greater analytical depth and adaptive flexibility.

## 3. Methodology

### 3.1 Overall Framework
Figure 1 illustrates FinRobot's multi-layer CoT structure, dividing the entire financial research process into three sequentially connected agent tiers. This enhances both analytical rigor and the readability of the final report.

![](https://fastly.jsdelivr.net/gh/bucketio/img17@main/2025/01/29/1738120339772-d962baa5-31f2-475a-8079-03411ce161c0.png)

1. **Data Processing Layer (Data-CoT Agent)**
   - Responsible for extracting information from SEC filings, earnings calls, company announcements, and other sources, then cleaning, formatting, and distilling key financial metrics.
   - This agent simultaneously gathers quantitative and qualitative data, laying the groundwork for subsequent conceptual analysis.

2. **Financial Concept Layer (Concept-CoT Agent)**
   - Transforms processed data into actionable financial concepts and forecasts, including **revenue growth**, **EBITDA trends**, and **market positioning**.
   - Employs analyst-style reasoning to evaluate competitive dynamics, sentiment factors, and potential risks.

3. **Equity Research Template Layer (Thesis-CoT Agent)**
   - Integrates the preceding analysis into a complete **investment research report**, including the investment thesis, risk assessment, valuation model, and a concluding rating (e.g., Buy/Hold/Sell).
   - Uses professional sell-side report templates to ensure the final output meets industry standards.

### 3.2 Data Processing Layer
The **Data-CoT Agent** aggregates and preprocesses multi-channel data, ensuring information **accuracy** and **completeness**. Primary data sources include:

- **Databases**: OceanBase, PostgreSQL, etc., for structured financial data storage.
- **Unstructured documents**: PDFs, DOCX files, images -- extracting text and key information.
- **Third-party interfaces**: Chart visualization, real-time API data feeds, etc.
- **Web search**: Aggregating multidimensional market intelligence and industry news.
- **Distributed file storage**: DFS, MinIO, etc., ensuring high availability and robustness for large-scale data.

Additionally, FinRobot performs fine-grained extraction from **SEC filings** (10-K, 10-Q, etc.) and **earnings calls**, capturing key figures such as **revenue, operating expenses, and SG&A**, then computing derived metrics including **revenue growth, contribution profit, EBITDA, and EBITDA margin** (see table below). These metrics form the foundation for subsequent analysis and valuation.

**Common financial formulas**:

| **Formula** | **Description** |
| --- | --- |
| **Revenue Growth** = $(\text{Revenue}_{current} - \text{Revenue}_{previous}) / \text{Revenue}_{previous}$ | Measures revenue growth relative to the prior period |
| **Contribution Profit** = Revenue $-$ Operating Expense | Gauges profitability after operating costs |
| **EBITDA Margin** = $ \text{EBITDA} / \text{Revenue} $ | EBITDA as a percentage of revenue, measuring operational efficiency |
| **CAGR** = $((\text{EV}/\text{BV})^{1/n}-1)\times 100$ | Compound Annual Growth Rate |
| **Enterprise Multiple** = $ \text{EV} / \text{EBITDA} $ | A widely used valuation multiple |

### 3.3 Financial Concept Layer
In the **Concept-CoT Agent**, FinRobot performs deeper analysis of the financial metrics generated in the previous step, addressing questions central to the investment thesis:

- **Revenue forecasting**: Considering historical growth, backlog, inflation, and market pricing to model both optimistic and conservative growth scenarios.
- **EBITDA and margins**: Stripping out one-time items to derive a more accurate profitability picture, then benchmarking margin trends against industry peers.
- **ROIC, WACC, and related metrics**: Evaluating capital efficiency and cost of capital to support DCF and other valuation models.
- **Financial Q&A**: Addressing questions such as the company's advantages versus peers, external impacts on profitability, and profit margin expansion potential in coming years.

### 3.4 Research Report Layer
The **Thesis-CoT Agent** presents the analytical results in a **sell-side research report** format, covering:

- **Investment thesis**: Combining financial forecasts and industry trends to provide a clear Buy/Sell/Hold rating.
- **Risk analysis**: Itemizing the key risk factors affecting valuation and growth, helping investors balance opportunity and risk.
- **Valuation and financial projections**: Including multi-year revenue, EBITDA, and margin forecasts, with target prices derived from DCF, P/E, or other models.
- **Competitive analysis**: Benchmarking the target company against peers on revenue growth, gross margins, EBITDA, and SG&A ratios to assess relative positioning.

![](https://fastly.jsdelivr.net/gh/bucketio/img0@main/2025/01/29/1738121121008-bf853eb2-10f3-4495-8f66-ff4e1c8c618f.png)

## 4. Experiments

### 4.1 Task Description
FinRobot is applicable to equity reports across multiple industries. This study uses **Waste Management, Inc.** (a leading North American waste management and environmental services company) as a case study. The framework comprehensively analyzes the company's financial performance, valuation methods, risk factors, and industry comparisons, supplemented with clear tables and charts. See the appendix for the full research report.

### 4.2 Implementation Details
1. **Data Processing (Data-CoT layer)**: Collected SEC filings, company announcements, and historical financial data.
2. **Conceptual Analysis (Concept-CoT layer)**: Applied analyst-style reasoning to address core questions about earnings drivers, the competitive landscape, and potential risks.
3. **Report Integration (Thesis-CoT layer)**: Compiled the above findings into a formal research report format with charts and executive summaries for quick investor comprehension.

### 4.3 Evaluation

#### 4.3.1 Expert Review
We invited several investment banking analysts to rate FinRobot-generated reports on three dimensions -- **Accuracy**, **Logicality**, and **Storytelling** -- on a 0-10 scale (Table 3 provides detailed criteria). Results in Table 2 show that most reviewers gave **scores of 9 or 10** for accuracy, indicating highly reliable figures and analysis. Logicality also received high marks, with minor room for improvement noted by some reviewers. Storytelling was generally well-received, though some reviewers suggested enhancing readability and narrative flow.

#### 4.3.2 LLM-Based Evaluation
In addition to expert review, we used **GPT-4** to rate the reports on the same dimensions (see Figure 3). Results aligned closely with expert assessments (Figure 4 shows detailed comments), further confirming the reports' **data accuracy, structural clarity, and content readability**.

#### 4.3.3 Stability Testing
To verify FinRobot's consistency, we generated multiple reports for the same company and had GPT-4 evaluate each for consistency, comparing against zero-shot, few-shot, and pure CoT prompting baselines. FinRobot consistently outperformed other prompting modes on **Accuracy, Logicality, and Storytelling** (see Figure 5), with low variance -- demonstrating stable and reliable report output.

## 5. Conclusion

**FinRobot** leverages a multi-agent Chain of Thought system to seamlessly integrate quantitative and qualitative analysis, significantly enhancing AI's practical value in sell-side equity research. With its **real-time data pipeline** and **professional risk assessment** capabilities, it produces accurate, detailed, and actionable research reports.

Looking ahead, we plan to extend FinRobot to additional industries and asset types, incorporating features such as broader coverage, reinforcement learning integration, and enhanced sentiment analysis to provide the financial industry with more diverse and innovative research tools.

## About LLMQuant

LLMQuant is a cutting-edge community composed of researchers from top universities and quantitative finance professionals worldwide, dedicated to exploring the intersection of artificial intelligence (AI) and quantitative finance (Quant). Our team members come from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other leading institutions, with external advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and top proprietary trading firms.
