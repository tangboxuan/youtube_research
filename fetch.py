import os
from googleapiclient.discovery import build

key = os.getenv('API_KEY')
fetch = build('youtube', 'v3', developerKey=key)

def channel(username):
    request = fetch.channels().list(
        part='statistics',
        forUsername=username
    )
    return request.execute()

def search(query):
    request = fetch.search().list(
        part='snippet',
        maxResults=5,
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