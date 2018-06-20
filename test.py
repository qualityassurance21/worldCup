# -*- coding: utf-8 -*-
# @Time    : 2018/6/18 9:22
# @Author  : Torre
# @Email   : klyweiwei@163.com
import time
import datetime
import getSoup
import requests
import re

# date = 152898840000
# date = str(date)
# date = date[0:10]
# date = int(date)
# print(date)
# time_local = time.localtime(date)
# # 转换成新的时间格式(2016-05-05 20:28:54)
# dt = time.strftime("%Y-%m-%d", time_local)
# print(dt)
# print(time.time())

url = 'http://api.sports.163.com/api/football/v1/2018/1002/16/groupInfo/groupby?groupType=groupName'
response = requests.get(url)
response.raise_for_status()
res = response.text
# print(res)
# re = re.compile(r'"homeLogo":"(.+?)",')
# homeLogo = re.findall(res)
# print(homeLogo)
# re = re.compile(r'"date":(.+?),')
# re = re.compile(r'"home":"(.+?)",')
re =re.compile(r'(http(s).*?png)')
print(re.findall(res))

for i in range(0,10):
    print(i)