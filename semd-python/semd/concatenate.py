import numpy as np


def concatenate(matrix_x: np.ndarray, num_interval: int):
    num_length = matrix_x.shape[0]
    num_signal = matrix_x.shape[1]

    matrix_a = matrix_x[:num_interval, 1:]
    matrix_b = matrix_x[-num_interval:, :-1]

    vector_a = np.linspace(0, 1, num_interval+2)[1:-1].reshape(-1, 1)
    vector_u = np.ones(num_signal-1).reshape(-1, 1)

    # transition
    matrix_t_a = np.flipud(matrix_a) * np.dot(vector_a, vector_u.T)
    matrix_t_b = np.flipud(matrix_b) * np.dot(np.flipud(vector_a), vector_u.T)

    matrix_t = matrix_t_a + matrix_t_b

    matrix_z = np.zeros(num_interval).reshape(-1, 1)

    # concatenate transition with zeros
    matrix_t = np.concatenate([matrix_t, matrix_z], axis=1)

    # result
    matrix_r = np.concatenate([matrix_x, matrix_t], axis=0)
    matrix_r = matrix_r.flatten(order='F')
    matrix_r = matrix_r[:-num_interval].reshape(-1, 1)

    return matrix_r
