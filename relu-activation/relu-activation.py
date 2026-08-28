import numpy as np

def relu(x) -> np.ndarray:
    return np.asarray(np.clip(np.asarray(x), 0, None))