import html

def search(response):
    result = []
    for item in response['items']:
        result.append({
            'title':html.unescape(item['snippet']['title']),
            'channel':item['snippet']['channelTitle'],
            'id':item['id']['videoId'],
            'cid':item['snippet']['channelId'],
        })
    return result

def channel(response):
    stats = response['items'][0]['statistics']
    if stats['hiddenSubscriberCount']:
        return 'hidden'
    else:
        return response['items'][0]['statistics']['subscriberCount'] 

def video(response):
    data = response['items'][0]
    published = data['snippet']['publishedAt']
    description = data['snippet']['description']
    prettyDescription = description.replace('\n', ' ').replace('\r', '')
    views = data['statistics']['viewCount']
    output = {'views':views, 'published':published, 'description':prettyDescription}
    return output

def categories(response):
    result = []
    for item in response['items']:
        result.append(item['snippet']['title'])
    result.sort()
    return '\n'.join(result)