#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/21 12:52
# @Author  : name
# @File    : 03.执行协程函数示例一.py
import asyncio

async def fun():
    print('来玩啊')
    response = await asyncio.sleep(2)
    print("结束", response)

# result = fun()
# loop = asyncio.get_event_loop()
# loop.run_until_complete(result)
asyncio.run(fun())


'''理解事件循环

# 伪代码

任务列表 = [ 任务一， 任务二， 任务三...]

while True:
    可执行的任务列表， 已完成的任务列表 = 去任务列表中检查所有的任务，将‘可执行’和‘已完成’的任务返回
    
    for 就绪任务 in 可执行的任务列表：
        执行已就绪的任务
        
    for 已完成的任务 in 已完成的任务列表:
        在任务列表中移除 已完成的任务
        
    如果 任务列表 中的任务都已完成，则终止循环

'''