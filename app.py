import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, render_template
app = Flask(__name__)


output = []

#----------------------------- Spotify -----------------------------#
## Login
scope = "user-library-read"
client_id='d975372af075408d9484c6347eeac929'
client_secret='0319b5236e5c46d18a6b13a6cbaa9467'
redirect_uri="http://127.0.0.1:5000/callback"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri))
results = sp.current_user_saved_tracks(limit=10)
user = sp.current_user()
playlists = sp.current_user_playlists(limit=50, offset=0)
#----------------------------- Spotify -----------------------------#

#----------------------------- Shuffle -----------------------------#
## Paramaters
decade_start = '2010-01-01'
decade_end = '2020-12-12'
artists = []
artists_pass = False
albums = []
albums_pass = False
songs = []
songs_pass = False
features = []
directory = []

## Paramaters

## James
for idx, item in enumerate(results['items']):
    track = item['track']

    if track['artists'][0]['name'] in artists:
        artists_pass = False
    else:
        artists_pass = True

    if track['name'] in songs:
        songs_pass = False
    else:
        songs_pass = True

    #directory.append([idx,track['artists'][0]['name']])
    artistAlbums = sp.artist_albums(track['artists'][0]['id'])
    
    for idx, album in enumerate(artistAlbums['items']):
        albumName = album['name']
        #directory.append(["album ",albumName])
        if albumName in albums:
            albums_pass = False
        else:
            albums_pass = True
        albumsTracks = sp.album_tracks(album['external_urls']['spotify'])
        
        for idx, track in enumerate(albumsTracks['items']):
            trackName = track['name']
            dir = [track['artists'][0]['name'],'/',albumName,'/',trackName]
            listToStr = ''.join(map(str, dir))
            directory.append(listToStr)
## Whale

## Functionality
for idx, item in enumerate(results['items']):
    track = item['track']
    duration = track['duration_ms']/1000
    
    album = sp.album(track['album']['external_urls']['spotify'])
    features.append(track['id'])

    if track['album']['release_date'] >= decade_start and track['album']['release_date'] <= decade_end and track['artists'][0]['name']:
        output.append([idx, track['artists'][0]['name'], track['name'], track['album']['release_date'],duration, album['genres']])
        #output.append(sp.audio_features(tracks=features[idx]))
## Functionality
#----------------------------- Shuffle -----------------------------#

# Algorithm
# Algorithm

@app.route('/')
def welcome():
    return render_template('welcome.htm')

@app.route('/login')
def login():
    return render_template('login.htm')

@app.route('/shuffle')
def shuffle():
    return render_template('shuffle.htm',tracks=output)

@app.route('/profile')
def profile():
    return render_template('profile.htm', user=user, pic=profile)

@app.route('/playlist')
def playlist():
    return render_template('playlist.htm', playlists=playlists)
