# -*- coding:gbk -*-

import requests
import re

num = 0
while True:
    url =  ['http://scitech.people.com.cn/GB/1056/index{}.html'.format(num)]
    num += 1
    print(url)
    if num > 8:
        break
    for urls in url:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"}
        response = requests.get(url = urls,headers = headers)
        response.encoding = 'gbk'
        html = response.text
        tech = re.findall(r'<li>.*?/n1/(.*?).html.*?', html, re.S)

        for i in tech:
            with open('tech.txt', 'a+') as f:
                url = 'http://scitech.people.com.cn/n1/' + str(i) + '.html'
                f.write(url)
                f.close()
                print(url)
                '''
                response = requests.get(url)
                response.encoding = 'gbk'
                html_01 = response.text
                try :
                    tech_01 = re.findall(r'<div class="box_pic"></div>(.*?)<div class="zdfy clearfix">', html_01, re.S)[0]
                except:
                    pass
                tech_02 = str(tech_01)
                print(tech_02.replace('<p>','').replace('3000','').replace('n','').replace('u','').replace('t','')
                      .replace('</p>','').replace('<p syle="ex-ide: 2em','').replace('</srog>','')
                      .replace('<p alig="ceer">','').replace('&bsp','').replace(' ','').replace('<palig="jsify">','')
                      .replace('<srog>','').replace('</div>','').replace(';">',''))
                with open('technology.txt', 'a+') as z:
                   z.write(tech_02.replace('<p>','').replace('3000','').replace('n','').replace('u','').replace('t','')
                           .replace('</p>','').replace('<p syle="ex-ide: 2em','').replace('</srog>','')
                           .replace('<p alig="ceer">','').replace('&bsp','').replace(' ','').replace('<palig="jsify">','')
                           .replace('<srog>','').replace('</div>','').replace(';">',''))
                   z.write('\r\n')
                   z.close()

'''



