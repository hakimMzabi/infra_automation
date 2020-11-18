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

def getArtiste():
    url = "http://httpbin.org/post"
    payload = dict(key1='value1', key2='value2')
    res = requests.post(url, data=payload)

    print(res.text)

if __name__ == "__main__":
    sp = getConnection_spotify_api()
  #  getPetitBiscuit(sp)
    getNekfeu(sp)
