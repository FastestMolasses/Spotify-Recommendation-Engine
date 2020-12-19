import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score


if __name__ == '__main__':
    # Ignores a false positive warning relating to copying and combining DataFrames
    pd.options.mode.chained_assignment = None

    dataColumns = ['Mode', 'Time Signature', 'Acousticness', 'Danceability', 'Energy',
                   'Instrumentalness', 'Liveness', 'Loudness', 'Speechiness', 'Valence', 'Tempo']

    # Load and concatenate the data
    likedRapSongs = pd.read_csv('data/likedRapSongs.csv')
    likedSongs = likedRapSongs[dataColumns]
    likedSongs['Liked'] = 1

    dislikedSongs = pd.read_csv('data/dislikedSongsHipHop.csv')
    dislikedSongs = dislikedSongs[dataColumns]
    dislikedSongs['Liked'] = 0

    allSongs = pd.concat([likedSongs, dislikedSongs])
    X = allSongs[dataColumns]
    y = allSongs['Liked']

    # Split the data
    xTrain, xTest, yTrain, yTest = train_test_split(X, y)

    # Feature scaling
    scaler = StandardScaler()
    scaler.fit(xTrain)

    xTrain = scaler.transform(xTrain)
    xTest = scaler.transform(xTest)

    # Train
    mlp = MLPClassifier(hidden_layer_sizes=(12, 7),
                        random_state=1,
                        activation='tanh',
                        max_iter=1000,
                        batch_size=64)
    mlp.fit(xTrain, yTrain)

    # Test
    predictions = mlp.predict(xTest)
    print(accuracy_score(yTest, predictions))
