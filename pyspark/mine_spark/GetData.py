#save data for lgb training by pyspark distribution
import datetime
import os

import sys
import json
from collections import defaultdict
import numpy as np
from pyspark import StorageLevel
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from sklearn.metrics import roc_auc_score


def getTodayDate():
    return datetime.datetime.now().strftime('%Y-%m-%d')

def getYesterdayDate():
    return (datetime.datetime.now()-datetime.timedelta(days=1)).strftime('%Y-%m-%d')

today = getTodayDate()
yesterday = getYesterdayDate()

LGM_PATH = '/home/jdduser/wangben/lightgbm_model_train'
today_LGM_PATH = os.path.join(LGM_PATH, today)

if not os.path.exists(today_LGM_PATH):
    os.mkdir(today_LGM_PATH)

def get_data_daily(sparkSession, p_day):
    """get lgb training data"""

    base_sql = f'''
            SELECT deviceid,
               essayid,
               label,
               n_activate_utilnow,
               d_st_ctime,
               d_st_titlelen,
               d_dy_histpv,
               d_dy_recvalidshow,
               d_dy_recread,
               d_dy_recclickrate,
               d_dy_finishrate,
               n_browse_price,
               u_dy_rt_poscnts,
               u_dy_rt_videoreadratio,
               d_st_playtime,
               plateform,
               province,
               city_level,
               is_rest_day,
               is_daytime,
               d_st_contenttype,
               d_st_covershowtype,
               d_st_life,
               d_dy_isexpired,
               position,
               n_context,
               d_st_tag_sjzc,
               u_dy_rt_notclickedtag_sjzc,
               u_dy_rt_readtag_sjzc,
               s_long_labels_sjzc,
               s_short_labels_sjzc,
               d_st_tag_sjcl,
               u_dy_rt_notclickedtag_sjcl,
               u_dy_rt_readtag_sjcl,
               s_long_labels_sjcl,
               s_short_labels_sjcl,
               d_st_tag_sg,
               u_dy_rt_notclickedtag_sg,
               u_dy_rt_readtag_sg,
               s_long_labels_sg,
               s_short_labels_sg,
               d_st_tag_jq,
               u_dy_rt_notclickedtag_jq,
               u_dy_rt_readtag_jq,
               s_long_labels_jq,
               s_short_labels_jq,
               d_st_tag_pc,
               u_dy_rt_notclickedtag_pc,
               u_dy_rt_readtag_pc,
               s_long_labels_pc,
               s_short_labels_pc,
               d_st_tag_tc,
               u_dy_rt_notclickedtag_tc,
               u_dy_rt_readtag_tc,
               s_long_labels_tc,
               s_short_labels_tc,
               d_st_tag_mtsh,
               u_dy_rt_notclickedtag_mtsh,
               u_dy_rt_readtag_mtsh,
               s_long_labels_mtsh,
               s_short_labels_mtsh,
               d_st_tag_mlgl,
               u_dy_rt_notclickedtag_mlgl,
               u_dy_rt_readtag_mlgl,
               s_long_labels_mlgl,
               s_short_labels_mlgl,
               d_st_tag_xc,
               u_dy_rt_notclickedtag_xc,
               u_dy_rt_readtag_xc,
               s_long_labels_xc,
               s_short_labels_xc,
               d_st_tag_ycgs,
               u_dy_rt_notclickedtag_ycgs,
               u_dy_rt_readtag_ycgs,
               s_long_labels_ycgs,
               s_short_labels_ycgs,
               d_st_tag_jm,
               u_dy_rt_notclickedtag_jm,
               u_dy_rt_readtag_jm,
               s_long_labels_jm,
               s_short_labels_jm,
               d_st_tag_kpzs,
               u_dy_rt_notclickedtag_kpzs,
               u_dy_rt_readtag_kpzs,
               s_long_labels_kpzs,
               s_short_labels_kpzs,
               d_st_tag_wxgz,
               u_dy_rt_notclickedtag_wxgz,
               u_dy_rt_readtag_wxgz,
               s_long_labels_wxgz,
               s_short_labels_wxgz,
               d_st_tag_wq,
               u_dy_rt_notclickedtag_wq,
               u_dy_rt_readtag_wq,
               s_long_labels_wq,
               s_short_labels_wq,
               d_st_tag_mn,
               u_dy_rt_notclickedtag_mn,
               u_dy_rt_readtag_mn,
               s_long_labels_mn,
               s_short_labels_mn,
               d_st_tag_zbpj,
               u_dy_rt_notclickedtag_zbpj,
               u_dy_rt_readtag_zbpj,
               s_long_labels_zbpj,
               s_short_labels_zbpj,
               d_st_tag_sp,
               u_dy_rt_notclickedtag_sp,
               u_dy_rt_readtag_sp,
               s_long_labels_sp,
               s_short_labels_sp,
               d_st_tag_ss,
               u_dy_rt_notclickedtag_ss,
               u_dy_rt_readtag_ss,
               s_long_labels_ss,
               s_short_labels_ss,
               d_st_tag_clpc,
               u_dy_rt_notclickedtag_clpc,
               u_dy_rt_readtag_clpc,
               s_long_labels_clpc,
               s_short_labels_clpc,
               d_st_tag_xcjc,
               u_dy_rt_notclickedtag_xcjc,
               u_dy_rt_readtag_xcjc,
               s_long_labels_xcjc,
               s_short_labels_xcjc,
               d_st_tag_qx,
               u_dy_rt_notclickedtag_qx,
               u_dy_rt_readtag_qx,
               s_long_labels_qx,
               s_short_labels_qx,
               d_st_tag_tag_null,
               u_dy_rt_notclickedtag_tag_null,
               u_dy_rt_readtag_tag_null,
               s_long_labels_tag_null,
               s_short_labels_tag_null,
               poscate_0,
               poscate_1,
               poscate_2,
               poscate_3,
               poscate_4,
               poscate_5,
               poscate_poscates_null,
               duration,
               d_dy_recreadtime,
               d_dy_recavgreadtime,
               p_day
            FROM bigdata_mtm.lightgbm_model_train_feature
            WHERE p_day='{p_day.replace("-", "")}'
            '''
    print(f"base_sql ====> {base_sql}")

    base_data_df = sparkSession.sql(base_sql)

    if base_data_df.rdd.isEmpty():
        print(f"{p_day}: sample count is 0 ")
        return

    base_data_df.toPandas().to_csv(os.path.join(today_LGM_PATH, 'lgb_data.csv'))


if __name__ =="__main__":
    sparkSession = SparkSession.builder \
        .appName("GetLgbData") \
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


    get_data_daily(sparkSession, yesterday)

