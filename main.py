from ast import arg
from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title : ", yt.title)

print("View : ", yt.views)

yd = yt.streams.get_audio_only()

yd.download('/Users/limhalim/Documents/Musik')

#* for Running Like this
#* python3.10 main.py "link youtubenya"