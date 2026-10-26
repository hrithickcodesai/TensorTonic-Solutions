import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    matrix = np.array(A)
    n, m = matrix.shape
    transposed = np.zeros(shape = (m, n), dtype = np.float32)
    for i in range(n):
        for j in range(m):
            transposed[j, i] = matrix[i, j]
    return transposed