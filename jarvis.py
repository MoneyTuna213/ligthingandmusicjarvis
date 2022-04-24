from nanoleaf import JarvisNanoleaf
from spotify import SpotifyNanoleaf
import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
import sys
import wavio as wv
from nanoleafapi import Nanoleaf 
from nanoleafapi import NanoleafDigitalTwin
from nanoleafapi import RED, ORANGE, YELLOW, GREEN, LIGHT_BLUE, BLUE, PINK, PURPLE, WHITE
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
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
# Sampling frequency
freq = 44100

# Recording duration
duration = 5
# Start recorder with the given values of 
# duration and sample frequency
recording = sd.rec(int(duration * freq), 
                   samplerate=freq, channels=2)
print("TALK. NOW.")

# Record audio for the given number of seconds
sd.wait()
write("recording0.wav", freq, recording)
wv.write("recording1.wav", recording, freq, sampwidth=2)
r = sr.Recognizer()
with sr.AudioFile('recording1.wav') as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data).lower()
    print(text)

if "nanoleaf red" in text:
        nl = Nanoleaf("192.168.1.239")
        digital_twin = NanoleafDigitalTwin(nl)
        panel_ids=nl.get_ids()
        panelone = ""
        i=-1
        nl.set_color(RED)     
elif "nanoleaf orange" in text:
        nl = Nanoleaf("192.168.1.239")
        digital_twin = NanoleafDigitalTwin(nl)
        panel_ids=nl.get_ids()
        panelone = ""
        i=-1
        nl.set_color(ORANGE)    
elif "nanoleaf yellow" in text:
        nl = Nanoleaf("192.168.1.239")
        digital_twin = NanoleafDigitalTwin(nl)
        panel_ids=nl.get_ids()
        panelone = ""
        i=-1
        nl.set_color(YELLOW)    
elif "nanoleaf green" in text:
        nl = Nanoleaf("192.168.1.239")
        digital_twin = NanoleafDigitalTwin(nl)
        panel_ids=nl.get_ids()
        panelone = ""
        i=-1
        nl.set_color(GREEN)    
elif "nanoleaf blue" in text:
        nl = Nanoleaf("192.168.1.239")
        digital_twin = NanoleafDigitalTwin(nl)
        panel_ids=nl.get_ids()
        panelone = ""
        i=-1
        nl.set_color(BLUE)
elif "nanoleaf purple" in text:
        nl = Nanoleaf("192.168.1.239")
        digital_twin = NanoleafDigitalTwin(nl)
        panel_ids=nl.get_ids()
        panelone = ""
        i=-1
        nl.set_color(PURPLE)    
elif "nanoleaf pink" in text:
        nl = Nanoleaf("192.168.1.239")
        digital_twin = NanoleafDigitalTwin(nl)
        panel_ids=nl.get_ids()
        panelone = ""
        i=-1
        nl.set_color(PINK)      
elif "nanoleaf white" in text:
        nl = Nanoleaf("192.168.1.239")
        digital_twin = NanoleafDigitalTwin(nl)
        panel_ids=nl.get_ids()
        panelone = ""
        i=-1
        nl.set_color(WHITE)      
elif "nanoleaf off" in text:
        nl = Nanoleaf("192.168.1.239")
        digital_twin = NanoleafDigitalTwin(nl)
        panel_ids=nl.get_ids()
        panelone = ""
        i=-1
        nl.power_off()   
elif "nanoleaf on" in text:
        nl = Nanoleaf("192.168.1.239")
        digital_twin = NanoleafDigitalTwin(nl)
        panel_ids=nl.get_ids()
        panelone = ""
        i=-1
        nl.power_on()  

elif "artist" in text:
    device_id="72f01996a421b8480cd6fc06120c24ffe1666e9b"
    if len(sys.argv) > 1:
        name = ' '.join(sys.argv[1:])
    else:
        name = text.split("artist ",1)[1]

        results = spotify.search(q='artist:' + name, type='artist')
        items = results['artists']['items']
        if len(items) > 0:
            artist = items[0]
            id = artist['uri']
            sp.start_playback(device_id=device_id, context_uri=id)
            #print(artist['name'], artist['images'][0]['url'])
elif "album" in text:
    device_id="72f01996a421b8480cd6fc06120c24ffe1666e9b"
    if len(sys.argv) > 1:
        name = ' '.join(sys.argv[1:])
    else:
        name = text.split("album ",1)[1]
    results = spotify.search(q='album:' + name, type='album')
    items = results['albums']['items']
    if len(items) > 0:
        album = items[0]
        id = album['uri']
        sp.start_playback(device_id=device_id, context_uri=id)
elif "playlist" in text:
        device_id="72f01996a421b8480cd6fc06120c24ffe1666e9b"
        if len(sys.argv) > 1:
                name = ' '.join(sys.argv[1:])
        else:
                name = text.split("playlist ",1)[1]
        data = sp.current_user_playlists(limit=50, offset=0)
        playlist_name_we_want = name
        playlists = data['items']
        for playlist in playlists:
                if playlist['name'] == playlist_name_we_want:
                        id = playlist['uri']
                        sp.start_playback(device_id=device_id, context_uri=id)

elif 'song' in text:
    device_id="72f01996a421b8480cd6fc06120c24ffe1666e9b"
    if len(sys.argv) > 1:
        name = ' '.join(sys.argv[1:])
    else:
        name = text.split("song ",1)[1]
        if len(sys.argv) > 1:
                name = ' '.join(sys.argv[1:])
        else:
                name = name
                results = spotify.search(q='track:' + name, type='track')
                items = results['tracks']['items']
        if len(items) > 0:
                track = items[0]
                id = track['uri']
                print(id)
                sp.start_playback(device_id=device_id, uris=[id])

