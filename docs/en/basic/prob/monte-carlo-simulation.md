![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)
# What Is a Monte Carlo Simulation?
![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

A Monte Carlo simulation is a modeling technique used to predict the probability of various outcomes in a process that is difficult to forecast due to the intervention of random variables. It is a method for understanding the impact of risk and uncertainty. Monte Carlo simulations can be applied to a wide range of problems across multiple domains, including investing, business, physics, and engineering. This technique is also referred to as multiple probability simulation.

### Key Takeaways

- A Monte Carlo simulation is a model used to predict the probability of multiple outcomes in the presence of random variables.
- Monte Carlo simulations help explain the impact of risk and uncertainty in forecasting and prediction models.
- A Monte Carlo simulation requires assigning multiple values to an uncertain variable to obtain multiple results, which are then averaged to produce an estimate.
- These simulations assume perfectly efficient markets.
- Monte Carlo simulations are increasingly being combined with artificial intelligence.

## How Monte Carlo Simulations Assess Risk

When making predictions or estimates under significant uncertainty, some approaches replace uncertain variables with a single average value. Monte Carlo simulation instead uses multiple values and then averages the results.

Monte Carlo simulations have broad applications in fields affected by random variables, particularly in business and investing. They are used to estimate the probability of cost overruns in large projects and to predict the likelihood that an asset price will move in a certain direction.

Telecommunications companies use them to evaluate network performance under various scenarios, enabling network optimization. Insurance companies use them to quantify potential risk exposure and price their policies accordingly. Investment analysts employ Monte Carlo simulations to assess default risk and to analyze derivatives such as options. Financial planners can use them to project the probability of a client running out of money in retirement. [1]

Monte Carlo simulations are also widely used beyond business and finance, including in meteorology, astronomy, and physics.

Today, Monte Carlo simulations are increasingly combined with new artificial intelligence (AI) models. According to IBM in 2024, many financial firms now use high-performance computing systems to run Monte Carlo simulations, and "as these simulations grow in number, covering an ever-expanding range of financial assets and instruments, making full sense of all that data becomes increasingly challenging." This is where AI comes in. IBM states that "using AI to assist professionals in evaluating these simulations can improve accuracy, provide more timely insights. In a business where timeliness is a key differentiator, that has immediate commercial value." [2]

## History of Monte Carlo Simulation

Monte Carlo simulations are named after the famous gambling destination in Monaco because chance and random outcomes are central to this modeling technique, just as they are to games of roulette, dice, and slot machines.

The technique was originally developed by mathematician Stanislaw Ulam, who worked on the Manhattan Project -- the secret effort to build the first atomic bomb. He shared his ideas with Manhattan Project colleague John von Neumann, and together they refined the Monte Carlo simulation. [3]

## How Monte Carlo Simulations Work

The Monte Carlo method acknowledges the core challenge faced by any simulation technique: the impossibility of precisely determining the probability of different outcomes when random variables are involved. Therefore, Monte Carlo simulations focus on constantly repeating random samples.

A Monte Carlo simulation assigns a random value to the uncertain variable, runs the model, and produces a result. This process is repeated many times, with many different values assigned to the relevant variables. Once the simulation is complete, the results are averaged to arrive at an estimate.

## Four Steps of a Monte Carlo Simulation

To perform a Monte Carlo simulation, there are four main steps. Using a program such as Microsoft Excel, you can create a Monte Carlo simulation to estimate the price movement of a stock or other asset.

Asset price movement has two components: drift, which is the constant directional movement, and a random input representing market volatility.

By analyzing historical price data, you can determine a security's drift, standard deviation, variance, and average price movement. These serve as the fundamental building blocks of a Monte Carlo simulation.

The four steps are:

**Step 1.** Using the asset's historical price data, generate a series of periodic daily returns using the natural logarithm (note that this formula differs from the standard percentage change formula) to project a possible price trajectory.

**Step 2.** Apply the AVERAGE, STDEV.P, and VAR.P functions to the entire series of results to obtain the average daily return, standard deviation, and variance inputs. The drift equals:

Alternatively, drift can be set to 0 -- this reflects a certain theoretical orientation, but for short time frames the difference is minimal.

**Step 3.** Obtain the random input:

The next day's price equation is:

**Step 4.** In Excel, to raise e to a given power x, use the EXP function: EXP(x). Repeat this calculation the desired number of times (each repetition represents one day). The result is a simulation of the asset's future price movement.

By generating any number of simulations, you can assess the probability that a security's price will follow a given trajectory.

## Interpreting Monte Carlo Simulation Results

The frequency of different outcomes generated by the simulation will form a normal distribution -- a bell curve. The most probable return lies at the center of the curve, meaning the actual return is equally likely to be above or below that value.

The probability that the actual return falls within one standard deviation of the most probable ("expected") rate is 68%. The probability within two standard deviations is 95%, and within three standard deviations is 99.7%.

However, there is no guarantee that the most expected outcome will occur or that actual movements will not exceed the most extreme projections.

Crucially, Monte Carlo simulations ignore all factors not built into the price movement model, such as macro trends, company leadership, market hype, and cyclical factors.

In other words, they assume perfectly efficient markets.

## Advantages and Disadvantages of Monte Carlo Simulations

Monte Carlo simulations were created to address perceived shortcomings of other methods for estimating possible outcomes.

The key distinction is that the Monte Carlo method tests multiple random variables and then averages them, rather than starting from a single average value.

Like any financial simulation, the Monte Carlo method uses historical price data as the basis for projecting future prices. It then disrupts the pattern by introducing random variables expressed numerically. Finally, it averages these numbers to estimate the risk that the pattern will be disrupted in real life.

Of course, no simulation can accurately predict inevitable outcomes. The Monte Carlo method aims to provide a more scientific probability estimate -- a forecast of how likely a given outcome is to deviate from expectations.

## Applications of Monte Carlo Simulation in Finance

Monte Carlo simulations are used to estimate the probability of a particular outcome, making them popular among investors and financial analysts for evaluating the potential success of investments they are considering. Common uses include:

- **Stock option pricing:** Tracking the potential price movements of the underlying asset across every possible variable. Results are averaged and discounted to the asset's current price. This aims to indicate the option's potential payoff.
- **Portfolio valuation:** Multiple alternative portfolios can be tested using Monte Carlo simulations to produce a comparative measure of their relative risk.
- **Fixed-income investments:** The short-term interest rate serves as the random variable. The simulation is used to calculate the potential impact of short-term rate fluctuations on fixed-income investments such as bonds.

## Which Professions Use Monte Carlo Simulations?

Although Monte Carlo simulations are best known for their financial applications, they are used in virtually every profession that needs to measure risk and plan accordingly.

For example, a telecommunications company might build its network to support all users' needs. To do this, it must account for all possible variations in service demand and determine whether the system can handle peak times and peak seasons.

A Monte Carlo simulation might help the company determine whether its service can handle the pressure of Super Bowl Sunday as well as an ordinary Sunday in August.

## What Factors Are Assessed in Monte Carlo Simulations?

Monte Carlo simulations in investing are based on the historical price data of the asset being evaluated.

The fundamental building blocks of the simulation are derived from historical data: drift, standard deviation, variance, and average price movement.

## Conclusion

Monte Carlo simulations reveal a spectrum of possible outcomes under uncertain conditions. The technique assigns multiple values to uncertain variables, obtains multiple results, and then averages those results to arrive at an estimate.

From investing to engineering, the Monte Carlo method is used across many fields to measure risk, including estimating the probability of investment gains or losses and the likelihood that a project will exceed its budget.

## References

[1] T. Rowe Price. "[How a Monte Carlo Analysis Could Help Improve Your Retirement Plan](https://www.troweprice.com/personal-investing/resources/insights/how-monte-carlo-analysis-could-improve-your-retirement-plan.html)."

[2] IBM. "[Working Together, AI & HPC Can Solve Large, Complex Problems](https://community.ibm.com/community/user/cloud/blogs/john-easton/2024/03/25/working-together-ai-hpc-can-solve-large-complex-ch?CommunityKey=74d589b7-7276-4d70-acf5-0fc26430c6c0)."

[3] Virginia Polytechnic Institute, via Internet Archive Wayback Machine. "[Monte Carlo Simulation](https://web.archive.org/web/20201025115012/https://sites.google.com/a/vt.edu/monte-carlo-simulation/history)."
