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

After creating an application, save the client ID and application secret. Now create a `.env` file

```bash
// Windows PowerShell
> New-Item .env -type file

// MacOS
$ touch .env
```

Fill the `.env` file with your application client ID and secret like so:

```
SPOTIFY_CLIENT_ID=<client id>
SPOTIFY_SECRET=<application secret>
TRAINING_PLAYLIST_ID=<your playlist ID>
```

The playlist ID is the ID of the playlist you want to analyze. I recommend putting all the songs you want to anaylze into a new playlist and use that for your training.

The Spotify script is now ready to be used to scrape song data. Run the `main.py` script in order to scrape and analyze your songs. Data will be saved in the `data/` folder.

---

## More Information

Spotify's API allows access to these variables which are calculated for each song.

| Variable         | Domain         | Description                                                                                                                                                                                                                                                    |
|------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| acousticness     | \[0\.0, 1\.0\] | A confidence score of whether the song is acoustic or not, 0 being absolutely not acoustic and 1 being absolutely acoustic\.                                                                                                                                   |
| danceability     | \[0\.0, 1\.0\] | Defines how danceable a song is\. 0 being not danceable and 1 being very danceable\.                                                                                                                                                                           |
| energy           | \[0\.0, 1\.0\] | Measures how much energy a song has\. 0 has low energy and 1 being high energy\. Energy is a measure of intensity\.                                                                                                                                            |
| instrumentalness | \[0\.0, 1\.0\] | A confidence score of whether a song has no lyrics\. Values above 0\.5 are considered instrumental, but higher values represent a better probability\.                                                                                                         |
| key              | \[0, 11\]      | Which key the track is, based on the Pitch Class Notation: https://en\.wikipedia\.org/wiki/Pitch\_class\.                                                                                                                                                      |
| liveness         | \[0\.0, 1\.0\] | A confidence score predicting the presence of an audience and the probability the song was performed live\. 0 being it is definitely not live, and 1 being definitely live\.                                                                                   |
| loudness         | \(\-60, 0\)    | The average decibel in the song\.                                                                                                                                                                                                                              |
| mode             | \{0, 1\}       | Whether the track is a major or minor\. 1 is major and 0 is minor\.                                                                                                                                                                                            |
| speechiness      | \[0\.0, 1\.0\] | Defines how much speech is in the song\. Values between 0\.33 \- 0\.66 represent the typical song, with a mix of vocals and beats\. Anything less indicates a song with more beats than speech\. Anything above 0\.66 indicates the song is primarily speech\. |
| tempo            | \[0, 1015\]    | The estimated beats per minute \(BPM\) in the overall song\.                                                                                                                                                                                                   |
| valence          | \[0\.0, 1\.0\] | A confidence score determining how positive, cheerful, and upbeat the song is\. 1\.0 being most positive and 0\.0 being the opposite\.                                                                                                                         |
| popularity       | \[0, 100\]     | The popularity of a song\. 0 being unpopular and 100 being very popular\. Takes into account how many hits the song has and its recency\.                                                                                                                      |
