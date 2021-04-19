import time
import requests
from lxml import etree
from selenium import webdriver
import pandas as pd
import re

def parse_data(html):
    tree = etree.HTML(html)
    jftr = tree.xpath('//div[@class="tab_box"]/div[2]/div[1]/table/tbody/tr')
    max = 0
    need = "-1"
    if len(jftr) > 1:
        for jf in jftr:
            jftd = jf.xpath('.//td/span/@title')
            if jftd:
                info = jftd[0]
                match = re.search(r'[1-9]\d*',info)
                if match:
                    number = int(match.group(0))
                    if number > max:
                        need = info
                        max = number


    if need != '-1':
        tmpneed = need.split(str(max))
        need = tmpneed[0] + str(max+1) + tmpneed[1]

    tr = tree.xpath('//div[@class="tab_box"]/div[1]/div[1]/table/tbody/tr')
    if len(tr)>1:
        for t in tr:
            td = t.xpath('.//td/span/@title')
            if td:
                if need == '-1':
                    if td[-1] == '未缴费':
                        return td
                else:
                    if (td[-1] == '未缴费') and (td[0] == need):
                        return td



def info():
    url = 'http://cpquery.sipo.gov.cn/txnQueryFeeData.do?select-key:shenqingh=2020202133352&select-key:zhuanlilx=2&select-key:gonggaobj=0&select-key:backPage=http://cpquery.sipo.gov.cn/txnQueryOrdinaryPatents.do?select-key:sortcol=&select-key:sort=&select-key:shenqingh=2020202133352&select-key:zhuanlimc=&select-key:shenqingrxm=&select-key:zhuanlilx=&select-key:shenqingr_from=&select-key:shenqingr_to=&verycode=1&inner-flag:open-type=window&inner-flag:flowno=1611900331266&token=1D682043624549EF987C6D4784624D55&inner-flag:open-type=window&inner-flag:flowno=1611900331266'
    headers = {
        'Host':'cpquery.sipo.gov.cn',
        'Connection':'keep-alive',
        'Cache-Control':'max-age=0',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        # 'Cookie':'UR3ZMlLdcLIE80S=rnLM4foua4V8kGvkJSwdjSyu9DcpIDCYB3CUXkaGI4h5_5QisxkGZBKbTrGv21IB; _gscu_699342174=1422594813roex33; _gscbrs_699342174=1; JSESSIONID=77d36533124bbe3415366c6eb8d6; bg6=65|AlOA/; _gscs_699342174=t1422804523039798|pv:2; UR3ZMlLdcLIE80T=4yQVf4i_CDfFQMMiUim4bt1tZ.xWvQQWmGFWIPHMAgQ9n33DDYC393QIigV3Pw0tjUpD22BKDWyxncI51CzSBoAOFoPwv297XlAA4fThQhmAKXwuigIYE8eT0tTe7NCH3vZNwqhOKccddKYbG56D_zszTqAcIuerOL6ODvCsspjhvydjRqkhI9dMo9qVp7O64xCRt0K2p5DpNeqZtW6ALkloVXrbXvDzQd_p14At0b4R40FJUf173rSm8XbM40aQcxZLoA3RW5c1kzEr5SESbQsd_h0Cl1nSc1p.I_yNcXcmHmU7lwGKFTigeNLcOXu_NbV6gWO6q1.5R19kaL.hDzIBX',
        'cookie':'UR3ZMlLdcLIE80S=NXyH92MU4FUEzmPOVvseXMBwReOQqPgWX1VVwNbTyBJXNLKuTr84RNkbETZk1wN0; _gscu_699342174=115634026jxsx383; UR3ZMlLdcLIE83S=VL4Uh3MFXdrfZlQjMcd8hdfoaUFgi2EKWupGy_EZLx1nyr8DQDDKLCd19oMUK8JT; UR3ZMlLdcLIE83T=4GlplM0MMenu6fEPNWBeCXRPwV4Yr7BCWYdqtC.zvn9MJz8UFWZw69xA7AZlJ4dXytS3nDD44o7w7qk8cbZUJwJYAYWSxfxSdcDRiWsWWVmzuqSJ0eK7wn83Ym5p.lukGKP1wRQrrFF.2GWFAjqihWMeEQe4gyyErLQnIxhB6xomgefUaI4Qwmip.J7.tMTiXbGKx7RqBrKF4l17Y26HmPT4SiNP4hVz7RwT5.HUz_Z4019KF855kgkpP0sitsKdK1DZN2u1z0LRHFzYVOnugPAEgMbTvgSTI.2G1AQVnMzc75vUzrEn6nntnAGUFhj6AZM9_i9GpqK4gYKoKyTCKqrJ0BxGrn5IF99d6l2CprmrPqA.hTDxfMt29tyRIV1cMcYV; bg6=50|AlPAj; JSESSIONID=8758b6afe38bd5347173a4c9ff74; _gscbrs_699342174=1; _gscs_699342174=14244319781rzc45|pv:1; UR3ZMlLdcLIEenable=true; UR3ZMlLdcLIE80T=4l.In6K3CVt3vUsCrM56dDFAuY.CW8ejF5iMuKlxuyKk34OZLlzScS4cmY4GKU8J3.DjxcnfYiy.L_DFtnMr47AN6f7bp1p0OdbpFUZbknOV.D3we7MpMGFNUBCUStJ3TkS0dnQsSQzKd_DZxFSzqDZAVeE5emkj8x.2g3ncJh7tnW0YvFeHu_hFEIvja.e_exgWzl65hWp2U637ULEIwDPCVVZ.kEvZ915jZ73cV7DcDrNwloBdcndWNhiGRT29OPkv1mVsELqPniEiTgPww940J9TSEGh51l2hNAIb8pIUo7P1RSPHyBAme07TGqSvQ.Bl'
    }
    res = requests.get(url, headers=headers)
    print(res.status_code)
    if res:
        print(res.text)
        parse_data(res.text)


def sendUrl():
    # title = ['费用种类', '应缴金额', '缴费截至日', '费用状态']
    title = ['待交费信息']
    with open(r'E:\1\授权费数据结果.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    result = []
    for line in lines:
        temp = line.strip()
        dic = {}
        pattern = "(.*?) (.*)"
        data = re.findall(pattern, temp)[0]
        dic['url'] = data[0]
        lit = data[1]
        if lit != '无':
            lit = eval(lit)
            lit = lit[2] + "前缴纳" + lit[0] + lit[1] + "元" ;

        with open(r'E:\1\授权费数据结果123.txt','a',encoding='utf-8') as f:
            f.write(data[0] + "\t" + str(lit) + "\n")
        # dic.update(zip(title, lit))
        # print(dic)
        # result.append(dic)

    # df = pd.DataFrame(result)
    # df.to_excel('E:\1\瑞昊结果123.xlsx', index=False)


if __name__ == '__main__':
    '''
    17625352648    15300856086   15371879627  18951130676 17319281614 13595066473 15952721945
    '''
    # 18551584084  Zrlh66234390@
    # sendUrl()
    driver = webdriver.Ie(executable_path=r'C:\IEDriverServer_x64_2.45.0\IEDriverServer.exe')
    url = 'http://cpquery.sipo.gov.cn/'
    driver.get(url)
    input('...')
    # df = pd.read_excel(r'C:\Users\lx\Desktop\zhuanli_url.xlsx')['Url']
    with open(r'E:\1\授权费数据.txt', 'r', encoding='utf-8') as fp:
        links = fp.readlines()

    with open(r'E:\1\授权费数据结果.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    finish_list = []
    for line in lines:
        finish_list.append(line.split(" ")[0])
    n = 0
    for link in links:
        n+=1
        link = link.strip()
        if link in finish_list:
            continue
        print(f'{n}/{len(links)} {link}')
        driver.get(link)
        time.sleep(2)
        html = driver.page_source
        if 'images/reach_top.png' in html:
            break
        data = parse_data(html)
        if data is None:
            data = '无'
        print(data)
        with open(r'E:\1\授权费数据结果.txt','a',encoding='utf-8') as f:
            f.write(link + " " + str(data) + "\n")

    driver.quit()
    print('查询次数上限,程序已退出!')
