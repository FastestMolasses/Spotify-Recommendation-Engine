import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    SPOTIFY_CLIENT_ID = os.environ['SPOTIFY_CLIENT_ID']
    SPOTIFY_SECRET = os.environ['SPOTIFY_SECRET']
    TRAINING_PLAYLIST_ID = os.environ['TRAINING_PLAYLIST_ID']
