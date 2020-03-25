import json
import parameters
import requests
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

class CreatePlaylist:

    def __init__(self, playlist_name, public):
        self.user_id = parameters.spotify_user_id
        self.token = parameters.spotify_token
        self.playlist_name = playlist_name
        self.public = public
        self.youtube_client = self.get_youtube_client()

    # Log into YouTube
    def get_youtube_client(self):
        # Copied from YouTube API
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

        api_service_name = 'youtube'
        api_version = 'v3'
        client_secrets_file = 'client_API_credential.json'

        # Get credentials and create an API client
        scopes = ['https://www.googleapis.com/auth/youtube.readonly']
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        credentials = flow.run_console()

        # from the Youtube DATA API
        youtube_client = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)

        return youtube_client

    # Grab the playlist to export into Spotify
    def get__playlist_to_export(self):
        pass

    # Create the playlist in Spotify
    def create_playlist(self):

        request_body = json.dumps({
            'name': self.playlist_name,
            'description': 'Playlist exported from YouTube playlist',
            'public': self.public
        })

        query = 'https://api.spotify.com/v1/users/{}/playlists'.format(self.user_id)

        response = requests.post(
            query,
            data=request_body,
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer {}'.format(self.token)
            }
        )
        response_json = response.json()

        # Return the playlist id
        return response_json['id']

    # Search the song in Spotify
    def get_spotify_uri(self, song_name, artist):
        query = 'https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20'.format(
            song_name,
            artist
        )
        response = requests.post(
            query,
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer {}'.format(self.token)
            }
        )
        response_json = response.json()
        songs = response_json['tracks']['item']
        # Get the first song uri
        song_uri = songs[0]['uri']
        return song_uri

    # Add the song into the new Spotify playlist
    def add_song_to_playlist(self):
        pass