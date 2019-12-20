import requests
import re
import json
#


def get_one_page(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"}
    response = requests.get(url, headers = headers)
    response.encoding = 'gbk'
    if response.status_code == 200:
        return response.text
    return None


def parse_one_page(html):
    pattern = re.compile(
        "<li><a href='(.*?)' target.*?>(.*?)</a> <em>(.*?)</em></li>", re.S
    )
    items = re.findall(pattern, html)
    print(items)
    for item in items:
        yield {
            'link': item[0],
            'title': item[1],
            'time': item[2]
        }


def write_to_file(content):
    with open('result_1.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main():
    url = 'http://scitech.people.com.cn/GB/1056/index.html'
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


main()











