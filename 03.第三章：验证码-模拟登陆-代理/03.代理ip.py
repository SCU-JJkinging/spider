#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 23:21
# @Author  : name
# @File    : 03.代理ip.py
import requests

if __name__ == "__main__":
    url = 'https://www.baidu.com/s?wd=ip'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }
    page_text = requests.get(url=url, headers=headers, proxies={'https': '175.43.33.44:9999'}).text
    with open('./ip.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)