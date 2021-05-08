import csv
import datetime
import os
import queue
import threading
import time
from lxml import etree
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import pyasn1


class qimai_fp_chrome(object):

    def __init__(self, thread, path=os.getcwd()):
        self.thread = thread
        self.csv_header = ['包名', '应用名称', '最新版本', '一级分类', '所属主体', '主体地址', '开发者名称',
                           '开发者地址', '应用描述', "下载量", '应用包渠道下载地址', '是否有效', '入库时间', '更新时间', '区域']
        self.base_url = 'https://www.qimai.cn'
        self.app_info_url = 'https://www.qimai.cn/rank/marketRank'
        self.path = path
        self.PROXY = "http://61.155.138.151:5010"
        self.page_queue = queue.Queue()
        self.app_queue = queue.Queue()

    def get_app_list(self):

        # 反反爬虫参数
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        browser = webdriver.Chrome(executable_path=r'C:\chromedriver_win32\chromedriver.exe', options=chrome_options)

        browser.get('https://www.qimai.cn/rank/marketRank')
        html = browser.page_source
        tree = etree.HTML(html)
        app_list = tree.xpath('//*[@id="marke-rank-list-index"]/div[2]/table/tbody/tr[*]/td[*]/div/a[*]/@href')
        i = 0
        for app in app_list:
            app_url = self.base_url + '{}'.format(str(app))
            self.page_queue.put(app_url)
            i = i + 1
            if i > 15:
                break
            print(app_url)

    def spider(self):
        while not self.page_queue.empty():
            try:
                app_url = self.page_queue.get()

                app_options = Options()
                app_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                app_browser = webdriver.Chrome(executable_path=r'C:\chromedriver_win32\chromedriver.exe',
                                               options=app_options)
                app_browser.get(app_url)
                time.sleep(random.randint(4, 8))
                app_html = app_browser.page_source
                app_tree = etree.HTML(app_html)
                app_info_dict = {"包名": "", "应用名称": "", "最新版本": "", "一级分类": "",
                                 "所属主体": "", "主体地址": "", "开发者名称": "", "开发者地址": "",
                                 "应用描述": "", "下载量": "", "应用包渠道下载地址": "",
                                 "是否有效": "", "入库时间": "", "更新时间": "", "区域": ""}

                # APP name
                app_name_l = app_tree.xpath("//*[@id='app-container']/div[1]/div[2]/div[1]/div[1]/div/text()")
                if len(app_name_l) > 0:
                    app_name = app_name_l[0]
                    app_info_dict["应用名称"] = app_name
                # 公司名称
                company_name_l = app_tree.xpath(
                    "//*[@id='app-container']/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/text()")
                if len(company_name_l) > 0:
                    company_name = company_name_l[0]
                    app_info_dict["开发者名称"] = company_name
                # APP 分类
                category_l = app_tree.xpath("//*[@id='app-container']/div[1]/div[2]/div[2]/div[3]/div[2]/text()")
                if len(category_l) > 0:
                    category = category_l[0]
                    app_info_dict["一级分类"] = category
                # 主包 bundle_id
                bundle_id_l = app_tree.xpath("//*[@id='app-container']/div[1]/div[2]/div[2]/div[11]/div[2]/text()")
                if len(bundle_id_l) > 0:
                    bundle_id = bundle_id_l[0]
                    app_info_dict["包名"] = bundle_id
                # 下载量
                download_l = app_tree.xpath("//*[@id='app-container']/div[1]/div[2]/div[2]/div[5]/div[2]/text()")
                if len(download_l) > 0:
                    download = download_l[0]
                    app_info_dict["下载量"] = download
                # APP 描述
                describe_l = app_tree.xpath("//*[@id='andApp-baseInfo']/div[2]/div[3]/div[2]/text()")
                if len(describe_l) > 0:
                    describe = "".join(describe_l[0:2]).replace(" ", "").replace("\n", "").replace("\r", "")
                    app_info_dict["应用描述"] = describe
                # 最新版本
                latest_version_l = app_tree.xpath("//*[@id='andApp-baseInfo']/div[2]/div[4]/ul/li[4]/p[2]/text()")
                if len(latest_version_l) > 0:
                    version = latest_version_l[0]
                    app_info_dict["最新版本"] = version
                # 最新版本发布日期
                version_date_l = app_tree.xpath(
                    "//*[@id='app-container']/div[1]/div[2]/div[2]/div[9]/div[2]/text()")
                if len(version_date_l) > 0:
                    version_date = version_date_l[0]
                    app_info_dict["更新时间"] = version_date

                # 公司详细信息的链接
                # company_href_l = app_tree.xpath("//*[@id='appMain']/div[1]/ul/li[@class='company-limit']/a/@href")
                # if len(company_href_l) > 0:
                #     company_href = self.baseurl + '{}'.format(str(company_href_l[0]))
                #     company_driver = webdriver.Ie(executable_path=r'C:\IEDriverServer_x64_2.45.0\IEDriverServer.exe')
                #     company_driver.get(company_href)
                #     print('正在爬取company：{}'.format(company_href))
                #     company_html = company_driver.page_source
                #     company_tree = etree.HTML(company_html)
                #     # 公司详细信息：地址
                #     address = company_tree.xpath("//*[@id='companyInfo']/div[2]/table/tbody/tr[1]/td[2]/text()")
                #     app_info_dict["主体地址"] = address[0]
                #     print("公司地址 {}".format(address[0]))
                # else:
                #     # 公司详细信息：主体
                #     company_zhu_ti_l = app_tree.xpath(
                #         "//*[@id='appMain']/div[1]/ul/li[@class='company-limit']/span/text()")
                #     if len(company_zhu_ti_l) > 0:
                #         company_zhu_ti = company_zhu_ti_l[0]
                #         app_info_dict["所属主体"] = company_zhu_ti

                # print("APP 名称：{}\n版本 {}\n版本日期 {}\n开发者名称：{}\nAPP 分类：{}\n主包 {}\n下载量 {}\n描述 {}\n"
                #       .format(app_name, version, version_date, company_name, category, bundle_id, download, describe))
                self.app_queue.put(app_info_dict)
                app_browser.quit()
            except:
                continue

    def run(self):
        self.get_app_list()
        thread_list = []
        for i in range(self.thread):
            t = threading.Thread(target=self.spider)
            thread_list.append(t)
        for t in thread_list:
            t.setDaemon(True)
            t.start()
        for t in thread_list:
            t.join()
        if os.path.exists(self.path):
            data_list = []
            self.path = os.path.join(self.path, 'save_data')
            while not self.app_queue.empty():
                data_list.append(self.app_queue.get())
            with open(os.path.join(self.path, 'qi_mai_{}_{}_{}_{}.csv'.format(datetime.datetime.now().month,
                                                                              datetime.datetime.now().day,
                                                                              datetime.datetime.now().hour,
                                                                              datetime.datetime.now().minute)), 'w',
                      newline='', encoding='utf-8-sig') as f:
                f_csv = csv.DictWriter(f, self.csv_header)
                f_csv.writeheader()
                f_csv.writerows(data_list)


if __name__ == '__main__':
    qimai_fp_chrome(thread=1).run()
