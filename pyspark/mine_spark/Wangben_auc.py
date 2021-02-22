import pandas as pd
import numpy as np
from sklearn.metrics import roc_auc_score
from collections import defaultdict

data = pd.read_csv('C:\\Users\JDD\Desktop\go_project\\auc_all.csv')

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


def compute_auc_gauc(data):
    deviceid = np.array(data.deviceid)
    label = np.array(data.action_type)
    prediction = np.array(data.score_fix)
    auc = roc_auc_score(label, prediction)
    gauc = cal_group_auc(label, prediction, deviceid)

    return auc, gauc


auc_hour_df = pd.DataFrame(
    columns=['hour', 'auc_a_andriod', 'auc_a_ios', 'auc_b_andriod', 'auc_b_ios', 'gauc_a_andriod', 'gauc_a_ios',
             'gauc_b_andriod', 'gauc_b_ios'])
auc_hour_df.hour = data.p_hour.unique()

for idx, hour in enumerate(sorted(data.p_hour.unique())):
    a_andriod = data.query(f'abversionid==0 and testid==\'f76cu9cns1u5owpznukf2joy79bzqrdr\' and p_hour=={hour}')
    a_ios = data.query(f'abversionid==0 and testid==\'dtdub87294xnrm2opn666lk6cjebb2og\' and p_hour=={hour}')
    b_andriod = data.query(f'abversionid==1 and testid==\'f76cu9cns1u5owpznukf2joy79bzqrdr\' and p_hour=={hour}')
    b_ios = data.query(f'abversionid==1 and testid==\'dtdub87294xnrm2opn666lk6cjebb2og\' and p_hour=={hour}')

    auc_hour_df.loc[idx, 'hour'] = hour
    auc_hour_df.loc[idx, 'auc_a_andriod'] = compute_auc_gauc(a_andriod)[0]
    auc_hour_df.loc[idx, 'gauc_a_andriod'] = compute_auc_gauc(a_andriod)[1]

    auc_hour_df.loc[idx, 'auc_a_ios'] = compute_auc_gauc(a_ios)[0]
    auc_hour_df.loc[idx, 'gauc_a_ios'] = compute_auc_gauc(a_ios)[1]

    auc_hour_df.loc[idx, 'auc_b_andriod'] = compute_auc_gauc(b_andriod)[0]
    auc_hour_df.loc[idx, 'gauc_b_andriod'] = compute_auc_gauc(b_andriod)[1]

    auc_hour_df.loc[idx, 'auc_b_ios'] = compute_auc_gauc(b_ios)[0]
    auc_hour_df.loc[idx, 'gauc_b_ios'] = compute_auc_gauc(b_ios)[1]