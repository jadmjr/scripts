from pytube import YouTube

import csv
with open('input/manoel_gomes.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

    line = 0

    for row in spamreader:
        if(line > 0):
            url = ', '.join(row)
            print(str(url))
            try:
                video = YouTube(url)
                stream = video.streams.filter(only_audio=True).first()
                stream.download(filename=f"{video.title}.mp3", output_path="output/manoel_gomes")
                print("The video is downloaded in MP3")
            except KeyError:
                print("Unable to fetch video information. Please check the video URL or your network connection.")
        line+=1