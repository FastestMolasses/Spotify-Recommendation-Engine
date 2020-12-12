import os
import numpy as np
import pandas as pd

SONGS_CSV_FILENAME = os.path.join('data', 'songs.csv')


def main():
    data = pd.read_csv(SONGS_CSV_FILENAME)
    print(data.head())


if __name__ == '__main__':
    main()
