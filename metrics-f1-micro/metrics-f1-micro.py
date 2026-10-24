def f1_micro(y_true: list[int], y_pred: list[int]) -> float:
    """
    Returns the micro-averaged F1 score as a Python float rounded to four decimals.
    """
    numerator = 0
    for true, pred in zip(y_true, y_pred):
        if true == pred:
            numerator += 1
    return numerator / len(y_true)