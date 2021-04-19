# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import re

if __name__ == "__main__":
    server = 'http://www.biqukan.com/'
    target = 'http://www.biqukan.com/1_1094/'
    req = requests.get(url=target)
    req.encoding = 'gbk'
    html = req.text
    div_bf = BeautifulSoup(html, "lxml")
    print("===:"+div_bf.text)
    div = div_bf.find_all('div', class_='listmain')
    a_bf = BeautifulSoup(str(div[0]))
    a = a_bf.find_all('a')
    for each in a:
        print(each.string, server + each.get('href'))
        # 获取网页的编码
        # enconding = requests.utils.get_encodings_from_content(req.text)
        # print(enconding)
        # print(req.text.encode('gbk', 'ignore').decode('gbk'))
