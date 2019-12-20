import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/hot'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"
}
html = requests.get(url, headers=headers).text
doc = pq(html)
print(doc)
'''
items = doc('.explore-tab.feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()
    file = open('explore.txt', 'a', encoding='utf-8')
    file.write('\n'.join([question,author,answer]))
    file.write('\n', '=' * 50 + '\n')
    file.close()
'''