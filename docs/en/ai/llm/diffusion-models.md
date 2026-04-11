![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

# Diffusion Models: An Overview of Training and Sampling

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

**Diffusion models** are inspired by non-equilibrium thermodynamics. They define a Markov chain of diffusion steps that gradually add random noise to data, then learn the reverse diffusion process to construct desired data samples from noise. Unlike VAEs or flow models, diffusion models are trained with a fixed procedure, and the latent variables are high-dimensional.

During **training**, noise is progressively added to an image, and the network receives this noisy image as input. The network's task is to predict the noise that was added.

During **inference**, starting from randomly generated noise, the network predicts the added noise at each step, which is then progressively removed until the original data is recovered.

---

# 1. The Forward Diffusion Process

- The forward process consists of incrementally adding noise to an image until it becomes pure noise.
- The added noise is Gaussian, and each timestep produces its noisy image from the previous timestep's result.

**The noise addition process:**

Two parameters are defined: $\alpha_t$ and $\beta_t$ (where $t$ ranges from 0 to $T$ as integers, and $\beta_t$ increases from $\beta_1$ to $\beta_T$ -- in the original paper, linearly from 0.0001 to 0.02 over $T$ steps).

The relationship between $\alpha_t$ and $\beta_t$ is:

$\alpha_t = 1 - \beta_t$             (1)

$T$ represents the total number of diffusion steps required to transform an image into pure noise. $t$ denotes a specific step within this process.

The noise addition at each step can be expressed as:

$x_t = \sqrt{\alpha_t} x_{t-1} + \sqrt{1-\alpha_t} z_t$          (2)

where $x_t$ is the image after adding noise at diffusion step $t$, $x_{t-1}$ is the image from step $t-1$, and $z_t$ is the noise added at step $t$, sampled from the standard normal distribution $N(0,1)$.

Following equation (2), we can sequentially diffuse from the original image $x_0$ to $x_T$:

$x_1 = \sqrt{\alpha_1} x_0 + \sqrt{1-\alpha_1} z_1$

$x_2 = \sqrt{\alpha_2} x_1 + \sqrt{1-\alpha_2} z_2$

......

$x_t = \sqrt{\alpha_t} x_{t-1} + \sqrt{1-\alpha_t} z_t$

......

$x_T = \sqrt{\alpha_T} x_{T-1} + \sqrt{1-\alpha_T} z_T$

As $\beta_t$ gradually increases, $\alpha_t$ correspondingly decreases, and $1 - \alpha_t$ grows -- meaning the proportion of added noise increases while the proportion of the original image diminishes, with noise levels escalating at each step.

However, for network training, data must be randomly sampled. Recursively computing from $x_0$ every time we sample a particular timestep $t$ would be prohibitively expensive.

We need a closed-form solution. Substituting $x_{t-1} = \sqrt{\alpha_{t-1}} x_{t-2} + \sqrt{1-\alpha_{t-1}} z_{t-1}$ into equation (2):

$x_t = \sqrt{\alpha_t}(\sqrt{\alpha_{t-1}} x_{t-2} + \sqrt{1-\alpha_{t-1}} z_{t-1}) + \sqrt{1-\alpha_t} z_t$

Expanding:

$x_t = \sqrt{\alpha_t} \sqrt{\alpha_{t-1}} x_{t-2} + \sqrt{\alpha_t} \sqrt{1-\alpha_{t-1}} z_{t-1} + \sqrt{1-\alpha_t} z_t$

$= \sqrt{\alpha_t} \sqrt{\alpha_{t-1}} x_{t-2} + (\sqrt{\alpha_t(1-\alpha_{t-1})} z_{t-1} + \sqrt{1-\alpha_t} z_t)$

Since all noise terms $z_1, z_2, \ldots, z_T$ are independently drawn from $N(0,1)$, and multiplying a normal distribution by a constant only changes the variance, and $N(0, \sigma_1^2) + N(0, \sigma_2^2) \sim N(0, \sigma_1^2 + \sigma_2^2)$, we can merge the coefficients:

$x_t = \sqrt{\alpha_t \alpha_{t-1}} x_{t-2} + \sqrt{1 - \alpha_t \alpha_{t-1}} z$

Continuing this recursive substitution all the way back to $x_0$:

$x_t = \sqrt{\alpha_t \alpha_{t-1} \cdots \alpha_2 \alpha_1} x_0 + \sqrt{1 - \alpha_t \alpha_{t-1} \cdots \alpha_2 \alpha_1} z$

$= \sqrt{\overline{\alpha_t}} x_0 + \sqrt{1 - \overline{\alpha_t}} z$    (3)

where $\overline{\alpha_t}$ denotes the cumulative product from $\alpha_1$ to $\alpha_t$.

# 2. The Training Process

The diffusion model training procedure is as follows:

1. Randomly select an image from the dataset.
2. Randomly sample a diffusion step from 1 to T.
3. Compute $x_t$ using equation (3).
4. Feed $x_t$ into the network, obtain the output, compute the loss against the added noise, and update gradients.
5. Repeat until convergence.

The detailed training code is as follows:

```python
for i, (x_0) in enumerate(tqdm_data_loader):  # Load data from the data loader
    x_0 = x_0.to(device)  # Move data to the computation device
    t = torch.randint(1, T, size=(x_0.shape[0],), device=device)  # Randomly sample a diffusion step in [1, T] for each image
    sqrt_alpha_t_bar = torch.gather(sqrt_alphas_bar, dim=0, index=t).reshape(-1, 1, 1, 1)  # Get sqrt(alpha_bar_t) for each sampled t
    """Get sqrt(1 - alpha_bar_t) for each sampled t"""
    sqrt_one_minus_alpha_t_bar = torch.gather(sqrt_one_minus_alphas_bar, dim=0, index=t).reshape(-1, 1, 1, 1)
    noise = torch.randn_like(x_0).to(device)  # Sample z from standard normal distribution
    x_t = sqrt_alpha_t_bar * x_0 + sqrt_one_minus_alpha_t_bar * noise  # Compute x_t
    out = net_model(x_t, t)  # Feed x_t into the model to get the prediction
    loss = loss_function(out, noise)  # Compute loss between model output and the added noise
    optimizer.zero_grad()  # Zero the optimizer gradients
    loss.backward()  # Backpropagate
    optimizer.step()  # Update parameters
```

# 3. The Reverse (Sampling) Process

The sampling process works backward from $x_T$, progressively removing noise to recover $x_0$.

Starting from $x_T$, we first infer $x_{t-1}$, then $x_{t-2}$, and so on until we reach $x_0$.

Using Bayes' theorem, the reverse step is derived as:
$$
x_{t-1} = \frac{1}{\sqrt{\alpha_t}} \left( x_t - \frac{1-\alpha_t}{\sqrt{1-\overline{\alpha_t}}} M(x_t, t) \right) + \sqrt{\beta_t} z
$$

The complete algorithm is:

1. Sample $x_T$ from the standard normal distribution.
2. Iterate from $T$ down to 1.
3. At each step, compute $x_{t-1}$ using the formula above, where $M(x_t, t)$ is the neural network that takes the current noisy image $x_t$ and the step index $t$ as inputs (the model encodes position information for each step). $z$ is sampled from $N(0,1)$, except at the final step where $z = 0$.

The implementation code:

```python
for t_step in reversed(range(T)):  # Iterate from T down to 0
    t = t_step
    t = torch.tensor(t).to(device)

    z = torch.randn_like(x_t, device=device) if t_step > 0 else 0  # Sample from N(0,1) if t > 0, otherwise 0
    """Compute x_{t-1} according to the formula"""
    x_t_minus_one = torch.sqrt(1/alphas[t]) * (x_t - (1-alphas[t]) * model(x_t, t.reshape(1,)) / torch.sqrt(1-alphas_bar[t])) + torch.sqrt(betas[t]) * z

    x_t = x_t_minus_one
```

# 4. The Network Architecture

The model uses a **UNet** architecture with positional encoding for the diffusion step $t$.
