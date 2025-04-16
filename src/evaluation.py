# src/evaluation.py

import numpy as np
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import (
    accuracy_score, f1_score, log_loss, confusion_matrix
)

def get_metrics():
    """Returns a dictionary of evaluation metric functions."""
    metrics = {
        "Accuracy": accuracy_score,
        "Macro F1-Score": lambda y_true, y_pred: f1_score(y_true, y_pred, average="macro"),
        "Log Loss": log_loss,
        "Confusion Matrix": confusion_matrix
    }
    return metrics

def evaluate_model(model, X, y, cv, metrics):
    """
    Evaluates a given model using cross-validation.

    Parameters
    ----------
    model : object
        A fitted sklearn-style model.

    X : array-like
        Features.

    y : array-like
        Target labels.

    cv : object
        Cross-validation strategy (e.g., StratifiedKFold).

    metrics : dict
        Dictionary of metric functions.

    Returns
    -------
    results : dict
        Evaluation scores for each metric.
    """
    results = {}
    y_pred = cross_val_predict(model, X, y, cv=cv)

    try:
        y_proba = cross_val_predict(model, X, y, cv=cv, method="predict_proba")
    except ValueError:
        y_proba = None

    for metric_name, metric_func in metrics.items():
        if metric_name == "Confusion Matrix":
            results[metric_name] = metric_func(y, y_pred)
        elif metric_name == "Log Loss" and y_proba is not None:
            results[metric_name] = metric_func(y, y_proba, labels=np.unique(y))
        else:
            results[metric_name] = metric_func(y, y_pred)

    return results
