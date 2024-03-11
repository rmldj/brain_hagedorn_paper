# Supplementary code 

Code and preprocessed data for reproducing Fig. 1B and 1C from the paper 

*Statistical thermodynamics of the human brain activity, the Hagedorn temperature and the Zipf law*


## Prerequisites

This code requires Python together with `numpy` and `matplotlib`. 
Easiest to first install Miniconda (https://docs.anaconda.com/free/miniconda/) and then write
```
conda install numpy matplotlib
```

## Reproducing figures

First we have to convert the binary state representations into integer identifiers. Also generate the decorrelated data by first randomly cyclically shifting each channel. To do that run
```
python prepare_stateids.py
```
Run
```
python plot_fig_1B.py
```
to reproduce Fig. 1B from the paper:

![Fig. 1B](img/fig_1B.png)

Run
```
python plot_fig_1C.py
```
to reproduce Fig. 1B from the paper:

![Fig. 1C](img/fig_1C.png)


## Information on downloading and preprocessing

TBC

