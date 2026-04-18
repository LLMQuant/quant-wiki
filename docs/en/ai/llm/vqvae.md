![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

# VQ-VAE Generative Model Overview

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

This is a PyTorch implementation of the VQ-VAE generative model (<https://arxiv.org/abs/1711.00937>).

You can find the authors' [original Tensorflow implementation here](https://github.com/deepmind/sonnet/blob/master/sonnet/python/modules/nets/vqvae.py), which includes [an example that can be run in a Jupyter notebook](https://github.com/deepmind/sonnet/blob/master/sonnet/examples/vqvae_example.ipynb).

## Installing Dependencies

To install the dependencies, create a conda or virtual environment with Python 3, then run `pip install -r requirements.txt`.

## Running the VQ-VAE

To run the VQ-VAE, simply execute `python3 main.py`. Include the `-save` flag if you want to save your model. You can also specify parameters on the command line. The default values are:

```python
parser.add_argument("--batch_size", type=int, default=32)
parser.add_argument("--n_updates", type=int, default=5000)
parser.add_argument("--n_hiddens", type=int, default=128)
parser.add_argument("--n_residual_hiddens", type=int, default=32)
parser.add_argument("--n_residual_layers", type=int, default=2)
parser.add_argument("--embedding_dim", type=int, default=64)
parser.add_argument("--n_embeddings", type=int, default=512)
parser.add_argument("--beta", type=float, default=.25)
parser.add_argument("--learning_rate", type=float, default=3e-4)
parser.add_argument("--log_interval", type=int, default=50)
```

## Model Architecture

The VQ-VAE consists of the following core components:

1. An `Encoder` class that defines the mapping `x -> z_e`
2. A `VectorQuantizer` class that converts the encoder output into discrete one-hot vectors representing the index of the nearest embedding vector: `z_e -> z_q`
3. A `Decoder` class that defines the mapping `z_q -> x_hat`, reconstructing the original image

The encoder and decoder are built from stacks of convolutions and transposed convolutions with residual blocks in the architecture (see the [ResNet paper](https://arxiv.org/abs/1512.03385)). The residual modules are defined by the `ResidualLayer` and `ResidualStack` classes.

These components are organized in the following directory structure:

```
models/
    - decoder.py -> Decoder
    - encoder.py -> Encoder
    - quantizer.py -> VectorQuantizer
    - residual.py -> ResidualLayer, ResidualStack
    - vqvae.py -> VQVAE
```

## PixelCNN -- Sampling from the VQ-VAE Latent Space

To sample from the latent space, we fit a PixelCNN over the latent pixel values `z_ij`. The key insight is that the VQ-VAE maps images to a latent space with the same structure as a single-channel image. For example, with default VQ-VAE parameters, an RGB image of shape `(32,32,3)` is mapped to a latent space of shape `(8,8,1)` -- equivalent to an `(8,8,1)` grayscale image. Therefore, PixelCNN can be used to model the distribution of "pixel" values in the 8x8 single-channel latent space.

To train PixelCNN on the latent representations, follow these steps:

1. Train a VQ-VAE on your chosen dataset.
2. Use the saved VQ-VAE parameters to encode the dataset and save the discrete latent space representations using `np.save`. In `quantizer.py`, this corresponds to the `min_encoding_indices` variable.
3. Specify the path to the saved latent space dataset in the `utils.load_latent_block` function.
4. Run the PixelCNN training script.

To run PixelCNN, simply execute:

`python pixelcnn/gated_pixelcnn.py`

along with any desired parameters (see the argparse statements). The default dataset is `LATENT_BLOCK`, which only works after you have trained a VQ-VAE and saved the latent representations.
