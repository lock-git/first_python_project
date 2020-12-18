# -*- coding: utf-8 -*-

import datetime
import inspect
import json
import logging.config
import os
import sys

logConfig = {
    'disable_existing_loggers': False,
    'version': 1,
    'formatters': {
        'logFormatter': {
            'format': '%(process)d - %(levelname)s - %(asctime)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        } #这里可以添加其他的 logFormatter 配置，其他的就和字典一样重新取个名字即可，添加一个键值对
    },
    'handlers': {
        'logHandler': {
            'level': 'INFO',
            'formatter': 'logFormatter',
            'class': 'logging.FileHandler',
            'filename': '{log_homeroot}/log/{logfilename}_{logdate}.log'.format(log_homeroot=os.getcwd(),logfilename='upload_data_data_process_column',logdate=str(datetime.date.today()).replace('-','_'))
        } #这里可以添加其他的 logHandler 配置，其他的就和字典一样重新取个名字即可，添加一个键值对
    },
    'loggers': {
        'drugProject': {
            'handlers': ['logHandler'],
            'level': 'INFO',
            'propagate': False
        }
    }
}

logging.config.dictConfig(logConfig)
logger = logging.getLogger('drugProject')

def printException(info=None,description=None):
    """
    返回异常信息
    :param info: 异常信息
    :return: None
    """
    exception_class, exception_info, exception_traceback = sys.exc_info()
    if ((exception_class is None) or (exception_info is None) or (exception_traceback is None)):
        baseErrorMessage = ''
    else:
        baseErrorMessage = '[{}];[{}] - [{}];[{}]'.format(inspect.stack()[1][1], exception_traceback.tb_lineno,
                                                          exception_class, exception_info)
    # 产生日志消息内容
    if description is None:
        logcontent=info
    else:
        try:
            try:
                logcontent='{} : {}'.format(description,info)
            except:
                try:
                    logcontent = u'{} : {}'.format(description, info)
                except:
                    logcontent = u'{} : {}'.format(json.dumps(description), json.dumps(info))
        except:
            logcontent=info
    # 记录正式日志
    try:
        try:
            log_info = '{} - ** - {}'.format(baseErrorMessage, logcontent)
        except:
            try:
                log_info = u'{} - ** - {}'.format(baseErrorMessage, logcontent)
            except:
                log_info = u'{} - ** - {}'.format(json.dumps(baseErrorMessage), json.dumps(logcontent))
    except:
        try:
            try:
                logger.error(json.dumps(baseErrorMessage))
            except:
                logger.error(baseErrorMessage)
            try:
                print(datetime.datetime.now(), baseErrorMessage)
            except:
                print(datetime.datetime.now(), json.dumps(baseErrorMessage))
        except:
            pass
    else:
        try:
            try:
                logger.error(json.dumps(log_info))
            except:
                logger.error(log_info)
            try:
                print_log_info = '{} - {}'.format(datetime.datetime.now(), log_info)
            except:
                print_log_info = u'{} - {}'.format(datetime.datetime.now(), log_info)
            print(print_log_info)
        except:
            try:
                try:
                    logger.error(json.dumps(baseErrorMessage))
                except:
                    logger.error(baseErrorMessage)
                try:
                    print(datetime.datetime.now(), baseErrorMessage)
                except:
                    print(datetime.datetime.now(), json.dumps(baseErrorMessage))
            except:
                pass


def printInfo(info=None,description=None):
    """
    打印基本执行过程中的信息
    :param info: 基本执行信息
    :return: None
    """
    baseInformation = '[{}];[{}]'.format(inspect.stack()[1][1], inspect.currentframe().f_back.f_lineno)
    # 产生日志消息内容
    if description is None:
        logcontent = info
    else:
        try:
            try:
                logcontent='{} : {}'.format(description,info)
            except:
                try:
                    logcontent = u'{} : {}'.format(description, info)
                except:
                    logcontent = u'{} : {}'.format(json.dumps(description), json.dumps(info))
        except:
            logcontent=info
    # 记录正式日志
    try:
        try:
            log_info = '{} - ** - {}'.format(baseInformation, logcontent)
        except:
            try:
                log_info = u'{} - ** - {}'.format(baseInformation, logcontent)
            except:
                log_info = u'{} - ** - {}'.format(json.dumps(baseInformation), json.dumps(logcontent))
    except:
        try:
            try:
                logger.info(json.dumps(logcontent))
            except:
                logger.info(logcontent)
        except:
            try:
                try:
                    print(datetime.datetime.now(),baseInformation)
                except:
                    print(datetime.datetime.now(), json.dumps(baseInformation))
            except:
                pass
        else:
            try:
                try:
                    print(datetime.datetime.now(),logcontent)
                except:
                    print(datetime.datetime.now(), json.dumps(logcontent))
            except:
                pass
    else:
        try:
            try:
                logger.info(json.dumps(log_info))
            except:
                logger.info(log_info)
            try:
                print_log_info = '{} - {}'.format(datetime.datetime.now(), log_info)
            except:
                print_log_info = u'{} - {}'.format(datetime.datetime.now(), log_info)
            print(print_log_info)
        except:
            try:
                try:
                    print(datetime.datetime.now(),baseInformation)
                except:
                    print(datetime.datetime.now(), json.dumps(baseInformation))
            except:
                pass


if __name__ == '__main__':
    try:
        1 / 0
    except:
        printException(info='...error...')
    printInfo(info='.......the exception information .....')
    printInfo(info='北京我来了')

