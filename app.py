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
results = sp.current_user_saved_tracks(limit=3)
user = sp.current_user()
playlists = sp.current_user_playlists(limit=50, offset=0)
#----------------------------- Spotify -----------------------------#

#----------------------------- Shuffle -----------------------------#
## Paramaters
decade_start = '2010-01-01'
decade_end = '2020-12-12'
artists = []
artists_pass = False
#albums = []
albums_pass = False
songs = []
songs_pass = False
features = []
directory = []

## Paramaters

## James
for idx, item in enumerate(results['items']):
    track = item['track']
    #directory.append([idx,track['artists'][0]['name']])
    artistAlbums = sp.artist_albums(track['artists'][0]['id'])
    
    for idx, album in enumerate(artistAlbums['items']):
        albumName = album['name']
        #directory.append(["album ",albumName])
        albumsTracks = sp.album_tracks(album['external_urls']['spotify'])
        
        for idx, track in enumerate(albumsTracks['items']):
            trackName = track['name']
            dir = [track['artists'][0]['name'],'/',albumName,'/',trackName]
            listToStr = ''.join(map(str, dir))
            directory.append(listToStr)
## Whale

## Functionality
#for idx, item in enumerate(results['items']):
    #track = item['track']
    
    
    #album = sp.album(track['album']['external_urls']['spotify'])
    #features.append(track['id'])

    #if track['album']['release_date'] >= decade_start and track['album']['release_date'] <= decade_end and track['artists'][0]['name']:
        #output.append([idx, track['artists'][0]['name'], " – ", track['name'], track['album']['release_date']])
        #output.append(album['genres'])
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
    return render_template('shuffle.htm',tracks=directory)

@app.route('/profile')
def profile():
    return render_template('profile.htm', user=user, pic=profile)

@app.route('/playlist')
def playlist():
    return render_template('playlist.htm', playlists=playlists)
