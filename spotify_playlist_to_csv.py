#!/usr/bin/env python3
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv

usernames = ['']
filename = "default.csv"

client_id = ''
client_secret = ''
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def main(): 
    for user in usernames:
        add_user_playlist(user)

    print("DONE")

def get_tracks_data(tracks, playlist, username):
    user_playlist = []
    for item in tracks['items']:
        playlist_entry = {}
        playlist_entry['playlist_name'] = playlist['name']
        playlist_entry['username'] = username

        track = item['track']
        playlist_entry['track_title'] = track['name']
        playlist_entry['track_id'] = track['id']
        playlist_entry['artist'] = track['artists'][0]['name']
        playlist_entry['duration_ms'] = track['duration_ms']
        playlist_entry['popularity'] = track['popularity']
        playlist_entry['explicit'] = track['explicit']
        playlist_entry['album'] = track['album']['name']

        # get album data not included in playlist
        if track['album']['uri'] is not None: 
            album_data = sp.album(track['album']['uri'])
            playlist_entry['release_date'] = album_data['release_date']
            playlist_entry['label'] = album_data['label']

            features = sp.audio_features(track['id'])
            playlist_entry['danceability'] = features[0]['danceability']
            playlist_entry['energy'] = features[0]['energy']
            playlist_entry['key'] = features[0]['key']
            playlist_entry['loudness'] = features[0]['loudness']
            playlist_entry['speechiness'] = features[0]['speechiness']
            playlist_entry['acousticness'] = features[0]['acousticness']
            playlist_entry['instrumentalness'] = features[0]['instrumentalness']
            playlist_entry['liveness'] = features[0]['liveness']
            playlist_entry['tempo'] = features[0]['tempo']
            playlist_entry['time_signature'] = features[0]['time_signature']

            user_playlist.append(playlist_entry)        
    return user_playlist

def add_user_playlist(username):
    with open(filename, 'a') as f:
        fieldnames = ['playlist_name', 'username', 'track_title', 'artist', 
                      'duration_ms', 'popularity', 'explicit', 'album', 
                      'release_date', 'label', 'danceability', 'energy',
                      'key', 'loudness', 'speechiness', 'acousticness', 'instrumentalness',
                      'liveness', 'tempo', 'time_signature']
        writer = csv.DictWriter(f, fieldnames)
        playlists = sp.user_playlists(username)

        print("Getting data from " + username + "'s playlists:")
        playlists = sp.user_playlists(username)

        for playlist in playlists['items']:
            user_playlist = []
            if playlist['owner']['id'] == username:
                print(playlist['name'])

                if 'display_name' in playlist['owner']:
                    disp_name = playlist['owner']['display_name']
                else:
                    disp_name = username

                results = sp.user_playlist(username, playlist['id'], fields="tracks,next")
                tracks = results['tracks']
                user_playlist = user_playlist + get_tracks_data(tracks, playlist, disp_name)
                while tracks['next']:
                    tracks = sp.next(tracks)
                    user_playlist = user_playlist + get_tracks_data(tracks, playlist, disp_name)
                writer.writerows(user_playlist)
            
    print()
    return user_playlist

if __name__ == '__main__':
    main()
