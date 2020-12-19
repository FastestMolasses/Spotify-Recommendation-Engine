import numpy as np
import pandas as pd

from typing import Tuple
from helper import loadData
from math import exp, pi, sqrt
from sklearn.model_selection import train_test_split

LAPLACE = 1


class NaiveBayesClassifier:
    def __init__(self, likedSongs: pd.DataFrame, dislikedSongs: pd.DataFrame):
        self.likedSongs = likedSongs[likedSongs.columns.difference(['Liked'])]
        self.dislikedSongs = dislikedSongs[dislikedSongs.columns.difference([
                                                                            'Liked'])]

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

    def predictSongs(self, songsTrain: pd.DataFrame) -> Tuple[int, int, float]:
        correct = 0
        incorrect = 0

        for index, row in songsTrain.iterrows():
            predLiked = self.predictIfLikeSong(
                row[:-1])  # Dont include the 'Liked' col
            actualLiked = bool(row[-1])

            if predLiked:
                if actualLiked:
                    correct += 1
                else:
                    incorrect += 1
            else:
                if actualLiked:
                    incorrect += 1
                else:
                    correct += 1

        accuracy = correct / len(songsTrain)
        return correct, incorrect, accuracy

    def predictIfLikeSong(self, songData: pd.Series):
        """
            Multiplies the probability of every feature based on
            the provided values.
        """
        probLiked = 1
        probDisliked = 1
        for i, col in enumerate(songData):
            probLiked *= calculateGuassianProbability(
                col, self.likedSongsMeans[i], self.likedSongsSTDs[i]) + LAPLACE
            probDisliked *= calculateGuassianProbability(
                col, self.dislikedSongsMeans[i], self.dislikedSongsSTDs[i]) + LAPLACE

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
    # Ignores a false positive warning relating to copying and combining DataFrames
    pd.options.mode.chained_assignment = None

    allSongs = loadData()
    # Split into 80/20 datasets
    trainingSongs = allSongs.sample(frac=0.80)
    testingSongs = allSongs.loc[~allSongs.index.isin(trainingSongs.index)]

    n = NaiveBayesClassifier(trainingSongs.loc[trainingSongs['Liked'] == 1],  # Liked songs
                                trainingSongs.loc[trainingSongs['Liked'] == 0])  # Disliked songs

    n.predictSongs(testingSongs)
