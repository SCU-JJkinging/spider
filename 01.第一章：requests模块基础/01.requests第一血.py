#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 22:27
# @Author  : name
# @File    : 01.requests第一血.py

import requests

if __name__ == "__main__":
    # step1:指定url
    url = r'https://www.sogou.com/'
    # step2:发起请求
    reponse = requests.get(url = url)
    # setp3:获取响应数据  text返回的是字符串形式的响应数据
    page_text = reponse.text
    print(page_text)
    # step4:持久化存储
    with open('./sogou.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取数据结束！')
