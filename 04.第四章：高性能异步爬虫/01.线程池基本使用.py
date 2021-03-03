#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/21 10:29
# @Author  : name
# @File    : 01.线程池基本使用.py
import time
from multiprocessing.dummy import Pool  # 导入线程池模块对应的类
'''
# 使用单线程串行方式执行
def get_page(str):
    print('正在下载：', str)
    time.sleep(2)
    print('下载成功：', str)

name_list = ['jinxiang', 'aa', 'bb', 'cc']

start_time = time.time()

for i in range(len(name_list)):
    get_page(name_list[i])

end_time = time.time()
print('%d second'% (end_time - start_time))
'''

# 使用线程池的方式执行
def get_page(str):
    print('正在下载：', str)
    time.sleep(2)
    print('下载成功：', str)

name_list = ['jinxiang', 'aa', 'bb', 'cc']

start_time = time.time()

pool = Pool(4)
pool.map(get_page, name_list)

end_time = time.time()
print('%d second'% (end_time - start_time))