from pytube import Playlist

p = Playlist('https://www.youtube.com/playlist?list=PLj1VRcS9RN36Kq2r91OzmsgsZGE9q2D3A')
#coloque aqui o nome da pasta
folder_name = ""

for video in p.videos:    
    stream = video.streams.filter(only_audio=True).first()
    #stream.download(filename=f"{video.title}.mp3", output_path="output/manoel_gomes")
    video.streams.first().download(filename=f"{video.title}.mp3", output_path=folder_name)
    print("The video is downloaded in MP3")
    