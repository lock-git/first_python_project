import datetime
import os

import sys
import json
from collections import defaultdict
import numpy as np
from pyspark import StorageLevel
from pyspark.sql import SparkSession
from sklearn.metrics import roc_auc_score


platform_list = ['0', '1']
content_type_list = ['1', '2']
city_level_list = ['1', '2', '3']
context_list = ['0', '1', '2', '3', '4', '5', '6', '7', '-1', 'A', 'B', 'C', 'D', 'E', 'N', 'T']
group_all_dict = {'d_platform': platform_list,'d_contenttype': content_type_list,'d_citylevel': city_level_list,'e_context': context_list}

url = "jdbc:mysql://10.10.11.126:3306/jdd_portrait?useUnicode=true&characterEncoding=utf8&useSSL=false&autoReconnect=true&serverTimezone=CST"
properties = {"driver": "com.mysql.cj.jdbc.Driver", "user": "jdd_portrait_rw", "password": "z7tw_Ao3"}
m_table_pay = "motor_model_auc_offline_monitor"
m_table_hour = "motor_model_auc_online_monitor"

def auc_hourly_statistics(sparkSession, statistics_day,hour):
    """Calculate hourly auc"""

    base_data_hour_sql = f"""
            SELECT deviceid,
                   essayid,
                   action_type,
                   probability AS score_fix
            FROM
              (SELECT a.deviceid,
                      a.essayid,
                      b.batchtime,
                      b.action_type,
                      a.probability,
                      row_number() over(PARTITION BY a.deviceid,a.essayid
                                        ORDER BY b.action_type DESC,b.batchtime DESC) AS rk
               FROM
                 ( SELECT deviceid,
                          essayid,
                          begintime,
                          probability
                  FROM bigdata_mtm.motor_model_online_feature
                  WHERE p_day='{statistics_day}'
                    AND p_hour='{hour}'
                    AND p_appkey='moto' ) AS a
               INNER JOIN
                 (SELECT deviceid,
                         action_type,
                         itemid,
                         batchtime,
                         begintime
                  FROM bigdata_mtm.motor_recommend_deviceid_item_median_info
                  WHERE p_day='{statistics_day}'
                    AND action_type IN(1,0)
                    AND item_type=0
                    AND batchtime!=0) AS b ON a.deviceid=b.deviceid
               AND a.essayid=b.itemid
               AND a.begintime=cast(b.batchtime AS string)) AS m
            WHERE rk = 1
    """
    print(f"base_data_hour_sql ===> {base_data_hour_sql} \n")

    base_data_hour_df = sparkSession.sql(base_data_hour_sql)
    hour_df = base_data_hour_df.rdd.map(lambda t: (t[0], int(t[2]), json_trans(t[3]))).toDF(["deviceid", "action_type", "click_score"])
    hour_df.persist(StorageLevel.MEMORY_ONLY_SER)
    print(f"hour {hour} data counts is  {hour_df.count()}")
    hour_df.show(10)

    """hour_auc"""
    cal_all_auc(hour_df, statistics_day, m_table_hour, hour)

    """hour_group_auc"""
    cal_group_auc(hour_df, statistics_day, m_table_hour, hour)

def auc_statistics(sparkSession, statistics_day):
    """statistics auc"""

    base_data_sql = f"""
    SELECT deviceid,
           action_type,
           d_platform,
           d_contenttype,
           d_citylevel,
           e_context,
           e_ctime,
           d_activate_utilnow,
           cast(predict_click_score AS DOUBLE) AS click_score 
    FROM  bigdata_mtm.motor_rank_model_offline_feature
    WHERE p_appkey='moto' AND  p_day='{statistics_day}' AND deviceid not in ('','null','NULL') 
    """
    print(f"base_data_sql ===> {base_data_sql} \n")

    base_data_df = sparkSession.sql(base_data_sql).persist(StorageLevel.MEMORY_ONLY_SER)
    base_data_df.createOrReplaceTempView("t_base_auc_tmp")
    base_data_df.show(10)

    """模型 group_auc"""
    cal_group_auc(base_data_df, statistics_day, m_table_pay, "-1")

    """模型 auc"""
    cal_all_auc(base_data_df, statistics_day, m_table_pay, "-1")

    """分组 auc (platform, contentType, cityLevel, context)"""
    cal_sub_auc(base_data_df, statistics_day, m_table_pay)

    """[数据还没有?] 分桶 auc : ctime(文章发布距今时间，需分桶) activeUntilNow(用户激活距今时间，需分桶))"""
    cal_bucket_auc(base_data_df, statistics_day, m_table_pay)

def cal_sub_auc(base_data_df, statistics_day, m_table):
    """Calculate sub auc"""

    global filter_auc_value, filter_date_rdd
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
                print(f"sub_auc: {feature_key} == {feature} , filter_auc_value ===> #为空值# ")
                filter_into_auc_df = sparkSession.createDataFrame([(statistics_day, feature_key, feature, 0, 0)],
                                                                  ["s_pday", "s_feature", "s_group", "n_auc_flag","n_value"])
                filter_into_auc_df.write.jdbc(url=url, mode="append", table=f"{m_table}",
                                              properties=properties)
            else:
                filter_date_rdd.toDF().show(2)
                filter_auc_df = filter_date_rdd.toDF().select("action_type", "click_score")
                filter_auc_row = filter_auc_df.collect()

                filter_label_list = []
                filter_score_list = []
                for two_score in filter_auc_row:
                    filter_label_list.append(int(two_score[0]))
                    filter_score_list.append(float(two_score[1]))

                try:
                    filter_auc_value = roc_auc_score(np.array(filter_label_list), np.array(filter_score_list))
                except Exception as e:
                    print(f"statistics auc stage exception ==> {e}")

                # 保存
                filter_into2_auc_df = sparkSession.createDataFrame(
                    [(statistics_day, feature_key, feature, 0, '%.6f' % float(filter_auc_value))],
                    ["s_pday", "s_feature", "s_group", "n_auc_flag", "n_value"])
                filter_into2_auc_df.write.jdbc(url=url, mode="append", table=f"{m_table}",
                                               properties=properties)
                print(f"sub_auv : {feature_key} -- {feature}  to mysql success , filter_auc_value = {filter_auc_value} ")

                # 清空list
                filter_auc_row.clear()
                filter_label_list.clear()
                filter_score_list.clear()

def cal_all_auc(base_data_df, statistics_day, m_table, hour_flag):
    """Calculate all device auc"""

    global all_auc_value
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
        print(f"statistics all auc stage exception ==> {e}")

    print(f"all_auc_value:  {all_auc_value} \n")

    if str(hour_flag) == "-1":
        all_into_auc_df = sparkSession.createDataFrame([(statistics_day, 'all', '1', 0, '%.6f' % float(all_auc_value))],
                                                       ["s_pday", "s_feature", "s_group", "n_auc_flag", "n_value"])
        all_into_auc_df.write.jdbc(url=url, mode="append", table=f"{m_table}", properties=properties)
    else:
        all_into_auc_df = sparkSession.createDataFrame([(statistics_day, str(hour_flag), 0, '%.6f' % float(all_auc_value))],
                                                       ["s_pday", "s_hour", "n_auc_flag", "n_value"])
        all_into_auc_df.write.jdbc(url=url, mode="append", table=f"{m_table}", properties=properties)

    # 清空
    label_list.clear()
    score_list.clear()
    all_auc_row.clear()

def cal_group_auc(base_data_df, statistics_day, m_table, hour_flag):
    """Calculate group auc"""

    device_row = base_data_df.select("deviceid", "action_type", "click_score").collect()
    device_label_score_dict = defaultdict(lambda: [])

    for t in device_row:
        device_label_score_dict[t[0]].append((int(t[1]), float(t[2])))

    # 标记用户
    filter_device_flag_dict = defaultdict(lambda: False)
    for k1 in device_label_score_dict.keys():
        vv = device_label_score_dict.get(k1)
        flag = False
        for i in range(len(vv) - 1):
            if vv[i][0] != vv[i + 1][0]:
                flag = True
                break
        filter_device_flag_dict[k1] = flag

    impression_total = 0
    total_auc = 0
    total_device = 0
    for k in device_label_score_dict.keys():
        if filter_device_flag_dict.get(k):
            total_device += 1
            v = device_label_score_dict.get(k)
            label_list = []
            score_list = []
            for label_score in v:
                label_list.append(label_score[0])
                score_list.append(label_score[1])
            auc = roc_auc_score(np.asarray(label_list), np.asarray(score_list))
            total_auc += auc * len(v)
            impression_total += len(v)
            label_list.clear()
            score_list.clear()

    group_auc = float(total_auc) / float(impression_total)
    group_auc = '%.6f' % group_auc
    print(f"group_auc: device_total = {len(device_label_score_dict)} ,device_cal = {total_device} ,total_auc = {total_auc} ,impression_total = {impression_total} ,gauc = {group_auc} \n")

    # 保存好 g_auc 的数据
    if str(hour_flag) == "-1":
        group_auc_df = sparkSession.createDataFrame([(statistics_day, 'all', 1, 1, group_auc)],
                                                    ["s_pday", "s_feature", "s_group", "n_auc_flag", "n_value"])
        group_auc_df.write.jdbc(url=url, mode="append", table=f"{m_table}", properties=properties)
    else:
        all_into_auc_df = sparkSession.createDataFrame([(statistics_day, str(hour_flag), 1, group_auc)],
                                                       ["s_pday", "s_hour", "n_auc_flag", "n_value"])
        all_into_auc_df.write.jdbc(url=url, mode="append", table=f"{m_table}", properties=properties)

    # 清空
    device_label_score_dict.clear()
    filter_device_flag_dict.clear()
    device_row.clear()

def cal_bucket_auc(base_data_df, statistics_day, m_table):
    """Calculate bucket auc"""

    return 0

def json_trans(json_str):
    """json_str transform """

    if len(json_str) == 0 or json_str.strip() == '':
        return float(0.0)
    else:
        j_obj = json.loads(json_str)
        return float(j_obj["values"][1])

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
    sparkSession.sparkContext.setLogLevel("ERROR")

    """ 0 == [T-1] auc/g_auc  , 1 == [H-1] auc/g_auc """

    if len(sys.argv) == 2 and str(sys.argv[1]) == "0":
        # yesterday = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y%m%d')
        yesterday = '20201214'
        print(f"[day T-1] statistics day is  {yesterday} \n")
        auc_statistics(sparkSession, yesterday)

    elif len(sys.argv) == 2 and str(sys.argv[1]) == "1":
        today = (datetime.datetime.now()).strftime('%Y%m%d')
        hour = (datetime.datetime.now() + datetime.timedelta(hours=-1)).strftime('%H')
        print(f"[hour H-1] statistics day is  {today}  hour is {hour}\n")
        auc_hourly_statistics(sparkSession, today, hour)