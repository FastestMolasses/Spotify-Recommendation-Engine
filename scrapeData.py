import os
import json

from time import sleep
from config import Config
from spotify import Spotify


def convertJsonDataToCSV(songs: list, fileName: str = 'songs'):
    """
        Converts scrapped json Spotify data into a csv format.
    """
    headers = ['Name', 'Artists', 'Album', 'Duration', 'Popularity',
               'Song ID', 'Key', 'Mode', 'Time Signature', 'Acousticness',
               'Danceability', 'Energy', 'Instrumentalness', 'Liveness',
               'Loudness', 'Speechiness', 'Valence', 'Tempo']

    with open(fileName + '.csv', 'w') as f:
        f.write(','.join(headers) + '\n')

        for song in songs:
            s = "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17}".format(
                song['name'].replace(',', ''),
                '/'.join(i['name'] for i in song['artists']),
                song['album']['name'].replace(',', ''),
                song['duration_ms'],
                song['popularity'],
                song['id'],
                song['data']['key'],
                song['data']['mode'],
                song['data']['time_signature'],
                song['data']['acousticness'],
                song['data']['danceability'],
                song['data']['energy'],
                song['data']['instrumentalness'],
                song['data']['liveness'],
                song['data']['loudness'],
                song['data']['speechiness'],
                song['data']['valence'],
                song['data']['tempo']
            )
            f.write(s + '\n')


if __name__ == '__main__':
    # All songs I want to analyze are saved on a playlist
    spotify = Spotify()
    songs = spotify.getPlaylistTracks(Config.TRAINING_PLAYLIST_ID)

    # Go through each song and add their analysis data
    for song in songs:
        print(f'Analyzing song: {song["name"]}')
        song['data'] = spotify.getTrackAnalysis(song['id'])
        sleep(1)

    fileName = os.path.join('data', 'allGenres')
    # Save the JSON data
    with open(fileName + '.json', 'w') as f:
        json.dump(songs, f, indent=4)

    # Save the data into a CSV file
    convertJsonDataToCSV(songs, fileName=fileName)
