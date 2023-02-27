from pytube import Playlist

# Se pide el enlace de la playlist de YouTube
playlist_link = input("Enlace aquí")

# Pytube crea un objeto Playlist a partir del enlace
playlist = Playlist(playlist_link)

# Imprime la información de la playlist
print("Title:", playlist.title)
print("Total videos:", len(playlist.video_urls))

# Descarga cada video de la playlist
for video_url in playlist.video_urls:
    video = pytube.YouTube(video_url)
    print("Downloading...", video.title)
    video.streams.get_highest_resolution().download()
