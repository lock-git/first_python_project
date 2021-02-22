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
from mmlspark.lightgbm import LightGBMClassifier
from pyspark.ml import feature, evaluation, Pipeline



DATE_FORMAT = '%Y-%m-%d'
def getDate(diff=0):
    return (datetime.datetime.now()-datetime.timedelta(days=diff)).strftime(DATE_FORMAT)

def get_data_daily(sparkSession, p_day):
    """get lgb training data"""

    base_sql = f'''
            SELECT deviceid,
               cast(essayid AS INT) essayid,
               cast(label AS INT) label,
               cast(n_activate_utilnow AS INT) n_activate_utilnow,
               cast(d_st_ctime as INT) d_st_ctime, 
               cast(d_st_titlelen AS INT) d_st_titlelen,
               cast(d_dy_histpv as INT) d_dy_histpv,
               cast(d_dy_recvalidshow AS INT) d_dy_recvalidshow,
               cast(d_dy_recread AS INT) d_dy_recread,
               d_dy_recclickrate,
               d_dy_finishrate,
               cast(n_browse_price AS INT) n_browse_price,
               cast(u_dy_rt_poscnts AS INT) u_dy_rt_poscnts,
               cast(u_dy_rt_videoreadratio AS INT) u_dy_rt_videoreadratio,
               d_st_playtime,
               cast(plateform AS INT) plateform,
               cast(province AS INT) province,
               cast(city_level AS INT) city_level,
               cast(is_rest_day AS INT) is_rest_day,
               cast(is_daytime AS INT) is_daytime,
               cast(d_st_contenttype AS INT) d_st_contenttype,
               cast(d_st_covershowtype AS INT) d_st_covershowtype,
               cast(d_st_life AS INT) d_st_life,
               cast(d_dy_isexpired AS INT) d_dy_isexpired,
               cast(position AS INT) position,
               cast(n_context AS INT) n_context,
               cast(d_st_tag_sjzc AS INT) d_st_tag_sjzc,
               cast(u_dy_rt_notclickedtag_sjzc AS INT) u_dy_rt_notclickedtag_sjzc,
               cast(u_dy_rt_readtag_sjzc AS INT) u_dy_rt_readtag_sjzc,
               cast(s_long_labels_sjzc AS INT) s_long_labels_sjzc,
               cast(s_short_labels_sjzc AS INT) s_short_labels_sjzc,
               cast(d_st_tag_sjcl AS INT) d_st_tag_sjcl,
               cast(u_dy_rt_notclickedtag_sjcl AS INT) u_dy_rt_notclickedtag_sjcl,
               cast(u_dy_rt_readtag_sjcl AS INT) u_dy_rt_readtag_sjcl,
               cast(s_long_labels_sjcl AS INT) s_long_labels_sjcl,
               cast(s_short_labels_sjcl AS INT) s_short_labels_sjcl,
               cast(d_st_tag_sg AS INT) d_st_tag_sg,
               cast(u_dy_rt_notclickedtag_sg AS INT) u_dy_rt_notclickedtag_sg,
               cast(u_dy_rt_readtag_sg AS INT) u_dy_rt_readtag_sg,
               cast(s_long_labels_sg AS INT) s_long_labels_sg,
               cast(s_short_labels_sg AS INT) s_short_labels_sg,
               cast(d_st_tag_jq AS INT) d_st_tag_jq,
               cast(u_dy_rt_notclickedtag_jq AS INT) u_dy_rt_notclickedtag_jq,
               cast(u_dy_rt_readtag_jq AS INT) u_dy_rt_readtag_jq,
               cast(s_long_labels_jq AS INT) s_long_labels_jq,
               cast(s_short_labels_jq AS INT) s_short_labels_jq,
               cast(d_st_tag_pc AS INT) d_st_tag_pc,
               cast(u_dy_rt_notclickedtag_pc AS INT) u_dy_rt_notclickedtag_pc,
               cast(u_dy_rt_readtag_pc AS INT) u_dy_rt_readtag_pc,
               cast(s_long_labels_pc AS INT) s_long_labels_pc,
               cast(s_short_labels_pc AS INT) s_short_labels_pc,
               cast(d_st_tag_tc AS INT) d_st_tag_tc,
               cast(u_dy_rt_notclickedtag_tc AS INT) u_dy_rt_notclickedtag_tc,
               cast(u_dy_rt_readtag_tc AS INT) u_dy_rt_readtag_tc,
               cast(s_long_labels_tc AS INT) s_long_labels_tc,
               cast(s_short_labels_tc AS INT) s_short_labels_tc,
               cast(d_st_tag_mtsh AS INT) d_st_tag_mtsh,
               cast(u_dy_rt_notclickedtag_mtsh AS INT) u_dy_rt_notclickedtag_mtsh,
               cast(u_dy_rt_readtag_mtsh AS INT) u_dy_rt_readtag_mtsh, 
               cast(s_long_labels_mtsh AS INT) s_long_labels_mtsh,
               cast(s_short_labels_mtsh AS INT) s_short_labels_mtsh,
               cast(d_st_tag_mlgl AS INT) d_st_tag_mlgl,
               cast(u_dy_rt_notclickedtag_mlgl AS INT) u_dy_rt_notclickedtag_mlgl,
               cast(u_dy_rt_readtag_mlgl AS INT) u_dy_rt_readtag_mlgl,
               cast(s_long_labels_mlgl AS INT) s_long_labels_mlgl,
               cast(s_short_labels_mlgl AS INT) s_short_labels_mlgl,
               cast(d_st_tag_xc AS INT) d_st_tag_xc,
               cast(u_dy_rt_notclickedtag_xc AS INT) u_dy_rt_notclickedtag_xc,
               cast(u_dy_rt_readtag_xc AS INT) u_dy_rt_readtag_xc,
               cast(s_long_labels_xc AS INT) s_long_labels_xc,
               cast(s_short_labels_xc AS INT) s_short_labels_xc,
               cast(d_st_tag_ycgs AS INT) d_st_tag_ycgs,
               cast(u_dy_rt_notclickedtag_ycgs AS INT) u_dy_rt_notclickedtag_ycgs,
               cast(u_dy_rt_readtag_ycgs AS INT) u_dy_rt_readtag_ycgs,
               cast(s_long_labels_ycgs AS INT) s_long_labels_ycgs,
               cast(s_short_labels_ycgs AS INT) s_short_labels_ycgs,
               cast(d_st_tag_jm AS INT) d_st_tag_jm,
               cast(u_dy_rt_notclickedtag_jm AS INT) u_dy_rt_notclickedtag_jm,
               cast(u_dy_rt_readtag_jm AS INT) u_dy_rt_readtag_jm,
               cast(s_long_labels_jm AS INT) s_long_labels_jm,
               cast(s_short_labels_jm AS INT) s_short_labels_jm,
               cast(d_st_tag_kpzs AS INT) d_st_tag_kpzs,
               cast(u_dy_rt_notclickedtag_kpzs AS INT) u_dy_rt_notclickedtag_kpzs,
               cast(u_dy_rt_readtag_kpzs AS INT) u_dy_rt_readtag_kpzs,
               cast(s_long_labels_kpzs AS INT) s_long_labels_kpzs,
               cast(s_short_labels_kpzs AS INT) s_short_labels_kpzs,
               cast(d_st_tag_wxgz AS INT) d_st_tag_wxgz,
               cast(u_dy_rt_notclickedtag_wxgz AS INT) u_dy_rt_notclickedtag_wxgz,
               cast(u_dy_rt_readtag_wxgz AS INT) u_dy_rt_readtag_wxgz,
               cast(s_long_labels_wxgz AS INT) s_long_labels_wxgz,
               cast(s_short_labels_wxgz AS INT) s_short_labels_wxgz,
               cast(d_st_tag_wq AS INT) d_st_tag_wq,
               cast(u_dy_rt_notclickedtag_wq AS INT) u_dy_rt_notclickedtag_wq,
               cast(u_dy_rt_readtag_wq AS INT) u_dy_rt_readtag_wq,
               cast(s_long_labels_wq AS INT) s_long_labels_wq,
               cast(s_short_labels_wq AS INT) s_short_labels_wq,
               cast(d_st_tag_mn AS INT) d_st_tag_mn,
               cast(u_dy_rt_notclickedtag_mn AS INT) u_dy_rt_notclickedtag_mn,
               cast(u_dy_rt_readtag_mn AS INT) u_dy_rt_readtag_mn,
               cast(s_long_labels_mn AS INT) s_long_labels_mn,
               cast(s_short_labels_mn AS INT) s_short_labels_mn,
               cast(d_st_tag_zbpj AS INT) d_st_tag_zbpj,
               cast(u_dy_rt_notclickedtag_zbpj AS INT) u_dy_rt_notclickedtag_zbpj,
               cast(u_dy_rt_readtag_zbpj AS INT) u_dy_rt_readtag_zbpj,
               cast(s_long_labels_zbpj AS INT) s_long_labels_zbpj,
               cast(s_short_labels_zbpj AS INT) s_short_labels_zbpj,
               cast(d_st_tag_sp AS INT) d_st_tag_sp,
               cast(u_dy_rt_notclickedtag_sp AS INT) u_dy_rt_notclickedtag_sp,
               cast(u_dy_rt_readtag_sp AS INT) u_dy_rt_readtag_sp,
               cast(s_long_labels_sp AS INT) s_long_labels_sp,
               cast(s_short_labels_sp AS INT) s_short_labels_sp,
               cast(d_st_tag_ss AS INT) d_st_tag_ss,
               cast(u_dy_rt_notclickedtag_ss AS INT) u_dy_rt_notclickedtag_ss,
               cast(u_dy_rt_readtag_ss AS INT) u_dy_rt_readtag_ss,
               cast(s_long_labels_ss AS INT) s_long_labels_ss,
               cast(s_short_labels_ss AS INT) s_short_labels_ss,
               cast(d_st_tag_clpc AS INT) d_st_tag_clpc,
               cast(u_dy_rt_notclickedtag_clpc AS INT) u_dy_rt_notclickedtag_clpc,
               cast(u_dy_rt_readtag_clpc AS INT) u_dy_rt_readtag_clpc,
               cast(s_long_labels_clpc AS INT) s_long_labels_clpc,
               cast(s_short_labels_clpc AS INT) s_short_labels_clpc,
               cast(d_st_tag_xcjc AS INT) d_st_tag_xcjc,
               cast(u_dy_rt_notclickedtag_xcjc AS INT) u_dy_rt_notclickedtag_xcjc,
               cast(u_dy_rt_readtag_xcjc AS INT) u_dy_rt_readtag_xcjc,
               cast(s_long_labels_xcjc AS INT) s_long_labels_xcjc,
               cast(s_short_labels_xcjc AS INT) s_short_labels_xcjc,
               cast(d_st_tag_qx AS INT) d_st_tag_qx,
               cast(u_dy_rt_notclickedtag_qx AS INT) u_dy_rt_notclickedtag_qx,
               cast(u_dy_rt_readtag_qx AS INT) u_dy_rt_readtag_qx,
               cast(s_long_labels_qx AS INT) s_long_labels_qx,
               cast(s_short_labels_qx AS INT) s_short_labels_qx,
               cast(d_st_tag_tag_null AS INT) d_st_tag_tag_null,
               cast(u_dy_rt_notclickedtag_tag_null AS INT) u_dy_rt_notclickedtag_tag_null,
               cast(u_dy_rt_readtag_tag_null AS INT) u_dy_rt_readtag_tag_null,
               cast(s_long_labels_tag_null AS INT) s_long_labels_tag_null,
               cast(s_short_labels_tag_null AS INT) s_short_labels_tag_null,
               cast(poscate_0 AS INT) poscate_0,
               cast(poscate_1 AS INT) poscate_1,
               cast(poscate_2 AS INT) poscate_2,
               cast(poscate_3 AS INT) poscate_3,
               cast(poscate_4 AS INT) poscate_4,
               cast(poscate_5 AS INT) poscate_5,
               cast(poscate_poscates_null AS INT) poscate_poscates_null,
               cast(duration AS INT) duration,
               cast(d_dy_recreadtime AS INT) d_dy_recreadtime,
               d_dy_recavgreadtime,
               p_day
            FROM bigdata_mtm.lightgbm_model_train_feature
            WHERE p_day='20210121'
            '''
    print(f"base_sql ====> {base_sql}")

    base_data_df = sparkSession.sql(base_sql)

    lgbm = LightGBMClassifier(featuresCol='features', labelCol='action_type',
                    boostingType = 'gbdt', objective = 'binary', metric={'binary_logloss', 'auc'}, maxDepth = 8, numLeaves = 128,
                    learningRate = 0.1, featureFraction = 0.8, baggingFraction = 0.8, baggingFreq = 5, maxBin = 128, verbosity = 1,
                    isUnbalance = True, baggingSeed = 50)

    featureCreater = feature.VectorAssembler(inputCols=[col for col in base_data_df.columns if col not in ["deviceid", "essayid", "duration", "p_day"]],
                                            outputCol="features")

    train, val = base_data_df.randomSplit([0.7, 0.3], seed=0)

    pipeline = Pipeline(stages=[featureCreater, lgbm])

    train_model = pipeline.fit(train)
    val_model = train_model.transform(val)

    evaluater = evaluation.BinaryClassificationEvaluator(rawPredictionCol="prediction", labelCol="action_type")
    print(evaluater.evaluate(val_model, {evaluater.metricName:"areaUnderROC"}))

    if base_data_df.rdd.isEmpty():
        print(f"{p_day}: sample count is 0 ")
        return

    base_data_df.show(10)

    base_data_df.write.csv("/user/hdfs/ML/moto/pmml/lightgbm-model")


if __name__ =="__main__":
    sparkSession = SparkSession.builder \
        .appName("GetData") \
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

    yesterday = getDate(1)

    get_data_daily(sparkSession, yesterday)
    #print(spark_df)
