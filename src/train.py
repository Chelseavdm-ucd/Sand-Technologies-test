# src/train.py

import pandas as pd
from sklearn.model_selection import StratifiedKFold
from data_loader import load_datasets
from ensemble_model import HyperParamEnsembleClassifier
from baseline_models import get_baseline_models
from evaluation import get_metrics, evaluate_model

def main():
    # Load datasets
    datasets = load_datasets()

    # Define evaluation strategy
    cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
    metrics = get_metrics()

    # Initialize storage for results
    ensemble_results = {}
    baseline_results = {}

    # Iterate over datasets
    for dataset_name, dataset in datasets.items():
        X, y = dataset["data"], dataset["target"]

        print(f"\nEvaluating the Ensemble Model on {dataset_name}")

        # Ensemble model
        ensemble_model = HyperParamEnsembleClassifier(
            base_estimator=baseline_models["Decision Tree"],
            param_grid={"max_depth": [3, 5, 10], "min_samples_split": [2, 4, 6]},
            n_estimators=5,
            random_state=42
        )
        ensemble_results[dataset_name] = evaluate_model(ensemble_model, X, y, cv, metrics)

        # Baseline models
        baseline_results[dataset_name] = {}
        for model_name, model in baseline_models.items():
            print(f"Evaluating {model_name} on {dataset_name}")
            baseline_results[dataset_name][model_name] = evaluate_model(model, X, y, cv, metrics)

    # Create DataFrames for results
    ensemble_df = pd.DataFrame(ensemble_results).T
    baseline_df = {model: pd.DataFrame({dataset: scores[model] for dataset, scores in baseline_results.items()}).T for model in baseline_models.keys()}

    # Print results
    print("\nEnsemble Model Performance:")
    print(ensemble_df)

    for model, df in baseline_df.items():
        print(f"\n{model} Performance:")
        print(df)

if __name__ == "__main__":
    baseline_models = get_baseline_models()
    main()
