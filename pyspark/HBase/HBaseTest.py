import website as website

from pyspark.HBase import HBaseUtil
import happybase
import thrift

if __name__ == "__main__":
    # 创建连接，通过参数size来设置连接池中连接的个数

    # 注意：需要连接的是 HBase Thrift Server [CDH 的 HBase]

    mobile_id = "52100000"[::-1]
    report_id = "24899000"[::-1]
    print("mobile_id == %s" % mobile_id)
    print("report_id == %s" % report_id)
    print("^^^^report_id == ^%s" % report_id)
    print("report_id + mobile_id == %s:%s" % (report_id,mobile_id))



    # connection = happybase.Connection(host='172.16.249.60', port=9090, timeout=None, autoconnect=True,
    #                                   table_prefix=None, table_prefix_separator=b'_', compat='0.98',
    #                                   transport='buffered', protocol='binary')
    # families = {
    #     'cf1': dict(max_versions=10),
    #     'cf2': dict(max_versions=1, block_cache_enabled=False),
    #     'cf3': dict()
    # }
    # tables = connection.table("MY_HBASE_TABLE_CONN")
    # for k in tables.families().keys():
    #     print(k)
    #     print(tables.families().get(k))
    #
    # connection.close()

