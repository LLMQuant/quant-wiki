![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# What Is the Coefficient of Determination?
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

The coefficient of determination is a statistical measure that examines how the variance of one variable can be explained by the variance of another, particularly when predicting the outcome of a specific event. More commonly known as r-squared (r²), it assesses the strength of the linear relationship between two variables and is widely relied upon by investors conducting trend analysis.

This measure typically addresses a key question: if a stock is listed on an index and experiences price fluctuations, what percentage of its price movement is attributable to the index's price movement?

### Key Takeaways

- The coefficient of determination is a complex concept rooted in statistical data analysis and financial modeling.
- It is used to explain the relationship between an independent variable and a dependent variable.
- The coefficient of determination is commonly referred to as r-squared (r²), which represents its statistical value.
- The value ranges between 0.0 and 1.0, where 1.0 indicates a perfect correlation -- a reliable model for future predictions.
- A value of 0.0 indicates that the asset's price does not depend on index movements.

## Understanding the Coefficient of Determination

The coefficient of determination measures how much of the variability in one factor is attributable to its relationship with another factor. This correlation is expressed as a value between 0.0 and 1.0, or equivalently, 0% to 100%.

A value of 1.0 indicates 100% price correlation and is a reliable model for future predictions. A value of 0.0 suggests that the model shows no price dependence on the index. [1]

A value of 0.20 indicates that 20% of the asset's price movement can be explained by the index, while 0.50 indicates that 50% of the price movement is explained.

**Important:** The coefficient of determination is the square of the correlation coefficient, commonly denoted as "r" in statistics. The value "r" can be negative, but r² cannot be negative, since r-squared is the product of "r" multiplied by itself, and squaring a negative number always yields a positive value. [2]

## Calculating the Coefficient of Determination

The coefficient of determination is calculated by creating a scatter plot and trend line of the data.

If you were to plot the closing prices of the S&P 500 and Apple (AAPL) stock from December 21 to January 20, you would collect the prices shown in the following table. [3][4]

||S&P Daily Close|AAPL Daily Close
|---|---|---|
|Jan 20|$3,972.61|$137.87
|19|$3,898.85|$135.27
|18|$3,928.86|$135.21
|17|$3,990.97|$135.94
|13|$3,999.09|$134.76
|12|$3,983.17|$133.41
|11|$3,969.61|$133.49
|10|$3,919.25|$130.73
|9|$3,892.09|$130.15
|6|$3,895.08|$129.62
|5|$3,808.10|$125.02
|4|$3,852.97|$126.36
|3|$3,824.14|$125.07
|Dec 30|$3,839.50|$139.93
|29|$3,849.28|$129.61
|28|$3,783.22|$126.04
|27|$3,829.25|$130.03
|23|$3,844.82|$131.86
|22|$3,822.39|$132.23
|21|$3,878.44|$135.45

Next, you would create a scatter plot. The degree to which the data fits the regression model is called the goodness of fit, which measures the distance between the trend line and all the data points scattered across the plot.

Most spreadsheet applications use the same formula to compute r² for a dataset. If the data is in columns A and B of your spreadsheet:

Using the formula and highlighting the corresponding cells yields an r² of 0.347 for the S&P 500 and Apple prices, indicating a relatively low correlation. Values of r² between 0.5 and 1.0 indicate a stronger correlation.

Manually calculating the coefficient of determination involves several steps. First, collect the data from the table above, then compute the required values as shown below: [4]

- x = S&P 500 Daily Close
- y = AAPL Daily Close

||x|x²|y|y²|xy
|---|---|---|---|---|---|
|Jan 20|$3,972.61|$15,781,630.21|$137.87|$19,008.14|$547,703.74
|19|$3,898.85|$15,201,031.32|$135.27|$18,297.97|$527,397.44
|18|$3,928.86|$15,435,940.90|$135.21|$18,281.74|$531,221.16
|17|$3,990.97|$15,927,841.54|$135.94|$18,479.68|$542,532.46
|13|$3,999.09|$15,992,720.83|$134.76|$18,160.26|$538,917.37
|12|$3,983.17|$15,865,643.25|$133.41|$17,798.23|$531,394.71
|11|$3,969.61|$15,757,803.55|$133.49|$17,819.58|$529,903.24
|10|$3,919.25|$15,360,520.56|$130.73|$17,090.33|$512,363.55
|9|$3,892.09|$15,148,364.57|$130.15|$16,939.02|$506,555.51
|6|$3,895.08|$15,171,648.21|$129.62|$16,801.34|$504,880.27
|5|$3,808.10|$14,501,625.61|$125.02|$15,630.00|$476,088.66
|4|$3,852.97|$14,845,377.82|$126.36|$15,966.85|$486,861.29
|3|$3,824.14|$14,624,046.74|$125.07|$15,642.50|$478,285.19
|Dec 30|$3,839.50|$14,741,760.25|$139.93|$19,580.40|$537,261.24
|29|$3,849.28|$14,816,956.52|$129.61|$16,798.75|$498,905.18
|28|$3,783.22|$14,312,753.57|$126.04|$15,886.08|$476,837.05
|27|$3,829.25|$14,663,155.56|$130.03|$16,907.80|$497,917.38
|23|$3,844.82|$14,782,640.83|$131.86|$17,387.06|$506,977.97
|22|$3,822.39|$14,610,665.31|$132.23|$17,484.77|$505,434.63
|21|$3,878.44|$15,042,296.83|$135.45|$18,346.70|$525,334.70
|Sum|$77,781.69|$302,584,424.00|$2,638.05|$348,307.23|$10,262,772.73

Using the following formula and substituting the values from each row, where n equals the number of samples (20 in this case):

$$ \begin{aligned}&r ^ 2 = \Big ( \frac {n ( \sum xy) - ( \sum x )( \sum y ) }{ \sqrt { [ n \sum x ^ 2 - ( \sum x ) ^ 2 ] } \times \sqrt { [ n \sum y ^ 2 - ( \sum y ) ^ 2 ] } } \Big ) ^ 2 \\\end{aligned} $$

Substituting the values:

$$ \begin{aligned}&r ^ 2 = \Big ( \tiny { \frac {20 ( 10,262,772.73) - ( 77,781.69 )( 2,638.05 ) }{ \sqrt { [ 20 ( 302,584,424 ) - ( 77,781.69 ) ^ 2 ] } \times \sqrt { [ 20 ( 348,307.23 ) - ( 2,638.05 ) ^ 2 ] } } } \Big ) ^ 2 \\\end{aligned} $$

This yields:

$$ \begin{aligned}&1. \tiny { ( 20 \times 10,262,772.73 ) - ( 77,781.69 \times 2,638.05 ) = 63,467.32 } \\&2. \tiny { (\sqrt { ( 20 \times 302,584,424 ) - ( 77,781.69 ) ^ 2 } = \sqrt { 1,697,180.74 } = 1,302.76 } \\&3. \tiny { (\sqrt { ( 20 \times 10,262,772.73 ) - ( 2,638.05 ) ^ 2 } = \sqrt { 6,836.85 } = 82.69 }\\\end{aligned} $$

Now multiply steps two and three, divide step one by the result, and square:

$$ \begin{aligned}&\Big ( \frac { 63,467.32 }{ 1,302.76 \times 82.69 } \Big ) ^ 2 = 0.347\end{aligned} $$

As you can see, this can become quite tedious and error-prone when working with even a few weeks of trading data.

## Interpreting the Coefficient of Determination

Once you have the coefficient of determination, you can use it to assess how closely an asset's price movements correlate with the price movements of an index or benchmark. In the Apple vs. S&P 500 example, the coefficient of determination for that period was 0.347.

**Tip:** Apple is listed on many indices, so you can calculate r² to determine whether its price movements correspond to those of other indices.

A coefficient of determination of 0.347 indicates a moderate correlation between Apple's stock price movements and the index, since 1.0 denotes high correlation and 0.0 indicates no correlation.

An important caveat is that r-squared does not inherently tell the analyst whether the value is good or bad. It is at the analyst's discretion to evaluate the correlation and its utility in future trend analysis.

## How Do You Interpret the Coefficient of Determination?

The coefficient of determination shows the degree of correlation between a dependent variable and an independent variable. Also known as r² or r-squared, the value should fall between 0.0 and 1.0. The closer to 0.0, the less correlated the dependent variable; the closer to 1.0, the more correlated. [1]

## What Does R-Squared Tell You in Regression?

In regression, r-squared tells you whether a dependency exists between two values and how strongly one value depends on the other.

## What Happens If the Coefficient of Determination Is Greater Than 1?

The coefficient of determination cannot exceed 1, as the formula always returns a number between 0.0 and 1.0. Values outside this range indicate a calculation error. [1]

## Conclusion

The coefficient of determination is a ratio that shows how dependent one variable is on another. Investors use it to judge the correlation between an asset's price movements and the index on which it is listed.

When an asset's r² is closer to zero, its price movements are not dependent on the index. When its r² is closer to 1.0, it is more dependent on the index's price movements.

## References

[1] Pennsylvania State University Eberly College of Science. "[STAT 462 Applied Regression Analysis: 2.5 - The Coefficient of Determination, r-squared](https://online.stat.psu.edu/stat462/node/95/)."

[2] LibreTexts Statistics. "[10.6: The Coefficient of Determination](https://stats.libretexts.org/Bookshelves/Introductory_Statistics/Introductory_Statistics_%28Shafer_and_Zhang%29/10%3A_Correlation_and_Regression/10.06%3A_The_Coefficient_of_Determination)."

[3] Nasdaq. "[APPL Historical Data](https://www.nasdaq.com/market-activity/stocks/aapl/historical)."

[4] Nasdaq. "[SPX Historical Data](https://www.nasdaq.com/market-activity/index/spx/historical)."

## About LLMQuant

LLMQuant is a cutting-edge community composed of professionals from top global universities and the quantitative finance industry, dedicated to exploring the limitless possibilities at the intersection of artificial intelligence (AI) and quantitative finance (Quant). Our team members hail from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other prestigious institutions, with external advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and leading proprietary trading firms.
