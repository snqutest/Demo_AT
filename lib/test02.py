import requests
import re


url = 'https://movie.douban.com/cinema/nowplaying/chengdu/'

pattern = re.compile('<li.*?list-item.*?data-title="(.*?)".*?data-score="(.*?)".*?>.*?<img.*?src="(.*?)".*?/>',re.S)

html = requests.get(url).text
print (html)

items = re.findall(pattern,html)
for item in items:
    yield{
        'title':item[0],
        'score':item[1],
        'image':item[2],
    }