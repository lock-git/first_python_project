# -*- coding: utf-8 -*-
"""
这个文件是将一个字典数据自动转化成相应的sql语句
"""

def transformDataToInsertStatementSimple(datadict,tablename):
    """
    将数据转化成sql插入语句,其中所有的值都认为是字符串
    :param datadict: dict
    :param tablename: str or unicode
    :return: unicode
    """
    sql_insert_template=u"insert into {table}({fields_list}) values({fields_values_list})"
    field_name_list=[]
    field_value_list=[]
    for key in datadict.keys():
        try:
            field_name_list.append(unicode(key))
        except:
            field_name_list.append(unicode(key,encoding='utf8'))
        try:
            field_value_list.append(unicode(datadict.get(key)))
        except:
            field_value_list.append(unicode(datadict.get(key),encoding='utf8'))
    field_value_list=[u"'{}'".format(fieldvalue) for fieldvalue in field_value_list]
    sql=sql_insert_template.format(table=tablename,fields_list=u','.join(field_name_list),fields_values_list=u','.join(field_value_list))
    return sql


def transformDataToUpdateStatementSimple(datadict,tablename,queryfield,queryfieldvalue):
    """
    将数据转化成sql插入语句,其中所有的值都认为是字符串
    :param datadict: dict
    :param tablename: str or unicode
    :return: unicode
    """
    sql_update_template=u"update {table} set {keyvalue} where {queryfield}='{queryfieldvalue}'"
    keyvalue_list=[]
    for key in datadict.keys():
        try:
            key_unicode=unicode(key)
        except:
            key_unicode=unicode(key,encoding='utf8')
        try:
            value_unicode=unicode(datadict.get(key))
        except:
            value_unicode = unicode(datadict.get(key),encoding='utf8')
        keyvalue_unicode=u"{key}='{value}'".format(key=key_unicode,value=value_unicode)
        keyvalue_list.append(keyvalue_unicode)
    sql=sql_update_template.format(table=tablename,keyvalue=u','.join(keyvalue_list),queryfield=queryfield,queryfieldvalue=queryfieldvalue)
    return sql


if __name__=='__main__':
    # 测试
    pass