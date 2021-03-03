#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/21 19:36
# @Author  : name
# @File    : 05.Task对象示例.py
import asyncio

async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return '返回值'

async def main():
    print("main开始...")

    # 创建Task列表，里面是Task对象
    task_list = {
        asyncio.create_task(func(), name='n1'),
        asyncio.create_task(func(), name='n2')
    }

    print('main结束...')
    done, pending = await asyncio.wait(task_list, timeout=None)
    print(done)
    print(pending)

asyncio.run(main())