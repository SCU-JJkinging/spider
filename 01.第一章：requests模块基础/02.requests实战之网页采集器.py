#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 22:57
# @Author  : name
# @File    : 02.requests实战之网页采集器.py

import requests

if __name__ == "__main__":
    # UA伪装：将对应的user-agent封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }
    url = 'https://www.sogou.com/web'
    # 处理url携带的参数，封装到字典中
    kw = input('enter a word:')
    param = {
        'query': kw
    }
    response = requests.get(url=url, params=param, headers=headers)
    page_text = response.text
    fileName = kw + '.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName, '保存成功！！！')
