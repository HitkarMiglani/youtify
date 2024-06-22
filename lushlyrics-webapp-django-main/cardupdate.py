from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from youtube_search import YoutubeSearch

PLAYLISTS = [#['Accidental','https://open.spotify.com/playlist/0zJ8hC8YJOcHYuk5nMPFm8?si=bec9bee69bf44f47'],
#['TimePass','https://open.spotify.com/playlist/6gADLrLFK1kXgEEOsENi1c', "PL59eqqQABruMSx6VSy1hbkBhG4XwtgSuy"],
#['CHILLS','https://open.spotify.com/playlist/3zs3QOLX8bASY5oV2dmEQw', 'PL59eqqQABruN3GyAPiPnQ6Jq-TngWjT-Y'],
#['Programming & Coding Music','https://open.spotify.com/playlist/6vWEpKDjVitlEDrOmLjIAj', 'PL59eqqQABruNew5O0cRvomfbU6FI0RGyl'],
['Spanish','https://open.spotify.com/playlist/6UVaFmnfL25RSvM3jqcGXE?si=4a1c25f0f7684c95']
]

# https://open.spotify.com/playlist/6UVaFmnfL25RSvM3jqcGXE?si=7816542bef0f425e,
client_credentials_manager = SpotifyClientCredentials(client_id='a1393f7d9b7249138d0daa3bc1359d0e',
                client_secret='914e1e5403fe4463ad4322b4e3469d97')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)



CONTAINER = []
for playlist in PLAYLISTS:
    Name,Link = playlist
    playlistcard = []
    count = 0
    PlaylistLink = "http://www.youtube.com/watch_videos?video_ids="
    for i in (sp.playlist_tracks(Link)['items']):
        if count == 50:
            break
        try:
            song = i['track']['name'] + i['track']['artists'][0]['name']
            songdic = (YoutubeSearch(song, max_results=1).to_dict())[0]
            playlistcard.append([songdic['thumbnails'][0],songdic['title'],songdic['channel'],songdic['id']])
            PlaylistLink += songdic['id'] + ','
        except:
            continue
        count += 1

    from urllib.request import urlopen
    req = urlopen(PlaylistLink)
    PlaylistLink = req.geturl()
    print(PlaylistLink)
    PlaylistId = PlaylistLink[PlaylistLink.find('list')+5:]

    CONTAINER.append([Name,playlistcard])

import json

json.dump(CONTAINER,open('card.json', 'w'),indent = 6) 
