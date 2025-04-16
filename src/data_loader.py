# src/data_loader.py

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris, load_wine, load_digits, fetch_openml
from sklearn.preprocessing import StandardScaler

def load_datasets():
    """Loads and preprocesses datasets (Iris, Wine, Digits, MNIST)."""
    
    # Load built-in datasets
    iris = load_iris()
    wine = load_wine()
    digits = load_digits()
    
    # Load MNIST subset
    X_mnist, y_mnist = fetch_openml('mnist_784', version=1, return_X_y=True, as_frame=False)
    X_mnist, y_mnist = X_mnist[:2000], y_mnist[:2000]
    y_mnist = y_mnist.astype(int)

    datasets = {
        "Iris": {"data": iris.data, "target": iris.target},
        "Wine": {"data": wine.data, "target": wine.target},
        "Digits": {"data": digits.data, "target": digits.target},
        "MNIST": {"data": X_mnist, "target": y_mnist},
    }
    
    # Standardize datasets
    scaler = StandardScaler()

    for dataset in datasets.values():
        dataset["data"] = scaler.fit_transform(dataset["data"])

    return datasets
