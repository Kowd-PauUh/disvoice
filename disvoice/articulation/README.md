## Articulation features

Compute articulation features from continuous speech.

122 descriptors are computed:

- 1 - 22. Bark band energies in onset transitions (22 BBE).
- 23 - 34. Mel frequency cepstral coefficients in onset transitions (12 MFCC onset)
- 35 - 46. First derivative of the MFCCs in onset transitions (12 DMFCC onset)
- 47 - 58. Second derivative of the MFCCs in onset transitions (12 DDMFCC onset)
- 59 - 80. Bark band energies in offset transitions (22 BBE).
- 81 - 92. MFCCs in offset transitions (12 MFCC offset)
- 93 - 104. First derivative of the MFCCs in offset transitions (12 DMFCC offset)
- 105 - 116. Second derivative of the MFCCs in offset transitions (12 DMFCC offset)
- 117 First formant Frequency
- 118 First Derivative of the first formant frequency
- 119 Second Derivative of the first formant frequency
- 120 Second formant Frequency
- 121 First derivative of the Second formant Frequency
- 122 Second derivative of the Second formant Frequency

In addition, static (for all utterance) or dynamic (at-frame level) features can be computed:

- The static feature vector is formed with 488 features (122 descriptors) x (4 functionals: mean, std, skewness, kurtosis)

- The dynamic matrix contains 58 descriptors (22 BBEs, 12 MFCC, 12DMFCC, 12 DDMFCC ) computed for frames of 40 ms of onset segments.

The first two frames of each recording are not considered for dynamic analysis to be able to stack the derivatives of MFCCs

#### Notes

1. The fundamental frequency is computed the PRAAT algorithm. To use the RAPT method,  change the "self.pitch method" variable in the class constructor.

2. The formant frequencies are computed using Praat

#### References

[[1]](https://www5.informatik.uni-erlangen.de/Forschung/Publikationen/2018/Vasquez-Correa18-TAA.pdf) Vásquez-Correa, J. C., et al. "Towards an automatic evaluation of the dysarthria level of patients with Parkinson's disease." Journal of communication disorders 76 (2018): 21-36.
