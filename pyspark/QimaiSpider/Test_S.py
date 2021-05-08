import csv
import datetime
import os
import queue
import threading
import time
from lxml import etree
import requests
from selenium import webdriver
import random

PROXY = "http://61.155.138.151:5010"

for i in range(3):
    print(random.randint(0, 9))
    req = requests.get(url=PROXY)
    print("--proxy-server={}".format(req.text))
