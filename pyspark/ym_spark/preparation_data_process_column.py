# -*- coding: utf-8 -*-
"""本文件的目的是为执行列治理而做准备工作-包含设置动态参数，参考字典，静态文件等"""

from spark.ym_spark.utils_drug_monitor_project_log import printException,printInfo   # 日志信息
from spark.ym_spark.config_01 import hdfs_uploaddata_root_path   # 上传数据在Hadoop集群中的路径
import os
from spark.ym_spark.utils_mysql_manipulate import ManipulateMysql
from spark.ym_spark.config_01 import mysql_host_data_process_column,mysql_port_data_process_column,\
    mysql_user_data_process_column,mysql_password_data_process_column,mysql_database_data_process_column
from spark.ym_spark.config_01 import mysql_table_data_process_column_rule_fuction_config,mysql_table_task_data_process_column
import numpy as np
from spark.ym_spark.config_01 import refer_dict_local_file_path


def __get_database_refer_dict_data(table_name,cols,version):
    mysqlobj = ManipulateMysql(mysql_host_data_process_column, mysql_port_data_process_column,
                               mysql_user_data_process_column, mysql_password_data_process_column,
                               mysql_database_data_process_column)
    refer_dict_table_query_sql = u"select {col} from {table_name} where version_code='{version}'".format(col=u'*' if len(cols) == 0 else u','.join(cols), table_name=table_name,version=version)
    refer_dict_table_data_tuple = mysqlobj.getDataFromDatabase(refer_dict_table_query_sql)
    mysqlobj.close()
    return np.array(refer_dict_table_data_tuple).tolist()



def _get_all_fuction_param_refer_dict():
    functions_data_process_module = __import__('functions_data_process_column_preparation_read_xlc')
    fuction_param_refer_dict={}
    try:
        mysqlobj = ManipulateMysql(mysql_host_data_process_column, mysql_port_data_process_column,
                                   mysql_user_data_process_column, mysql_password_data_process_column,
                                   mysql_database_data_process_column)
        fuctions_refer_dict_sql = u"select function_name,param_func_refer_dict from {table_rule_func_data_process} where param_func_refer_dict is not null and param_func_refer_dict !='' and process_style='column' and flag='1'".format(
            table_rule_func_data_process=mysql_table_data_process_column_rule_fuction_config
        )
        fuctions_refer_dict_tuple = mysqlobj.getDataFromDatabase(fuctions_refer_dict_sql)
        if (fuctions_refer_dict_tuple is None) or (len(fuctions_refer_dict_tuple)==0):
            pass
        else:
            # 查询出来所有的function 及 静态字典的配置
            functions_refer_dict_list =dict(fuctions_refer_dict_tuple)
            # 过滤所有的无效的参考字典-形成的dict形式-{functionname: { referdict config} }
            functions_refer_dict_list = { key:eval(functions_refer_dict_list.get(key)) if ((functions_refer_dict_list.get(key) is not None) and (functions_refer_dict_list.get(key).strip() != u'')) else {} for key in functions_refer_dict_list }
            # 循环处理每个函数的静态字典
            for function_name_key in functions_refer_dict_list:
                functions_refer_dict_specific=functions_refer_dict_list.get(function_name_key)   # 取出的值 {'config1':{},}
                specific_fuction_refer_dict_dict={}
                for config_key in functions_refer_dict_specific:
                    config_require_info=functions_refer_dict_specific.get(config_key)
                    flag=int(config_require_info.get('flag',0))  # 1 文件，2 数据库表
                    if flag==1:
                        # 文件
                        file_path_name=config_require_info.get('file_path_name')
                        file_process_func = config_require_info.get(u'file_process_func')
                        process_function=getattr(functions_data_process_module,file_process_func)
                        specific_fuction_refer_dict_dict[config_key]=process_function(os.path.join(refer_dict_local_file_path,file_path_name))
                    elif flag==2:
                        # 数据库表
                        table_name = config_require_info.get(u'table_name')
                        file_process_func = config_require_info.get(u'file_process_func')
                        process_function=getattr(functions_data_process_module,file_process_func)
                        cols=config_require_info.get(u'columns',[])
                        version=config_require_info.get(u'version')
                        specific_fuction_refer_dict_dict[config_key]=process_function(__get_database_refer_dict_data(table_name,cols,version))
                fuction_param_refer_dict[function_name_key]=specific_fuction_refer_dict_dict
    except:
        printException(info='get fuction param refer dict fail....')
        raise
    else:
        printInfo(info=[len(fuction_param_refer_dict),fuction_param_refer_dict.keys()],description='we have get function param refer dict,succeed')
        return fuction_param_refer_dict
    finally:
        mysqlobj.close()

fuction_param_refer_dict=_get_all_fuction_param_refer_dict()





# [u'org_id',u'batch_year',u'batch_month',u'table_name',u'batch_id',u'task_id',u'table_code',u'file_json_path']
# dept_id,task_year,task_month,table_name,batch_id,task_id,table_code,file_path

def prepare_data_process_task_info_integration_dict(task_info_dict):
    """ 数据治理执行都是按照周期进行的 """
    # 1.当前医院上传数据在Hadoop集群上存储的hdfs路径
    table_name = task_info_dict.get(u'table_name', u'')
    file_hdfs_path = os.path.join(hdfs_uploaddata_root_path, table_name)
    file_hdfs_path = os.path.join(file_hdfs_path, u'org_name={}'.format(task_info_dict.get(u'org_id', u'')))
    file_hdfs_path = os.path.join(file_hdfs_path, u'year={}'.format(task_info_dict.get(u'batch_year', u'')))
    file_hdfs_path = os.path.join(file_hdfs_path, u'month={}'.format(task_info_dict.get(u'batch_month', u'')))
    task_info_dict[u'file_hdfs_path'] = file_hdfs_path
    # 2.当前用户，在同一周期下，当前表一共上传了多少有效文件，如果上传多个，待会要同时更新状态
    try:
        mysqlobj = ManipulateMysql(mysql_host_data_process_column, mysql_port_data_process_column,
                                   mysql_user_data_process_column, mysql_password_data_process_column,
                                   mysql_database_data_process_column)
        upload_file_info_sql=u"select task_id from {mysql_table_task_data_process_column} where dept_id='{org_id}' and task_year='{batch_year}' and task_month='{batch_month}' and table_code='{table_code}' and status in ('ZL00','ZL01','ZL02','ZL03') and flag='1'".format(
            mysql_table_task_data_process_column=mysql_table_task_data_process_column,org_id=task_info_dict.get(u'org_id', u''),batch_year=task_info_dict.get(u'batch_year', u''),batch_month=task_info_dict.get(u'batch_month', u''),table_code=task_info_dict.get(u'table_code', u'')
        )
        taskids_tuple=mysqlobj.getDataFromDatabase(upload_file_info_sql)
        assert (taskids_tuple is not None) and (len(taskids_tuple)>0)
    except:
        printException(info=upload_file_info_sql,description='get all taskid list that have the same orgid batch year and batch month and table code fail....')
        task_info_dict[u'taskids']=[task_info_dict.get(u'task_id', u'')]
    else:
        printInfo(info='get the same orgid batch year batch month table code taskid list succeed !')
        taskids=[taskid_tuple[0] for taskid_tuple in taskids_tuple]
        task_info_dict[u'taskids'] = taskids
    finally:
        mysqlobj.close()
    # 3. 为治理函数做准备工作（1）加载动态参数 （2）加载参考字典
    # 3.1 添加动态字典
    task_info_dict[u'params_dynamic']={}
    # 3.2添加参考字典
    task_info_dict[u'params_refer_dict']=fuction_param_refer_dict
    return task_info_dict



if __name__=='__main__':
    pass
