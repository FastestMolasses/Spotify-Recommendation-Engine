import os
import pandas as pd

from typing import Tuple
from sklearn.model_selection import train_test_split

LIKED_RAP = 'likedRapSongs.csv'
LIKED_HIPHOP = 'likedHipHopSongs.csv'
DISLIKED_HIPHOP = 'dislikedSongsHipHop.csv'
ALL_GENRES = 'allGenres.csv'


def getSplitData() -> Tuple[pd.DataFrame, pd.Series]:
    """
        Splits the loaded data and returns it.
    """
    allSongs = loadData()
    X, y = allSongs[allSongs.columns.difference(['Liked'])], allSongs['Liked']

    # Split the data
    return train_test_split(X, y)


def loadData() -> pd.DataFrame:
    """
        Gets 2 datasets of liked and disliked songs and combines them.
    """
    dataColumns = ['Mode', 'Time Signature', 'Acousticness', 'Danceability', 'Energy',
                   'Instrumentalness', 'Liveness', 'Loudness', 'Speechiness', 'Valence',
                   'Tempo']

    # Load and concatenate the data
    likedRapSongs = pd.read_csv(os.path.join('data', LIKED_HIPHOP))
    likedSongs = likedRapSongs[dataColumns]
    likedSongs['Liked'] = 1

    dislikedSongs = pd.read_csv(os.path.join('data', DISLIKED_HIPHOP))
    dislikedSongs = dislikedSongs[dataColumns]
    dislikedSongs['Liked'] = 0

    allSongs = pd.concat([likedSongs, dislikedSongs])
    return allSongs
