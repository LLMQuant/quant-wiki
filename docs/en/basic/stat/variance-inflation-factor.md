![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# What Is the Variance Inflation Factor (VIF)?
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

The Variance Inflation Factor (VIF) is a measure of the degree of multicollinearity in regression analysis. Multicollinearity arises when multiple independent variables in a multiple regression model are correlated, which can adversely affect regression results. The VIF estimates the extent to which the variance of a regression coefficient is inflated due to multicollinearity.

### Key Takeaways

- The VIF provides a measure of multicollinearity among independent variables in a multiple regression model.
- Detecting multicollinearity is important because, while it does not reduce the model's overall explanatory power, it does reduce the statistical significance of the individual independent variables.
- A high VIF for an independent variable indicates a strong collinear relationship with other variables, which should be considered or adjusted for in the model's structure and variable selection.

## Understanding the Variance Inflation Factor (VIF)

The VIF is a tool for identifying the degree of multicollinearity. Multiple regression is used when a researcher wants to test the effect of multiple variables on a particular outcome. The dependent variable is the outcome being influenced by the independent variables. Multicollinearity exists when one or more independent variables are linearly related or correlated.

Multicollinearity creates problems in the multiple regression model because the independent variables influence each other and are not truly independent, making it difficult to test how individual combinations of independent variables affect the dependent variable.

Although multicollinearity does not reduce the model's overall predictive power, it can produce regression coefficient estimates that are not statistically significant. In a sense, it can be viewed as a form of double-counting within the model.

In statistics, a multiple regression model with high multicollinearity makes it more difficult to estimate the relationship between each independent variable and the dependent variable. When two or more independent variables are closely related or measure nearly the same thing, the underlying effect they measure is accounted for across the variables. When independent variables are highly correlated, it becomes difficult to determine which one is influencing the dependent variable.

Small changes in the data or adjustments to the model equation structure can produce large and unstable changes in the estimated coefficients. This is problematic because many econometric models aim to test precisely this type of statistical relationship between independent and dependent variables.

To ensure proper model specification and functioning, tests for multicollinearity can be conducted. The VIF is one such measure. Using the VIF helps identify the severity of any multicollinearity issues so that the model can be adjusted. The VIF measures the extent to which the behavior (variance) of an independent variable is influenced by its interaction or correlation with other independent variables.

The VIF provides a quick measure of how much a variable contributes to the standard error in a regression. When significant multicollinearity issues exist, the VIF will be very large for the variables involved. Once these variables are identified, several approaches can be used to eliminate or combine the collinear variables, resolving the multicollinearity problem.

## VIF Formula and Calculation

The VIF formula is:

$$ \begin{aligned}&\text{VIF}_i = \frac{ 1 }{ 1 - R_i^2 } \\&\textbf{where:} \\&R_i^2 = \text{Unadjusted coefficient of determination from regressing the } i\text{th independent variable on the remaining independent variables} \\\end{aligned} $$

## What the VIF Can Tell You

When $R_i^2$ equals 0, the VIF (or tolerance) is 1, meaning the $i$th independent variable is uncorrelated with the remaining independent variables and multicollinearity is not present.

As a general guideline:

- VIF equal to 1 = variables are uncorrelated
- VIF between 1 and 5 = variables are moderately correlated
- VIF greater than 5 = variables are highly correlated

The higher the VIF, the greater the likelihood that multicollinearity exists and requires further investigation. When the VIF exceeds 10, significant multicollinearity is present and requires correction.

## Example of Using the VIF

For instance, suppose an economist wants to test whether there is a statistically significant relationship between the unemployment rate (independent variable) and the inflation rate (dependent variable). Including additional independent variables related to the unemployment rate, such as new initial jobless claims, would likely introduce multicollinearity into the model.

The overall model might show strong statistical explanatory power but be unable to determine whether the effect is primarily due to the unemployment rate or new initial jobless claims. This is the issue the VIF can detect, potentially suggesting that one variable be dropped from the model or that some way be found to consolidate them to capture their joint effect, depending on the hypothesis being tested.

## What Is a Good VIF Value?

As a rule of thumb, a VIF below 3 is not a cause for concern. As the VIF increases, the reliability of your regression results decreases.

## What Does a VIF of 1 Represent?

A VIF of 1 indicates that the independent variables are uncorrelated and that no multicollinearity exists in the regression model.

## What Is the VIF Used For?

The VIF is used to measure the strength of correlation among independent variables in a regression analysis. This correlation is known as multicollinearity and can cause problems for the regression model.

## Summary

While a moderate degree of multicollinearity in a regression model is acceptable, higher levels can become a concern.

Two measures can be taken to correct high multicollinearity. First, one or more highly correlated variables can be removed, since the information they provide is redundant. Second, methods such as principal component analysis or partial least squares regression can be used instead of ordinary least squares regression to either reduce the variables to a smaller uncorrelated set or create new uncorrelated variables. This will improve the model's predictive ability.

## References

[1] CFI. "[Variance Inflation Factor](https://corporatefinanceinstitute.com/resources/knowledge/other/variance-inflation-factor-vif/)."

[2] Isixsigma. "[Variance Inflation Factor (VIF)](https://www.isixsigma.com/dictionary/variance-inflation-factor-vif/)."

## About LLMQuant

LLMQuant is a cutting-edge community composed of professionals from top global universities and the quantitative finance industry, dedicated to exploring the limitless possibilities at the intersection of artificial intelligence (AI) and quantitative finance (Quant). Our team members hail from Cambridge, Oxford, Harvard, ETH Zurich, Peking University, USTC, and other prestigious institutions, with external advisors from Microsoft, HSBC, Citadel, Man Group, Citi, Jump Trading, and leading proprietary trading firms.
