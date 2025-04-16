from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

def get_baseline_models():
    """Returns a dictionary of baseline classification models."""
    models = {
        "Decision Tree": DecisionTreeClassifier(),
        "Random Forest": RandomForestClassifier(),
        "Support Vector Machine": SVC(probability=True),
        "Logistic Regression": LogisticRegression(max_iter=500),
        "K-Nearest Neighbors": KNeighborsClassifier()
    }
    return models