# -*- coding: UTF-8 -*-
__author__ = 'Joynice'
from faker import Faker
user_agent = Faker('zh-CN').user_agent()
# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"

import time

def get_header():
    return {
        'User-Agent': user_agent
    }

def get_time():
    return int(time.time())
# https://static.qimai.cn/static/js/manifest.e50676524e0070aea5f0.js