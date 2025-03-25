import pytest
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from ml.model import train_model, inference, compute_model_metrics
from ml.data import process_data

@pytest.fixture
def setup_data():
    """Fixture to prepare test data."""
    data = {
        "workclass": ["Private", "Self-emp"],
        "education": ["Bachelors", "Masters"],
        "marital-status": ["Single", "Married"],
        "occupation": ["Tech", "Exec"],
        "relationship": ["Not-in-family", "Husband"],
        "race": ["White", "Black"],
        "sex": ["Male", "Female"],
        "native-country": ["USA", "Canada"],
        "salary": [">50K", "<=50K"]
    }
    df = pd.DataFrame(data)
    cat_features = [
        "workclass", "education", "marital-status",
        "occupation", "relationship", "race", "sex", "native-country"
    ]
    X, y, encoder, lb = process_data(df, categorical_features=cat_features, label="salary", training=True)
    model = train_model(X[:1], y[:1])
    return model, X, y

def test_return_types(setup_data):
    """Check if ML functions return expected types."""
    model, X, y = setup_data
    preds = inference(model, X[1:])
    assert isinstance(preds, np.ndarray)
    assert preds.shape == y[1:].shape

    precision, recall, fbeta = compute_model_metrics(y[1:], preds)
    assert isinstance(precision, float)
    assert isinstance(recall, float)
    assert isinstance(fbeta, float)

def test_model_algorithm(setup_data):
    """Check if the trained model is a RandomForestClassifier."""
    model, _, _ = setup_data
    assert isinstance(model, RandomForestClassifier)

def test_dataset_sizes(setup_data):
    """Check if dataset sizes are as expected."""
    _, X, y = setup_data
    assert X.shape[0] == 2
    assert y.shape[0] == 2
    assert isinstance(X, np.ndarray)
    assert isinstance(y, np.ndarray)
