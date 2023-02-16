import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id='oscar_jl@hotmail.com',
                                                      client_secret='retorfe1010')
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'Radiohead'

results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    print(artist['name'], artist['images'][0]['url'])





'''

https://stackoverflow.com/questions/44251937/spotipy-simple-code-from-readthedocs-got-exception
import spotipy

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'



spotify = spotipy.Spotify()
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print ('track    : ' + track['name'])
    print ('audio    : ' + track['preview_url'])
    print ('cover art: ' + track['album']['images'][0]['url'])'''