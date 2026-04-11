![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

# Tail Risk in Financial Markets: Extreme Value Theory (EVT) for VaR and ES Estimation

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

## Extreme Value Theory (EVT): Modeling Tail Risk

In financial risk management, **Extreme Value Theory (EVT)** provides a rigorous statistical framework for analyzing and modeling the tail behavior of return distributions. Financial markets are periodically subject to extreme movements that can inflict significant losses. EVT equips risk managers with tools to better understand, estimate, and prepare for such events.

## Two Principal Approaches in EVT

The central objective of EVT is to model the behavior of extreme observations. Two parametric approaches dominate the literature: the **Block Maxima** method and the **Peaks-Over-Threshold (POT)** method.

### The Block Maxima Method

The Block Maxima approach partitions historical data into non-overlapping blocks (e.g., monthly, quarterly, or annual periods) and extracts the maximum observation from each block. These block maxima form the sample used for tail risk estimation.

Suppose we observe $n$ independent and identically distributed (i.i.d.) random variables with cumulative distribution function $F(x)$. We seek to model the distribution of the sample maximum $M_n = \max(X_1, X_2, \ldots, X_n)$. The CDF of the maximum is:

$$
\Pr(M_n \leq z) = \Pr(X_1 \leq z, \ldots, X_n \leq z) = [F(z)]^n
$$

In practice, the true distribution $F(x)$ is unknown. However, the **Fisher-Tippett-Gnedenko theorem** establishes that, under appropriate normalization, the distribution of the sample maximum converges to one of three families: the **Gumbel**, **Fréchet**, or **Weibull** distributions. These are unified under the **Generalized Extreme Value (GEV)** distribution:

$$
G(x) = \exp \left\{- \left[1 + \xi \left(\frac{x - \mu}{\sigma}\right)\right]^{-1/\xi}\right\}
$$

where $\mu$ is the location parameter, $\sigma$ is the scale parameter, and $\xi$ is the shape parameter. The value of $\xi$ determines the tail behavior:

- $\xi = 0$: Gumbel distribution (light tail)
- $\xi < 0$: Weibull distribution (bounded tail)
- $\xi > 0$: Fréchet distribution (heavy tail)

![](https://fastly.jsdelivr.net/gh/bucketio/img17@main/2025/02/15/1739614133652-5a5c0ac5-0c4f-4bb7-a076-75928efb3481.png)

#### Fitting the Block Maxima Model

To apply the GEV distribution to financial data, we can partition daily return series into monthly blocks and extract the maximum loss from each block. Maximum likelihood estimation (MLE) is then used to fit the GEV parameters.

```r
require(quantmod)
require(xts)
SPY_prices <- Ad(getSymbols('SPY', from = '2006-01-01', to = '2019-01-01', auto.assign = FALSE))
returns_xts <- diff(log(SPY_prices), k = 1)[-1] * 100  # Daily log returns (%)
```

#### Converting to losses and computing monthly block maxima:

```r
monthly_max_daily_loss <- do.call(rbind, lapply(split(x = -1 * returns_xts, 'months'), function(x) x[which.max(x)]))
```

The resulting series of monthly maximum losses is then used to estimate the GEV parameters via MLE.

#### Risk Estimation: VaR

With fitted GEV parameters, risk metrics such as **Value at Risk (VaR)** and **Expected Shortfall (ES)** can be computed. VaR at confidence level $1 - \alpha$ is obtained via the quantile function:

```r
GEV_VAR <- function(params, alpha = .05){
    mu    <- rep(params[1], length(alpha))
    sigma <- rep(params[2], length(alpha))
    xi    <- rep(params[3], length(alpha))
    y <- -log(1 - alpha)
    result <- ifelse(abs(xi) < 0.0001, mu - sigma * log(-y), mu - sigma / xi * (1 - y ^ -xi))
    return(result)
}
```

Computing VaR at multiple confidence levels:

```r
my_fit_vals <- my_gev_fit$par
GEV_VAR(my_fit_vals, alpha = c(.05, .025, .01))
```

---

### The Peaks-Over-Threshold (POT) Method

Unlike the Block Maxima approach, the **POT method** considers all observations exceeding a specified threshold $u$. This approach typically makes more efficient use of extreme observations, particularly when multiple extreme values occur within a single block.

Under the POT framework, exceedances above the threshold are modeled using the **Generalized Pareto Distribution (GPD)**. The **Pickands-Balkema-de Haan theorem** establishes that for a sufficiently high threshold, the conditional distribution of exceedances converges to the GPD:

$$
P(X \leq x \mid X > u) \approx \begin{cases}
1 - \left( 1 + \xi \dfrac{x}{\tau} \right)^{-1/\xi} & \text{if } \xi \neq 0 \\[6pt]
1 - \exp \left( -\dfrac{x}{\tau} \right) & \text{if } \xi = 0
\end{cases}
$$

where $\xi$ and $\tau$ are the shape and scale parameters, respectively.

#### Fitting the POT Model

First, define a threshold and extract exceedances:

```r
require(quantmod)
require(xts)

SPY_prices <- Ad(getSymbols('SPY', from = '2006-01-01', to = '2019-01-01', auto.assign = FALSE))
returns_xts <- -1 * diff(log(SPY_prices), k = 1)[-1] * 100  # Daily log losses (%)
names(returns_xts) <- 'SPY_Returns'

# Set threshold
my_threshold <- 0.85

# Extract exceedances
my_data <- returns_xts[returns_xts > my_threshold]
```

Parameter estimation via maximum likelihood:

```r
gpd_loglik <- function(params, threshold, data){
    xi <- params[1]; tau <- params[2]
    data <- data - threshold  # y = x - u
    data <- coredata(data[data > 0])
    m <- nrow(data)
    if((tau <= 0) | (xi <= -1)) return(1e6)  # Parameter constraints
    term1 <- -m * log(tau)
    if(abs(xi) < 0.0001){
        result <- term1 - 1 / tau * sum(data)
    } else {
        if(any(1 + xi * data / tau <= 0)) return(1e6)
        result <- term1 - (1 + 1 / xi) * sum(log(1 + xi * data / tau))
    }
    return(-result)
}
```

Optimization:

```r
my_gpd_fit <- optim(par = c(0.5, 0.5), fn = gpd_loglik, method = "Nelder-Mead",
                    threshold = my_threshold, data = returns_xts)
my_gpd_fit
```

### Computing VaR and ES

#### Value at Risk (VaR)

VaR represents the loss threshold at a specified confidence level. The quantile function for the GEV distribution is:

$$
\hat{z}_p = \begin{cases}
\mu - \dfrac{\sigma}{\hat{\xi}} \left[ 1 - y_p^{-\xi} \right] & \text{if } \hat{\xi} \neq 0 \\[6pt]
\hat{\mu} - \hat{\sigma} \log(-y_p) & \text{if } \hat{\xi} = 0
\end{cases}
$$

where $y_p = -\log(1 - p)$ and $p$ is the tail probability (e.g., $p = 0.05$ for the 95th percentile).

```r
GEV_VAR <- function(params, alpha = .05){
    mu    <- rep(params[1], length(alpha))
    sigma <- rep(params[2], length(alpha))
    xi    <- rep(params[3], length(alpha))
    y <- -log(1 - alpha)
    result <- ifelse(abs(xi) < 0.0001, mu - sigma * log(-y), mu - sigma / xi * (1 - y ^ -xi))
    return(result)
}

my_fit_vals <- my_gev_fit$par
GEV_VAR(my_fit_vals, alpha = c(.05, .025, .01))
```

#### Expected Shortfall (ES)

**Expected Shortfall** (also known as Conditional VaR) quantifies the average loss conditional on the loss exceeding VaR. It captures the severity of tail events beyond the VaR threshold:

$$
\mathrm{ES}_{\alpha} = \frac{1}{1 - \alpha} \int_{\alpha}^{1} q_x(F) \, \mathrm{d}x = \frac{\text{VaR}_{\alpha}}{1 - \xi} + \frac{\tilde{\sigma} - \xi u}{1 - \xi}
$$

Implementation in R:

```r
GEV_ES <- function(params, alpha = .05){
    my_fun <- function(x) {GEV_VAR(x, params = params)}
    result <- 1 / alpha * integrate(my_fun, lower = .00001, upper = alpha, stop.on.error = FALSE)$value
    return(result)
}

GEV_ES(my_fit_vals, alpha = .01)
```

This yields the expected average loss in the tail — a more informative risk measure than VaR alone, as it accounts for the magnitude of extreme losses rather than simply their frequency.

## Summary

Extreme Value Theory provides a powerful toolkit for modeling tail risk in financial markets, particularly during episodes of extreme volatility. Through the **Block Maxima** and **Peaks-Over-Threshold** approaches, practitioners can estimate tail distributions using the **Generalized Extreme Value (GEV)** and **Generalized Pareto Distribution (GPD)**, respectively.

The derived risk metrics — **Value at Risk (VaR)** and **Expected Shortfall (ES)** — enable financial institutions and investors to quantify the impact of extreme events and implement appropriate risk controls. VaR provides a threshold for potential losses at a specified confidence level, while ES offers a deeper characterization of tail risk by averaging over all losses that exceed the VaR boundary.

Together, these tools form an essential component of modern quantitative risk management, complementing standard distributional assumptions that may understate the probability and severity of extreme market events.
