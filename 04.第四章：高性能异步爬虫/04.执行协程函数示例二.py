#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/21 18:00
# @Author  : name
# @File    : 04.执行协程函数示例二.py
import asyncio

# await 就是等待对象的值得到结果之后再继续往下走

async def others():
    print('start')
    await asyncio.sleep(2)
    print('end')
    return "返回值"

async def func():
    print("指行协程函数内部代码")

    response = await others()

    print('IO请求结束， 结果为：', response)

asyncio.run(func())