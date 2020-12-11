from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.sql.types import *
import os
import sys



spark = SparkSession.builder \
    .master('local[1]') \
    .appName('SparkByExamples.com') \
    .getOrCreate()
sc = spark.sparkContext
spotify_data_lake = "hdfs://d271ee89-3c06-4d40-b9d6-d3c1d65feb57.priv.instances.scw.cloud:8020/user/datagang/lab/spotify"


def main():
    from pandas.io import json

    import pandas as pd
    import time
    import numpy as np
    from spotipy.oauth2 import SpotifyClientCredentials
    import spotipy
    client_id = 'd5e7ac18c19f483c9c6fc7c6d848f004'
    client_secret = 'b3b0efc54fcd4cce82091ceb8eb05386'

    client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    artist_names = ["{petit biscuit}", "{koba lad}", "{Aya Nakamura}", "{Dadju}"]
    all_data = []
    df_final = pd.DataFrame()
    df = pd.DataFrame()

    for artist in artist_names:
        request = sp.search(artist)
        request = json.dumps(request)
        all_data.append(request)

    for result in all_data:
        result = json.loads(result)
        artist_uri = result['tracks']['items'][0]['artists'][0]['uri']
        # Pull all of the artist's albums
        sp_albums = sp.artist_albums(artist_uri, album_type='album')

        album_names = []
        album_uris = []

        for i in range(len(sp_albums['items'])):
            album_names.append(sp_albums['items'][i]['name'])
            album_uris.append(sp_albums['items'][i]['uri'])

        spotify_albums = {}
        album_count = 0
        for i in album_uris:
            album = i
            spotify_albums[album] = {}
            spotify_albums[album]['album'] = []
            spotify_albums[album]['artist'] = []
            spotify_albums[album]['track_number'] = []
            spotify_albums[album]['id'] = []
            spotify_albums[album]['name'] = []
            spotify_albums[album]['uri'] = []
            tracks = sp.album_tracks(album)
            for n in range(len(tracks['items'])):
                spotify_albums[album]['album'].append(album_names[album_count])
                spotify_albums[album]['track_number'].append(tracks['items'][n]['track_number'])
                spotify_albums[album]['id'].append(tracks['items'][n]['id'])
                spotify_albums[album]['name'].append(tracks['items'][n]['name'])
                spotify_albums[album]['uri'].append(tracks['items'][n]['uri'])

            album_count += 1

        sleep_min = 2
        sleep_max = 5
        start_time = time.time()
        request_count = 0
        for album in spotify_albums:

            spotify_albums[album]['acousticness'] = []
            spotify_albums[album]['danceability'] = []
            spotify_albums[album]['energy'] = []
            spotify_albums[album]['instrumentalness'] = []
            spotify_albums[album]['liveness'] = []
            spotify_albums[album]['loudness'] = []
            spotify_albums[album]['speechiness'] = []
            spotify_albums[album]['tempo'] = []
            spotify_albums[album]['valence'] = []
            spotify_albums[album]['popularity'] = []

            # create a track counter
            track_count = 0
            for track in spotify_albums[album]['uri']:
                name_artist = sp_albums['items'][0]['artists'][0]['name']
                spotify_albums[album]['artist'].append(name_artist)

                features = sp.audio_features(track)

                spotify_albums[album]['acousticness'].append(features[0]['acousticness'])
                spotify_albums[album]['danceability'].append(features[0]['danceability'])
                spotify_albums[album]['energy'].append(features[0]['energy'])
                spotify_albums[album]['instrumentalness'].append(features[0]['instrumentalness'])
                spotify_albums[album]['liveness'].append(features[0]['liveness'])
                spotify_albums[album]['loudness'].append(features[0]['loudness'])
                spotify_albums[album]['speechiness'].append(features[0]['speechiness'])
                spotify_albums[album]['tempo'].append(features[0]['tempo'])
                spotify_albums[album]['valence'].append(features[0]['valence'])

                pop = sp.track(track)
                spotify_albums[album]['popularity'].append(pop['popularity'])
                track_count += 1
            request_count += 1
            if request_count % 5 == 0:
                time.sleep(np.random.uniform(sleep_min, sleep_max))

        dic_df = {'artist': [], 'album': [], 'track_number': [], 'id': [], 'name': [], 'uri': [], 'acousticness': [],
                  'danceability': [], 'energy': [], 'instrumentalness': [], 'liveness': [], 'loudness': [],
                  'speechiness': [], 'tempo': [], 'valence': [], 'popularity': []}

        for album in spotify_albums:
            for feature in spotify_albums[album]:
                dic_df[feature].extend(spotify_albums[album][feature])
        df_dic = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in dic_df.items()]))
        df_final = df_final.append(df_dic)
        mySchema = StructType([StructField("artist", StringType(), True) \
                          , StructField("album", StringType(), True) \
                          , StructField("track_number", StringType(), True) \
                          , StructField("id", StringType(), True) \
                          , StructField("name", StringType(), True) \
                          , StructField("uri", StringType(), True) \
                          , StructField("acousticness", StringType(), True) \
                          , StructField("danceability", StringType(), True) \
                          , StructField("energy", StringType(), True) \
                          , StructField("instrumentalness", StringType(), True) \
                          , StructField("liveness", StringType(), True) \
                          , StructField("loudness", StringType(), True) \
                          , StructField("speechiness", StringType(), True) \
                          , StructField("tempo", StringType(), True) \
                          , StructField("valence", StringType(), True) \
                          , StructField("popularity", StringType(), True)])

    #print(df_final)
    #df_final.to_csv("data_sp.csv")
    sdf = spark.createDataFrame(df_final, mySchema)
    sdf.write.format("com.databricks.spark.avro").save(spotify_data_lake)

