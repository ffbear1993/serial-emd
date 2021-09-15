import numpy as np
from PyEMD import EMD

from concatenate import concatenate
from deconcatenate import deconcatenate

from matplotlib import pyplot as plt

if __name__ == '__main__':
    # toy examples

    # num_signal: the number of signals
    # num_length: the length of each signal
    num_signal = 15
    num_length = 500  

    # x: toy signals, to verify the function. each column is a signal, time-points are in the rows.
    x = np.kron(np.random.rand(num_signal, 1), np.ones((1, num_length))).T
    print(f'multi-dimensional signal shape:\t{x.shape}')

    # num_interval: the only parameter needed. Amount of samples that we will use between each column of our signals (columns of X) as the transition between signals. 
    num_interval = 50

    serilized_x = concatenate(x, num_interval).reshape(-1)
    print(f'concatenated signal shape:\t{serilized_x.shape}')

    serilized_imfs = EMD()(serilized_x).T
    print(f'concatenated imfs shape:\t{serilized_imfs.shape}')

    # imfs for each signal, [num_length, num_imf_modes, num_signal]
    imfs = deconcatenate(serilized_imfs, num_interval, num_signal)
    print(f'multi-dimensional imfs shape:\t{imfs.shape}')
