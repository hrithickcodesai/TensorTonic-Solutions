import numpy as np

def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
    arr = np.asarray(x)
    fx = np.where(arr >= 0, arr, alpha * arr)
    return fx