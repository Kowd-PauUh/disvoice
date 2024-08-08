## Phonation features

(Perturbation features)

Compute phonation-based features from sustained vowels and continuous speech utterances.

For continuous speech, the features are computed over voiced segments.

Seven descriptors are computed:

1. First derivative of the fundamental Frequency
2. Second derivative of the fundamental Frequency
3. Jitter
4. Shimmer
5. Amplitude perturbation quotient
6. Pitch perturbation quotient
7. Logaritmic Energy

Additionally, static (for all utterance) or dynamic (frame by frame) features can be computed:

- The static feature vector is formed with 28 features and contains (seven descriptors) x (4 functionals: mean, std, skewness, kurtosis)

- The dynamic feature matrix is formed with the seven descriptors computed for frames of 40 ms with a time-shift of 20 ms.

#### Notes

1. For the dynamic features, the first 11 frames of each recording are not considered to be able to stack the APQ and PPQ descriptors with the remaining ones.

2. The fundamental frequency is computed the RAPT algorithm. To use the PRAAT method,  change the "self.pitch method" variable in the class constructor.

#### References

[[1]](https://link.springer.com/article/10.1007%2Fs12559-017-9497-x) T. Arias-Vergara, J. C. Vásquez-Correa, J. R. Orozco-Arroyave, Parkinson’s Disease and Aging: Analysis of Their Effect in Phonation and Articulation of Speech, Cognitive computation, (2017).

