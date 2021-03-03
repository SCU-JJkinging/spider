#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/19 14:42
# @Author  : name
# @File    : 01.正则解析.py
import requests
import re
# 需求： 爬取糗事百科中热图板块下的所有图片
if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }
    # 使用通用爬虫对url中的一整张页面进行爬取
    # page_text = requests.get(url=url, headers=headers)
    # print(page_text)
# ex = '<div class="phimage">.*?<img src="(.*?)" data-thumb_url.*?</div>'

