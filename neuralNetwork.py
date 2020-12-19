import numpy as np
import pandas as pd

from typing import Tuple
from helper import getSplitData
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier


def trainMLP(xTrain: pd.DataFrame, xTest: pd.DataFrame,
             yTrain: pd.DataFrame, yTest: pd.DataFrame) -> MLPClassifier:
    """
        Trains the MLP with the provided data and returns the model.
    """
    # Feature scaling
    scaler = StandardScaler()
    scaler.fit(xTrain)

    xTrain = scaler.transform(xTrain)
    xTest = scaler.transform(xTest)

    # Train
    mlp = MLPClassifier(hidden_layer_sizes=(12, 8, 4),
                        random_state=1,  # To get reproducible outputs
                        activation='tanh',
                        max_iter=2000,  # Epochs
                        batch_size=64)
    mlp.fit(xTrain, yTrain)

    return mlp


def predict(mlp: MLPClassifier, xTest: pd.DataFrame,
            yTest: pd.DataFrame) -> Tuple[np.ndarray, np.float64]:
    """
        Predicts whether we will like the songs or not,
        and gives an accuracy score.
    """
    predictions = mlp.predict(xTest)
    return predictions, accuracy_score(yTest, predictions)


if __name__ == '__main__':
    # Ignores a false positive warning relating to copying and combining DataFrames
    pd.options.mode.chained_assignment = None

    # Training
    xTrain, xTest, yTrain, yTest = getSplitData()
    mlp = trainMLP(xTrain, xTest, yTrain, yTest)

    # Testing
    predictions, accuracy = predict(mlp, xTest, yTest)
