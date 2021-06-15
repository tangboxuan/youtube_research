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

def categories(response):
    result = []
    for item in response['items']:
        result.append(item['snippet']['title'])
    result.sort()
    return '\n'.join(result)