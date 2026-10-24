import math
import numpy as np

def log_loss(y_true: list, y_pred: list, eps: float = 1e-15) -> float:
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    # we want to clip the values for safety
    # y_pred are probabilities of p(y=1|x) 
    # y_pred is probability of being y = 1
    y_pred = np.clip(y_pred, a_min = eps, a_max = 1 - eps)

    loss = - (
        y_true * np.log(y_pred)
        + (1 - y_true) * np.log(1 - y_pred)
    )

    return loss.tolist()