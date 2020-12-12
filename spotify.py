import base64
import requests

from time import sleep
from config import Config


class Spotify:
    def __init__(self):
        self._getAccessToken()

    def _getAccessToken(self):
        """
            Requests an access token from Spotify API services.
        """
        # Encode client id and secret to get an authorization token
        encodedHeader = f'{Config.SPOTIFY_CLIENT_ID}:{Config.SPOTIFY_SECRET}'.encode(
            'ascii')
        encodedHeader = base64.b64encode(encodedHeader).decode('ascii')

        # Request access token
        resp = requests.post('https://accounts.spotify.com/api/token',
                             data={
                                 'grant_type': 'client_credentials'
                             },
                             headers={
                                 'Authorization': f'Basic {encodedHeader}',
                             })

        self.accessToken = resp.json()['access_token']

    def getPlaylistTracks(self, playlistID: str) -> list:
        """
            Gets the information for all the tracks in a playlist.
        """
        songs = []
        requestURL = f'https://api.spotify.com/v1/playlists/{playlistID}/tracks?fields=total,next,previous,items(track(name,href,duration_ms,album(name,id,images),artists(id,name),id,popularity,duration))'
        while True:
            resp = requests.get(requestURL,
                                headers={
                                    'Authorization': f'Bearer {self.accessToken}',
                                }).json()

            # Add all the songs to the list
            songs.extend([i['track'] for i in resp['items']])

            # Get the next batch of songs if they exist
            if resp['next']:
                requestURL = resp['next']
                sleep(1)  # To avoid rate limit
            else:
                break

        return songs

    def getTrack(self, trackID: str) -> dict:
        """
            Requests song information such as name, album and artist names.
        """
        resp = requests.get(f'https://api.spotify.com/v1/tracks/{trackID}',
                            headers={
                                'Authorization': f'Bearer {self.accessToken}',
                            }).json()
        return {
            'id': resp['id'],
            'name': resp['name'],
            'popularity': resp['popularity'],
            'href': resp['href'],
            'duration_ms': resp['duration_ms'],
            'album': {
                'id': resp['album']['id'],
                'images': resp['album']['images'],
                'name': resp['album']['name'],
            },
            'artists': [{'name': i['name'], 'id': i['id']} for i in resp['artists']],
        }

    def getTrackAnalysis(self, trackID: str) -> dict:
        """
            Requests song analysis from spotify returning parameters such as
            accousticness, tempo, bouncieness, etc.
        """
        resp = requests.get(f'https://api.spotify.com/v1/audio-features/{trackID}',
                            headers={
                                'Authorization': f'Bearer {self.accessToken}',
                            }).json()
        return {
            'key': resp['key'],
            'mode': resp['mode'],
            'time_signature': resp['time_signature'],
            'acousticness': resp['acousticness'],
            'danceability': resp['danceability'],
            'energy': resp['energy'],
            'instrumentalness': resp['instrumentalness'],
            'liveness': resp['liveness'],
            'loudness': resp['loudness'],
            'speechiness': resp['speechiness'],
            'valence': resp['valence'],
            'tempo': resp['tempo'],
            'id': resp['id'],
            'track_href': resp['track_href'],
            'analysis_url': resp['analysis_url'],
        }
