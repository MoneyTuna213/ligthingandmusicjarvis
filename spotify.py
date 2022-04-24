from pickle import TRUE
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import sys
import pandas as pd
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import json
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#scope = "user-library-read"
class SpotifyNanoleaf:
    def activateSpotify():
        scope = "user-modify-playback-state"
        client_secret="d5ea8517bd444b08be53cc621f80b35b"
        client_id="86769814c5cc4492abd6e2df2a55acad"
        redirect_uri="http://127.0.0.1:9090"
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, scope=scope, client_secret=client_secret, redirect_uri=redirect_uri))
        spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
        payload = {"ids": "27cZdqrQiKt3IT00338dws"}
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % ("BQAYZVSUzCaVKgtZFv0e5RJVU-E-yeAaLcaE9cmQzuJeUGiQ8t32sBKXfv-P-O10wdFdTmjNoSc3n9lFw_zVp5bmmgxk1_jJQ5pSy80HX-wi20V0yoBfCmndkI3DqyqIICmesntgPxG6xShsNgqXqXTkveSp3ZmoU03YBaE") 
        }
        DevQuestion = input("What device are we using today?")
        if DevQuestion == ("xbox"):
            device_id="05ed3071-7fd8-4307-ac7f-8e750f1e6cc1"
        elif DevQuestion == ("phone"):
            device_id="1485e6dbe9ad93717134f589dafb5b2b8b3d4837"
        elif DevQuestion == ("alexa"):
            device_id="664d1332-e798-47ab-a0f1-3a9878671798_amzn_1"
        elif DevQuestion == ("pc"):
            device_id="29c5de2ebdae420ae8701b492b8f0bc8d9d309c7"
        elif DevQuestion == ("parents alexa"):
            device_id="dd2e8f93df813898e6aac9b2947326e47f0596bc"
        SpoQuestion = input("What would you like me to pull up from your genius taste in music Sir?")
        if SpoQuestion == ("artist"):
            ArtQuestion = input("What artist would you like to listen to today?")
            if len(sys.argv) > 1:
                name = ' '.join(sys.argv[1:])
            else:
                name = ArtQuestion

            results = spotify.search(q='artist:' + name, type='artist')
            items = results['artists']['items']
            if len(items) > 0:
                artist = items[0]
                id = artist['uri']
                sp.start_playback(device_id=device_id, context_uri=id)
                #print(artist['uri'])
                print(artist['name'], artist['images'][0]['url'])
        elif SpoQuestion == ("album"):
            AlbQuestion = input("What album would you like to listen to today?")
            if len(sys.argv) > 1:
                name = ' '.join(sys.argv[1:])
            else:
                name = AlbQuestion

            results = spotify.search(q='album:' + name, type='album')
            items = results['albums']['items']
            if len(items) > 0:
                album = items[0]
                id = album['uri']
                sp.start_playback(device_id=device_id, context_uri=id)
                print(album['name'], album['images'][0]['url']) 
        elif SpoQuestion == ("song"):
            SongQuestion = input("What song would you like to listen to today?")
            if len(sys.argv) > 1:
                name = ' '.join(sys.argv[1:])
            else:
                name = SongQuestion
            results = spotify.search(q='track:' + name, type='track')
            items = results['tracks']['items']
            if len(items) > 0:
                track = items[0]
                id = track['uri']
                print(id)
                sp.start_playback(device_id=device_id, uris=[id])
                print(track['name'])
        elif SpoQuestion == ("playlist"):
            PlayQuestion = input("What playlist would you like to listen to today?")
            data = sp.current_user_playlists(limit=50, offset=0)
            playlist_name_we_want = PlayQuestion
            playlists = data['items']
            for playlist in playlists:
                if playlist['name'] == playlist_name_we_want:
                    print(playlist['external_urls']['spotify'])
                    id = playlist['uri']
                    sp.start_playback(device_id=device_id, context_uri=id)
                print(playlist['name'])
        elif SpoQuestion == ("shuffle"):
            ShuQuestion = input("On or Off Sir?")
            if ShuQuestion == ("on"):
                sp.shuffle(state=True)
            elif ShuQuestion == ("off"):
                sp.shuffle(state=False)
        elif SpoQuestion == ("repeat"):
            RQuestion = input("Song, Off, or Context Sir?")
            if RQuestion == ("song"):
                sp.repeat(state="track")
            elif RQuestion == ("off"):
                sp.repeat(state="off")
            elif RQuestion == ("context"):
                sp.repeat(state="context")