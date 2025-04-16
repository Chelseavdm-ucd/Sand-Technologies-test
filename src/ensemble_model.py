
import numpy as np
from collections import Counter
from sklearn.base import BaseEstimator, ClassifierMixin, clone
import sklearn.utils.validation

# Create a new classifier which is based on the sckit-learn BaseEstimator and ClassifierMixin classes
class HyperParamEnsembleClassifier(BaseEstimator, ClassifierMixin):

    """An ensemble classifier

    Parameters
    ----------


    Attributes
    ----------


    Notes
    -----


    See also
    --------



    Examples
    --------


    """
    # Constructor for the classifier object
    def __init__(self, base_estimator, param_grid, n_estimators=10, random_state=None ):
        """Setup a HyperParamClassifier classifier .
        Parameters
        ----------



        Returns
        -------
        Nothing
        """

        # Initialise class variabels

        self.base_estimator = base_estimator
        self.param_grid = param_grid
        self.n_estimators = n_estimators
        self.random_state = random_state
        self.models = []
        self.classes_ = None


    # The fit function to train a classifier
    def fit(self, X, y):
        """Build a HyperParamClassifier classifier from the training set (X, y).
        Parameters
        ----------
        X : array-like, shape = [n_samples, n_features]
            The training input samples.
        y : array-like, shape = [n_samples]
            The target values (class labels) as integers or strings.
        Returns
        -------
        self : object
        """
        X, y = sklearn.utils.validation.check_X_y(X, y)

        self.random_state_ = sklearn.utils.validation.check_random_state(self.random_state)

        self.classes_ = np.unique(y)

        param_combinations = [
            {key: self.random_state_.choice(values) for key, values in self.param_grid.items()}
            for _ in range(self.n_estimators)
        ]

        self.models = []

        for params in param_combinations:
            model = clone(self.base_estimator)
            model.set_params(**params)
            model.fit(X, y)
            self.models.append(model)

        # Return the classifier
        return self

    # The predict function to make a set of predictions for a set of query instances
    def predict(self, X):
        """Predict class labels of the input samples X.
        Parameters
        ----------
        X : array-like matrix of shape = [n_samples, n_features]
            The input samples.
        Returns
        -------
        p : array of shape = [n_samples, ].
            The predicted class labels of the input samples.
        """

        sklearn.utils.validation.check_is_fitted(self, ['models'])

        X = sklearn.utils.validation.check_array(X)

        predictions = np.array([model.predict(X) for model in self.models])

        prediction = np.apply_along_axis(lambda row: Counter(row).most_common(1)[0][0], axis=0, arr=predictions)

        # Return the prediction made by the classifier
        return prediction

    # The predict function to make a set of predictions for a set of query instances
    def predict_proba(self, X):

        """Predict class probabilities of the input samples X.
        Parameters
        ----------
        X : array-like matrix of shape = [n_samples, n_features]
            The input samples.
        Returns
        -------
        p : array of shape = [n_samples, n_labels].
            The predicted class label probabilities of the input samples.
        """
        sklearn.utils.validation.check_is_fitted(self, ['models'])

        X = sklearn.utils.validation.check_array(X)

        valid_models = [model for model in self.models if hasattr(model, "predict_proba")]

        if not valid_models:
            raise ValueError("No models in the ensemble support probability prediction.")

        all_classes = self.classes_

        class_index = {cls: i for i, cls in enumerate(all_classes)}

        adjusted_probabilities = []

        for model in valid_models:
            model_probability = np.zeros((X.shape[0], len(all_classes)))

            for i, cls in enumerate(model.classes_):
                model_probability[:, class_index[cls]] = model.predict_proba(X)[:, i]

            adjusted_probabilities.append(model_probability)

        # Return the prediction made by the classifier
        return np.mean(adjusted_probabilities, axis=0)