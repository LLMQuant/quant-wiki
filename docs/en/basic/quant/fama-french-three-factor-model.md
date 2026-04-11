![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# Introduction to the Fama-French Three-Factor Model

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)
The Fama-French Three-Factor Model is an asset pricing model developed in 1992. It extends the Capital Asset Pricing Model (CAPM) by adding size risk and value risk factors to the market risk factor. The model accounts for the well-documented tendency of value stocks and small-cap stocks to outperform the broader market. By incorporating these two additional factors, the model adjusts for this outperformance, making it a more effective tool for evaluating manager performance.

### Key Takeaways

- The Fama-French Three-Factor Model is an asset pricing model that extends CAPM by incorporating size risk and value risk factors.
- The model was developed by Nobel laureate Eugene Fama and his colleague Kenneth French in the 1990s.
- The model is essentially the result of an econometric regression analysis of historical stock prices.

## Understanding the Fama-French Three-Factor Model

Nobel laureate Eugene Fama and researcher Kenneth French, former professors at the University of Chicago Booth School of Business, sought to better measure market returns. Through their research, they found that value stocks consistently outperform growth stocks.[1] Similarly, small-cap stocks tend to outperform large-cap stocks. As an evaluation tool, portfolios with a high proportion of small-cap or value stocks would typically underperform the CAPM result, since the three-factor model adjusts downward for the observed outperformance of small-cap and value stocks.

The three factors in the Fama-French model are firm size, book-to-market value, and excess return on the market. In other words, the model uses Small Minus Big (SMB), High Minus Low (HML), and portfolio return minus the risk-free rate. SMB accounts for publicly traded companies with small market capitalizations that tend to generate higher returns, while HML captures value stocks with high book-to-market ratios that tend to earn higher returns relative to the market.[2]

There is considerable debate over whether the outperformance tendency is driven by market efficiency or market inefficiency. On the efficiency side, the outperformance is generally explained by the excess risk that value stocks and small-cap stocks face due to their higher cost of capital and greater business risk. On the inefficiency side, the argument is that market participants misprice these companies, providing excess returns over the long run. Investors who subscribe to the Efficient Market Hypothesis (EMH) are more likely to agree with the efficiency explanation.

The formula is:

$$ \begin{aligned} &R_{it} - R_{ft} = \alpha_{it} + \beta_1 ( R_{Mt} - R_{ft} ) + \beta_2SMB_t + \beta_3HML_t + \epsilon_{it} \\ &\textbf{where:} \\ &R_{it} = \text{total return of stock or portfolio } i \text{ at time } t \\ &R_{ft} = \text{risk-free rate of return at time } t \\ &R_{Mt} = \text{total market portfolio return at time } t \\ &R_{it} - R_{ft} = \text{expected excess return} \\ &R_{Mt} - R_{ft} = \text{excess return on the market portfolio (index)} \\ &SMB_t = \text{size premium (small minus big)} \\ &HML_t = \text{value premium (high minus low book-to-market)} \\ &\beta_{1,2,3} = \text{factor coefficients} \\ \end{aligned} $$

Fama and French emphasized that investors must be able to tolerate the additional volatility and periodic underperformance that may occur in the short term. Investors with a time horizon of 15 years or longer will be rewarded for short-term losses. By testing their model against thousands of random stock portfolios, Fama and French found that when size and value factors are combined with the beta factor, they can explain up to 95% of the returns in a diversified stock portfolio.

Given the model's ability to explain up to 95% of a portfolio's return, investors can construct portfolios that receive an average expected return based on the relative risks they assume. The primary factors driving expected returns include market sensitivity, size sensitivity, and sensitivity to value stocks as measured by book-to-market ratio. Any additional average expected return may be attributed to unpriced or unsystematic risk.

## The Fama-French Five-Factor Model

In recent years, researchers have expanded the three-factor model to include additional factors such as "momentum," "quality," and "low volatility." In 2014, Fama and French adapted their model to include five factors. In addition to the original three factors, the new model introduces the concept that companies reporting higher future earnings tend to deliver higher stock market returns -- a factor referred to as profitability.

The fifth factor, called "investment," relates to the concept of internal investment and returns, suggesting that companies directing profits toward major growth projects may experience losses in the stock market.[3]

## What the Fama-French Three-Factor Model Means for Investors

The Fama-French Three-Factor Model underscores that investors must be willing to endure additional volatility and periodic underperformance in the short term. Investors with a time horizon of 15 years or longer will ultimately benefit from short-term losses. Given the model's ability to explain up to 95% of the return in a diversified stock portfolio, investors can tailor their portfolios to receive an average expected return commensurate with the relative risk they assume.

The primary factors driving expected returns include market sensitivity, size sensitivity, and sensitivity to value stocks as measured by book-to-market ratio. Any additional average expected return may be attributed to unpriced or unsystematic risk.

## What Are the Three Factors in the Model?

The Fama-French model has three factors: firm size, book-to-market value, and excess return on the market. Specifically, the model uses Small Minus Big (SMB), High Minus Low (HML), and portfolio return minus the risk-free rate. SMB accounts for publicly traded companies with small market capitalizations that tend to generate higher returns, while HML captures value stocks with high book-to-market ratios that tend to outperform the market.

## What Is the Fama-French Five-Factor Model?

In 2014, Fama and French expanded their model to five factors. Beyond the original three, the new model adds the concept that companies reporting higher future earnings tend to deliver higher stock market returns -- a factor known as profitability. The fifth factor, called "investment," relates to internal investment and return patterns, suggesting that companies directing profits toward major growth projects may experience losses in the stock market.

## References

[1] Eugene F. Fama and Kenneth R. French. "Value versus Growth: The International Evidence." The Journal of Finance, Volume 53, No. 6, 1988, Pages 1975-1999.

[2] Eugene F. Fama and Kenneth R. French. "Multifactor Explanations of Asset Pricing Anomalies." The Journal of Finance, Volume 51, No. 1, 1996, Pages 55-84.

[3] Journal of Financial Economics. "[A Five-Factor Asset Pricing Model](https://www.sciencedirect.com/science/article/abs/pii/S0304405X14002323)." Accessed Aug. 30, 2021.

## About LLMQuant
LLMQuant is a cutting-edge community composed of professionals from world-leading universities and the quantitative finance industry, dedicated to exploring the frontiers of artificial intelligence (AI) and quantitative (Quant) research. Our team members hail from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other top institutions, with external advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and leading proprietary trading firms.
