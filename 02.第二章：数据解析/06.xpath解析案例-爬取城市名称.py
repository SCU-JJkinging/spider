#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 13:40
# @Author  : name
# @File    : 06.xpath解析案例-爬取城市名称.py
import requests
from lxml import etree

if __name__ == "__main__":
    url = 'https://www.aqistudy.cn/historydata/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }
    page_text = requests.get(url=url, headers=headers).text
    # 解析
    tree = etree.HTML(page_text)
    city_list = []
    # 获取包含城市的a标签
    # a_list = tree.xpath('//div[@class="col-lg-9 col-md-8 col-sm-8 col-xs-12"]//a')
    a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    for a in a_list:
        city = a.xpath('./text()')[0]
        city_list.append(city)
    print (len(city_list), city_list)
