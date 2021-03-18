# -*- coding: utf-8 -*-
"""
本文件是配置文件，方便修改
"""

# 数据库配置
mysql_host_data_process_column='xxx'
mysql_port_data_process_column='xxx'
mysql_user_data_process_column='xxx'
mysql_password_data_process_column='xxx'
mysql_database_data_process_column='xxx'
# 列治理的规则函数配置表
mysql_table_data_process_column_rule_fuction_config='xxx'

# 列治理的任务调度表
mysql_table_task_data_process_column='task_info_hive_and_check'


# 医院信息表
mysql_table_dept_info='view_sys_dept_info'


# 有可能数据需要从数据库中进行过滤，并不是原始的生产库
hdfs_data_filter_result_root_path='/app/data_process/filter'
hdfs_uploaddata_root_path=hdfs_data_filter_result_root_path


# 数据治理结果存储位置
hdfs_data_process_column_result_root_path='/app/data_process/column'


# 执行时标记执行版本,如果是默认的话，暂时设置为覆盖，如果是其他值，则是追加
execute_version='default'


# xxx 参考字典-本地文件路径
refer_dict_local_file_path='./RegexFind/config'

