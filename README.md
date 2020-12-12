# Spotify Song Recommendation Engine

CECS 456 final class project. Scrapes song data and trains a model in order to predict songs that a user might like. Can also be used to predict popularity or whether a song might go viral or not.

---

## Installation


Create a new Python environment (optional)

```bash
$ python3 -m venv env
```

Install required libraries

```bash
$ pip install -r requirements.txt
```

You can now run the model, given that you have the data. If you have no data and want to scrape it from Spotify, then you need a Spotify application. Create one here: https://developer.spotify.com/dashboard/applications

After creating an application, save the client ID and application secret. Now create a .env file

```bash
// Windows PowerShell
> New-Item .env -type file

// MacOS
$ touch .env
```

Fill the .env file with your application client ID and secret like so:

```
SPOTIFY_CLIENT_ID=<client id>
SPOTIFY_SECRET=<application secret>
TRAINING_PLAYLIST_ID=<your playlist ID>
```

The playlist ID is the ID of the playlist you want to analyze. I recommend putting all the songs you want to anaylze into a new playlist and use that for your training.

The Spotify script is now ready to be used to scrape song data. Run the `main.py` script in order to scrape and analyze your songs. Data will be saved in the `data/` folder.
