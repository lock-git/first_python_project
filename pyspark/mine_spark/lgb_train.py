# 连接Hive数据库
import pandas as pd
import time
import os
import datetime
from impala.dbapi import connect
import numpy as np
import lightgbm as lgb
from pyhdfs import HdfsClient
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from collections import defaultdict

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

def getTodayDate():
    return datetime.datetime.now()

def getYesterdayDate():
    return datetime.datetime.now()-datetime.timedelta(days=1)

today = getTodayDate().strftime('%Y-%m-%d')
yesterday = getYesterdayDate().strftime('%Y%m%d')
HDFS_PATH = '/user/hdfs/ML/moto/pmml/lightgbm-model'
LGM_PATH = '/home/jdduser/wangben/lightgbm_model_train'
today_HDFS_PATH = os.path.join(HDFS_PATH, today)
today_LGM_PATH = os.path.join(LGM_PATH, today)

if not os.path.exists(today_LGM_PATH):
    os.mkdir(today_LGM_PATH)

with open(today_LGM_PATH+'/lgb_train_log.txt', 'w') as f:
    f.write(datetime.datetime.now().strftime(DATETIME_FORMAT)+' '*10+'Starting Traning Task!\n')

# f.write('processing hive data cost {} min \n'.format(round((hive_time_x - start_time) / 60, 4)))


sql = '''
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
WHERE p_day='20210121' 
'''


def impala_conn_exec(sql):
    conn = connect(host='172.16.1.112', port=21050, auth_mechanism='PLAIN', user='hdfs', password='hdfs')
    cur = conn.cursor()
    with open(today_LGM_PATH + '/lgb_train_log.txt', 'a') as f:
        f.write(datetime.datetime.now().strftime(DATETIME_FORMAT) + ' ' * 10 + 'Starting Connecting to Hive!\n')
    cur.execute(sql)
    data_list = cur.fetchall()

    return data_list
data_list = impala_conn_exec(sql)
with open(today_LGM_PATH + '/lgb_train_log.txt', 'a') as f:
    f.write(datetime.datetime.now().strftime(DATETIME_FORMAT) + ' ' * 10 + 'Sucessed to Get All Data, end connceting!\n')

with open(today_LGM_PATH + '/lgb_train_log.txt', 'a') as f:
    f.write(datetime.datetime.now().strftime(DATETIME_FORMAT) + ' ' * 10 + 'Start to transform data to pandas dataframe!\n')
data = pd.DataFrame(data_list, columns=[
 'deviceid',
 'essayid',
 'label',
 'n_activate_utilnow',
 'd_st_ctime',
 'd_st_titlelen',
 'd_dy_histpv',
 'd_dy_recvalidshow',
 'd_dy_recread',
 'd_dy_recclickrate',
 'd_dy_finishrate',
 'n_browse_price',
 'u_dy_rt_poscnts',
 'u_dy_rt_videoreadratio',
 'd_st_playtime',
 'plateform',
 'province',
 'city_level',
 'is_rest_day',
 'is_daytime',
 'd_st_contenttype',
 'd_st_covershowtype',
 'd_st_life',
 'd_dy_isexpired',
 'position',
 'n_context',
 'd_st_tag_sjzc',
 'u_dy_rt_notclickedtag_sjzc',
 'u_dy_rt_readtag_sjzc',
 's_long_labels_sjzc',
 's_short_labels_sjzc',
 'd_st_tag_sjcl',
 'u_dy_rt_notclickedtag_sjcl',
 'u_dy_rt_readtag_sjcl',
 's_long_labels_sjcl',
 's_short_labels_sjcl',
 'd_st_tag_sg',
 'u_dy_rt_notclickedtag_sg',
 'u_dy_rt_readtag_sg',
 's_long_labels_sg',
 's_short_labels_sg',
 'd_st_tag_jq',
 'u_dy_rt_notclickedtag_jq',
 'u_dy_rt_readtag_jq',
 's_long_labels_jq',
 's_short_labels_jq',
 'd_st_tag_pc',
 'u_dy_rt_notclickedtag_pc',
 'u_dy_rt_readtag_pc',
 's_long_labels_pc',
 's_short_labels_pc',
 'd_st_tag_tc',
 'u_dy_rt_notclickedtag_tc',
 'u_dy_rt_readtag_tc',
 's_long_labels_tc',
 's_short_labels_tc',
 'd_st_tag_mtsh',
 'u_dy_rt_notclickedtag_mtsh',
 'u_dy_rt_readtag_mtsh',
 's_long_labels_mtsh',
 's_short_labels_mtsh',
 'd_st_tag_mlgl',
 'u_dy_rt_notclickedtag_mlgl',
 'u_dy_rt_readtag_mlgl',
 's_long_labels_mlgl',
 's_short_labels_mlgl',
 'd_st_tag_xc',
 'u_dy_rt_notclickedtag_xc',
 'u_dy_rt_readtag_xc',
 's_long_labels_xc',
 's_short_labels_xc',
 'd_st_tag_ycgs',
 'u_dy_rt_notclickedtag_ycgs',
 'u_dy_rt_readtag_ycgs',
 's_long_labels_ycgs',
 's_short_labels_ycgs',
 'd_st_tag_jm',
 'u_dy_rt_notclickedtag_jm',
 'u_dy_rt_readtag_jm',
 's_long_labels_jm',
 's_short_labels_jm',
 'd_st_tag_kpzs',
 'u_dy_rt_notclickedtag_kpzs',
 'u_dy_rt_readtag_kpzs',
 's_long_labels_kpzs',
 's_short_labels_kpzs',
 'd_st_tag_wxgz',
 'u_dy_rt_notclickedtag_wxgz',
 'u_dy_rt_readtag_wxgz',
 's_long_labels_wxgz',
 's_short_labels_wxgz',
 'd_st_tag_wq',
 'u_dy_rt_notclickedtag_wq',
 'u_dy_rt_readtag_wq',
 's_long_labels_wq',
 's_short_labels_wq',
 'd_st_tag_mn',
 'u_dy_rt_notclickedtag_mn',
 'u_dy_rt_readtag_mn',
 's_long_labels_mn',
 's_short_labels_mn',
 'd_st_tag_zbpj',
 'u_dy_rt_notclickedtag_zbpj',
 'u_dy_rt_readtag_zbpj',
 's_long_labels_zbpj',
 's_short_labels_zbpj',
 'd_st_tag_sp',
 'u_dy_rt_notclickedtag_sp',
 'u_dy_rt_readtag_sp',
 's_long_labels_sp',
 's_short_labels_sp',
 'd_st_tag_ss',
 'u_dy_rt_notclickedtag_ss',
 'u_dy_rt_readtag_ss',
 's_long_labels_ss',
 's_short_labels_ss',
 'd_st_tag_clpc',
 'u_dy_rt_notclickedtag_clpc',
 'u_dy_rt_readtag_clpc',
 's_long_labels_clpc',
 's_short_labels_clpc',
 'd_st_tag_xcjc',
 'u_dy_rt_notclickedtag_xcjc',
 'u_dy_rt_readtag_xcjc',
 's_long_labels_xcjc',
 's_short_labels_xcjc',
 'd_st_tag_qx',
 'u_dy_rt_notclickedtag_qx',
 'u_dy_rt_readtag_qx',
 's_long_labels_qx',
 's_short_labels_qx',
 'd_st_tag_tag_null',
 'u_dy_rt_notclickedtag_tag_null',
 'u_dy_rt_readtag_tag_null',
 's_long_labels_tag_null',
 's_short_labels_tag_null',
 'poscate_0',
 'poscate_1',
 'poscate_2',
 'poscate_3',
 'poscate_4',
 'poscate_5',
 'poscate_poscates_null',
 'duration',
 'd_dy_recreadtime',
 'd_dy_recavgreadtime',
 'p_day'
],)
with open(today_LGM_PATH + '/lgb_train_log.txt', 'a') as f:
    f.write(datetime.datetime.now().strftime(DATETIME_FORMAT) + ' ' * 10 + 'Success to transform data to pandas dataframe, start traning!\n')


def TimeWeight(data):
    if data>2:
        return np.log(data)/np.log(1.5)
    else:
        return 1
data['duration'] = data['duration'].apply(lambda x: TimeWeight(x))

y = data['label']
X = data.drop(['label'],axis=1)

x_train, x_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=100)


def GetNewDataByPandas(x, y):
    y = np.array(y)
    deviceid = np.array(x.deviceid)
    time_weight = np.array(x.duration)
    X = x.drop(['deviceid', 'essayid', 'duration','p_day'], axis=1)
    feature_names = list(X.columns)

    X = np.array(X)
    X = np.where(X != '无', X, np.nan)  # 缺失值处理，x为true替换值，y为false替换值
    return X, y, deviceid, time_weight, feature_names


x_train, y_train, deviceid_train, time_Weight_train, feature_names_train = GetNewDataByPandas(x_train, y_train)
x_val, y_val, deviceid_val, time_Weight_val, feature_names_val = GetNewDataByPandas(x_val, y_val)



cate_list = ['plateform','city_level','is_rest_day','is_daytime','d_st_contenttype','d_st_covershowtype','d_st_life',
             'd_dy_isexpired', 'province','n_context','position',
             'd_st_tag_sjzc',
 'u_dy_rt_notclickedtag_sjzc',
 'u_dy_rt_readtag_sjzc',
 's_long_labels_sjzc',
 's_short_labels_sjzc',
 'd_st_tag_sjcl',
 'u_dy_rt_notclickedtag_sjcl',
 'u_dy_rt_readtag_sjcl',
 's_long_labels_sjcl',
 's_short_labels_sjcl',
 'd_st_tag_sg',
 'u_dy_rt_notclickedtag_sg',
 'u_dy_rt_readtag_sg',
 's_long_labels_sg',
 's_short_labels_sg',
 'd_st_tag_jq',
 'u_dy_rt_notclickedtag_jq',
 'u_dy_rt_readtag_jq',
 's_long_labels_jq',
 's_short_labels_jq',
 'd_st_tag_pc',
 'u_dy_rt_notclickedtag_pc',
 'u_dy_rt_readtag_pc',
 's_long_labels_pc',
 's_short_labels_pc',
 'd_st_tag_tc',
 'u_dy_rt_notclickedtag_tc',
 'u_dy_rt_readtag_tc',
 's_long_labels_tc',
 's_short_labels_tc',
 'd_st_tag_mtsh',
 'u_dy_rt_notclickedtag_mtsh',
 'u_dy_rt_readtag_mtsh',
 's_long_labels_mtsh',
 's_short_labels_mtsh',
 'd_st_tag_mlgl',
 'u_dy_rt_notclickedtag_mlgl',
 'u_dy_rt_readtag_mlgl',
 's_long_labels_mlgl',
 's_short_labels_mlgl',
 'd_st_tag_xc',
 'u_dy_rt_notclickedtag_xc',
 'u_dy_rt_readtag_xc',
 's_long_labels_xc',
 's_short_labels_xc',
 'd_st_tag_ycgs',
 'u_dy_rt_notclickedtag_ycgs',
 'u_dy_rt_readtag_ycgs',
 's_long_labels_ycgs',
 's_short_labels_ycgs',
 'd_st_tag_jm',
 'u_dy_rt_notclickedtag_jm',
 'u_dy_rt_readtag_jm',
 's_long_labels_jm',
 's_short_labels_jm',
 'd_st_tag_kpzs',
 'u_dy_rt_notclickedtag_kpzs',
 'u_dy_rt_readtag_kpzs',
 's_long_labels_kpzs',
 's_short_labels_kpzs',
 'd_st_tag_wxgz',
 'u_dy_rt_notclickedtag_wxgz',
 'u_dy_rt_readtag_wxgz',
 's_long_labels_wxgz',
 's_short_labels_wxgz',
 'd_st_tag_wq',
 'u_dy_rt_notclickedtag_wq',
 'u_dy_rt_readtag_wq',
 's_long_labels_wq',
 's_short_labels_wq',
 'd_st_tag_mn',
 'u_dy_rt_notclickedtag_mn',
 'u_dy_rt_readtag_mn',
 's_long_labels_mn',
 's_short_labels_mn',
 'd_st_tag_zbpj',
 'u_dy_rt_notclickedtag_zbpj',
 'u_dy_rt_readtag_zbpj',
 's_long_labels_zbpj',
 's_short_labels_zbpj',
 'd_st_tag_sp',
 'u_dy_rt_notclickedtag_sp',
 'u_dy_rt_readtag_sp',
 's_long_labels_sp',
 's_short_labels_sp',
 'd_st_tag_ss',
 'u_dy_rt_notclickedtag_ss',
 'u_dy_rt_readtag_ss',
 's_long_labels_ss',
 's_short_labels_ss',
 'd_st_tag_clpc',
 'u_dy_rt_notclickedtag_clpc',
 'u_dy_rt_readtag_clpc',
 's_long_labels_clpc',
 's_short_labels_clpc',
 'd_st_tag_xcjc',
 'u_dy_rt_notclickedtag_xcjc',
 'u_dy_rt_readtag_xcjc',
 's_long_labels_xcjc',
 's_short_labels_xcjc',
 'd_st_tag_qx',
 'u_dy_rt_notclickedtag_qx',
 'u_dy_rt_readtag_qx',
 's_long_labels_qx',
 's_short_labels_qx',
 'd_st_tag_tag_null',
 'u_dy_rt_notclickedtag_tag_null',
 'u_dy_rt_readtag_tag_null',
 's_long_labels_tag_null',
 's_short_labels_tag_null',
 'poscate_0',
 'poscate_1',
 'poscate_2',
 'poscate_3',
 'poscate_4',
 'poscate_5',
 'poscate_poscates_null']

#dataset包装
train_data = lgb.Dataset(data=x_train, label=y_train, feature_name = feature_names_train, weight=time_Weight_train, categorical_feature = cate_list)
val_data = lgb.Dataset(data=x_val, label=y_val, feature_name = feature_names_train, weight=time_Weight_val, categorical_feature = cate_list)

# 参数设置
params = {
    'boosting_type': 'gbdt',  # 设置提升类型
    'objective': 'binary',  # 目标函数
    'metric': {'binary_logloss', 'auc'},  # 评估函数
    'num_trees': 100,
    'max_depth': 8,
    'num_leaves': 128,  # 叶子节点数
    'learning_rate': 0.1,  # 学习速率
    'feature_fraction': 0.8,  # 建树的特征选择比例
    'bagging_fraction': 0.8,  # 建树的样本采样比例
    'bagging_freq': 5,  # 每 k 次迭代执行bagging
    'min_data_in_leaf': 500,
    'max_bin': 128,
    'verbose': 1,  # <0 显示致命的, =0 显示错误 (警告), >0 显示信息
    'is_unbalance': True,
    'min_data_in_bin': 50
}

num_round = 10
lgb_model = lgb.train(params, train_data, num_round, valid_sets=[val_data])
with open(today_LGM_PATH + '/lgb_train_log.txt', 'a') as f:
    f.write(datetime.datetime.now().strftime(DATETIME_FORMAT) + ' ' * 10 + 'Success to training, start save files!\n')

y_pred = lgb_model.predict(x_val)
y_pred_binary = np.where(y_pred > 0.5, 1, 0)
acc = accuracy_score(y_predict, y_pred_binary)
recall = recall_score(y_predict, y_pred_binary)
auc = roc_auc_score(y_predict, y_pred)

from collections import defaultdict
from sklearn.metrics import roc_auc_score
import numpy as np

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


def cross_entropy_loss(labels, preds):
    """calculate cross_entropy_loss
      loss = -labels*log(preds)-(1-labels)*log(1-preds)
      Args:
        labels, preds
      Returns:
         log loss
    """

    if len(labels) != len(preds):
        raise ValueError(
            "labels num should equal to the preds num,")

    z = np.array(labels)
    x = np.array(preds)
    res = -z * np.log(x) - (1 - z) * np.log(1 - x)
    return res.tolist()

gauc = cal_group_auc(y_val, y_pred,deviceid_val)

with open(today_LGM_PATH + '/lgb_train_log.txt', 'a') as f:
    f.write(datetime.datetime.now().strftime(DATETIME_FORMAT) + ' ' * 10 + f'auc:{auc}, gauc:{gauc}, acc:{acc}, recall:{recall}\n')

if not os.path.exists(today_LGM_PATH):
    os.mkdir(today_LGM_PATH)

lgb_model.save_model(today_LGM_ROOT+'/lightgbm_model.txt')
with open(today_LGM_PATH + '/lgb_train_log.txt', 'a') as f:
    f.write(datetime.datetime.now().strftime(DATETIME_FORMAT) + ' ' * 10 + 'success to save lightgbm.txt to local file!\n')

hdfs = HdfsClient(hosts=['10.101.32.116:50070','172.16.1.129 :50070'],user_name='hdfs')
if not hdfs.exists(today_HDFS_PATH):
    hdfs.mkdirs(today_HDFS_PATH)
hdfs.copy_from_local(today_LGM_ROOT+'/lightgbm_model.txt',today_HDFS_PATH+'/lightgbm_model.txt')

with open(today_LGM_PATH + '/lgb_train_log.txt', 'a') as f:
     f.write(datetime.datetime.now().strftime(DATETIME_FORMAT) + ' ' * 10 + 'success to save lightgbm.txt to hdfs file!\n')
hdfs.copy_from_local(today_LGM_ROOT+'/lgb_train_log.txt',today_HDFS_PATH+'/lgb_train_log.txt')


feature_names = lgb_model.feature_name()
feature_importance = lgb_model.feature_importance()
important_features = {}
for k, v in zip(feature_names, feature_importance):
    if v>0:
        important_features[k] = v

final_features = sorted(important_features.keys(), key=lambda x:x[1], reverse=True)