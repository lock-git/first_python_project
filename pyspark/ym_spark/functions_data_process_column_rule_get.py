# -*- coding: utf-8 -*-
""" 获取每张表所需要治理的具体函数名称 """

from utils_drug_monitor_project_log import printException, printInfo  # 日志
from utils_mysql_manipulate import ManipulateMysql
from config_01 import mysql_host_data_process_column, mysql_port_data_process_column, mysql_user_data_process_column, \
    mysql_password_data_process_column, mysql_database_data_process_column, mysql_table_data_process_column_rule_fuction_config
import pandas as pd
import numpy as np

def __utils_drop_space(x):
    if (x is None) or pd.isnull(x):
        return None
    else:
        if not isinstance(x,unicode):
            try:
                try:
                    x=unicode(x)
                except:
                    x = unicode(x,encoding='utf8')
            except:
                pass

        try:
            x=x.strip()
        except:
            pass
        return x

def __utils_upper_name(x):
    if (x is None) or pd.isnull(x):
        return None
    else:
        if not isinstance(x, unicode):
            try:
                try:
                    x = unicode(x)
                except:
                    x = unicode(x, encoding='utf8')
            except:
                pass
        try:
            x = x.upper().replace(u' ',u'')  # 转大写并且去中间空格
        except:
            pass
        return x


# 获取所有列治理函数
def _get_all_data_process_column_functions():
    """获取所有列治理函数"""
    rule_data_process_functions_cols = [u'table_code', u'field_name', u'function_name', u'param_func_dynamic', u'param_func_static',u'param_func_refer_dict', u'param_func_refer_other_fields',u'result_func_fields',u'func_init']
    query_all_data_process_column_functions_sql=u"select {cols} from {rule_data_process_functions_table} where flag='1' and process_style='column'".format(
        cols=u','.join(rule_data_process_functions_cols),rule_data_process_functions_table=mysql_table_data_process_column_rule_fuction_config
    )
    try:
        mysqlobj = ManipulateMysql(mysql_host_data_process_column, mysql_port_data_process_column,
                                   mysql_user_data_process_column, mysql_password_data_process_column,
                                   mysql_database_data_process_column)
        data_process_functions_tuple = mysqlobj.getDataFromDatabase(query_all_data_process_column_functions_sql)
        assert ( data_process_functions_tuple is not None ) and ( len(data_process_functions_tuple)>0 )
    except:
        printException(info=query_all_data_process_column_functions_sql, description='get all data process column rule funcitons fail..;the sql is')
        raise
    else:
        printInfo(info=len(data_process_functions_tuple),description='we have get data process column all rule funcitons')
        data_process_column_functions_dataframe = pd.DataFrame(data=np.array(data_process_functions_tuple), columns=rule_data_process_functions_cols)
        for col in data_process_column_functions_dataframe.columns:
            data_process_column_functions_dataframe[col]=data_process_column_functions_dataframe[col].apply(__utils_drop_space)
        data_process_column_functions_dataframe[u'field_name']=data_process_column_functions_dataframe[u'field_name'].apply(__utils_upper_name)
        data_process_column_functions_dataframe[u'param_func_refer_other_fields']=data_process_column_functions_dataframe[u'param_func_refer_other_fields'].apply(__utils_upper_name)
        data_process_column_functions_dataframe[u'result_func_fields'] = data_process_column_functions_dataframe[u'result_func_fields'].apply(__utils_upper_name)
        return data_process_column_functions_dataframe
    finally:
        mysqlobj.close()

data_process_column_functions_dataframe = _get_all_data_process_column_functions()


# 获取当前表数据治理的所有函数
def get_specific_table_data_process_column(task_info_dict):
    table_code = task_info_dict.get(u'table_code', u'')
    specific_table_data_process_functions = data_process_column_functions_dataframe[data_process_column_functions_dataframe.table_code==table_code]
    specific_table_data_process_functions_list = specific_table_data_process_functions.to_dict(orient='records')
    return specific_table_data_process_functions_list




if __name__ == '__main__':
    pass


