# -*- coding:utf-8 -*-
#import chardet
import requests
import re
import jieba


def __init__(self):
    self.write_path = "D:\\PycharmProjects\\xiaoshuo\\"
    self.keyword_list_path = 'D:\\PycharmProjects\\xiaoshuo\\keyword_list.txt'
    self.stopword_list_path = 'D:\\PycharmProjects\\xiaoshuo\\stopword_list.txt'
    self.keyword_list_ge = (line.strip() for line in open(self.keyword_list_path, 'r', encoding='UTF-8').readlines())
    self.keyword_list = []
    for wd in self.keyword_list_ge:
        self.keyword_list.append(wd)
    self.stopword_list_ge = (line.strip() for line in open(self.stopword_list_path, 'r', encoding='UTF-8').readlines())
    self.stopword_list = []
    for wd in self.stopword_list_ge:
        self.stopword_list.append(wd)


num = 0
while True:
    url =  ['http://scitech.people.com.cn/GB/1056/index{}.html'.format(num)]
    num += 1
    #print(url)
    if num > 8:
        break
    for urls in url:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"}
        response = requests.get(url = urls,headers = headers)
        response.encoding = 'gbk'
        html = response.text
        tech = re.findall(r'<li>.*?/n1/(.*?).html.*?</em></li>', html, re.S)
        for i in tech:
            #with open('tech.txt', 'a+') as f:
                url = 'http://scitech.people.com.cn/n1/' + str(i) + '.html'
                #print(url)
                response = requests.get(url)
                response.encoding = 'gbk'
                html_01 = response.text
                print(html_01)

                matching_a = 0
                for one_a in html_01:
                    if self.get_matching_times(one_a) >= 1:
                        matching_a += 1
                if matching_a >= 3:
                    try:
                        tech_01 = re.findall(r'<div class="box_pic"></div>(.*?)<div class="zdfy clearfix">', html_01, re.S)[0]
                    except:
                        pass
                    tech_02 = str(tech_01)
                    print(tech_02.replace('<p>', '').replace('3000', '').replace('n', '').replace('u', '')
                          .replace('t', '')
                      .replace('</p>', '').replace('<p syle="ex-ide: 2em', '').replace('</srog>', '')
                      .replace('<p alig="ceer">', '').replace('&bsp', '').replace(' ', '').replace('<palig="jsify">','')
                      .replace('<srog>', '').replace('</div>', '').replace(';">', ''))
'''       
                with open('renmingwang.txt', 'a+') as z:
                    z.write(tech_02.replace('<p>','').replace('3000','').replace('n','').replace('u','').replace('t','')
                       .replace('</p>','').replace('<p syle="ex-ide: 2em','').replace('<srog>','')
                       .replace('<p alig="ceer">','').replace('&bsp','').replace(' ','')
                       .replace('<palig="jsify">','').replace('<srog>','').replace('</div>','').replace(';">',''))
                    z.write('\r\n')
                    z.close()
'''


def get_matching_times(self, one_a):
    matching_times = 0
    if not one_a.text:
        return 0
    a_text = one_a.text
    for seg in jieba.cut(a_text, cut_all=True):
        if seg.strip() in self.stopword_list:
            return 0
        if seg.strip() in self.keyword_list:
            matching_times += 1
    return matching_times

