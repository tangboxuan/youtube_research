import fetch
import parser
from writer import write
from datetime import datetime

def search(query, time):
    searchResponse = fetch.search(query+" review")
    searchOutput = parser.search(searchResponse)

    channelOutput = []
    for video in searchOutput:
        channelResponse = fetch.channel(video['cid'])
        video['subscribers'] = parser.channel(channelResponse)
        channelOutput.append(video)

    videoOutput = []
    for video in channelOutput:
        videoResponse = fetch.video(video['id'])
        videoParsed = parser.video(videoResponse)
        for key in videoParsed.keys():
            video[key] = videoParsed[key]
        videoOutput.append(video)
    
    write(time, query, videoOutput)

with open('input.txt', 'r') as f:
    lines = f.readlines()
now = datetime.now()
time = now.strftime("%m-%d_%H:%M:%S")

for line in lines:
    search(line.strip(), time)