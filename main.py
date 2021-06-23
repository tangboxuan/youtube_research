import fetch
import parser
from writer import write

def search(query):
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
    
    write(query, videoOutput)

search('surface laptop 4')