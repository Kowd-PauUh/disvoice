# DisVoice

It's a fixed version of a [DisVoice](https://github.com/jcvasquezc/DisVoice) package **for Linux machines**, compatible with the latest versions of its dependencies and applied code refactoring where necessary. 

This work is a part of the [Speech Based Distress Recognition](https://gitlab.com/Kowd-PauUh/speech-based-distress-recognition/) project and is aimed to help researches who are willing to use DisVoice, since the original package code has outdated dependencies, bugs and is difficult to deal with.

DisVoice is a python package designed to compute features from speech files. Disvoice computes glottal, phonation, articulation, prosody, phonological, and features representation learnig strategies using autoencoders. The features can be computed both from sustained vowels and continuous speech utterances with the aim to recognize praliguistic aspects from speech.

The features can be used in classifiers to recognize emotions, or communication capabilities of patients with different speech disorders including diseases with functional origin such as larinx cancer or nodules; craneo-facial based disorders such as hipernasality developed by cleft-lip and palate; or neurodegenerative disorders such as Parkinson's or Hungtinton's diseases.

The features are also suitable to evaluate mood problems like depression based on speech patterns.

### Installation

```
apt-get install praat
pip install git+https://gitlab.com/Kowd-PauUh/disvoice.git
```

### Development

As an alternative to the direct installation (in case you need to fix something or add new functionalities) you can clone this repository and install it in editable mode:

```
git clone https://gitlab.com/Kowd-PauUh/disvoice.git kowd-pauuh-disvoice
cd kowd-pauuh-disvoice
```

Now if you want to work in fully isolated environment it's recommended to have a docker daemon on your machine and execute the following commands (you can see more `make` targets in `Makefile`):
```
make build
make start
```

It will build and start a docker container with Python 3.10 (you can also change it in first line of `docker/pythonenv/Dockerfile`) which you then can enter and work iside it:
```
make shell
pip install -e .
```

You may also want to omit the steps with Docker. In that case you just install the package how you would normally do:
```
git clone https://gitlab.com/Kowd-PauUh/disvoice.git kowd-pauuh-disvoice
cd kowd-pauuh-disvoice
pip install -e .
```

## Reference

If you use Disvoice for research purposes, please cite the following papers, depending on the features you use:

## Glottal features

[1] Belalcázar-Bolaños, E. A., Orozco-Arroyave, J. R., Vargas-Bonilla, J. F., Haderlein, T., & Nöth, E. (2016, September). Glottal Flow Patterns Analyses for Parkinson’s Disease Detection: Acoustic and Nonlinear Approaches. In International Conference on Text, Speech, and Dialogue (pp. 400-407). Springer.

## Phonation features

[1] T. Arias-Vergara, J. C. Vásquez-Correa, J. R. Orozco-Arroyave, Parkinson's Disease and Aging: Analysis of Their Effect in Phonation and Articulation of Speech, Cognitive computation, (2017).

[2] Vásquez-Correa, J. C., et al. "Towards an automatic evaluation of the dysarthria level of patients with Parkinson's disease." Journal of communication disorders 76 (2018): 21-36.

## Articulation features

[1] Vásquez-Correa, J. C., et al. "Towards an automatic evaluation of the dysarthria level of patients with Parkinson's disease." Journal of communication disorders 76 (2018): 21-36.

[2]. J. R. Orozco-Arroyave, J. C. Vásquez-Correa et al. "NeuroSpeech: An open-source software for Parkinson's speech analysis." Digital Signal Processing (2017).

## Prosody features

[1]. N., Dehak, P. Dumouchel, and P. Kenny. "Modeling prosodic features with joint factor analysis for speaker verification." IEEE Transactions on Audio, Speech, and Language Processing 15.7 (2007): 2095-2103.

[2] Vásquez-Correa, J. C., et al. "Towards an automatic evaluation of the dysarthria level of patients with Parkinson's disease." Journal of communication disorders 76 (2018): 21-36.

## Phonological features

[1] Vásquez-Correa, J. C., et al (2019). Phonet: a Tool Based on Gated Recurrent Neural Networks to Extract Phonological Posteriors from Speech. Proc. Interspeech 2019, 549-553.

## Representaton learning-based features

[1] Vasquez-Correa, J. C., et al. (2020). Parallel Representation Learning for the Classification of Pathological Speech: Studies on Parkinson’s Disease and Cleft Lip and Palate. Speech Communication, 122, 56-67.
