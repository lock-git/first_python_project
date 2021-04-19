# -*- coding: UTF-8 -*-
__author__ = 'lock'

import requests
from lxml.html import etree
from practice_code.ZhaopinSpider.utils.utils import get_header
from practice_code.ZhaopinSpider.config import  QIMAI_COOKIE
import queue
import csv
import os

class qimai_spider_test:

    def __init__(self, keyword, city='苏州', thread=4, path=os.getcwd()):
        self.keyword = keyword
        self.city = city
        self.thread = thread
        self.csv_header = ['包名', '应用名称', '最新版本', '一级分类', '所属主体', '主题地址', '开发者名称',
                           '区域地址', '应用描述', '应用包渠道下载地址', '是否有效', '入库时间', '更新时间', '区域']
        self.baseurl = 'https://www.qimai.cn/rank/release'
        self.header = get_header()
        self.path = path
        self.pageQueue = queue.Queue()
        self.appInfoQueue = queue.Queue()



if __name__ == '__main__':
    target = 'https://api.qimai.cn/rank/release'
    header = get_header()
    params = {
        'analysis': 'dQ51TyxjAEd+cwBHdh5+TylecxV9dGFEfXRTQilNYgxWcRlaUlcNDXATFxZWVg8bRARcVVFDVXATCVQFD1AGBVEDBQUCcBMB',
        'genre': '36',
        'date': '2021-04-07',
        'is_preorder': 'all',
        'status': '3',
        'sdate': '2021-04-07',
        'edate': '',
        'country': 'cn'
    }

    # req = requests.get(url=target,params=params, headers=get_header())
    req = requests.get(url='https://api.qimai.cn/rank/marketList?analysis=dQ51TyxjAEd%2BcwBHdyUKBSQXGRNRXlsfXVFCUwFDdA1HQiETAQACCAAJDlwHDVQAdkIB&date=2021-04-08', headers=get_header())
    print(req.url)

    req.encoding = 'gbk'

    # app_info_json = req.json()['rankInfo']
    app_info_json = req.json()['marketList']

    for app_info in app_info_json :
        print("appName is {}".format(app_info['appInfo']["appName"]))
        print("genre is {}".format(app_info["genre"]))
        print(" ================================= ")

