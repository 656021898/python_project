# -*- coding:utf-8 -*-
import requests
from splinter import Browser
import time

activity_url='http://test.h5.sosho.cn/activity/detail.html?id=10057'

#driver_name='firefox'默认为
browser = Browser()
browser.visit(activity_url)
time.sleep(5)
browser.find_element_by_id('bottom-button').click()

