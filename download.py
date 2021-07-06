import youtube_dl
import os

ydl_opts = {
    # "writesubtitles": True
    "writeautomaticsub": True
}

def download(time, name, links):
    os.chdir(f'output/{time}/{name}')
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(links)