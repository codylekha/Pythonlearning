import requests
import sys
if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())


'''
PS C:\Users\DELL\Python30days> cd 03
PS C:/Users/DELL/Python30days/03> python library.py weezer
{'resultCount': 1, 'results': [{'wrapperType': 'track', 'kind': 'song', 'artistId': 115234, 'collectionId': 1440878798, 'trackId': 1440879551, 'artistName': 'Weezer', 'collectionName': 'Weezer', 'trackName': "Say It Ain't So", 'collectionCensoredName': 'Weezer', 'trackCensoredName': "Say It Ain't So", 'artistViewUrl': 'https://music.apple.com/us/artist/weezer/115234?uo=4', 'collectionViewUrl': 'https://music.apple.com/us/album/say-it-aint-so/1440878798?i=1440879551&uo=4', 'trackViewUrl': 'https://music.apple.com/us/album/say-it-aint-so/1440878798?i=1440879551&uo=4', 'previewUrl': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview122/v4/5c/07/84/5c078405-d5db-0762-d346-0f6ae3ccb530/mzaf_5370611585102254803.plus.aac.p.m4a', 'artworkUrl30': 'https://is2-ssl.mzstatic.com/image/thumb/Music125/v4/fc/74/67/fc74674a-1eb0-d50d-33fe-215caee529d1/16UMGIM52971.rgb.jpg/30x30bb.jpg', 'artworkUrl60': 'https://is2-ssl.mzstatic.com/image/thumb/Music125/v4/fc/74/67/fc74674a-1eb0-d50d-33fe-215caee529d1/16UMGIM52971.rgb.jpg/60x60bb.jpg', 'artworkUrl100': 'https://is2-ssl.mzstatic.com/image/thumb/Music125/v4/fc/74/67/fc74674a-1eb0-d50d-33fe-215caee529d1/16UMGIM52971.rgb.jpg/100x100bb.jpg', 'collectionPrice': 10.99, 'trackPrice': 1.29, 'releaseDate': '1994-05-10T12:00:00Z', 'collectionExplicitness': 'notExplicit', 'trackExplicitness': 'notExplicit', 'discCount': 1, 'discNumber': 1, 'trackCount': 10, 'trackNumber': 7, 'trackTimeMillis': 258853, 'country': 'USA', 'currency': 'USD', 'primaryGenreName': 'Rock', 'isStreamable': True}]}'''