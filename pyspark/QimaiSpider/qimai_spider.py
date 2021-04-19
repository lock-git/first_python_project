# -*- coding: UTF-8 -*-
__author__ = 'lock'

import requests
from practice_code.ZhaopinSpider.utils.utils import get_header
import csv
import os
from lxml.html import etree
import config
from bs4 import BeautifulSoup


if __name__ == '__main__':
    target = 'http://www.biqukan.com/1_1094/5403177.html'
    req = requests.get(url=target)
    html = req.text
    print(html)
    bf = BeautifulSoup(html)
    texts = bf.find_all('div', class_='showtxt')
    print(texts[0].text.replace('\xa0' * 8, '\n\n'))