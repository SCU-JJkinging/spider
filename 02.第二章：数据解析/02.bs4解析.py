#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/19 16:14
# @Author  : name
# @File    : 02.bs4解析.py

import requests
from bs4 import BeautifulSoup
# 需求：爬取诗词名句网中三国演义的目录及章节内容
if __name__ == "__main__":
    url = 'http://mathfunc.com/book/sanguoyanyi.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }
    page_text = requests.get(url=url, headers=headers).text
    # 在首页中解析出章节的标题和详情页的url
    # 1.实例化BeautifulSoup对象
    soup = BeautifulSoup(page_text, 'lxml')
    a_list = soup.select('.book-mulu > ul a')
    fp = open('./三国演义.txt', 'a', encoding='utf-8')
    for a in a_list:
        title = a.string  # 获取章节标题
        detail_url = 'http://mathfunc.com' + a['href'] # 获取到对应章节的url
        # print(detail_url)
        # 对详情页发起请求，解析页面内容
        detail_text = requests.get(url=detail_url, headers=headers).text
        detail_soup = BeautifulSoup(detail_text, 'lxml')
        data = ''  # 一个章节的内容
        for p in detail_soup.select('.chapter_content > p'):
            p = p.text  # 一个段落
            p = p.replace('\xa0\xa0\xa0\xa0', '')
            data += '\n'
            data += p
        fp.write(title + ':' + data + '\n')
        print(title, '爬取完毕！！！')
    fp.close()

