import requests
from django.conf import settings

def get_spotify_token():
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': settings.SPOTIFY_CLIENT_ID,
        'client_secret': settings.SPOTIFY_CLIENT_SECRET,
    })

    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    return access_token


def get_music_by_genre(genre):
    token = get_spotify_token()
    headers = {
        'Authorization': f'Bearer {token}',
    }

    search_url = f'https://api.spotify.com/v1/search?q=genre:{genre}&type=track&limit=10'
    response = requests.get(search_url, headers=headers)
    response_data = response.json()

    tracks = response_data.get('tracks', {}).get('items', [])
    track_list = [{'name': track['name'], 'artist': track['artists'][0]['name'], 'url': track['external_urls']['spotify']} for track in tracks]

    return track_list
