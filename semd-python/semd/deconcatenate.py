import numpy as np


def deconcatenate(matrix_r: np.ndarray, num_interval: int, num_signal: int):
    num_mode = matrix_r.shape[1]

    # fill zeros
    matrix_z = np.zeros([num_interval, num_mode])
    matrix_r = np.concatenate([matrix_r, matrix_z], axis=0)

    matrix_imf = matrix_r.reshape([-1, num_signal, num_mode], order='F')
    matrix_imf = matrix_imf[:-num_interval, :, :]
    matrix_imf = matrix_imf.transpose((0, 2, 1))

    return matrix_imf
