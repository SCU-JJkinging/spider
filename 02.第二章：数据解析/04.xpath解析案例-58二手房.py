#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/19 20:41
# @Author  : name
# @File    : 04.xpath解析案例-58二手房.py
from lxml import etree
import requests
# 需求：爬取58二手房中的房源信息
if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }
    # 爬取到页面源码数据
    url = 'https://gaoan.58.com/ershoufang/'
    page_text = requests.get(url=url, headers=headers).text

    # 数据解析
    tree = etree.HTML(page_text)
    fp = open('./58.txt', 'w', encoding='utf-8')
    title_list = tree.xpath('//div[@class="property-content-title"]')
    for div in title_list:
        title = div.xpath('./h3/text()')[0]
        fp.write(title+'\n')
        print(title)


