
# Replacing Quant Researchers? Using ChatGPT o1 to Auto-Generate and Backtest Trading Algorithms from Academic Papers

To better understand the AI + quantitative finance landscape, we explore a novel AI-assisted workflow that **leverages ChatGPT o1 to automatically generate code from quantitative finance articles and backtest trading algorithms using QuantConnect**. For the latest at the intersection of AI and quantitative finance, follow LLMQuant.

Quantitative finance depends heavily on data-driven strategies derived from extensive research. However, translating insights from dense academic papers into executable trading algorithms is often time-consuming and error-prone. While creating a production-ready solution immediately may not be realistic, our goal is to generate boilerplate code for QuantConnect within seconds. This initial code can help determine whether a paper proposes a promising strategy worth further investigation -- or one that can be safely set aside.

## Overview

We detail how to run this code and present our preliminary tests. For the underlying principles, this article serves as a companion to the earlier work "LLM Pair Programming in Algorithmic Trading." Notably, our approach uses a linear workflow, setting aside the dual-agent architecture for now. The tool not only extracts and summarizes key trading strategies and risk management techniques from PDF articles, but also generates syntactically correct QuantConnect Python code with syntax highlighting for easy review.

Initial testing indicates that the generated code is error-free, though achieving 100% accuracy across all tests has not yet been accomplished. The tool's NLP component uses basic techniques that can be refined in future iterations. However, we chose to release the code quickly as a proof of concept in this rapidly evolving field. This project is a work in progress -- consider what is described here as the beta version.

## How It Works

The core of this automation is the `ArticleProcessor` class, which orchestrates the entire workflow from PDF extraction to code generation. Here is a breakdown of its components:

### 1. PDF Text Extraction with pdfplumber

The process begins by loading and extracting text from PDF files using the pdfplumber library. Unlike other PDF parsing tools, pdfplumber provides superior accuracy, particularly for the complex layouts common in academic articles.

```python
def load_pdf(self, pdf_path: str) -> str:
    try:
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        logging.info("PDF loaded successfully.")
        return text
    except Exception as e:
        logging.error(f"Failed to load PDF: {e}")
        return ""
```

### 2. Text Preprocessing

Once text is extracted, cleaning and preprocessing are critical. This includes using regular expressions to remove URLs, headers, footers, standalone numbers (such as page numbers), and other irrelevant content.

```python
def preprocess_text(self, text: str) -> str:
    try:
        text = re.sub(r'https?://\S+', '', text)
        text = re.sub(r'Electronic copy available at: .*', '', text)
        text = re.sub(r'^\d+\s*$', '', text, flags=re.MULTILINE)
        text = re.sub(r'\n+', '\n', text)
        text = re.sub(r'^\s*(Author|Title|Abstract)\s*$', '', text, flags=re.MULTILINE | re.IGNORECASE)
        text = text.strip()
        logging.info("Text preprocessing successful.")
        return text
    except Exception as e:
        logging.error(f"Failed to preprocess text: {e}")
        return ""
```

### 3. Heading Detection with SpaCy

Understanding article structure is essential. Using SpaCy's NLP capabilities, the tool identifies section headings based on heuristics such as sentence length and title formatting. This segmentation helps organize content more effectively for analysis.

```python
def detect_headings(self, text: str) -> List[str]:
    try:
        doc = self.nlp(text)
        headings = []
        for sent in doc.sents:
            sent_text = sent.text.strip()
            if len(sent_text.split()) < 10 and sent_text.istitle():
                headings.append(sent_text)
        logging.info(f"Detected {len(headings)} headings.")
        return headings
    except Exception as e:
        logging.error(f"Failed to detect headings: {e}")
        return []
```

### 4. Section Splitting and Keyword Analysis

After identifying headings, the text is split into corresponding sections. The tool then performs keyword analysis, categorizing sentences as `trading_signal` or `risk_management`. This classification is based on predefined lists of relevant keywords, ensuring that only pertinent information is passed to subsequent stages.

```python
def keyword_analysis(self, sections: Dict[str, str]) -> Dict[str, List[str]]:
    keyword_map = defaultdict(list)

    risk_management_keywords = [
        "drawdown", "volatility", "reduce", "limit", "risk", "risk-adjusted",
        "maximal drawdown", "market volatility", "bear markets", "stability",
        "sidestep", "reduce drawdown", "stop-loss", "position sizing", "hedging"
    ]
    trading_signal_keywords = [
        "buy", "sell", "signal", "indicator", "trend", "SMA", "moving average",
        "momentum", "RSI", "MACD", "bollinger bands", "Rachev ratio", "stay long",
        "exit", "market timing", "yield curve", "recession", "unemployment",
        "housing starts", "Treasuries", "economic indicator"
    ]

    irrelevant_patterns = [
        r'figure \d+',
        r'\[\d+\]',
        r'\(.*?\)',
        r'chart',
        r'\bfigure\b',
        r'performance chart',
        r'\d{4}-\d{4}',
        r'^\s*$'
    ]

    processed_sentences = set()

    for section, content in sections.items():
        doc = self.nlp(content)
        for sent in doc.sents:
            sent_text = sent.text.lower().strip()

            if any(re.search(pattern, sent_text) for pattern in irrelevant_patterns):
                continue
            if sent_text in processed_sentences:
                continue
            processed_sentences.add(sent_text)

            if any(kw in sent_text for kw in trading_signal_keywords):
                keyword_map['trading_signal'].append(sent.text.strip())
            elif any(kw in sent_text for kw in risk_management_keywords):
                keyword_map['risk_management'].append(sent.text.strip())

    for category, sentences in keyword_map.items():
        unique_sentences = list(set(sentences))
        keyword_map[category] = sorted(unique_sentences, key=len)

    logging.info("Keyword analysis complete.")
    return keyword_map
```

### 5. Summary and QuantConnect Code Generation with OpenAI GPT-4

Leveraging OpenAI's GPT-4, the tool generates concise summaries of extracted strategies and risk management techniques. More impressively, it translates these insights into fully functional QuantConnect Python algorithms, ensuring adherence to best practices and syntactic correctness.

```python
def generate_qc_code(self, extracted_data: Dict[str, List[str]]) -> str:
    trading_signals = '\n'.join(extracted_data.get('trading_signal', []))
    risk_management = '\n'.join(extracted_data.get('risk_management', []))

    prompt = f"""
    You are an expert QuantConnect algorithm developer. Convert the following trading strategy and risk management descriptions into a complete, error-free QuantConnect Python algorithm.

    ### Trading Strategy:
    {trading_signals}

    ### Risk Management:
    {risk_management}

    ### Requirements:
    1. **Initialize method**:
        - Set start and end dates.
        - Set initial capital.
        - Define stock selection logic.
        - Initialize required indicators.
    2. **OnData method**:
        - Implement buy/sell logic based on indicators.
        - Ensure indicators are properly updated.
    3. **Risk Management**:
        - Implement a 15% drawdown limit.
        - Apply the described position sizing or stop-loss mechanisms.
    4. **Ensure compliance**:
        - Use only QuantConnect-supported indicators and methods.
        - Code must be syntactically correct and error-free.

    ### Example Structure:
    ```python
    from AlgorithmImports import *

    class MyAlgorithm(QCAlgorithm):
        def Initialize(self):
            self.SetStartDate(2020, 1, 1)
            self.SetEndDate(2023, 1, 1)
            self.SetCash(100000)
            # Define stock selection, indicators, etc.

        def OnData(self, data):
            # Trading logic

        def OnEndOfDay(self):
            # Risk management
    ```

    ### Generated Code:
    ```
    # LLM will generate code after this line
    ```
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an assistant specialized in generating QuantConnect algorithms in Python."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2500,
            temperature=0.3,
            n=1
        )
        generated_code = response['choices'][0]['message']['content'].strip()
        code_match = re.search(r'```python(.*?)```', generated_code, re.DOTALL)
        if code_match:
            generated_code = code_match.group(1).strip()
        logging.info("LLM generated code.")
        return generated_code
    except Exception as e:
        logging.error(f"Failed to generate code: {e}")
        return ""
```

### 6. Displaying Results with Tkinter and Pygments

For a user-friendly experience, the tool uses Tkinter to display the article summary and generated code in separate windows. The Pygments library enhances readability by adding syntax highlighting to the Python code.

```python
def display_summary_and_code(self, summary: str, code: str):
    # Create main Tkinter root
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Summary window
    summary_window = tk.Toplevel()
    summary_window.title("Article Summary")
    summary_window.geometry("800x600")

    summary_text = scrolledtext.ScrolledText(summary_window, wrap=tk.WORD, font=("Arial", 12))
    summary_text.pack(expand=True, fill='both')
    summary_text.insert(tk.END, summary)
    summary_text.configure(state='disabled')  # Read-only

    # Code window
    code_window = tk.Toplevel()
    code_window.title("Generated QuantConnect Code")
    code_window.geometry("1000x800")

    code_text = scrolledtext.ScrolledText(code_window, wrap=tk.NONE, font=("Consolas", 12), bg="#2B2B2B", fg="#F8F8F2")
    code_text.pack(expand=True, fill='both')

    # Apply syntax highlighting
    self.apply_syntax_highlighting(code, code_text)

    code_text.configure(state='disabled')  # Read-only

    # Start Tkinter event loop
    root.mainloop()
```

### 7. Initial Testing

We tested the tool using the article "Avoiding Bear Markets with Market Timing Strategies" by L. Durian and R. Vojtko from Quantpedia. The output is shown below:

![View of Code and Summary](https://fastly.jsdelivr.net/gh/bucketio/img7@main/2024/10/12/1728730721023-f1a5f810-c487-4c2e-a6a4-acc2b63df7a8.png)

The code generated on the first run produced the following backtest results:

![Backtest Results of Generated Code -- Powered by QuantConnect](https://cdn-images-1.readmedium.com/v2/resize:fit:800/1*X_7QwYDI7EZOvwRS1Y8UIg.png)

The algorithm was flat in 2020 -- exactly as expected, avoiding the COVID-19 bear market. The article does appear to successfully manage bear market avoidance, making it well worth further investigation.

## Conclusion

Automating the translation of quantitative finance research into executable trading algorithms can significantly improve efficiency. By integrating powerful libraries -- pdfplumber, SpaCy, OpenAI's GPT-4, Tkinter, and Pygments -- this Python-based tool provides a seamless solution that bridges the gap between research and implementation.

---

**Commentary**

- The current process of converting financial papers into trading algorithms is time-consuming and error-prone, underscoring the need for automation.
- While the generated code is largely error-free, achieving complete accuracy remains a goal for future development.
- The tool's ability to categorize sentences into trading signals and risk management is a key feature, ensuring that only relevant information feeds into code generation.
- The use of GPT-4 for code generation is particularly innovative, showcasing AI's potential in quantitative finance.
- The project shows strong promise for continuous improvement and becoming a valuable asset for quantitative analysts and traders.
- The use of Tkinter for a user-friendly interface and Pygments for syntax highlighting reflects attention to user experience and code readability.
