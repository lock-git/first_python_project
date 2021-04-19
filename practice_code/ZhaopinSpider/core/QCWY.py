__author__ = 'Joynice'
from practice_code.ZhaopinSpider.utils.utils import get_header, get_time
import requests
import queue
from lxml import etree
import threading
import os
import csv
import json
import datetime


class QCWY(object):
    '''
    前程无忧
    :param
    传入参数:关键字、城市、线程数
    传出：csv文件
    '''

    def __init__(self, keyword, city='北京', thread=4, path=os.getcwd()):
        self.keyword = keyword
        self.city = city
        self.thread = thread
        self.csv_header = ['职位名称', '详细链接', '公司名称', '工作地点', '薪资', '发布时间', '职位信息', '公司信息']
        self.baseurl = 'https://search.51job.com/list/'
        self.header = get_header()
        self.path = path
        self.pagequeue = queue.Queue()
        self.jobqueue = queue.Queue()

    def _get_city_code(self):
        url = 'https://js.51jobcdn.com/in/js/2016/layer/area_array_c.js'
        req = requests.get(url, headers=self.header).text
        #  找到 城市名称的索引位置
        a = req.find(self.city)
        #  截取 areaCode
        return req[a - 9:a - 3]

    def _get_max_page(self):
        city_code = self._get_city_code()
        url = self.baseurl + '{},000000,0000,00,9,99,{},2,1.html'.format(city_code, self.keyword)
        print(url)
        req = requests.get(url=url, headers=self.header)
        req.encoding = 'gbk'
        html = etree.HTML(req.text)
        result = html.xpath("//script[@type='text/javascript']/text()")
        max_page = str(result[0]).split("total_page\":\"")[1].split("\"")[0]
        print("max_page is {}".format(max_page))
        for page in range(1, int(20) + 1):
            page_url = self.baseurl + '{},000000,0000,00,9,99,{},2,{}.html'.format(city_code, self.keyword, page)
            self.pagequeue.put(page_url)

    def Spider(self):
        while not self.pagequeue.empty():
            url = self.pagequeue.get()
            print('正在爬取：{}'.format(url))
            req = requests.get(url, headers=get_header())
            req.encoding = 'gbk'
            html = etree.HTML(req.text)

            try:
                # 获取 目标json数据 c_result
                c_result = html.xpath("//script[@type='text/javascript' and contains(text(),'window.__SEARCH_RESULT__')]/text()")[0]
                c_c_result = c_result.split("window.__SEARCH_RESULT__ = ")[1]
                if c_c_result == None:
                    break

                # 解析 json 数据 j_result
                j_result = json.loads(c_c_result)
                companys_result = j_result["engine_search_result"]

                for i in (companys_result):
                    single_company = i
                    if single_company == None:
                        continue

                    print("job_name is {}".format(single_company["job_name"]))
                    print("company_name is {}".format(single_company["company_name"]))

                    data = {
                        "职位名称": single_company["job_name"],
                        "公司名称": single_company["company_name"],
                        "详细链接": single_company["job_href"],
                        "工作地点": single_company["workarea_text"],
                        "薪资":single_company["providesalary_text"],
                        "发布时间": single_company["issuedate"],
                        "职位信息": single_company["attribute_text"],
                        "公司信息": single_company["company_href"]
                    }

                    self.jobqueue.put(data)

            except:
                continue

    def run(self):
        self._get_max_page()
        thread_list = []
        for i in range(self.thread):
            t = threading.Thread(target=self.Spider)
            thread_list.append(t)
        for t in thread_list:
            t.setDaemon(True)
            t.start()
        for t in thread_list:
            t.join()
        if os.path.exists(self.path):
            data_list = []
            self.path = os.path.join(self.path, 'save-data')
            while not self.jobqueue.empty():
                data_list.append(self.jobqueue.get())
            with open(os.path.join(self.path, '51job_{}_{}_{}.csv'.format(self.keyword, self.city,datetime.datetime.now().minute)), 'w',
                      newline='', encoding='utf-8-sig') as f:
                f_csv = csv.DictWriter(f, self.csv_header)
                f_csv.writeheader()
                f_csv.writerows(data_list)


if __name__ == '__main__':
    a = QCWY(keyword='大数据', city='深圳').run()
