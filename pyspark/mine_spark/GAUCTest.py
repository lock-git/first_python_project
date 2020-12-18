import datetime
import os

import sys
from collections import defaultdict
import numpy as np
from pyspark import StorageLevel
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from sklearn.metrics import roc_auc_score

os.environ['JAVA_HOME'] = "D:\Java_development_tools\JDK"
sys.path.append("D:\Java_development_tools\JDK\bin")

os.environ['SPARK_HOME'] = "E:\Code\spark-2.1.1-bin-hadoop2.7"
sys.path.append("E:\Code\spark-2.1.1-bin-hadoop2.7\python")
sys.path.append("E:\Code\spark-2.1.1-bin-hadoop2.7\python\pyspark")

os.environ['PYTHON_HOME'] = "D:\software\\anaconda\envs\pyspark_env_3.6"
sys.path.append("D:\Java_development_tools\python3.6.8\python.exe")


def auc_statistics(sparkSession, statistics_day):
    """statistics auc"""


    base_data_df = sparkSession.read \
        .option("inferschema", "true") \
        .option("header", "true") \
        .option("encoding", "gbk") \
        .csv("C:\\Users\JDD\Desktop\\auc_base_data.csv")
    base_data_df.createOrReplaceTempView("t_base_auc_tmp")
    base_data_df.show(10)

    # 计算GAUC
    device_row = base_data_df.select("deviceid", "action_type", "click_score").collect()

    device_label_score_dict = defaultdict(lambda: [])

    for t in device_row:
        device_label_score_dict[t[0]].append((int(t[1]), float(t[2])))

    # 剔除行为全部一样的用户
    filter_device = defaultdict(lambda: False)
    for k1 in device_label_score_dict.keys():
        vv = device_label_score_dict.get(k1)
        flag = False
        for i in range(len(vv) - 1):
            if vv[i][0] != vv[i + 1][0]:
                flag = True
                break
        filter_device[k1] = flag

    impression_total = 0
    total_auc = 0
    total_device = 0
    for k in device_label_score_dict.keys():
        if filter_device.get(k):
            total_device += 1
            v = device_label_score_dict.get(k)
            label_list = []
            score_list = []
            for label_score in v:
                label_list.append(label_score[0])
                score_list.append(label_score[1])
            auc = roc_auc_score(np.asarray(label_list), np.asarray(score_list))
            # print(f"用户 {k} 的 行为数是 {len(v)} auc的值为 {auc} ")
            total_auc += auc * len(v)
            impression_total += len(v)
            label_list.clear()
            score_list.clear()

    group_auc = float(total_auc) / float(impression_total)
    group_auc = '%.6f' % group_auc

    print(f"总户数是 {len(device_label_score_dict)} ，参与计算的用户数为{total_device} ，total_auc 为 {total_auc} ，impression_total 为{impression_total} ，最终的 gauc 值为 {group_auc}")

    #清空内存
    device_label_score_dict.clear()
    filter_device.clear()
    device_row.clear()


if __name__ == "__main__":
    sparkSession = SparkSession.builder \
        .master("local") \
        .appName("FlowModelAUC") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()

    sparkSession.sparkContext.setLogLevel("ERROR")

    # 获取昨天的数据
    # yesterday = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y%m%d')
    yesterday = '20201214'
    print(f"计算的日期是 {yesterday}")

    # 计算auc
    auc_statistics(sparkSession, yesterday)
