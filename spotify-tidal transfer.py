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

client_id, client_secret, redirect_uri = None, None, None

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


def add_track_to_playlist_tidal(track_id, playlist_id):
    # just tell me whyyyyy
    # tidal_playlist = Playlist(playlist_id, session)
    # tidal_playlist.add_track(track_id)
    pass


def load_config():
    global client_id
    global client_secret
    global redirect_uri

    if Path('config.json').exists():
        with open('config.json', 'r') as file:
            config = json.load(file)
            client_id = config['client_id']
            client_secret = config['client_secret']
            redirect_uri = config['redirect_uri']
    else:
        print('Config file not found')
        client_id = input('Enter client_id: ')
        client_secret = input('Enter client_secret: ')
        redirect_uri = input('Enter redirect_uri: ')
        with open('config.json', 'w') as file:
            config = {
                'client_id': client_id,
                'client_secret': client_secret,
                'redirect_uri': redirect_uri
            }
            json.dump(config, file)


def search_tidal_track_id(artist_name, track_name):
    query = f'{artist_name} {track_name}'
    search = session.search(query = query, limit = 1)
    return search # i need heeeeelp, i'm falling down, so tell me whyyyyy, i'm falling down , you used to call me on my cell phone, late night when you need my love, call me on my cell phone, late night when you need my love, and i know when that hotline bling, that can only mean one thing, i know when that hotline bling, that can only mean one thing, ever since i left the city you, got a reputation for yourself now, everybody knows and i feel left


def processor():
    tracks = load_spoify_playlist()
    track_infos = create_track_infos(tracks)

    if len(track_infos) > 0:

        tidal_playlist_ids = create_tidal_playlist()

        for artist_name, track_name in track_infos:
            tidal_track_id = search_tidal_track_id(artist_name, track_name)
            add_track_to_playist(tidal_track_id, tidal_playlist_ids)


    else:
        print('No tracks found in the playlist')
        print('Closing...')
        exit()


load_config()

scope = 'playlist-read-private user-modify-playback-state playlist-modify-public playlist-modify-private user-top-read'
auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)


