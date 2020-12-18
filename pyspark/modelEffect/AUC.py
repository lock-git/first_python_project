import numpy as np
from sklearn import metrics
from sklearn.metrics import roc_auc_score

y_true = np.array([0, 0, 1, 1])
y_scores = np.array([0.1, 0.4, 0.35, 0.8])
auc_score = roc_auc_score(y_true, y_scores)
print(auc_score)
# 输出：0.75

y = np.array([1, 1, 2, 2])  # 实际值
scores = np.array([0.1, 0.4, 0.35, 0.8])  # 预测值
fpr, tpr, thresholds = metrics.roc_curve(y, scores, pos_label=2)  # pos_label=2，表示值为2的实际值为正样本
print(fpr)
print(tpr)
print(thresholds)

# 输出：array([ 0. ,  0.5,  0.5,  1. ])array([ 0.5,  0.5,  1. ,  1. ])array([ 0.8 ,  0.4 ,  0.35,  0.1 ])
# [0.  0.  0.5 0.5 1. ]
# [0.  0.5 0.5 1.  1. ]
# [1.8  0.8  0.4  0.35 0.1 ]
