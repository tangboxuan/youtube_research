import html
import emoji
from datetime import datetime

def search(response):
    result = []
    for item in response['items']:
        result.append({
            'title':html.unescape(emoji.demojize(item['snippet']['title'])),
            'channel':item['snippet']['channelTitle'],
            'link':"https://www.youtube.com/watch?v="+item['id']['videoId'],
            'id':item['id']['videoId'],
            'cid':item['snippet']['channelId'],
        })
    nextPage = response['nextPageToken']
    return {"result":result, "nextPage": nextPage}

def channel(response):
    stats = response['items'][0]['statistics']
    if stats['hiddenSubscriberCount']:
        subscriber = 'hidden'
    else:
        subscriber = stats['subscriberCount']
    videos = stats['videoCount']
    views = stats['viewCount']
    return {
        "subscribers":subscriber,
        "channel_videos":videos,
        "channel_views":views,
    }

def video(response):
    data = response['items'][0]
    published = datetime.strptime(data['snippet']['publishedAt'][0:10], "%Y-%m-%d")
    description = data['snippet']['description']
    prettyDescription = description.replace('\n', ' ').replace('\r', '')
    views = data['statistics']['viewCount']
    try:
        likes = data['statistics']['likeCount']
    except KeyError:
        likes = 'hidden'
    try:
        dislikes = data['statistics']['dislikeCount']
    except KeyError:
        dislikes = 'hidden'
    comments = data['statistics']['commentCount']
    duration = data['contentDetails']['duration'][2:]
    output = {
        'views':views,
        'duration':duration,
        'likes':likes,
        'dislikes':dislikes,
        'comments':comments,
        'published':published, 
        'description':prettyDescription,
    }
    return output

def categories(response):
    result = []
    for item in response['items']:
        result.append(item['snippet']['title'])
    result.sort()
    return '\n'.join(result)