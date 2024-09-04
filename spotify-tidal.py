import spotipy
import tidalapi
from tidalapi import Quality
from tidalapi import Playlist
from pathlib import Path
from spotipy.oauth2 import SpotifyOAuth
import requests
import json

def load_spoify_playlist():
    playlist_url = input('Enter Spotify Playlist URL: ')
    if playlist_url.startswith('https://open.spotify.com/playlist/'):
        playlist_id = playlist_url.split('/')[-1].split('?')[0]
        tracks = sp.playlist_tracks(playlist_id)
        playlist_name = sp.playlist(playlist_id)['name']
        return tracks, playlist_name
    else:
        print('Invalid URL')
        print('Closing...')
        exit()


def create_tidal_playlist(playlist_name):
    user_input = input('Do you want playlist to be public? (y/n): ')
    
    if user_input.lower() == 'y':
        tidal_playlist = session.user.create_playlist(playlist_name, 'Transfered from spotify', public=True)
    else:
        tidal_playlist = session.user.create_playlist(playlist_name, 'Transfered from spotify', public=False)

    return tidal_playlist


def get_track_info(spotify_track_id):
    track_info = sp.track(spotify_track_id)
    artist_name = track_info['artists'][0]['name']
    track_name = track_info['name']
    return artist_name, track_name


def create_track_infos(tracks):
    track_infos = []
    for track in tracks:
        artist_name, track_name = get_track_info(track['id'])
        track_infos.append((artist_name, track_name))
    return track_infos


def add_track_to_playlist_tidal(track_id, playlist_id):
    tidal_playlist = Playlist(playlist_id, session)
    tidal_playlist.add(track_id)
    pass


def load_config():
    global client_id
    global client_secret
    global redirect_uri
    global tidal_username
    global tidal_password

    if Path('config.json').exists():
        with open('config.json', 'r') as file:
            config = json.load(file)
            client_id = config['client_id']
            client_secret = config['client_secret']
            redirect_uri = config['redirect_uri']
            tidal_password = config['tidal_password']
            tidal_username = config['tidal_username']
    else:
        print('Config file not found')
        client_id = input('Enter client_id: ')
        client_secret = input('Enter client_secret: ')
        redirect_uri = input('Enter redirect_uri: ')
        tidal_username = input('Enter tidal_username: ')
        tidal_password = input('Enter tidal_password: ')

        with open('config.json', 'w') as file:
            config = {
                'client_id': client_id,
                'client_secret': client_secret,
                'redirect_uri': redirect_uri,
                'tidal_username': tidal_username,
                'tidal_password': tidal_password
            }
            json.dump(config, file)


def search_tidal_track_id(artist_name, track_name):
    query = f'{artist_name} {track_name}'
    search = session.search(query = query, limit = 1)
    return search

def processor():
    tracks, playlist_name = load_spoify_playlist()
    track_infos = create_track_infos(tracks)

    if len(track_infos) > 0:

        tidal_playlist = create_tidal_playlist(playlist_name)

        for artist_name, track_name in track_infos:
            tidal_track_id = search_tidal_track_id(artist_name, track_name)
            add_track_to_playlist_tidal(tidal_track_id, tidal_playlist)
    else:
        print('No tracks found in the playlist')
        print('Closing...')
        exit()

client_id, client_secret, redirect_uri, tidal_username, tidal_password = None, None, None, None, None

load_config()

scope = 'playlist-read-private user-modify-playback-state playlist-modify-public playlist-modify-private user-top-read'
auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)

tidal_playlist_id = None

session = tidalapi.Session()

session.login(tidal_username, tidal_password)
session.audio_quality = Quality.hi_res


processor()