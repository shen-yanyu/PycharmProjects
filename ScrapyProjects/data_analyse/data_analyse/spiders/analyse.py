import requests
import json
import re
from pyquery import PyQuery as pq # 从pyquery导入PyQuery并重命名为pq
# import time

# 获取页面源代码


def get_one_page(n):
    # 爬取目标的URL
    url = f'https://maoyan.com/board/4?offset={n*10}'
    # 反爬虫机制 添加表头信息
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.7.0.18838'}
    r = requests.get(url, headers=header)
    return r.text

# 使用pyquery解析源代码


def parse(new_url):
    # 获取new_url的网页源代码
    r = requests.get(new_url)
    # 将网页源代码解析为文本格式
    html = r.text
    # 使用pyquery对文本进行解析
    t = pq(html)
    # 定位
    names = t('body > div.banner > div > div.celeInfo-right.clearfix > div.movie-brief-container > h3').text()
    film_type = t('body > div.banner > div > div.celeInfo-right.clearfix > div.movie-brief-container > ul > li:nth-child(1)').text()
    releasetimes = t('body > div.banner > div > div.celeInfo-right.clearfix > div.movie-brief-container > ul > li:nth-child(3)').text()[-4:-2]
#     print(names, film_type, releasetimes)
    # time.sleep(1)
    return releasetimes

# 把获取的信息写入到本地
# movie.json
# tyoe.json
# year.json
# nature.json


def save_file(data):
    with open('nature.json', 'a', encoding='utf-8') as f:
        # 把字典 列表 转化成字符串 \n 换行
        data = json.dumps(data, ensure_ascii=False) + ',\n'
        f.write(data)
        f.close()

# 主函数


def run():
    for n in range(0, 10):
        # 获取每一页的电影
        html_text = get_one_page(n)
        doc = pq(html_text)
        for n in range(1, 11):
            # （pyquery解析的是字符串）
            link = doc("#app > div > div > div.main > dl > dd:nth-child(" + str(n) + ") > div > div > div.movie-item-info > p.name > a").attr("href")
            # 进行字符串拼接
            really_link = 'https://maoyan.com' + str(link)
            # 使用pyquery解析源代码
            items = parse(really_link)
            save_file(items)
        #     print(items)

# 运行程序入口


if __name__ == "__main__":
    run()



'''
def parse_one_page(html):
    pass


def write_to_file(content):
    pass


def main():
    pass


if __name__ == '__main__':
    main()
    pass
'''