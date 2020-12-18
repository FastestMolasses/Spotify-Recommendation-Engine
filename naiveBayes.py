import numpy as np
import pandas as pd

from math import exp, pi, sqrt


class NaiveBayesClassifier:
    def __init__(self, likedSongs: pd.DataFrame, dislikedSongs: pd.DataFrame):
        self.likedSongs = likedSongs[['Mode', 'Time Signature', 'Acousticness', 'Danceability', 'Energy',
                                      'Instrumentalness', 'Liveness', 'Loudness', 'Speechiness', 'Valence', 'Tempo']]
        self.dislikedSongs = dislikedSongs[['Mode', 'Time Signature', 'Acousticness', 'Danceability', 'Energy',
                                            'Instrumentalness', 'Liveness', 'Loudness', 'Speechiness', 'Valence', 'Tempo']]

        # Store all the means and standard deviations of the columns
        self.likedSongsMeans = []
        self.likedSongsSTDs = []
        for column in self.likedSongs:
            self.likedSongsMeans.append(mean(self.likedSongs[column]))
            self.likedSongsSTDs.append(std(self.likedSongs[column]))

        self.dislikedSongsMeans = []
        self.dislikedSongsSTDs = []
        for column in self.dislikedSongs:
            self.dislikedSongsMeans.append(mean(self.dislikedSongs[column]))
            self.dislikedSongsSTDs.append(std(self.dislikedSongs[column]))

    def predictIfLikeSong(self, songData: np.ndarray):
        """
            Multiplies the probability of every feature based on
            the provided values.
        """
        probLiked = 1
        probDisliked = 1
        for i, col in enumerate(songData):
            probLiked *= calculateGuassianProbability(
                col, self.likedSongsMeans[i], self.likedSongsSTDs[i])
            probDisliked *= calculateGuassianProbability(
                col, self.dislikedSongsMeans[i], self.dislikedSongsSTDs[i])

        return probLiked > probDisliked


def mean(numbers: list):
    """
        Gets the average from a list of numbers.
    """
    return sum(numbers) / float(len(numbers))


def std(numbers: list) -> float:
    """
        Gets the standard deviation of a list of numbers.
    """
    avg = mean(numbers)
    variance = sum([(i - avg) ** 2 for i in numbers]) / float(len(numbers) - 1)
    return sqrt(variance)


def calculateGuassianProbability(num: float, mean: float, stdev: float) -> float:
    """
        Calculates the probability of a number by using the
        Guassian Probability Distribution Function.
    """
    exponent = exp(-((num - mean) ** 2 / (2 * stdev ** 2)))
    return (1 / (sqrt(2 * pi) * stdev)) * exponent


if __name__ == '__main__':
    likedRapSongs = pd.read_csv('data/likedRapSongs.csv')
    dislikedSongs = pd.read_csv('data/allGenres.csv')

    n = NaiveBayesClassifier(likedRapSongs, dislikedSongs)

    print(n.predictIfLikeSong(
        np.array([1,4,0.141,0.679,0.587,6.35e-06,0.137,-7.015,0.276,0.486,186.003])))
    print(n.predictIfLikeSong(
        np.array([1,4,0.0161,0.539,0.887,4.18e-06,0.267,-6.935,0.037,0.448,100.017])))
