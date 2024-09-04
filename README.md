# Spotify-Tidal

**⚠️ Warning: This application is currently under early development and has not been even tested. It may not work as expected. Use at your own risk. ⚠️**

Spotify-Tidal is a Python application that allows users to transfer their Spotify playlists to Tidal. The application uses the Spotify and Tidal APIs to fetch playlists from Spotify and recreate them in Tidal.

## Resources used
- Spotipy
- Tidalapi

## Before you install

Before you can use Spotify-Tidal, you need to create a Spotify Developer application to get your `client_id`, `client_secret`, and `redirect_uri`. Here's how you can do it:

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Log in with your Spotify account.
3. Click on 'Create an App'.
4. Fill in the 'Name', 'Description' and redirect_uri (I recommend using http://localhost:3000/) for your new app, then click 'Create'.
5. On the next page, you will see your `client_id` and `client_secret`. You will need these to authenticate your application.
6. Click on 'Edit Settings'.
7. In the 'Redirect URIs' field, enter the URI where you want Spotify to redirect you after a successful login.
8. Click 'Save'.

## Installation

1. Make sure you have Python 3.9 or later installed. If not, you can download it from the [official website](https://www.python.org/downloads/). Make sure to add Python to PATH during installation.
2. Clone the repository or download the ZIP file and extract it.
3. Open the Spotify-Tidal folder.
4. Run `setup.bat` file to install required packages.

## Usage

1. Open the folder in cmd and type `python spotify-tidal.py` or open `run.bat` file in the Spotify-Tidal folder.
2. The application will ask you to enter your `client_id`, `client_secret`, `redirect_uri`, `tidal_username`, and `tidal_password`. Enter the values from the Spotify Developer Dashboard and your Tidal account.
3. Enter the Spotify playlist URL when prompted.
4. Choose whether you want the Tidal playlist to be public or private.

Enjoy your music!