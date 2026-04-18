![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# What Is Multiple Linear Regression (MLR)?
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

Multiple linear regression (MLR), also known simply as multiple regression, is a statistical technique that uses several explanatory variables to predict the outcome of a response variable. The goal of MLR is to model the linear relationship between the explanatory (independent) variables and the response (dependent) variable. In practice, multiple regression is an extension of ordinary least squares (OLS) regression, as it involves more than one explanatory variable.

### Key Takeaways

- Multiple linear regression (MLR) is a statistical technique that uses several explanatory variables to predict the outcome of a response variable.
- It is also known as multiple regression.
- Multiple regression is an extension of linear (OLS) regression, which uses only one explanatory variable.
- MLR is widely used in econometrics and financial inference.
- Multiple regression is used for making predictions, explaining relationships among financial variables, and testing existing theories.

## Formula and Calculation of MLR

$$ \begin{aligned}&y_i = \beta_0 + \beta _1 x_{i1} + \beta _2 x_{i2} + ... + \beta _p x_{ip} + \epsilon\\&\textbf{where, for } i = n \textbf{ observations:}\\&y_i=\text{dependent variable}\\&x_i=\text{explanatory variables}\\&\beta_0=\text{y-intercept (constant term)}\\&\beta_p=\text{slope coefficient for each explanatory variable}\\&\epsilon=\text{the model's error term (also known as the residuals)}\end{aligned} $$

## What MLR Can Tell You

Simple linear regression is a function that allows an analyst or statistician to make predictions about one variable based on known information about another. Linear regression can be used only when there are two continuous variables -- one independent and one dependent. The independent variable is the parameter used to calculate the dependent variable or outcome. A multiple regression model extends to multiple explanatory variables.

The MLR model is based on the following assumptions:

- A linear relationship exists between the dependent and independent variables
- The independent variables are not overly correlated with one another
- Observations are selected independently and randomly from the population
- Residuals are normally distributed with a mean of 0 and variance of σ²

**Important:** MLR assumes a linear relationship between the dependent and independent variables, no strong correlations among independent variables, and constant variance of the residuals.

The coefficient of determination (R-squared) is a statistical metric that measures how much of the variation in outcomes can be explained by the variation in the independent variables. R² always increases when more predictors are added to the MLR model, even if the predictors are unrelated to the outcome variable.

Therefore, R² alone cannot be used to identify which predictors should be included in or excluded from a model. R² ranges from 0 to 1, where 0 means the outcome cannot be predicted by any of the independent variables, and 1 means the outcome can be predicted without error.

When interpreting multiple regression results, beta coefficients are valid while holding all other variables constant ("ceteris paribus"). The output from a multiple regression can be presented as an equation or displayed vertically in a table.

## Example of Using MLR

For instance, an analyst may want to know how market movements affect the stock price of ExxonMobil (XOM). In this case, the linear equation would use the S&P 500 index value as the independent variable (or predictor) and XOM's price as the dependent variable.

In practice, multiple factors can predict the outcome of an event. For example, ExxonMobil's stock price depends on more than just overall market performance. Other predictors such as oil prices, interest rates, and crude oil futures prices also influence XOM's price and the prices of other oil companies. To understand relationships involving more than two variables, MLR is used.

MLR is used to determine the mathematical relationship among several random variables. In other words, MLR examines how multiple independent variables relate to one dependent variable. Once the predictive power of each independent variable is established, information from multiple variables can be used to accurately predict the effect on the outcome variable. The model creates a best-fit linear relationship that comes as close as possible to all individual data points.

Referring to the MLR equation above, in our example:

- yi = dependent variable -- XOM's price
- xi1 = interest rates
- xi2 = oil price
- xi3 = S&P 500 index value
- xi4 = crude oil futures prices
- B0 = y-intercept at time zero
- B1 = regression coefficient measuring the unit change in the dependent variable when xi1 changes -- the effect of interest rate changes on XOM's price
- B2 = coefficient measuring the unit change in the dependent variable when xi2 changes -- the effect of oil price changes on XOM's price

The least-squares estimates -- B0, B1, B2...Bp -- are typically computed by statistical software. Multiple variables can be included in the regression model, with each independent variable distinguished by a number: 1, 2, 3, 4...p.

**Tip:** Multiple regression can also be nonlinear, in which case the dependent and independent variables do not follow a straight-line relationship.

The multiple regression model enables analysts to predict an outcome based on information from multiple explanatory variables. However, since each data point may deviate slightly from the model's predicted outcome, the model is not always perfectly accurate. The residual value E -- the difference between actual and predicted outcomes -- is included in the model to account for these small variations.

Running the XOM price regression model in statistical software returns the following output:

An analyst would interpret this output as follows: if other variables are held constant, XOM's price will increase by 7.8% when the market price of oil rises by 1%. The model also shows that XOM's price will decrease by 1.5% following a 1% rise in interest rates. R² indicates that 86.5% of the variation in ExxonMobil's stock price can be explained by changes in interest rates, oil prices, oil futures, and the S&P 500 index.

## Difference Between Linear and Multiple Regression

Ordinary least squares (OLS) regression compares the response of a dependent variable given changes in some explanatory variables. However, a dependent variable is rarely explained by only one variable. In such cases, an analyst uses multiple regression, which attempts to explain the dependent variable using more than one independent variable.

Multiple regression can be either linear or nonlinear. MLR is based on the assumption that a linear relationship exists between the dependent and independent variables. It also assumes no major correlation exists among the independent variables.

## What Makes Multiple Regression "Multiple"?

Multiple regression considers the effect of more than one explanatory variable on some outcome of interest. It evaluates the relative effect of these explanatory (independent) variables on the dependent variable while holding all other variables in the model constant.

## Why Use Multiple Regression Instead of Simple OLS Regression?

A dependent variable is rarely explained by only one variable. In such cases, an analyst uses multiple regression, which attempts to explain the dependent variable using more than one independent variable. The model assumes no major correlation among the independent variables.

## Can I Perform Multiple Regression by Hand?

This is unlikely, since multiple regression models are complex, and the complexity increases as more variables are included or the volume of data grows. To run a multiple regression, you will likely need specialized statistical software or functions within programs like Excel.

## What Does "Linear" Mean in Multiple Regression?

In multiple linear regression, the model calculates the best-fit line that minimizes the variance associated with each variable relative to the dependent variable. Because it fits a straight line, it is a linear model. Nonlinear regression models involving multiple variables also exist, such as logistic regression, quadratic regression, and probit models.

## How Are Multiple Regression Models Used in Finance?

Any econometric model that considers multiple variables may be a form of multiple regression. Factor models compare two or more factors to analyze relationships among variables and their resulting performance. The Fama-French Three-Factor Model is one such model, extending the Capital Asset Pricing Model (CAPM) by adding size risk and value risk factors to the market risk factor. By incorporating these two additional factors, the model adjusts for outperformance tendencies, making it a better tool for evaluating manager performance.

## Conclusion

MLR is a statistical tool used to predict the outcome of a variable based on two or more explanatory variables. If only one variable influences the dependent variable, a simple linear regression model is sufficient; if multiple factors affect it, MLR is needed.

A classic example involves the drivers of a company's stock market valuation. Typically, a company's share price is influenced by multiple factors. In this case, the dependent variable is the stock price -- what we are trying to predict -- and the independent (explanatory) variables are the factors that influence the stock price.

## References

[1] Yale University. "[Multiple Linear Regression](http://www.stat.yale.edu/Courses/1997-98/101/linmult.htm)."

[2] CFA Institute. "[Basics of Multiple Regression and Underlying Assumptions](https://www.cfainstitute.org/en/membership/professional-development/refresher-readings/multiple-regression#:~:text=Five%20main%20assumptions%20underlying%20multiple,5%29%20independence%20of%20independent%20variables.)."

[3] Boston University Medical Campus-School of Public Health. "[Multiple Linear Regression](https://sphweb.bumc.bu.edu/otlt/MPH-Modules/PH717-QuantCore/PH717-Module12-MultipleRegression/PH717-Module12-MultipleRegression3.html)."

## About LLMQuant

LLMQuant is a cutting-edge community composed of professionals from top global universities and the quantitative finance industry, dedicated to exploring the limitless possibilities at the intersection of artificial intelligence (AI) and quantitative finance (Quant). Our team members hail from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other prestigious institutions, with external advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and leading proprietary trading firms.
