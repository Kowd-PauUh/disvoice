## Features based on Representation learning strategies using Autoencoders

Compute Features based on Representation learning strategies using convolutional and recurrent Autoencoders

Two types of features are computed

1. 256 features extracted from the bottleneck layer of the autoencoders
2. 128 features based on the MSE between the decoded and input spectrograms of the autoencoder in different frequency regions


Additionally, static (for all utterance) or dynamic (for each 500 ms speech segments) features can be computed:

- The static feature vector is formed with 1536 features and contains (384 descriptors) x (4 functionals: mean, std, skewness, kurtosis)

- The dynamic feature matrix is formed with the 384 descriptors computed for speech segments with 500ms length and 250ms time-shift

- You can choose between features computed from a convolutional or recurrent autoencoder

#### Notes

1. Detailed information is found in 

Vasquez-Correa, J. C., et al. (2020). Parallel Representation Learning for the Classification of Pathological Speech: Studies on Parkinson’s Disease and Cleft Lip and Palate. Speech Communication, 122, 56-67.

2. Additional trained models can be found in 

https://github.com/jcvasquezc/AEspeech

#### References

[1] Vasquez-Correa, J. C., et al. (2020). Parallel Representation Learning for the Classification of Pathological Speech: Studies on Parkinson’s Disease and Cleft Lip and Palate. Speech Communication, 122, 56-67.
