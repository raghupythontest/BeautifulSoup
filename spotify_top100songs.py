from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID="6b5c30707e1649da9f877c39f280efd0"
CLIENT_SECRET="cc3c0874e239459fabe44dd02796e37e"
date=input("Which year do you want to travel? Enter the the date in Formar YYYY-MM-DD:")
url="https://www.billboard.com/charts/hot-100/"+date

response=requests.get(url=url)

music_web=response.text
soup=BeautifulSoup(music_web,"html.parser")
song_tags=soup.select("li h3")
songs_list=[song.getText().strip() for song in song_tags]
print(songs_list)

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example1.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

# Searching Spotify for songs by title
song_uris=[]
year = date.split("-")[0]
for song in songs_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify.Skipped.")


# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)
print(len(song_uris))

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
