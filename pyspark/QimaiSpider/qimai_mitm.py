from lxml import etree
import queue
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random
import os
import csv
import datetime

# print(datetime.datetime.now().minute)
# print(datetime.datetime.now().month)
# print(datetime.datetime.now().day)
# print(datetime.datetime.now().hour)

# 表头
csv_header = ['包名', '应用名称', '最新版本', '一级分类', '所属主体', '主体地址', '开发者名称',
              '开发者地址', '应用描述', "下载量", '应用包渠道下载地址', '是否有效', '入库时间', '更新时间', '区域']
# 队列
page_queue = queue.Queue()
app_queue = queue.Queue()

# 浏览器参数
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
browser = webdriver.Chrome(executable_path=r'C:\chromedriver_win32\chromedriver.exe', options=chrome_options)

# 获取所有的子页面
browser.get('https://www.qimai.cn/rank/marketRank')
html = browser.page_source
tree = etree.HTML(html)
app_list = tree.xpath('//*[@id="marke-rank-list-index"]/div[2]/table/tbody/tr[*]/td[*]/div/a[*]/@href')
i = 0
for app in app_list:
    app_url = 'https://www.qimai.cn' + '{}'.format(str(app))
    page_queue.put(app_url)
    i = i + 1
    if i > 50:
        break
    print(app_url)

# 针对每一个子页面进行解析
while not page_queue.empty():
    try:
        app_url = page_queue.get()
        browser.get(app_url)
        time.sleep(random.randint(4, 10))
        app_html = browser.page_source
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

        app_queue.put(app_info_dict)
    except:
        continue

if os.path.exists(os.getcwd()):
    data_list = []
    path = os.path.join(os.getcwd(), 'save_data')
    while not app_queue.empty():
        data_list.append(app_queue.get())
    with open(os.path.join(path, 'qi_mai_{}_{}_{}_{}.csv'.format(datetime.datetime.now().month,
                                                                 datetime.datetime.now().day,
                                                                 datetime.datetime.now().hour,
                                                                 datetime.datetime.now().minute)), 'w',
              newline='', encoding='utf-8-sig') as f:
        f_csv = csv.DictWriter(f, csv_header)
        f_csv.writeheader()
        f_csv.writerows(data_list)
    pass
