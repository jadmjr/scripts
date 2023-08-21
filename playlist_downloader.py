from pytube import Playlist

p = Playlist('https://www.youtube.com/playlist?list=PLj1VRcS9RN36Kq2r91OzmsgsZGE9q2D3A')
print(f'Downloading: {p.title}')

for video in p.videos:
    video.streams.first().download()