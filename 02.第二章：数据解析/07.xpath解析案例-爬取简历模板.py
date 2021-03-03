#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 14:11
# @Author  : name
# @File    : 07.xpath解析案例-爬取简历模板.py
import requests
from lxml import etree
import os
# 现存问题：1.未解决滚动刷新的爬取，2.未解决切换主题的页面的爬取
if __name__ == "__main__":
    if not os.path.exists('./template'):
        os.mkdir('./template')
    url = 'https://landing.zhaopin.com/resume-templates'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }
    page_text = requests.get(url=url, headers=headers).text
    
    # 解析
    tree = etree.HTML(page_text)
    a_list = tree.xpath('//div[@class="resume-templates-list__container"]/a')
    for a in a_list:
        template_url = 'https://landing.zhaopin.com' + a.xpath('./@href')[0] + '/download'
        template_name = a.xpath('./span/text()')[0]
        template_text = requests.get(url=template_url, headers=headers).text

        path = './template/' + template_name + '.doc'
        template = requests.get(url=url, headers=headers).content
        with open(path, 'wb') as fp:
            fp.write(template)
        print(template_name + "爬取完毕！")