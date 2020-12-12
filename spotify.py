import base64
import requests

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
            'duration': resp['duration_ms'],
            'albumName': resp['album']['name'],
            'artists': [i['name'] for i in resp['artists']],
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
