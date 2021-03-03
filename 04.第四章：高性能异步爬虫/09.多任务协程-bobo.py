#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/22 11:50
# @Author  : name
# @File    : 09.多任务协程-bobo.py
import time
import asyncio

async def request(url):
    print("正在下载：", url)
    # 在异步协程中如果出现了同步模块相关的代码，那么就无法实现异步。
    # time.sleep(2)
    # 当在asyncio中遇到阻塞操作必须进行手动挂起
    await asyncio.sleep(2)
    print("下载完毕：", url)

start_time = time.time()
tasks = []
urls = [
    'www.baidu.com',
    'www.sogou.com',
    'www.goubanjia.com'
]

#任务列表：存放多个任务对象
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
#需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(tasks))

print(time.time() - start_time)