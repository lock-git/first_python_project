import datetime
import os

import sys
import json
from collections import defaultdict
from pyspark.sql import SparkSession
from pyspark.sql.functions import *


# 分组
from pyspark.mine_spark.mysql_utils import ManipulateMysql

group_all_dict = {'d_platform': ['0', '1'],
                  'd_contenttype': ['1', '2'],
                  'd_citylevel': ['1', '2', '3'],
                  'e_context': ['-1', '1', '2', '3', '4', '5', 'A', 'B', 'C', 'D', 'N', 'T']}

# 分桶
bucket_dict = {"d_activate_utilnow": [1, 7, 15, 30, 45],
               "e_ctime": [604800, 1296000, 2592000, 5184000]}

url = "jdbc:mysql://10.10.11.126:3306/jdd_portrait?useUnicode=true&characterEncoding=utf8&useSSL=false&autoReconnect" \
      "=true&serverTimezone=CST "
properties = {"driver": "com.mysql.cj.jdbc.Driver", "user": "jdd_portrait_rw", "password": "z7tw_Ao3"}
m_table_pay = "motor_model_auc_offline_monitor"
m_table_hour = "motor_model_auc_online_monitor"

mysqlObj = ManipulateMysql("10.10.11.126", 3306, "jdd_portrait_rw", "z7tw_Ao3", "jdd_portrait")


def auc_hourly_statistics(sparkSession, statistics_day, hour):
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
                  WHERE p_day='{statistics_day.replace("-", "")}'
                    AND p_hour='{hour}'
                    AND p_appkey='moto' ) AS a
               INNER JOIN
                 (SELECT deviceid,
                         action_type,
                         itemid,
                         batchtime,
                         begintime
                  FROM bigdata_mtm.motor_recommend_deviceid_item_median_info
                  WHERE p_day='{statistics_day.replace("-", "")}'
                    AND action_type IN(1,0)
                    AND item_type=0
                    AND batchtime!=0) AS b ON a.deviceid=b.deviceid
               AND a.essayid=b.itemid
               AND a.begintime=cast(b.batchtime AS string)) AS m
            WHERE rk = 1
    """
    print(f"base_data_hour_sql ===> {base_data_hour_sql} \n")

    base_data_hour_df = sparkSession.sql(base_data_hour_sql)

    if base_data_hour_df.rdd.isEmpty():
        mysqlObj.deleteDataFromDatabase(
            "delete from jdd_portrait_user_group_portrait_result_test where s_sub_category = '注册日期距今'")
        print("删除成功")
    else:
        mysqlObj.deleteDataFromDatabase(
            "delete from jdd_portrait_user_group_portrait_result_test where s_sub_category = '注册日期距今'")
        print("删除成功")
        base_data_hour_df.repartition(1)
    return


if __name__ == "__main__":

    sparkSession = SparkSession.builder \
        .appName("ModuleInstall") \
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

    if len(sys.argv) == 2 and str(sys.argv[1]) == "1":
        today = (datetime.datetime.now() + datetime.timedelta(hours=-2)).strftime('%Y-%m-%d')
        hour = (datetime.datetime.now() + datetime.timedelta(hours=-2)).strftime('%H')
        print(f"[hour H-1] statistics day is  {today}  hour is {hour}\n")
        auc_hourly_statistics(sparkSession, today, hour)
