# -*- coding: utf-8 -*-
"""
这个文件的主要目的是实现MySQL常用的操作
"""
import pymysql as mysqldb


class ManipulateMysql:
    """操作MySQL，查询，插入，更新"""

    def __init__(self, mysql_host, mysql_port, mysql_user, mysql_password,
                 mysql_database):  # mysql连接的必要信息，ip，端口号，用户名，密码，数据库
        """初始化mysql连接，并且创建一个cursor，为后续执行"""
        try:
            self._connection = mysqldb.connect(host=mysql_host,
                                               port=mysql_port,
                                               user=mysql_user,
                                               passwd=mysql_password,
                                               db=mysql_database,
                                               charset="utf8")
        except:
            print('创建mysql连接失败！请重新尝试！！')
            return None
        else:
            self._cursor = self._connection.cursor()

    def getDataFromDatabase(self, sql):
        """从mysql中读取数据,注：sql语句拼接时，除了整形或浮点类型数据，类型都可以为字符串（str 或 Unicode）"""
        try:
            records = self._cursor.execute(sql)
        except:
            print(f'查询数据库中数据失败，请检查sql是否正确，sql语句是 {sql}')
            return None
        else:
            if records == 0:
                # print(info=sql,description='在数据库中并未查询到相应的记录,sql语句是')
                pass
            else:
                print(f'在数据库中查询到相应记录的条数为 {records}')
            datatuple = self._cursor.fetchall()  # 数据结构是元组的元组
            return datatuple

    def updateDataIntoDatabase(self, sql):
        """更新mysql数据库中的数据,注：sql语句拼接时，除了整形或浮点类型数据，类型都可以为字符串（str 或 Unicode）"""
        try:
            records = self._cursor.execute(sql)
        except:
            print(f'更新mysql数据库中的数据失败，请检查sql语句是否正确，sql语句是 {sql}')
        else:
            if records == 0:
                print(f'在mysql数据库中并未更新任何数据,sql语句是 {sql}')
            else:
                print(f'在mysql数据库中更新数据条数为 {records}')
            self._connection.commit()

    def deleteDataFromDatabase(self, sql):
        """删除mysql数据库中的数据,注：sql语句拼接时，除了整形或浮点类型数据，类型都可以为字符串（str 或 Unicode）"""
        try:
            records = self._cursor.execute(sql)
        except:
            print(f'删除mysql数据库中的数据失败，请检查sql语句是否正确，sql语句是 {sql}')
        else:
            if records == 0:
                print(f'在mysql数据库中并未删除任何数据,sql语句是 {sql}')
            else:
                print(f'在mysql数据库中删除数据条数为 {records}')
            self._connection.commit()

    def insertDataIntoDatabase(self, sql):
        """向mysql数据库插入数据,注：sql语句拼接时，除了整形或浮点类型数据，类型都可以为字符串（str 或 Unicode）"""
        try:
            records = self._cursor.execute(sql)
        except:
            print(f'向mysql数据库中插入数据失败，请检查sql语句是否正确，sql语句是 {sql}')
        else:
            if records == 0:
                print(f'并未向mysql数据库中插入任何数据,sql语句是 {sql}')
            else:
                print(f'向mysql数据库中插入数据条数为 ==> {records}')
            self._connection.commit()

    def insertDataIntoDatabaseBatch(self, sql_list):
        """批量向mysql数据库插入数据,注：sql语句拼接时，除了整形或浮点类型数据，类型都可以为字符串（str 或 Unicode）"""
        try:
            # records = self._cursor.executemany(u';'.join(sql_list))
            # records = self._cursor.executemany(u';'.join(sql_list))
            records = 0
            for sql in sql_list:
                try:
                    records = records + self._cursor.execute(sql)
                except:
                    print(f'向mysql数据库中插入数据失败，请检查sql语句是否正确，sql语句是 {sql}')
        except:
            print(f'向mysql数据库中插入数据失败，请检查sql语句是否正确，sql语句是 {sql_list}')
            self._connection.rollback()  # 批量插入不成功，回滚
        else:
            if records == 0:
                print(f'并未向mysql数据库中插入任何数据,sql语句是 {sql_list}')
            else:
                print(f'向mysql数据库中插入数据条数为 {records}')
            self._connection.commit()

    def close(self):
        """关闭与mysql之间的连接"""
        try:
            self._cursor.close()
        except:
            pass
        try:
            self._connection.close()
        except:
            pass


if __name__ == '__main__':
    # 测试
    mysql_host = '172.16.201.4'
    mysql_port = 6606
    mysql_user = 'root'
    mysql_password = 'jdd.com'
    mysql_database = 'jdd_portrait'

    taday = '2010'

    delete_sql = f"delete from  `motor_model_auc_offline_monitor` where s_pday = '{taday}' "
    print(delete_sql)

    jdd_portrait_base = ManipulateMysql(mysql_host, mysql_port, mysql_user, mysql_password, mysql_database)
    insert_sql = f"INSERT INTO `motor_model_auc_offline_monitor` ( `s_pday`, `s_feature`, `s_group`, `n_auc_flag`, `n_value`) VALUES ( '2020-12-15', 'd_platform', '1', 0, '0.23587689')"
    insert_value = jdd_portrait_base.insertDataIntoDatabase(insert_sql)

    select_sql = f"select * from  `motor_model_auc_offline_monitor`"
    select_value = jdd_portrait_base.getDataFromDatabase(select_sql)
    print(f"select_value ==> {select_value}")


    delete_sql = f"delete from  `motor_model_auc_offline_monitor` where s_pday = '2020-12-15' "
    # delete_value = jdd_portrait_base.deleteDataFromDatabase(delete_sql)
    # print(f"delete_value ==> {delete_value}")

    pass
