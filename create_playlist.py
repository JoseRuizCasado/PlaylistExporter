import json
import parameters
import requests

class CreatePlaylist:

    def __init__(self, playlist_name, public):
        self.user_id = parameters.spotify_user_id
        self.token = parameters.spotify_token
        self.playlist_name = playlist_name
        self.public = public

    # Log into YouTube
    def get_youtube_client(self):
        pass

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
        return response_json[id]

    # Search the song in Spotify
    def get_spotify_uri(self):
        pass

    # Add the song into the new Spotify playlist
    def add_song_to_playlist(self):
        pass