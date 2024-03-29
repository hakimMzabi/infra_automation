import json

import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time


def getConnection_spotify_api():
    client_id = 'd5e7ac18c19f483c9c6fc7c6d848f004'
    client_secret = 'b3b0efc54fcd4cce82091ceb8eb05386'

    client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return sp


def getNekfeu(sp):
    lz_uri = 'spotify:artist:4LXBc13z5EWsc5N32bLxfH'

    results = sp.artist_top_tracks(lz_uri)

    for track in results['tracks'][:10]:
        print('track    : ' + track['name'])
        print('cover art: ' + track['album']['images'][0]['url'])
        print()


def getJul(sp):
    results = sp.search(q='Jul', limit=20)
    for idx, track in enumerate(results['tracks']['items']):
        print(idx, track['name'])


def getPetitBiscuit(sp):
    results = sp.search(q='Petit Biscuit', limit=20)
    for idx, track in enumerate(results['tracks']['items']):
        print(idx, track['name'])


def getTrackSpotify(sp):
    url = "37i9dQZEVXbIPWwFssbupI"
    result = sp.playlist(url)
    s1 = json.dumps(result)
    data = json.loads(s1)
    df = pd.DataFrame.from_dict(data["tracks"])
    #récupération items
    json_dict = json.loads(df["items"].to_json(orient='split'))
    del json_dict['index']
    s1_items = json.dumps(json_dict)
    data_items = json.loads(s1_items)
    df_items = pd.DataFrame.from_dict(data_items["data"])
    #récupération track
    json_dict = json.loads(df_items["track"].to_json(orient='split'))
    del json_dict['index']
    s1_track = json.dumps(json_dict)
    data_track = json.loads(s1_track)

    df_artist = pd.DataFrame(columns=['name','album','popularity'])
    for i in range(len(data_track["data"])):
        for j in data_track["data"][i]["artists"]:
            df_artist = df_artist.append({'name':j['name'], 'album':data_track["data"][i]["name"],'popularity':data_track["data"][i]["popularity"]},ignore_index=True)
    print(df_artist)




if __name__ == "__main__":
    sp = getConnection_spotify_api()
  #  getPetitBiscuit(sp)
  #  getNekfeu(sp)
    getTrackSpotify(sp)

