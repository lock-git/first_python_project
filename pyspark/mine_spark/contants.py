# -*- coding: utf-8 -*-
"""
本文件是配置文件，方便修改
"""

# 数据库配置

#jdd_portrait线上库
MYSQL_JDD_PORTRAIT_URL_PROD = "jdbc:mysql://10.10.11.126:3306/jdd_portrait?useUnicode=true&characterEncoding=utf8&useSSL=false&autoReconnect=true&serverTimezone=CST"
JP_U_CHN = "jdd_portrait_rw"
JP_P_CHN = "z7tw_Ao3"

JP_HS = "10.10.11.126"
JP_PT = 3306
JP_DB = "jdd_portrait"


#jdd_portrait测试库
MYSQL_JDD_PORTRAIT_URL_PROD_C = "jdbc:mysql://172.16.201.4:36606/jdd_portrait?useUnicode=true&characterEncoding=utf8&useSSL=false&autoReconnect=true&serverTimezone=CST"
JP_U_CHN_C = "root"
JP_P_CHN_C = "jdd.com"

JP_HS_C = "172.16.201.4"
JP_PT_C = 6606
JP_DB_C = "jdd_portrait"



# table name
AUC_OFFLINE_TABLE = "motor_model_auc_offline_monitor"
