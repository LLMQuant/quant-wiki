![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

# 2024 Review of Key AI Literature in Finance

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

Over the past two years, the rapid advancement of generative AI and large language models (LLMs) has ushered in a new wave of innovation in financial research and applications. This article compiles and presents the most representative **key academic papers** and **practical case studies** at the intersection of quantitative finance and LLMs. Through a systematic overview of historical evolution, methodological challenges, application scenarios, and evaluation benchmarks, this review provides readers with a clear roadmap to better understand and leverage LLM technology for driving innovation in finance.

## Table of Contents

1. A Brief History of LLMs
2. General Application Scenarios for LLMs
3. FinLLM Methodologies, Applications, and Challenges
4. The Financial LLM Landscape
5. Directory of 48 Key Generative AI Papers in Finance
   - Financial Forecasting, Investment Strategy, and Risk Management
   - Sentiment Analysis and Text Mining
   - Time Series Analysis and Forecasting
   - LLM Development (Fine-tuning) and Financial Data Integration
   - Evaluation and Benchmarking of Financial LLMs

---

### A Brief History of LLMs

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/12/14/1734186113125-da5c35e4-7718-45c6-9e72-e60a09c42d87.png)

---

### General Application Scenarios for LLMs

![](https://fastly.jsdelivr.net/gh/bucketio/img5@main/2024/12/14/1734186140553-0f9c1d40-6c10-4dd6-857e-5edd165fb9e3.png)

- **Fine-Tuning**: Adapts a general-purpose LLM into a domain-specific expert. Starting from a broadly knowledgeable LLM, the model is trained with domain-specific data to understand specialized documents (such as medical records or legal filings) and perform related tasks.

- **Prompt Engineering**: When sufficient fine-tuning data is unavailable, carefully designed instructions and prompts can guide the model to perform specific tasks effectively despite limited data.

- **RAG (Retrieval-Augmented Generation)**: When neither fine-tuning nor prompt data is adequate, the LLM is provided with a large searchable data repository. Using text embedding and encoding techniques, the model retrieves information similar to the query to fill knowledge gaps and enhance response quality.

- **COT (Chain of Thought)**: Helps LLMs decompose complex problems into smaller steps for deeper logical reasoning.

- **Agent CodeLLM (LLM with Solver)**: Systems like Code Interpreter that can directly process code and data.

- **Agent LLM with Search Engine Integration**: Systems like Perplexity that enable LLMs to use search engines for real-time information to answer complex queries.

- **Self-Reflection**: The LLM evaluates its own outputs, selecting the most appropriate response from different candidates to improve accuracy and relevance.

- **Multishot Prompting**: Providing multiple examples within a single prompt helps the LLM better understand the task, producing higher-quality and more precise outputs.

- **Hallucinations / Machine Unlearning / Safety**: Due to data quality, generation method biases, probabilistic nature, high temperature settings, or misleading prompts, LLMs may produce factually incorrect responses. Safety strategies and model improvements are needed to mitigate these risks.

### FinLLM Methodologies, Applications, and Challenges

- **Applications**:
  - Market news sentiment analysis
  - Financial report risk assessment
  - Automated financial advice
  - Automated trading strategies
  - Fraud detection
  - Customer service chatbots
  - Market trend analysis

- **Challenges**:
  - Data privacy and security
  - Model interpretability
  - Bias mitigation
  - Seamless integration with existing systems
  - Accurate backtesting (avoiding temporal information leakage in GPT models)

- **Future Directions**:
  - Enhancing model transparency
  - Exploring unsupervised learning opportunities
  - Establishing ethical standards for AI in finance

Choosing the right approach significantly impacts model effectiveness for specific financial tasks.

### The Financial LLM Landscape

![](https://fastly.jsdelivr.net/gh/bucketio/img18@main/2024/12/14/1734187108044-881dd1ac-af20-447a-bc58-511eb0d6941c.png)

### Financial Forecasting, Investment Strategy, and Risk Management

- [ChatGPT Stock Forecasting](): Uses ChatGPT to analyze news sentiment for stock return prediction, significantly outperforming traditional methods.

- [FinancialStatementAnalysis](): LLMs use financial report text to predict corporate earnings changes, outperforming human analysts.

- [Ploutos](): Introduces a financial LLM framework integrating text and numerical data to improve stock prediction accuracy and interpretability.

- [QuantAgent](): A self-improving quantitative investment LLM Agent that enhances financial prediction and signal mining through a dual-loop learning process.

- [MarketSenseAI](): Leverages GPT-4 to analyze diverse data sources, delivering exceptional stock selection performance.

- [RiskLabs](): An LLM-based risk model that outperforms both traditional and AI models in predicting market volatility and VaR.

- [LOB-LLM](): An end-to-end autoregressive model for limit order book prediction with strong correlation performance.

- [Alpha-GPT](): Integrates humans into the decision loop for efficient, precise quantitative investing.

- [LLMFinAdvice](): In providing actionable investment advice, foundation and large models outperform small fine-tuned models.

- [LLMsCostROI](): Uses decision theory to evaluate LLM costs and benefits, analyzing ROI and profit potential.

- [SystemicRisk](): Leverages LLM embeddings and knowledge graphs to assess systemic risk from financial news, finding relatively low interconnectedness among U.S. financial institutions.

### Sentiment Analysis and Text Mining

- [FinLlama](): A Llama 2 7B fine-tuned financial sentiment analysis model with better contextual understanding and robustness in volatile markets.

- [BioFinBERT](): Focuses on the impact of biotech news releases on stock prices through financial sentiment analysis.

- [SALLMRef](): Evaluates ChatGPT and other LLMs on sentiment analysis -- LLMs show advantages in few-shot learning but remain limited on complex tasks.

- [SentiEval](): Proposes the SENTIEVAL benchmark for comprehensive evaluation of LLMs on sentiment analysis tasks.

- [FinSentGPT](): A ChatGPT fine-tuned financial sentiment model supporting multiple languages and outperforming existing models.

- [CryptoSentiment](): Fine-tuned GPT-4 outperforms BERT and FinBERT in cryptocurrency sentiment analysis.

- [FinancialTextAnalytics](): JPMorgan research evaluating ChatGPT and GPT-4 for financial text analysis.

- [NumLLM](): A model trained on Chinese financial textbooks that significantly outperforms existing models in understanding numerical financial questions.

![](https://fastly.jsdelivr.net/gh/bucketio/img12@main/2024/12/14/1734186490555-6ddcb578-42e2-4925-a748-e5df8030cc69.png)

### Time Series Analysis and Forecasting

- [LLM-TimeSeries](): JPMorgan's systematic evaluation and taxonomy of LLM capabilities in time series understanding.

- [TimeGPT-1](): A pre-trained foundation model for time series forecasting that outperforms traditional statistical, ML, and deep learning methods in zero-shot settings.

- [TiMaGPT](): Time Machine GPT -- performs temporally adaptive training on historical data to prevent future data leakage.

- [SEEDS-GEE-WeatherForecast](): Diffusion-model-based weather forecast simulation, offering new approaches for commodity trading.

- [LLMsStochasticFiltering](): The MoE-F algorithm dynamically fuses predictions from multiple pre-trained LLMs, delivering significant F1 improvements.

- [LLMsDistributionalShifts](): JPMorgan proposes a framework using LLMs and APIs to collect diverse time series data for handling distributional shifts.

- [AnomalyDetection](): Uses LLM embeddings to improve accuracy in financial anomaly detection.

### LLM Development (Fine-tuning) and Financial Data Integration

- [BloombergGPT](): The first dedicated financial LLM combining financial and text data.

- [FinGPT](): An open-source financial LLM fine-tuned with RLHF technology.

- [FinMEM](): An LLM Agent with human-aligned memory mechanisms for automated trading.

- [FinAgent](): A multimodal financial trading foundation agent integrating multiple data sources, tool extensions, and advanced reasoning.

- [FinTextQA](): A financial Q&A dataset where Baichuan2-7B performs close to GPT-3.5-turbo.

- [FinGPT-RLSP](): FinGPT uses RLSP to automatically collect and fine-tune from diverse real-time data, improving real-time processing.

- [FinTral](): A multimodal financial LLM suite based on Mistral-7b, adaptable to diverse data types and domain training.

- [Shai](): A 10-billion-parameter LLM purpose-built for asset management.

- [FinVerse](): A financial agent system with 600+ APIs, using LLM-driven SFT to enhance data analysis.

- [FinRobot](): An open-source platform integrating specialized AI agents with financial analysis to boost analytical and decision-making efficiency.

- [BlackScholesInDiffusionModels](): Incorporates the Black-Scholes algorithm into diffusion model prompt mixing to generate more realistic images.

- [FLAN-FinXC](): Achieves strong performance on financial numerical labeling tasks through FLAN-T5 and LoRA fine-tuning.

### Evaluation and Benchmarking of Financial LLMs

- [LLM-InvestingRationality](): Proposes an economic rationality evaluation method -- GPT-4 Turbo performs best among 14 LLMs. See also [Are Large Language Models Rational Investors?]().

- [FinBen](): An open-source LLM evaluation benchmark for finance, encompassing 35 datasets and 23 tasks.

- [FinLLMs](): A survey of LLMs in finance.

- [LLMsRiskProfile](): LLMs become more risk-averse after alignment with human ethics, affecting economic decisions and investment behavior.

- [LLMsEffectOnCryptoLiquidity](): The AI revolution improves cryptocurrency market efficiency and liquidity, particularly after the launch of ChatGPT-3.

- [AutoGPT](): Extends LLM capabilities to complex reasoning and collaborative tasks.

- [FinGPT-Benchmark](): Evaluates diversity and performance of open-source financial LLMs through instruction fine-tuning integration and benchmarking.

- [Portfolio with GenAI](): Uses graph models for cost-effective portfolio replication, matching investor preferences while maintaining high correlation and stability.

- [FinGen](): Proposes three forward-looking financial argument generation tasks using evidence, charts, and news, highlighting current challenges.

- [AIinFinance](): A BIS study on the impact of generative AI on financial intermediation, insurance, asset management, and payments, while raising new challenges for financial stability and regulation.

## About LLMQuant

LLMQuant is a cutting-edge community of researchers and practitioners from the world's leading universities and quantitative finance firms, dedicated to exploring the intersection of artificial intelligence (AI) and quantitative finance (Quant). Our team members come from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other top institutions, with external advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and leading proprietary trading firms.
