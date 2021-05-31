#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import numpy as np

batch_minute_date = datetime.datetime.strptime("202105190716", '%Y%m%d%H%M')
batch_minute_date_tom = batch_minute_date + datetime.timedelta(days=1)
print(batch_minute_date)
print(batch_minute_date_tom)

# 在python中 None,  False, 空字符串"", 0, 空列表[], 空字典{}, 空元组()都相当于False ，即：
# not None == not False == not '' == not 0 == not [] == not {} == not ()

a = []
if not a:
    print("nihao============")

if not a:
    print("tahao============")

# 测试list取数
A = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6]])
print(" A[ 0: 2 ]:", A[0: 2])
print(" A[ 2: ]:", A[2:])
print(" A[ : 2 ]:", A[: 2])
print(" A[ : , 2]:", A[:, 2])

# 快速生成list
list_0 = [x * 2 for x in range(5)]
print(list_0)

# 字符串格式化
str_one = """
insert into test.qxb_user_auto_yunying_v3 partition(batch='%s')
select user_id,mobile,desc,company_type,active_type,eid,'%s' template from t_all
 """ % (1, 2)

str_two = """
select distinct b.user_id,b.mobile,a.type desc,'{company_type}' company_type,'{active_type}' active_type,
a.eid
from {data_table} a
join {user_table} b on a.user_id = b.user_id
join t_mysql on b.user_id = t_mysql.user_id
""".format(company_type="1", active_type="2",
           data_table="3", user_table="4")

a = 'python'
b = a[::-1]
print(b)  # nohtyp
c = a[::-2]
print(c)  # nhy
# 从后往前数的话，最后一个位置为-1
d = a[:-1]  # 从位置0到位置-1之前的数
print(d)  # pytho
e = a[:-2]  # 从位置0到位置-2之前的数
print(e)  # pyth

batch = "20210521"
table_name_1 = """ts_qxb_m_activation_silence_push_allmt_cn_%s_1""" % batch
table_name_2 = "ts_qxb_m_activation_silence_push_allmt_cn_{b}_1".format(b=batch)
print(table_name_1)
print(table_name_2)

print(str([1, 2, 3]))




# spark 注册函数 string --》 array
#   def get_label_list(str):
#         """
#         :param str:
#         :return:
#         """
#         if str and str != '{}':
#             str_dict = json.loads(str)
#             if isinstance(str_dict, dict):
#                 return str_dict.items()
#         return []
#
#     spark.udf.register('get_label_list', get_label_list, ArrayType(StructType([
#         StructField("label", StringType(), True),
#         StructField("num", IntegerType(), True)])))
