import happybase


class HBaseUtil(object):
    # 获取一个连接
    def getHbaseConnection(self):
        conn = happybase.Connection(host='172.16.249.56', port=9090, timeout=None, autoconnect=True,
                                    table_prefix=None, table_prefix_separator=b'_', compat='0.98',
                                    transport='buffered', protocol='binary')
        return conn

    # 返回单行数据，返回tuple
    def querySingleLine(self, table, rowkey):
        conn = self.getHbaseConnection()
        t = happybase.Table(table, conn)
        return t.row(rowkey)

    # 返回多行数据，返回dict
    def queryMultilLines(self, table, list):
        conn = self.getHbaseConnection()
        t = happybase.Table(table, conn)
        return dict(t.rows(list))

    # 批量插入数据
    def batchPut(self, table):
        conn = self.getHbaseConnection()
        t = happybase.Table(table, conn)
        batch = t.batch(batch_size=10)
        return batch

    # exmple
    # batch_put = batchPut(table)
    #     person1 = {'info:name': 'lianglin', 'info:age': '30', 'info:addr': 'hubei'}
    #     person2 = {'info:name': 'jiandong', 'info:age': '22', 'info:addr': 'henan', 'info:school': 'henandaxue'}
    #     person3 = {'info:name': 'laowei', 'info:age': '29'}
    #     with batch_put as bat:
    #         bat.put('lianglin', person1)
    #         bat.put('jiandong', person2)
    #         bat.put('laowei', person3)

    # 插入单条数据
    def singlePut(self, table, rowkey, data):
        conn = self.getHbaseConnection()
        t = happybase.Table(table, conn)
        t.put(rowkey, data=data)

    # 批量删除数据
    def batchDelete(self, table, rowkeys):
        conn = self.getHbaseConnection()
        t = happybase.Table(table, conn)
        with t.batch() as bat:
            for rowkey in rowkeys:
                bat.delete(rowkey)

    # 删除单行数据
    def singleDelete(self, table, rowkey):
        conn = self.getHbaseConnection()
        t = happybase.Table(table, conn)
        t.delete(rowkey)

    # 删除多个列族的数据
    def deleteColumns(self, table, rowkey, columns):
        conn = self.getHbaseConnection()
        t = happybase.Table(table, conn)
        t.delete(rowkey, columns=columns)

    # 删除一个列族中的几个列的数据
    def deleteDetailColumns(self, table, rowkey, detailColumns):
        conn = self.getHbaseConnection()
        t = happybase.Table(table, conn)
        t.delete(rowkey, columns=detailColumns)

    # 清空表
    def truncatTable(self, table, name, families):
        conn = self.getHbaseConnection()
        conn.disable_table(table)
        conn.delete_table(table)
        conn.create_table(table, name, families)

    # 删除hbase中的表
    def deletTable(self, table):
        conn = self.getHbaseConnection()
        conn.disable_table(table)
        conn.delete_table(table)

    # 扫描一张表
    def scanTable(self, table, row_start, row_stop, row_prefix):
        conn = self.getHbaseConnection()
        t = happybase.Table(table, conn)
        scan = t.scan(row_start=row_start, row_stop=row_stop, row_prefix=row_prefix)
        for key, value in scan:
            print(key, value)
