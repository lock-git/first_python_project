#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2018/3/13

import happybase
import time
import re
from pyspark.config.HBase_config import HBASE_MASTER, HBASE_MASTER_ONLINE


class Hbase(object):
    def __init__(self, host=HBASE_MASTER):
        """

        :param host: hbase host
        """
        self.host = host

    def create_table(self, table_name, column_family='cf'):
        conn = happybase.Connection(self.host)
        conn.create_table(table_name, {column_family: dict()})
        conn.close()

    def put_row(self, table_name: str, row_key: str, col: str, value: str, column_family='cf'):
        conn = happybase.Connection(self.host)
        table = conn.table(table_name)
        value = '%s' % value if not value is None else 'null'
        table.put(row_key, {':'.join([column_family, col]): '%s' % value})
        conn.close()

    def put_rows(self, table_name: str, row_key: str, rows: dict, column_family="cf"):
        conn = happybase.Connection(self.host)
        table = conn.table(table_name)
        for k, v in rows.items():
            value = '%s' % v if not v is None else 'null'
            table.put(row_key, {':'.join([column_family, k]): '%s' % value})
        conn.close()

    def get_rows(self, table_name: str, row_key: str, include_timestamp=False, column_family="cf"):
        conn = happybase.Connection(self.host)
        table = conn.table(table_name)
        rows = table.row('%s' % row_key, include_timestamp=include_timestamp)
        conn.close()
        if include_timestamp:
            return {re.sub('^%s:' % column_family, '', k.decode("utf8")): (
                v[0].decode("utf8"), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(v[1] / 1000))) for k, v in
                rows.items()}
        else:
            return {re.sub('^%s:' % column_family, '', k.decode("utf8")): v.decode("utf8") for k, v in rows.items()}

    def get_rows_specified_columns(self, table_name: str, row_key: str, columns: list, include_timestamp=False,
                                   column_family="cf"):
        conn = happybase.Connection(self.host)
        table = conn.table(table_name)
        rows = table.row('%s' % row_key, columns=columns, include_timestamp=include_timestamp)
        conn.close()
        if include_timestamp:
            return {re.sub('^%s:' % column_family, '', k.decode("utf8")): (
                v[0].decode("utf8"), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(v[1] / 1000))) for k, v in
                rows.items()}
        else:
            return {re.sub('^%s:' % column_family, '', k.decode("utf8")): v.decode("utf8") for k, v in rows.items()}

    def get_rows_valid(self, table_name: str, row_key: str, valid_time: int, column_family: str = "cf") -> dict:
        """

        :param table_name: 表名
        :param row_key: rowkey
        :param valid_time: 有效时间，单位天
        :param column_family: 一级列名，默认 cf
        :return:
        """
        valid_second = valid_time * 24 * 60 * 60
        conn = happybase.Connection(self.host)
        table = conn.table(table_name)
        rows = table.row('%s' % row_key, include_timestamp=True)
        conn.close()
        return {re.sub('^%s:' % column_family, '', k.decode("utf8")): v[0].decode("utf8") for k, v in rows.items() if
                (time.time() - (v[1] / 1000)) <= valid_second}

    def delete_row(self, table_name: str, row_key: str, column_family='cf', keys=None):
        conn = happybase.Connection(self.host)
        table = conn.table(table_name)
        if keys:
            print('delete keys:%s from row_key:%s' % (keys, row_key))
            key_list = ['%s:%s' % (column_family, key) for key in keys]
            table.delete(row_key, key_list)
        else:
            print('delete row(%s) from hbase' % row_key)
            table.delete(row_key)

    def scan_table(self, table_name: str, column_family='cf', columns=None):
        if columns is None:
            columns = []
        else:
            columns = list(map(lambda x: column_family + ':' + x, columns))
        conn = happybase.Connection(self.host)
        table = conn.table(table_name)
        scan_list = map(lambda x: {
            x[0].decode("utf8"): {k.decode("utf8").replace(column_family + ':', ''): (v[0].decode("utf8"), v[1]) for
                                  k, v in
                                  x[1].items()}},
                        table.scan(columns=columns, include_timestamp=True))
        return list(scan_list)

    def scan_table_range(self, table_name: str, column_family='cf', columns=None, row_start=None, row_stop=None):
        if columns is None:
            columns = []
        else:
            columns = list(map(lambda x: column_family + ':' + x, columns))
        conn = happybase.Connection(self.host)
        table = conn.table(table_name)
        scan_list = map(lambda x: {
            x[0].decode("utf8"): {k.decode("utf8").replace(column_family + ':', ''): (v[0].decode("utf8"), v[1]) for
                                  k, v in
                                  x[1].items()}},
                        table.scan(row_start, row_stop, columns=columns, include_timestamp=True))
        return list(scan_list)

    def scan_table_limit(self, table_name: str, column_family='cf', columns=None, limit=100):
        if columns is None:
            columns = []
        else:
            columns = list(map(lambda x: column_family + ':' + x, columns))
        conn = happybase.Connection(self.host)
        table = conn.table(table_name)
        scan_list = map(lambda x: {
            x[0].decode("utf8"): {k.decode("utf8").replace(column_family + ':', ''): (v[0].decode("utf8"), v[1]) for
                                  k, v in
                                  x[1].items()}},
                        table.scan(columns=columns, include_timestamp=True, limit=limit))
        return list(scan_list)

    @staticmethod
    def transform(hbase_result: dict, type_dic: dict):
        result = {}
        for k, v in hbase_result.items():
            if k in type_dic:
                if 'null' == v:
                    result[k] = None
                elif 'int' == type_dic[k]:
                    result[k] = int(float(v))
                elif 'float' == type_dic[k]:
                    result[k] = float(v)
                elif 'str' == type_dic[k]:
                    result[k] = v
                else:
                    print('hbase transfer error\r\n not valid type')
                    raise Exception
        return result


if '__main__' == __name__:
    # mobile_id = "52100000"[::-1]
    # report_id = "24899000"[::-1]
    report_id = "24890009"[::-1]
    hbase_offline = Hbase()

    # a = hbase_online.get_rows("API_VAR_CCL_EXT_V1", report_id)
    # b = hbase_online.put_rows("api_score_ccl_ext_v1_test", "test_ccl_ext_v1_0_case_1"[::-1],a)
    # print(a)

    a = hbase_offline.scan_table('ANTI_INFO')
    print(a)

    b = hbase_offline.get_rows("ANTI_INFO", "deviceId_qk:test111", False, "info")
    print(b)

    # hbase_offline.put_row("ANTI_INFO", "deviceId_qk:test111", "uids", "11,22,33", "info")
    # hbase_offline.put_row("ANTI_INFO", "deviceId_qk:test222", "uids", "44,55,66", "info")
    # hbase_offline.put_row("ANTI_INFO", "ip:3333", "type", "1", "info")

    # a1 = hbase_online.get_rows("API_VAR_JXL_INS", mobile_id)
    # a2 = hbase_online.get_rows("API_VAR_EXT_INS", report_id)
    # b1 = hbase_online.put_rows("API_VAR_JXL_INS", "test1"[::-1],a1)
    # b2 = hbase_online.put_rows("test_credit_ext", "test2"[::-1], a2)

    # a4 = hbase_offline.get_rows("CREDIT_V1_MOB_VAR", mobile_id)
    # a5 = hbase_offline.get_rows("CREDIT_V1_EXT_VAR", report_id)
    # b4 = hbase_offline.put_rows("CREDIT_V1_MOB_VAR", "test_offline1"[::-1],a4)
    # b5 = hbase_offline.put_rows("CREDIT_V1_EXT_VAR", "test_offline2"[::-1], a5)

    # a=np.random.rand(5)
    # print(a)
    # [ 0.64061262  0.8451399   0.965673    0.89256687  0.48518743]
    #
    # print(a[-1]) ###取最后一个元素
    # [0.48518743]
    #
    # print(a[:-1])  ### 除了最后一个取全部
    # [ 0.64061262  0.8451399   0.965673    0.89256687]
    #
    # print(a[::-1]) ### 取从后向前（相反）的元素
    # [ 0.48518743  0.89256687  0.965673    0.8451399   0.64061262]
    #
    # print(a[2::-1]) ### 取从下标为2的元素翻转读取
    # [ 0.965673  0.8451399   0.64061262]
