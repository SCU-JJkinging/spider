#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/19 0:23
# @Author  : JJingking
# @File    : 04.requests实战之豆瓣电影爬取.py
import requests
import json
if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',  # 从库中的第几部电影去取
        'limit': '20',   # 一次取出的个数
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }
    response = requests.get(url=url, params=param, headers=headers)
    list_data = response.json()
    # 持久化存储
    fp = open('./douban.json', 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)