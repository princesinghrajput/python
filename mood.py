import spotipy
from spotipy.oauth2 import SpotifyOAuth
from textblob import TextBlob
import random
import webbrowser

# Spotify credentials
SPOTIPY_CLIENT_ID = '592dfe6cf57e44958b68be6de88edf57'
SPOTIPY_CLIENT_SECRET = '095562aa571b4fefa94540f6d8f5da09'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'
mood_keywords = {
    'happy': ['happy', 'joyful', 'uplifting'],
    'sad': ['sad', 'melancholy', 'blue'],
    'relaxed': ['relaxing', 'chill', 'calm'],
}

def analyze_mood(text):
    blob = TextBlob(text)
    if blob.sentiment.polarity > 0.5:
        return 'happy'
    elif blob.sentiment.polarity < -0.1:
        return 'sad'
    else:
        return 'relaxed'

def find_song(mood):
    query = random.choice(mood_keywords[mood])
    results = sp.search(q=query, type='track', limit=10)
    tracks = results['tracks']['items']
    if tracks:
        return random.choice(tracks)['uri']  # Return Spotify URI
    return None

def play_song(song_uri):
    devices = sp.devices()
    if devices['devices']:
        device_id = devices['devices'][0]['id']
        sp.start_playback(device_id=device_id, uris=[song_uri])
    else:
        webbrowser.open(f"https://open.spotify.com/track/{song_uri.split(':')[-1]}")

# User input
user_input = input("How are you feeling today? (Write a few sentences): ")

# Determine mood
mood = analyze_mood(user_input)
print(f"Detected mood: {mood.capitalize()}")

# Find and play a song based on the mood
song_uri = find_song(mood)
if song_uri:
    print(f"Playing a {mood} song...")
    play_song(song_uri)
else:
    print(f"Could not find a song for the mood: {mood}")