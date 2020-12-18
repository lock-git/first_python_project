import datetime
import os

import sys
from collections import defaultdict
import numpy as np
from pyspark import StorageLevel
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from sklearn.metrics import roc_auc_score

# from spark.mine_spark.mysql_utils import ManipulateMysql
# from spark.mine_spark.contants import JP_HS_C, JP_PT_C, JP_U_CHN_C, JP_P_CHN_C, JP_DB_C, AUC_OFFLINE_TABLE

# os.environ['JAVA_HOME'] = "D:\Java_development_tools\JDK"
# sys.path.append("D:\Java_development_tools\JDK\bin")
#
# os.environ['SPARK_HOME'] = "E:\Code\spark-2.1.1-bin-hadoop2.7"
# sys.path.append("E:\Code\spark-2.1.1-bin-hadoop2.7\python")
# sys.path.append("E:\Code\spark-2.1.1-bin-hadoop2.7\python\pyspark")
#
# os.environ['PYTHON_HOME'] = "D:\software\\anaconda\envs\pyspark_env_3.6"
# sys.path.append("D:\Java_development_tools\python3.6.8\python.exe")

platform_list = ['0', '1']
content_type_list = ['1', '2']
city_level_list = ['1', '2', '3']
context_list = ['0', '1', '2', '3', '4', '5', '6', '7', '-1', 'A', 'B', 'C', 'D', 'E', 'N', 'T']
group_all_dict = {
    'd_platform': platform_list,
    'd_contenttype': content_type_list,
    'd_citylevel': city_level_list,
    'e_context': context_list}

# mysql_jdbc = ManipulateMysql(JP_HS_C, JP_PT_C, JP_U_CHN_C, JP_P_CHN_C, JP_DB_C)
url = "jdbc:mysql://10.10.11.126:3306/jdd_portrait?useUnicode=true&characterEncoding=utf8&useSSL=false&autoReconnect=true&serverTimezone=CST"
properties = {"driver": "com.mysql.cj.jdbc.Driver", "user": "jdd_portrait_rw", "password": "z7tw_Ao3"}


def auc_statistics(sparkSession, statistics_day):
    """statistics auc"""

    global filter_auc_value
    base_data_sql = f"""SELECT deviceid,action_type,d_platform,d_contenttype,
    d_citylevel,e_context,e_ctime,d_activate_utilnow,
    cast(predict_click_score AS DOUBLE) AS click_score,
    cast(predict_exposure_score AS DOUBLE) AS exposure_score
    FROM  bigdata_mtm.motor_rank_model_offline_feature
    WHERE p_appkey='moto' AND  p_day='{statistics_day}'"""
    print(f"base_data_sql ===> {base_data_sql}")

    base_data_df = sparkSession.sql(base_data_sql).persist(StorageLevel.MEMORY_ONLY_SER)
    base_data_df.printSchema()
    base_data_df.createOrReplaceTempView("t_base_auc_tmp")

    # global filter_date_rdd
    # base_data_df = sparkSession.read \
    #     .option("inferschema", "true") \
    #     .option("header", "true") \
    #     .option("encoding", "gbk") \
    #     .csv("C:\\Users\JDD\Desktop\\auc_base_data.csv")
    # base_data_df.createOrReplaceTempView("t_base_auc_tmp")
    base_data_df.show(10)

    # 计算模型auc
    all_auc_df = base_data_df.select("action_type", "click_score")
    all_auc_row = all_auc_df.collect()

    label_list = []
    score_list = []
    for two_score in all_auc_row:
        label_list.append(int(two_score[0]))
        score_list.append(float(two_score[1]))

    try:
        all_auc_value = roc_auc_score(np.array(label_list), np.array(score_list))
    except Exception as e:
        print(f"statistics auc stage exception ==> {e}")

    print(f"模型 all_auc_value ===> {all_auc_value}")

    all_into_auc_df = sparkSession.createDataFrame([(statistics_day, 'all', '1', 0, '%.6f' % float(all_auc_value))],["s_pday", "s_feature", "s_group", "n_auc_flag", "n_value"])
    all_into_auc_df.write.jdbc(url=url, mode="append", table="motor_model_auc_offline_monitor", properties=properties)

    label_list.clear()
    score_list.clear()
    all_auc_row.clear()

    # 分组 AUC（组名：platform, contentType, citylevel, context）
    for feature_key in group_all_dict.keys():
        feature_list = group_all_dict.get(feature_key)
        for feature in feature_list:
            filter_date_df1 = base_data_df.select(feature_key, "action_type", "click_score")
            try:
                filter_date_rdd = filter_date_df1.rdd.filter(
                    lambda r: str(r[0]) == feature)
            except Exception as e:
                print(f"filter stage exception ==> {e}")

            # 判断一下，filter之后数据是否为空
            if filter_date_rdd.isEmpty():
                print(f"{feature_key} == {feature} 模型 filter_auc_value ===> #为空值#")
                filter_into_auc_df = sparkSession.createDataFrame([(statistics_day, feature_key, feature, 0, 0)],["s_pday", "s_feature", "s_group", "n_auc_flag","n_value"])
                filter_into_auc_df.write.jdbc(url=url, mode="append", table="motor_model_auc_offline_monitor",properties=properties)
            else:
                try:
                    filter_date_rdd.toDF().show(10)
                    filter_auc_df = filter_date_rdd.toDF().select("action_type", "click_score")
                    filter_auc_row = filter_auc_df.collect()

                    filter_label_list = []
                    filter_score_list = []
                    for two_score in filter_auc_row:
                        try:
                            filter_label_list.append(int(two_score[0]))
                            filter_score_list.append(float(two_score[1]))
                        except Exception as e:
                            print(f"statistics 数据转化 116  exception ==> {e} label==》 {two_score[0]} score==》{two_score[1]}")

                    print(f" 准备计算auc --》 120")
                    try:
                        filter_auc_value = roc_auc_score(np.array(filter_label_list), np.array(filter_score_list))
                    except Exception as e:
                        print(f"statistics auc stage exception ==> {e}")

                    print(f"{feature_key} == {feature} 模型 准备写入mysql filter_auc_value ===> {filter_auc_value}")

                    # 保存好 auc 的数据[先删后插]
                    filter_into2_auc_df = sparkSession.createDataFrame([(statistics_day, feature_key, feature, 0, '%.6f' % float(filter_auc_value))],["s_pday", "s_feature", "s_group", "n_auc_flag", "n_value"])
                    filter_into2_auc_df.write.jdbc(url=url, mode="append", table="motor_model_auc_offline_monitor", properties=properties)
                    print(f"{feature_key} == {feature} 写入mysql成功 模型 filter_auc_value ===> {filter_auc_value}")

                    # 保存好 auc 的数据以后，清空list
                    filter_auc_row.clear()
                    filter_label_list.clear()
                    filter_score_list.clear()
                except Exception as e:
                    print(f"filter stage exception 136 ==> {e}")

    # ctime（文章发布距今时间，需分桶）
    # activeUntilNow（用户激活距今时间，需分桶））


def cal_group_auc(labels, preds, user_id_list):
    """Calculate group auc"""

    print('*' * 50)
    if len(user_id_list) != len(labels):
        raise ValueError(
            "impression id num should equal to the sample num," \
            "impression id num is {0}".format(len(user_id_list)))
    group_score = defaultdict(lambda: [])
    group_truth = defaultdict(lambda: [])
    for idx, truth in enumerate(labels):
        user_id = user_id_list[idx]
        score = preds[idx]
        truth = labels[idx]
        group_score[user_id].append(score)
        group_truth[user_id].append(truth)

    group_flag = defaultdict(lambda: False)
    for user_id in set(user_id_list):
        truths = group_truth[user_id]
        flag = False
        for i in range(len(truths) - 1):
            if truths[i] != truths[i + 1]:
                flag = True
                break
        group_flag[user_id] = flag

    impression_total = 0
    total_auc = 0
    #
    for user_id in group_flag:
        if group_flag[user_id]:
            auc = roc_auc_score(np.asarray(group_truth[user_id]), np.asarray(group_score[user_id]))
            total_auc += auc * len(group_truth[user_id])
            impression_total += len(group_truth[user_id])
    group_auc = float(total_auc) / impression_total
    group_auc = round(group_auc, 4)
    return group_auc



if __name__ == "__main__":
    sparkSession = SparkSession.builder \
        .appName("FlowModelAUC") \
        .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
        .config("hive.metastore.uris", "thrift://node001.cdh.jdd.com:9083") \
        .config("spark.dynamicAllocation.enabled", "false") \
        .config("spark.debug.maxToStringFields", "10000") \
        .config("spark.sql.adaptive.enabled", "true") \
        .config("spark.sql.adaptive.minNumPostShufflePartitions", "50") \
        .config("spark.sql.adaptive.maxNumPostShufflePartitions", "500") \
        .config("spark.sql.adaptive.shuffle.targetPostShuffleInputSize", "67108864") \
        .config("spark.sql.autoBroadcastJoinThreshold", "200485760") \
        .config("spark.sql.broadcastTimeout", 1200) \
        .config("spark.locality.wait", "6") \
        .config("spark.shuffle.file.buffer", "64") \
        .config("spark.reducer.maxSizeInFlight", "96") \
        .config("spark.shuffle.sort.bypassMergeThreshold", "400") \
        .config("hive.exec.dynamic.partition.mode", "nonstrict") \
        .config("hive.exec.dynamic.partition", "true") \
        .config("hive.exec.max.dynamic.partitions", "100000") \
        .config("hive.exec.max.dynamic.partitions.pernode", "10000") \
        .config("hive.exec.max.dynamic.partitions.pernode.Maximum", "10000") \
        .config("hive.exec.max.created.files", "100000") \
        .enableHiveSupport().getOrCreate()

    # sparkSession = SparkSession.builder \
    #     .master("local") \
    #     .appName("FlowModelAUC") \
    #     .config("spark.some.config.option", "some-value") \
    #     .getOrCreate()

    sparkSession.sparkContext.setLogLevel("ERROR")



    # 获取昨天的数据
    # yesterday = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y%m%d')
    yesterday = '20201214'
    print(f"计算的日期是 {yesterday}")

    # 计算auc
    auc_statistics(sparkSession, yesterday)
