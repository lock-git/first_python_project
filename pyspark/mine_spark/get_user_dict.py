"""
@Time: 2021/1/14 19:44

@Author: yubingbing
"""

import pandas as pd
import pymysql as pymysql
import datetime
from impala.dbapi import connect
import re


#连接hive节点
con=connect(host='172.16.1.111', port=10000, auth_mechanism='PLAIN', user='hdfs', password='hdfs')
print('hive连接成功')
hive_cur=con.cursor()
#连接线上节点
conn = pymysql.connect(host='10.10.11.126', port=3306, user='motor_rw', passwd='eUF1y_3zD', db='motor', charset='utf8')
print('mysql连接成功')
cur = conn.cursor()




#create_sql = """CREATE TABLE motor_user_dict (
#             motor_word VARCHAR(100) NOT NULL,
#             type INT,
#             update_time VARCHAR(30))"""
#cur.excute(create_sql)
#print('空表创建成功')


def insertDataIntoDatabase(sql):
    """向mysql数据库插入数据,注：sql语句拼接时，除了整形或浮点类型数据，类型都可以为字符串（str 或 Unicode）"""
    try:
        records = cur.execute(sql)
    except:
        print(f'向mysql数据库中插入数据失败，请检查sql语句是否正确，sql语句是 {sql}')
    else:
        if records == 0:
            print(f'并未向mysql数据库中插入任何数据,sql语句是 {sql}')
        conn.commit()

'''
#读取车型无关基础词汇
word_lst=[]      #基础词汇列表
with open('/data/azkaban/taskFile/moto/yubingbing/get_user_dict/user_dict1.txt', "r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        if line not in word_lst:
            word_lst.append(line)
print('data ready')
now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
insert_sql_kw = "INSERT INTO `motor_user_dict` ( `motor_word`, `type`, `update_time`) VALUES ( '{}', 0, '{}' )"
insert_sql_q = "INSERT INTO `motor_user_dict` ( `motor_word`, `type`, `update_time`) VALUES ( '{}', 1, '{}' )"
for i in word_lst:
    insertDataIntoDatabase(insert_sql_kw.format(i,now_time))
print('kw基础词汇写入完成')
for i in word_lst:
    insertDataIntoDatabase(insert_sql_q.format(i,now_time))
print('query基础词汇写入完成')
'''


sql1='''select distinct goods_name,keywords from dw_moto.motor_imall_goods_models'''   
sql2='''select distinct goods_name,keywords from dw_moto.motor_imall_goods_models where add_time>=date_add(from_unixtime(unix_timestamp(), 'yyyy-MM-dd HH:mm:ss'), -1)'''

'''
#历史全量车型
hive_cur.execute(sql1)
name_list = hive_cur.fetchall()
car_type_tb=pd.DataFrame(list(name_list),columns=['goods_name','keywords'])
historial_name_list_kw=[]
historial_name_list_q=[]
for i in car_type_tb.index:
    goods_name=car_type_tb['goods_name'][i]
    keywords=car_type_tb['keywords'][i]
    origin_name_list=[]
    origin_name_list.append(goods_name)
    if type(keywords)==str:
        for k in keywords.split(','):
            origin_name_list.append(k)
    for name in origin_name_list:   #kw部分
        name=name.replace("'","")
        nonboard_goods_name=name.replace(' ','').replace('/','').replace('-','').replace('·','').replace('.','')
        lower_goods_name1=nonboard_goods_name.lower()
        lower_goods_name2=name.lower()
        tmp_name_lst=list(set([name,nonboard_goods_name,lower_goods_name1,lower_goods_name2]))
        for j in tmp_name_lst:
            if j not in historial_name_list_kw:
                historial_name_list_kw.append(j)
    for name in origin_name_list:   #q部分
        lower_goods_name=name.lower()
        chinese = re.findall(".*?([\u4E00-\u9FA5]+).*?",lower_goods_name)
        eng=re.findall('[a-zA-Z0-9]+',lower_goods_name)
        eng=[x for x in eng if len(x)>2]
        tmp_name_lst=eng+chinese
        for j in tmp_name_lst:
            if j not in historial_name_list_q:
                historial_name_list_q.append(j)
#写入mysql
print('data ready')
now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
insert_sql_kw = "INSERT INTO `motor_user_dict` ( `motor_word`, `type`, `update_time`) VALUES ( '{}', 0, '{}' )"
insert_sql_q = "INSERT INTO `motor_user_dict` ( `motor_word`, `type`, `update_time`) VALUES ( '{}', 1, '{}' )"
for i in historial_name_list_kw:
    insertDataIntoDatabase(insert_sql_kw.format(i,now_time))
print('kw历史车型写入完成')
for i in historial_name_list_q:
    insertDataIntoDatabase(insert_sql_q.format(i,now_time))
print('query历史车型写入完成')
'''


#新增车型
hive_cur.execute(sql2)
name_list = hive_cur.fetchall()
car_type_tb=pd.DataFrame(list(name_list),columns=['goods_name','keywords'])
new_name_list_kw=[]
new_name_list_q=[]
for i in car_type_tb.index:
    goods_name=car_type_tb['goods_name'][i]
    keywords=car_type_tb['keywords'][i]
    origin_name_list=[]
    origin_name_list.append(goods_name)
    if type(keywords)==str:
        for k in keywords.split(','):
            origin_name_list.append(k)
    for name in origin_name_list:   #kw部分
        name=name.replace("'","")
        nonboard_goods_name=name.replace(' ','').replace('/','').replace('-','').replace('·','').replace('.','')
        lower_goods_name1=nonboard_goods_name.lower()
        lower_goods_name2=name.lower()
        tmp_name_lst=list(set([name,nonboard_goods_name,lower_goods_name1,lower_goods_name2]))
        for j in tmp_name_lst:
            if j not in new_name_list_kw:
                new_name_list_kw.append(j)
    for name in origin_name_list:   #q部分
        lower_goods_name=name.lower()
        chinese = re.findall(".*?([\u4E00-\u9FA5]+).*?",lower_goods_name)
        eng=re.findall('[a-zA-Z0-9]+',lower_goods_name)
        eng=[x for x in eng if len(x)>2]
        tmp_name_lst=eng+chinese
        for j in tmp_name_lst:
            if j not in new_name_list_q:
                new_name_list_q.append(j)
#写入mysql
print('data ready')
now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
insert_sql_kw = "INSERT INTO `motor_user_dict` ( `motor_word`, `type`, `update_time`) VALUES ( '{}', 0, '{}' )"
insert_sql_q = "INSERT INTO `motor_user_dict` ( `motor_word`, `type`, `update_time`) VALUES ( '{}', 1, '{}' )"
for i in new_name_list_kw:
    insertDataIntoDatabase(insert_sql_kw.format(i,now_time))
print('kw新增车型写入完成')
for i in new_name_list_q:
    insertDataIntoDatabase(insert_sql_q.format(i,now_time))
print('query新增车型写入完成')



# 关闭游标连接
cur.close()
# 关闭数据库连接
conn.close()
hive_cur.close()
con.close()
