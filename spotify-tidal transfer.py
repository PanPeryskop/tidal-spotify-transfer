import spotipy
import tidalapi
from tidalapi import Quality
from tidalapi import Playlist
from pathlib import Path
from spotipy.oauth2 import SpotifyOAuth
import requests
import json

tidal_playlist_id = None

tidal_session_file = Path('tidal_session.json')
session = tidalapi.Session()
session.login_session_file(tidal_session_file)

session.audio_quality = Quality.hi_res




def load_spoify_playlist():
    playlist_url = input('Enter Spotify Playlist URL: ')
    if playlist_url.startswith('https://open.spotify.com/playlist/'):
        playlist_id = playlist_url.split('/')[-1].split('?')[0]
        tracks = sp.playlist_tracks(playlist_id)
        return tracks
    else:
        print('Invalid URL')
        print('Closing...')
        exit()


def create_tidal_playlist():
    tidal_playlist_id = "test"
    return tidal_playlist_id


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


def add_track_to_playist(track_id, playlist_id):

    pass


def load_config():
    pass


def search_tidal_track_id(artist_name, track_name):
    query = f'{artist_name} {track_name}'
    search = session.search(query = query, limit = 1)
    return search.tracks[0].id


scope = 'playlist-read-private user-modify-playback-state playlist-modify-public playlist-modify-private user-top-read'
auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)


def processor():
    tracks = load_spoify_playlist()
    track_infos = create_track_infos(tracks)

    if len(track_infos) > 0:

        tidal_playlsit_id = create_tidal_playlist()

        for artist_name, track_name in track_infos:
            tidal_track_id = search_tidal_track_id(artist_name, track_name)
            add_track_to_playist(tidal_track_id, tidal_playlsit_id)


    else:
        print('No tracks found in the playlist')
        print('Closing...')
        exit()