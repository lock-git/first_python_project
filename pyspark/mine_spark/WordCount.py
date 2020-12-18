import os
import random
import sys
import math
import pandas as pd
import numpy as np
import datetime

from scipy import stats

from pyspark.sql.types import StructType, StructField, StringType
from sklearn import metrics
from sklearn.cluster import DBSCAN, KMeans
from pyspark import Row
from pyspark.sql import SparkSession

os.environ['JAVA_HOME'] = "D:\Java_development_tools\JDK"
sys.path.append("D:\Java_development_tools\JDK\bin")

os.environ['SPARK_HOME'] = "E:\Code\spark-2.1.1-bin-hadoop2.7"
sys.path.append("E:\Code\spark-2.1.1-bin-hadoop2.7\python")
sys.path.append("E:\Code\spark-2.1.1-bin-hadoop2.7\python\pyspark")

os.environ['PYTHON_HOME'] = "D:\software\\anaconda\envs\pyspark_env_3.6"
sys.path.append("D:\Java_development_tools\python3.6.8\python.exe")

LOGIN_DRUCTION = 1000 * 60 * 5

#    #!/bin/sh
#    spark2-submit \
#    --master yarn \
#    --deploy-mode cluster \
#    --driver-memory 48g \
#    --executor-memory 16g \
#    --executor-cores 2 \
#    --num-executors 30 \
#    --queue bigdata_jdd \
#    --proxy-user hdfs \
#    --archives python_spark_env_3.6.zip#python_spark_env \
#    --conf spark.yarn.appMasterEnv.PYSPARK_PYTHON=python_spark_env/python_spark_env_3.6/bin/python \
#    --conf spark.executorEnv.PYSPARK_PYTHON=python_spark_env/python_spark_env_3.6/bin/python \
#    --jars mysql-connector-java-6.0.2.jar \
#    userBehavior.py $1 $2 $3 $4

'''
计算登录次数
'''


def calcLoginTimes(uid_group):
    uid = uid_group[0]
    # group = set(uid_group[1])
    group = sorted(set(uid_group[1]), key=lambda x: x[1])

    eventid_list = []
    begintime_list = []
    times_list = []
    result_array = []
    login_count = 0
    for v in group:
        eventid_list.append(v[0])
        begintime_list.append(v[1])
        times_list.append(v[2])

    for duration in times_list:
        i = times_list.index(duration)
        if (duration < LOGIN_DRUCTION):
            result_array.append((uid, eventid_list[i], begintime_list[i], login_count))
        else:
            result_array.append((uid, eventid_list[i], begintime_list[i], login_count))
            login_count = login_count + 1
    return (result_array)


'''
计算流转矩阵
'''


def calcFlowMatrix(uid_group, feature_eventid_list):
    uid = uid_group[0]
    group = uid_group[1]

    eventid_list = []
    for v in group:
        eventid_list.append(v)

    tmp_eventid_list = []
    tmp_eventid_list.append(eventid_list[0])

    # 相邻重复数据去重复
    for i in range(len(eventid_list) - 1):
        v = eventid_list[i + 1]
        if (tmp_eventid_list[len(tmp_eventid_list) - 1] != v):
            tmp_eventid_list.append(v)

    # 过滤不用做特征的eventid
    feature_list = []
    for v in tmp_eventid_list:
        if (v in feature_eventid_list):
            feature_list.append(v)

    # feature_index_list = []
    #
    # for v in feature_list:
    #     feature_index_list.append(1)
    #
    # feature_zip_list = list(zip(feature_list,feature_index_list))
    # eventid_dict = {}
    # for f in feature_zip_list:
    #     k = f[0]
    #     v = f[1]
    #     if (k in eventid_dict):
    #         n = eventid_dict[k]
    #         c = n + v
    #         eventid_dict[k] = c
    #     else:
    #         eventid_dict[k] = v
    # feature_length = len(feature_list)
    #
    # for k,v in eventid_dict.items():
    #     if (v / feature_length < 0.05):
    #         feature_list.remove(k)
    feature_list_length = len(feature_list)

    size = len(feature_eventid_list)
    matrix = np.zeros((size, size))
    for i in range(len(feature_list) - 1):
        eventid_1 = feature_list[i]
        eventid_2 = feature_list[i + 1]

        eventid_1_index = feature_eventid_list.index(eventid_1)
        eventid_2_index = feature_eventid_list.index(eventid_2)

        count = matrix[eventid_1_index][eventid_2_index]
        matrix[eventid_1_index][eventid_2_index] = count + 1
    sum = matrix.sum()

    for a in range(len(matrix)):
        for b in range(len(matrix)):
            if (matrix[a][b] / sum < 0.05):
                matrix[a][b] = 0
    return (uid, (matrix, feature_list))


'''
计算概率矩阵
'''


def calcProbabilityMatrix(data):
    uid = data[0]
    matrix = np.mat(data[1])
    probability_list = []
    rowSum = matrix.sum(axis=1).getA1()
    array = data[1]
    # array = matrix.getA

    for i in range(len(array)):
        l1 = []
        if (rowSum[i] == 0):
            for n in range(len(array[i])):
                l1.append(0.0)
        else:
            for n in range(len(array[i])):
                l1.append(array[i][n] / rowSum[i])
        probability_list.append(l1)

    return (uid, np.array(probability_list))


'''
矩阵膨胀后标准化操作
'''


def standardized(data):
    uid = data[0]
    matrix = np.mat(data[1])
    probability_list = []
    rowSum = matrix.sum(axis=1).getA1()
    array = data[1]
    # array = matrix.getA

    for i in range(len(array)):
        l1 = []
        if (rowSum[i] == 0):
            for n in range(len(array[i])):
                l1.append(0.0)
        else:
            for n in range(len(array[i])):
                l1.append(array[i][n] / rowSum[i])
        probability_list.append(l1)
    return (uid, np.array(probability_list))


def Dbscan_Cluster(uid_list, distance_matrix, para_one, para_two):
    cluster = DBSCAN(eps=para_one, min_samples=para_two, metric='precomputed')
    cluster.fit(distance_matrix)
    labels = cluster.labels_
    labels_df = pd.DataFrame(labels, index=uid_list, columns=['label'])
    return labels_df


'''
计算相似度矩阵
'''


def calcSimilarityMatrix(uid_list, data):
    uid_1 = data[0][0]
    uid_2 = data[1][0]

    m1 = data[0][1]
    m2 = data[1][1]

    kl = stats.entropy((m1 + 0.1), (m2 + 0.1)).sum()
    kl_reverse = stats.entropy((m2 + 0.1), (m1 + 0.1)).sum()
    js_distance = (kl + kl_reverse) / 2

    uid_1_index = uidList.index(uid_1)
    uid_2_index = uidList.index(uid_2)
    # if (uid_1 == 310207 and uid_2 == 604546 ):
    #     print("js_distance:"+js_distance)

    return (uid_1_index, uid_2_index, js_distance)


'''
模型参数选择
'''


def parameterSelection(uid_list, sim_df, esp_list, min_sample_list, noise_ratio_filter, cluster_ratio_filter):
    diag = np.eye(len(sim_df), k=0)
    distance_matrix = (sim_df + 0.0001) - diag
    para_one_list = []
    para_two_list = []
    evaluation_list = []
    for para_one in esp_list:
        for para_two in min_sample_list:
            evaluation = []
            cluster = DBSCAN(eps=para_one, min_samples=para_two, metric='precomputed')
            cluster.fit(distance_matrix)
            labels = cluster.labels_
            labels_df = pd.DataFrame(labels, index=uid_list)
            label_counts = labels_df[0].value_counts().reset_index()
            #            print(label_counts)
            cluster_number = len(label_counts)
            noise_ratio = int(label_counts[label_counts['index'] == -1][0]) / (label_counts[0].sum())
            label_counts_without_noise = label_counts[label_counts['index'] != -1].reset_index()
            if cluster_number <= 11:
                cluster_ratio = 1
            else:
                cluster_ratio = (label_counts_without_noise[0][:int(len(label_counts_without_noise) / 3)].sum()) / (
                    label_counts_without_noise[0].sum())
            score = metrics.silhouette_score(sim_df, labels, metric="precomputed")
            para_one_list.append(para_one)
            para_two_list.append(para_two)
            evaluation.append(cluster_number)
            evaluation.append(noise_ratio)
            evaluation.append(cluster_ratio)
            evaluation.append(score)
            evaluation_list.append(evaluation)
    evaluation_df = pd.DataFrame(evaluation_list, index=[para_one_list, para_two_list],
                                 columns=['cluster_number', 'noise_ratio', 'cluster_ratio', 'score'])
    print(evaluation_df)

    # 按顺序筛选参数
    filter0_score = evaluation_df[evaluation_df['score'] > -0.1]
    filter1_cluster_number = filter0_score[filter0_score['cluster_number'] < (50 * math.log(len(distance_matrix), 50))]
    filter2_noise_ratio = filter1_cluster_number[filter1_cluster_number['noise_ratio'] <= noise_ratio_filter]
    filter3_cluster_ratio = filter2_noise_ratio[filter2_noise_ratio['cluster_ratio'] > cluster_ratio_filter]
    if len(filter1_cluster_number) == 0 or len(filter0_score) == 0:
        raise Exception('Cluster failure: this dataset is too decentralized to cluster!')
    else:
        if len(filter2_noise_ratio) == 0:
            best_parameter = filter1_cluster_number['noise_ratio'].idxmin()
        else:
            if len(filter3_cluster_ratio) == 0:
                best_parameter = filter2_noise_ratio['score'].idxmax()
            else:
                best_parameter = filter3_cluster_ratio['score'].idxmax()

    best_evaluation = evaluation_df.loc[best_parameter]
    print(best_evaluation)

    return best_evaluation

    # kmeans模型二次聚类


def Kmeans_Cluster_2nd(left_sim_df, cluster_number):
    index_2nd = left_sim_df.index.values
    clf_km = KMeans(random_state=1, precompute_distances=True, n_clusters=cluster_number)
    clf_km.fit(left_sim_df)
    labels_km = clf_km.labels_
    labels_df_2nd = pd.DataFrame(labels_km, index=index_2nd)
    return labels_df_2nd


def SecondaryClustering(uidlist, sim_matrix, best_evaluation, sim_df_2):
    label_1st_df = Dbscan_Cluster(uidlist, sim_matrix, best_evaluation.name[0], best_evaluation.name[1])
    print(label_1st_df)
    label_count_1st = label_1st_df['label'].value_counts().reset_index()
    print(label_count_1st)
    label_counts_1st_without_noise = label_count_1st[label_count_1st['index'] != -1]
    print(label_counts_1st_without_noise)
    reindex_df = pd.DataFrame(label_counts_1st_without_noise['label'].values,
                              index=label_counts_1st_without_noise['index'].values)
    print(reindex_df)
    label_df_2 = label_1st_df
    print(sim_df_2)
    print(label_df_2['label'])
    print(type(label_df_2['label'].values))
    print(label_df_2['label'].values)
    print(np.shape(label_df_2['label'].values))
    print(len(np.shape(label_df_2['label'].values)))
    if (best_evaluation.iloc[2] > 0.6):
        for index in reindex_df.index[0:3].values:
            last_score = metrics.silhouette_score(sim_matrix, label_df_2['label'].values, metric="precomputed")
            label_for_2nd = index
            label_number_for_2nd = reindex_df.loc[index, 0]
            user_bool_for_2nd = label_1st_df['label'] == label_for_2nd
            sim_for_2nd = sim_df_2.loc[user_bool_for_2nd, user_bool_for_2nd]
            max_distance_for_2nd = sim_for_2nd.max().max()
            cluster_number_for_2nd = int(round(max_distance_for_2nd / 0.5))
            print("------------------------------")
            print(last_score)
            print(label_number_for_2nd)
            print(cluster_number_for_2nd)
            print("--------------------------------")
            if last_score < -0.1:
                cluster_number_for_2nd = cluster_number_for_2nd + int(round(0.5 * (max_distance_for_2nd / 0.5)))
            #            print(cluster_number_for_2nd)
            if (last_score < 0.05) and (label_number_for_2nd > 50) and (cluster_number_for_2nd > 1):
                #                print(new_label.loc[label_df[0] ==label_for_2nd, 0])
                label_2nd_df = Kmeans_Cluster_2nd(sim_for_2nd, cluster_number_for_2nd)
                renamed_label_2nd_df = label_2nd_df * 0.001 + label_for_2nd
                new_label = label_df_2.copy()
                new_label.loc[label_df_2['label'] == label_for_2nd, 'label'] = renamed_label_2nd_df[0]
                label_df_2 = new_label
            #                print('second cluster is performed on label ', label_for_2nd)
            #                print('cluster number of the second cluster is ', cluster_number_for_2nd)
            if last_score >= 0.05:
                break

    last_score = metrics.silhouette_score(sim_matrix, label_df_2['label'].values, metric="precomputed")
    print('cluster number = ', len(label_df_2['label'].value_counts()))
    print('noise ratio = ', best_evaluation.iloc[1])
    print('cluster score = ', last_score)
    print('the cluster score is ', last_score)
    print(label_df_2['label'].value_counts())
    return label_df_2


def MatrixAssignment(data, uidList):
    sim_matrix_data = np.zeros((len(uidList), len(uidList)))
    sim_matrix_data[data[0]][data[1]] = data[2]
    return sim_matrix_data


if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("userBehavior") \
        .enableHiveSupport() \
        .config("spark.sql.warehouse.dir", "/user/hive/warehouse") \
        .config("hive.metastore.uris", "thrift://node001.cdh.jdd.com:9083") \
        .config("spark.driver.maxResultSize", "16g") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    eventRatio = 0.05
    loginTime = 0

    appkey = sys.argv[1]
    version = sys.argv[2]
    plateform = sys.argv[3]
    pday = sys.argv[4]

    # readcsvpath = os.path.join("F:\\", 'test_1203.csv')
    # df = spark.read.csv(readcsvpath, header=True)
    sql = "SELECT uid,eventid,begintime FROM dw_app.facet_logs WHERE p_appkey = '" + appkey + "' and version = '" + version + "' and plateform = '" + plateform + "' and p_day = '" + pday + "' and eventid like 'P%' and uid !=0 ORDER BY begintime ASC"
    print(sql)
    df = spark.sql(sql)
    df.show()
    # df.where('uid = 1439816').show(1000)
    df.createOrReplaceTempView('tmp_data_view')

    # df = spark.sql("SELECT uid,eventid,begintime FROM dw_app.facet_logs WHERE p_appkey = 'moto' and version = '1.6.3' and plateform = 'android' and p_day = '20181126' and eventid like 'P%' and uid !=0 ORDER BY begintime ASC")

    # queryLogSql = "select uid,eventid,begintime from tmp_data_view order by begintime ASC "
    # logDF = spark.sql(queryLogSql)
    # logDF.createOrReplaceTempView("log_df_view")
    # logDF.show()

    sql = "select uid,eventid,begintime,row_number() over (PARTITION BY uid order by begintime asc) as row_num from tmp_data_view"
    df2 = spark.sql(sql)
    df2.createOrReplaceTempView("tmp_view")
    df2.show()
    # df2.where('uid = 1439816').show(1000)

    joinSql = "select " \
              " b.uid,b.eventid,b.begintime,(a.begintime - b.begintime) as tims " \
              " from tmp_view a " \
              " join tmp_view b " \
              " on a.uid = b.uid and a.row_num  = b.row_num +1 order by  begintime asc"

    joinDF = spark.sql(joinSql)
    # joinDF.createOrReplaceTempView("tmp_join_view")
    # joinDF.where('uid = 1439816').show(1000)

    rdd = joinDF.rdd.map(lambda row: (row[0], (row[1], row[2], row[3]))).groupByKey().map(
        lambda x: calcLoginTimes(x)).flatMap(lambda z: z).map(lambda v: Row(v[0], v[1], v[2], str(v[3])))
    # print(rdd.take(10))

    loginTimeDataScheame = StructType(
        [
            StructField("uid", StringType(), True),
            StructField("eventid", StringType(), True),
            StructField("begintime", StringType(), True),
            StructField("logintime", StringType(), True)
        ]
    )

    try:
        loginTimeDF = spark.createDataFrame(rdd, loginTimeDataScheame)
        loginTimeDF.show(100)
        loginOneTimeDF = loginTimeDF.where("logintime = '0'")
        print(loginOneTimeDF.count())
        # loginTimeDF.orderBy('logintime').where('uid = 1439816 ').show(100)
        # loginOneTimeDF.where('uid = 1439816 ').show(100)
    except Exception as e:
        print(e)

    loginOneTimeDF.createOrReplaceTempView("tmp_login_view")
    loginTimeOneDF = spark.sql("select T.uid uid,count(uid) cou from tmp_login_view T group by T.uid having cou > 2")
    try:
        print(loginTimeOneDF.count())
        loginTimeOneDF.show()
        # loginTimeOneDF.where('uid = 1439816').show()
    except Exception as e:
        print(e)

    resDF = loginTimeOneDF.join(loginOneTimeDF, 'uid', "left")
    print(resDF.count())

    # resDF.show()
    resDF.createOrReplaceTempView("tmp_res_view")
    # resDF.where("uid = 1439816").show(1000)

    try:
        allUserCount = resDF.groupBy("uid").count().count()
    except Exception as e:
        print(e)

    # print(allUserCount)

    eventDF = spark.sql("select eventid,count(distinct (uid)) con from tmp_res_view group by eventid")
    eventDF.show(100)

    print(allUserCount)
    print(eventRatio)
    # ff = eventDF.rdd.map(lambda x: (x[0], x[1] / allUserCount)).filter(
    #         lambda z: z[1] > eventRatio)
    # ff.take(100)

    try:
        feature_eventid_list = eventDF.rdd.map(lambda x: (x[0], x[1] / allUserCount)).filter(
            lambda z: z[1] > eventRatio).map(lambda a: a[0]).collect()
        print(feature_eventid_list)
    except Exception as e:
        print(e)

    # 流转矩阵
    uidFlowMatrixRDD = resDF.select("uid", "eventid").rdd.map(lambda x: (x[0], x[1])).groupByKey().map(
        lambda x: calcFlowMatrix(x, feature_eventid_list))
    try:
        print(uidFlowMatrixRDD.take(2))
    except Exception as e:
        print(e)

    # 概率矩阵
    uidProbabilityMatrixRDD = uidFlowMatrixRDD.map(lambda v: calcProbabilityMatrix((v[0], v[1][0])))
    try:
        print(uidProbabilityMatrixRDD.take(10))
    except Exception as e:
        print(e)

    # 矩阵膨胀两次
    probabilityIntensifyRDD = uidProbabilityMatrixRDD.map(lambda v: (v[0], pow(v[1], 2))).map(
        lambda a: standardized(a)).map(lambda z: (z[0], pow(z[1], 2))).map(lambda a: standardized(a))
    print(probabilityIntensifyRDD.take(10))

    uidList = probabilityIntensifyRDD.map(lambda v: v[0]).collect()
    print(uidList)
    print(len(uidList))

    featureMatrix = np.zeros((len(uidList), len(uidList)))
    Similaritymatrix = probabilityIntensifyRDD.cartesian(probabilityIntensifyRDD).map(
        lambda v: calcSimilarityMatrix(uidList, v))
    print(Similaritymatrix.take(5))
    # print(Similaritymatrix.count())

    sim_matrix = np.zeros((len(uidList), len(uidList)))

    # SimilaritymatrixRDD = Similaritymatrix.map(lambda v:MatrixAssignment(v,uidList)).reduce(lambda a,b:np.array(a)+np.array(b))

    sim_list = Similaritymatrix.collect()

    for v in sim_list:
        sim_matrix[v[0]][v[1]] = v[2]
    print(sim_matrix)
    # np.save("test",sim_matrix)

    # print(sim_matrix[i1][i2])
    esp_list = [0.2, 0.3, 0.4, 0.5, 0.6]
    min_sample_list = [2, 3, 4, 5]
    noise_ratio = 0.25
    cluster_ratio = 0.6

    best_evaluation = parameterSelection(uidList, sim_matrix, esp_list, min_sample_list, noise_ratio, cluster_ratio)

    print(best_evaluation.name[0])
    print(best_evaluation.name[1])
    label_df = Dbscan_Cluster(uidList, sim_matrix, best_evaluation.name[0], best_evaluation.name[1])
    label_df.index.name = 'uid'
    label_df = label_df.reset_index()

    print(type(label_df))
    print(label_df)

    labelsDF = spark.createDataFrame(label_df)
    labelsDF.show()
    label_resdf = labelsDF.join(resDF, 'uid', 'left')
    labelsDF.join(resDF, 'uid', 'left')
    label_resdf.show()
    # label_resdf.select("uid","label", "eventid").rdd.map(lambda x: ((x[0],x[1]), x[2])).groupByKey().map(lambda s:(s[0],list(s[1]))).repartition(1).saveAsTextFile("/user/hdfs/ML/dkq/behavior_data/uidPath")
    # uidFlowMatrixRDD.map(lambda z: (z[0], z[1][1])).repartition(1).saveAsTextFile("/user/hdfs/ML/dkq/behavior_data/uidFeatureV2")

    # for uid in uidList:
    #     each_login_page_selected = resDF.select("eventid").where("uid = "+uid)

    # 二次聚类
    sim_df_2 = pd.DataFrame(sim_matrix, index=uidList, columns=uidList)
    label_df_2 = SecondaryClustering(uidList, sim_matrix, best_evaluation, sim_df_2)
    label_df_3 = label_df_2
    label_df_2.index.name = 'uid'
    label_df_2 = label_df_2.reset_index()
    print(label_df_2)
    labelDF2 = spark.createDataFrame(label_df_2)
    labelDF2.show()
    label_2_resDF = labelDF2.join(resDF, 'uid', 'left')
    label_2_resDF.show()
    # label_2_resDF.select("uid", "label", "eventid").rdd.map(lambda x: ((x[0], x[1]), x[2])).groupByKey().map(
    #     lambda s: (s[0], list(s[1]))).repartition(1).saveAsTextFile("/user/hdfs/ML/dkq/behavior_data/uidPath")
    # uidFlowMatrixRDD.map(lambda z: (z[0], z[1][1])).repartition(1).saveAsTextFile(
    #     "/user/hdfs/ML/dkq/behavior_data/uidFeatureV2")

    # 聚类中心判断
    label_list = set(label_df_3['label'])
    center_arr = []
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for i in label_list:
        one_center = []
        label_bool = (label_df_3['label'] == i)
        label_sim_df = sim_df_2.loc[label_bool, label_bool]
        label_mean = label_sim_df.mean()
        label_max = label_sim_df.max(axis=1)
        min_distance = min(label_mean.values)
        max_distance = max(label_max.values)
        min_data = label_mean[label_mean == min_distance].reset_index()
        min_users = min_data['index']
        random_index = random.randint(0, len(min_users) - 1)
        center_user = min_users[random_index]
        one_center.append(i)
        one_center.append(len(label_sim_df))
        # one_center.append(min_distance)
        # one_center.append(max_distance)
        one_center.append(center_user)
        one_center.append(appkey)
        one_center.append(version)
        one_center.append(plateform)
        one_center.append(pday)
        one_center.append(now_time)
        center_arr.append(one_center)
    center_df_mid = pd.DataFrame(center_arr, columns=(
    'n_cluster_label_id', 'n_cluster_label_count', 'n_cluster_label_center_uid', 's_app_key', 'n_version',
    'n_plateform', 'n_calc_date', 'n_create_date'))
    print(center_df_mid)
    center_df_mid_spark = spark.createDataFrame(center_df_mid.reset_index())
    center_df_mid_spark.show(100)

    uidFlowMatrixRowRDD = uidFlowMatrixRDD.map(lambda z: Row(z[0], z[1][1]))
    uidFlowMatrixSchema = StructType(
        [
            StructField("n_cluster_label_center_uid", StringType(), True),
            StructField("n_cluster_label_center_behavior", StringType(), True),
        ]
    )
    uidFlowMatrixDF = spark.createDataFrame(uidFlowMatrixRowRDD, uidFlowMatrixSchema)
    uidFlowMatrixDF.show()

    midCenterDF = center_df_mid_spark.join(uidFlowMatrixDF, 'n_cluster_label_center_uid', 'left').select(
        'n_cluster_label_id', 'n_cluster_label_count', 'n_cluster_label_center_uid', 'n_cluster_label_center_behavior',
        'n_version', 'n_plateform', 'n_calc_date', 's_app_key', 'n_create_date')

    midCenterDF.show(100)

    url = "jdbc:mysql://10.10.11.126:3306/jdd_portrait?useUnicode=true&characterEncoding=utf8&useSSL=false&autoReconnect=true&serverTimezone=CST"
    properties = {"driver": "com.mysql.cj.jdbc.Driver", "user": "jdd_portrait_rw", "password": "z7tw_Ao3"}
    midCenterDF.write.jdbc(url=url, mode="append", table="jdd_portrait_behavior_cluster_center", properties=properties)