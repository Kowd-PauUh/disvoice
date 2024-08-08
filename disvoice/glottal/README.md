## Glottal source features

Compute phonation features derived from the glottal source reconstruction from sustained vowels.

Nine descriptors are computed:

1. Variability of time between consecutive glottal closure instants (GCI)
2. Average opening quotient (OQ) for consecutive glottal cycles: rate of opening phase duration / duration of glottal cycle
3. Variability of opening quotient (OQ) for consecutive glottal cycles: rate of opening phase duration /duration of glottal cycle
4. Average normalized amplitude quotient (NAQ) for consecutive glottal cycle: ratio of the amplitude quotient and the duration of the glottal cycle
5. Variability of normalized amplitude quotient (NAQ) for consecutive glottal cycles: ratio of the amplitude quotient and the duration of the glottal cycle
6. Average H1H2: Difference between the first two harmonics of the glottal flow signal
7. Variability H1H2: Difference between the first two harmonics of the glottal flow signal
8. Average of Harmonic richness factor (HRF): ratio of the sum of the harmonics amplitude and the amplitude of the fundamental frequency
9. Variability of HRF

Static or dynamic features can be computed:

The static matrix is formed with 36 features formed with (9 descriptors) x (4 functionals: mean, std, skewness, kurtosis)

Dynamic matrix is formed with the 9 descriptors computed for frames of 200 ms length.

#### Notes

1. The fundamental frequency is computed using the RAPT algorithm.

#### References

[[1]](https://link.springer.com/chapter/10.1007/978-3-319-45510-5_46) Belalcázar-Bolaños, E. A., Orozco-Arroyave, J. R., Vargas-Bonilla, J. F., Haderlein, T., & Nöth, E. (2016, September). Glottal Flow Patterns Analyses for Parkinson’s Disease Detection: Acoustic and Nonlinear Approaches. In International Conference on Text, Speech, and Dialogue (pp. 400-407). Springer.
