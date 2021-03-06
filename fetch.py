import os
from googleapiclient.discovery import build

key = os.getenv('API_KEY')
fetch = build('youtube', 'v3', developerKey=key)

def video(id):
    request = fetch.videos().list(
        part=['contentDetails','snippet','statistics'],
        id=id
    )
    return request.execute()

# def caption(id):
#     request = fetch.captions().list(
#         part='id',
#         videoId=id
#     )
#     return request.execute()

# def download(captionid):
#     request = fetch.captions().download(id=captionid)
#     return request.execute()


def channel(cid):
    request = fetch.channels().list(
        part='statistics',
        id=cid
    )
    return request.execute()

def search(query, page):
    request = fetch.search().list(
        part='snippet',
        maxResults=50,
        pageToken=page,
        q=query,
        relevanceLanguage='en',
        type='video'
    )
    return request.execute()

def categories():
    request = fetch.videoCategories().list(
        part='snippet',
        regionCode='sg'
    )
    return request.execute()