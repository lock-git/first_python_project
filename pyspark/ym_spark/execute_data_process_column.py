# -*- coding: utf-8 -*-
"""实现上传数据列治理"""

from pyspark.sql import SparkSession
import time
import datetime

# 创建一个spark session对象
spark_application_name='spark_uploaddata_dataprocess_column_{}'.format(str(datetime.date.today()).replace('-','_'))
spark = SparkSession.builder.appName(spark_application_name).config('spark.driver.maxResultSize','64g').enableHiveSupport().getOrCreate()

# 添加辅助文件及包
sc = spark.sparkContext

# yarn 模式需要添加的额外文件
# sc.addFile("xxxxxx.py")
# sc.addFile('config_01.py')
# sc.addFile('functions_data_process_column_module_xlc.py')
# sc.addFile('functions_data_process_column_rule_get.py')
# sc.addFile('preparation_data_process_column.py')
# sc.addPyFile('RegexFind.zip')
# sc.addFile('save_data_process_column_result.py')
# sc.addFile('table_data_process_column_process_flow.py')
# sc.addFile('table_data_process_column_realise.py')
# sc.addFile('util_extend_fact_table.py')
# sc.addFile('utils_drug_monitor_project_log.py')
# sc.addFile('utils_mysql_manipulate.py')
# sc.addFile('utils_sql_statements_generator.py')


# 设置日志等级
sc.setLogLevel("WARN")

from spark.ym_spark.config_01 import mysql_host_data_process_column,mysql_port_data_process_column,\
    mysql_user_data_process_column,mysql_password_data_process_column,\
    mysql_database_data_process_column,mysql_table_task_data_process_column
from spark.ym_spark.utils_drug_monitor_project_log import printException,printInfo   # 日志信息
from spark.ym_spark.utils_mysql_manipulate import ManipulateMysql
from spark.ym_spark.preparation_data_process_column import prepare_data_process_task_info_integration_dict # 准备治理函数的动态参数和参考字典
from spark.ym_spark.table_data_process_column_process_flow import realise_table_data_process_column  # 完整的列治理的过程

def execute(mysql_table_task_data_process_column,tables=None,dept_id_begin=u'%'):
    # 获取任务
    task_info_cols=[u'org_id',u'batch_year',u'batch_month',u'table_name',u'batch_id',u'task_id',u'table_code',u'file_json_path']
    while True:
        try:
            mysqlobj=ManipulateMysql(mysql_host_data_process_column,mysql_port_data_process_column,mysql_user_data_process_column,mysql_password_data_process_column,mysql_database_data_process_column)
            if tables is None:
                task_info_sql=u"select dept_id,task_year,task_month,table_name,batch_id,task_id,table_code,file_path from {mysql_table_task_data_process_column} where status='ZL01' and flag='1' and dept_id like '{dept_id_begin}%' limit 1".format(mysql_table_task_data_process_column=mysql_table_task_data_process_column,dept_id_begin=dept_id_begin)
            else:
                task_info_sql=u"select dept_id,task_year,task_month,table_name,batch_id,task_id,table_code,file_path from {mysql_table_task_data_process_column} where status='ZL01' and flag='1' and table_code in ({tables}) and dept_id like '{dept_id_begin}%' limit 1".format(mysql_table_task_data_process_column=mysql_table_task_data_process_column,tables=tables,dept_id_begin=dept_id_begin)
            task_tuple=mysqlobj.getDataFromDatabase(task_info_sql)
            mysqlobj.close()
        except:
            # 数据库连接不上，或配置错误等导致查询不到正确的任务数据
            printException(info=task_info_sql,description='get task data from mysql fail...;the query sql is')
            #raise  # 测试时可以打开，生产必须注释
            time.sleep(5)

        else:
            # 判断正确查询了数据，是否有任务
            try:
                assert len(task_tuple)==1
            except:
                printException(info='the current has no task! waiting.....')
                time.sleep(20)
                #break # 没有任务，终止程序

            else:
                # 获取到一个任务信息，并且在此处添加进行数据治理函数的动态参数，参考字典等相关配置信息
                task_info_dict=dict(zip(task_info_cols,task_tuple[0]))    # 形成一个任务信息dict
                try:
                    task_info_dict_integration=prepare_data_process_task_info_integration_dict(task_info_dict)   #  添加此处进行数据治理的动态参数，参考字典等相关配置信息
                except:
                    printException(info=task_info_dict,description='format the integration task info dict fail,the task info is')
                    #raise # 测试时可以打开，生产必须注释
					
                    # 任务信息dict形成失败，更新相应的表并且备注错误【-4	flag=-4 程序执行需要的任务信息不完整或形成有误	表设计（字段）】--如果执行不成功，自动再次执行，可以忽略，不必过多考虑
                    try:
                        mysqlobj = ManipulateMysql(mysql_host_data_process_column, mysql_port_data_process_column,mysql_user_data_process_column, mysql_password_data_process_column, mysql_database_data_process_column)
                        task_info_update_sql = u"update {mysql_table_task_data_process_column} set flag='-4',comment='the current data process column task add params execute fail,please check' where task_id='{task_id}' and flag='1' and status like 'ZL%'".format(
                            mysql_table_task_data_process_column=mysql_table_task_data_process_column, task_id=task_info_dict.get(u'task_id')
                        )
                        mysqlobj.updateDataIntoDatabase(task_info_update_sql)
                        mysqlobj.close()
                    except:
                        printException(info=task_info_dict,description='the current task info integration execute fail but update task table fail,the task info is')
                        # raise # 测试时可以打开，生产必须注释

                else:
                    # 对本周期上传的数据，进行列数据治理
                    try:
                        data_process_column_flag=realise_table_data_process_column(spark,task_info_dict_integration)
                        assert data_process_column_flag == True
                    except:
                        printException(info=task_info_dict_integration,description='the task realise data process column fail ..;the task info is')
                        # raise # 测试时可以打开，生产必须注释
						
                        ## 错误编码参考数据库
                        try:
                            error_sql=None
                            if data_process_column_flag == -2:
                                error_sql=u"update {mysql_table_task_data_process_column} set flag='-2',comment='the data process column program execute fail,please check' where task_id='{task_id}' and flag='1' and status like 'ZL%'".format(mysql_table_task_data_process_column=mysql_table_task_data_process_column, task_id=task_info_dict_integration.get(u'task_id'))
                            elif data_process_column_flag == -3:
                                error_sql = u"update {mysql_table_task_data_process_column} set flag='-1',comment='the data process column file read fail,please check' where task_id='{task_id}' and flag='1' and status like 'ZL%'".format(mysql_table_task_data_process_column=mysql_table_task_data_process_column,task_id=task_info_dict_integration.get(u'task_id'))
                            elif data_process_column_flag == -6:
                                error_sql = u"update {mysql_table_task_data_process_column} set comment='save the data process column result execute fail,please check' where task_id='{task_id}' and flag='1' and status like 'ZL%'".format(mysql_table_task_data_process_column=mysql_table_task_data_process_column,task_id=task_info_dict_integration.get(u'task_id'))
                            elif data_process_column_flag == -7:
                                error_sql = u"update {mysql_table_task_data_process_column} set status='ZL02',comment='the data process column have no process functions,please check' where task_id='{task_id}' and flag='1' and status like 'ZL%'".format(mysql_table_task_data_process_column=mysql_table_task_data_process_column,task_id=task_info_dict_integration.get(u'task_id'))
                                # raise  # 这个问题非常严重的，没有规则，也有可能是真的，目前这个不存在的
                            else:
                                pass
                            if error_sql is not None:
                                try:
                                    mysqlobj = ManipulateMysql(mysql_host_data_process_column, mysql_port_data_process_column,mysql_user_data_process_column, mysql_password_data_process_column, mysql_database_data_process_column)
                                    mysqlobj.updateDataIntoDatabase(error_sql)
                                except:
                                    printException(info=error_sql,description='the current task execute fail...,but update the task table fail ...')
                                finally:
                                    try:
                                        mysqlobj.close()
                                    except:
                                        pass
                        except:
                            pass
                            # raise

                    else:
                        # 任务表在更新时可能会出现死锁等状况，这个时候，如果无法更新就重新执行一次
                        try:
                            taskids=task_info_dict_integration.get(u'taskids')
                            task_info_update_sql_list=[u"update {mysql_table_task_data_process_column} set status='ZL02' where task_id='{task_id}' and flag='1'".format(mysql_table_task_data_process_column=mysql_table_task_data_process_column,task_id=task_id) for task_id in taskids]
                            mysqlobj=ManipulateMysql(mysql_host_data_process_column,mysql_port_data_process_column,mysql_user_data_process_column,mysql_password_data_process_column,mysql_database_data_process_column)
                            # mysqlobj.updateDataIntoDatabase(u';'.join(task_info_update_sql_list))
                            mysqlobj.insertDataIntoDatabaseBatch(task_info_update_sql_list)
                        except:
                            printException(info=task_info_update_sql_list,description='the current task execute succeed,but upadate the status fail...')
                        finally:
                            try:
                                mysqlobj.close()
                            except:
                                pass

        # break   # 测试时不要注释
    

if __name__=='__main__':
    # execute(mysql_table_task_data_process_column)
    # B03-B08 / B09-B13 / B14-B19   -后两个基本平衡，第一个差2个小时
    # B03-B06 default / B07-B13  shengchan / B13-B19  kylin  -最大时差是1个小时 其中default最先跑完，半个小时后是kylin，最后是shengchan
    # table_codes=[u'B0{}'.format(i) if i<10 else u'B{}'.format(i) for i in range(1,7,1) if i!=4]
    # table_codes.append(u'B04_non_chinese')
    # table_codes.append(u'B04_chinese')
    # table_codes = [u'B0{}'.format(i) if i < 10 else u'B{}'.format(i) for i in range(7, 12, 1) if i != 4]
    # table_codes = [u'B0{}'.format(i) if i < 10 else u'B{}'.format(i) for i in range(12, 20, 1) if i != 4]
    dept_id_begin_list = [u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9', u'a', u'b', u'c', u'd', u'e', u'f']
    dept_id_begin = dept_id_begin_list[0]
    # B01/B02
    start_table_code_include=1
    end_table_code_exclude=3
    table_codes=[]
    for i in range(start_table_code_include,end_table_code_exclude,1):
        if i==4:
            table_codes.append(u'B04_non_chinese')
            table_codes.append(u'B04_chinese')
        elif i < 10:
            table_codes.append(u'B0{}'.format(i))
        else:
            table_codes.append(u'B{}'.format(i))
    table_code_unicodes=u','.join([u"'{}'".format(table_code) for table_code in table_codes])
    execute(mysql_table_task_data_process_column,table_code_unicodes)
    # execute(mysql_table_task_data_process_column, table_code_unicodes, dept_id_begin)
    spark.stop()
