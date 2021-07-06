import fetch
import parser
from writer import write
from datetime import datetime
from csv import reader
from download import download

PAGES = 1

def search(query, time, dateFrom, dateTo):
    nextPage = ""
    for i in range(PAGES):
        print(f"Obtaining data for {query} page {i+1}")

        searchResponse = fetch.search(query+" review", nextPage)
        searchOutput = parser.search(searchResponse)
        nextPage = searchOutput["nextPage"]

        channelOutput = []
        links = []
        for video in searchOutput["result"]:
            channelResponse = fetch.channel(video['cid'])
            channelParsed = parser.channel(channelResponse)
            del video['cid']
            for key in channelParsed.keys():
                video[key] = channelParsed[key]
            channelOutput.append(video)
            links.append(video['link'])

        videoOutput = []
        for video in channelOutput:
            videoResponse = fetch.video(video['id'])
            videoParsed = parser.video(videoResponse)
            del video['id']
            if dateFrom <= videoParsed['published'] <= dateTo:
                videoParsed['published'] = datetime.strftime(videoParsed['published'], "%d-%m-%Y")
                for key in videoParsed.keys():
                    video[key] = videoParsed[key]
                videoOutput.append(video)
        
        print(f"Writing data for {query} page {i+1}")

        englishOutput = []
        for video in videoOutput:
            if video['title'].isascii():
                englishOutput.append(video)
        name = '_'.join(query.split())
        write(time, name, videoOutput, i, False)
        write(time, name, englishOutput, i, True)
        download(time, name, links)

now = datetime.now()
time = now.strftime("%m-%d_%H:%M:%S")

with open('input.csv', 'r') as f:
    lines = reader(f)
    next(lines)
    for line in lines:
        if line[1]:
            dateFrom = datetime.strptime(line[1], "%d-%m-%Y")
        else:
            dateFrom = datetime.strptime("01-01-2000", "%d-%m-%Y")
        if line[2]:
            dateTo = datetime.strptime(line[2], "%d-%m-%Y")
        else:
            dateTo = now
        search(line[0], time, dateFrom, dateTo)
    print("Completed!")