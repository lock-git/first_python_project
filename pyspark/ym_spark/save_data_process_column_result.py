# -*- coding: utf-8 -*-
from spark.ym_spark.utils_drug_monitor_project_log import printException,printInfo   # 日志信息
from spark.ym_spark.config_01 import hdfs_data_process_column_result_root_path,execute_version
from pyspark.sql.functions import lit
import datetime
import uuid
import os


def save_data_process_column_results(dataframe_pyspark,task_info_dict):
    # 添加数据治理的时间和UID标记
    data_process_column_uid = unicode(uuid.uuid1()).replace(u'-', u'')  # 每一个批次有相同的UUID
    data_process_column_create_time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
    dataframe_pyspark=dataframe_pyspark.withColumn(u'DATA_PROCESS_COLUMN_UID',lit(data_process_column_uid)).withColumn(u'DATA_PROCESS_COLUMN_CREATE_TIME',lit(data_process_column_create_time))
    # 删除添加的临时不必要的列
    required_columns=[col for col in dataframe_pyspark.columns if not col.endswith('_TEMP_1YONGCLOUD')]
    dataframe_pyspark_required=dataframe_pyspark.select(*required_columns)
    # 生成路径
    table_name = task_info_dict.get(u'table_name')
    org_id = task_info_dict.get(u'org_id')
    batch_year = task_info_dict.get(u'batch_year')
    batch_month=task_info_dict.get(u'batch_month')
    file_path_name = os.path.join(hdfs_data_process_column_result_root_path, table_name)
    file_path_name = os.path.join(file_path_name, 'org_name={}'.format(org_id))
    file_path_name = os.path.join(file_path_name, 'year={}'.format(batch_year))
    file_path_name = os.path.join(file_path_name, 'month={}'.format(batch_month))
    # 保存
    if execute_version=='default':
        # dataframe_pyspark_required.coalesce(2).write.json(file_path_name, mode='overwrite')
        dataframe_pyspark_required.write.json(file_path_name, mode='overwrite')
    else:
        # dataframe_pyspark_required.coalesce(2).write.json(file_path_name,mode='append')
        dataframe_pyspark_required.write.json(file_path_name,mode='append')
    return file_path_name



if __name__=='__main__':
    pass