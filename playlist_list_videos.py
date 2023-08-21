from pytube import Playlist

p = Playlist('https://www.youtube.com/playlist?list=PLj1VRcS9RN36Kq2r91OzmsgsZGE9q2D3A')
print(f'Downloading: {p.title}')
i = 0
for url in p.video_urls:
    print(i)
    print(url)
    i+=1