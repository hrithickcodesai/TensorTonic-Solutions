import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    # we need to make sure it is numerically stable to compute
    x = np.array(x, dtype=np.float32)
    return 1 / (1 + np.exp(- x))

