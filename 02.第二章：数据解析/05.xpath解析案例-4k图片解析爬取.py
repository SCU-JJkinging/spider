#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/19 21:47
# @Author  : name
# @File    : 05.xpath解析案例-4k图片解析爬取.py
import requests
from lxml import etree
import os

if __name__ == "__main__":
    if not os.path.exists('./picture'):
        os.mkdir('./picture')
    url = 'http://pic.netbian.com/4kmeinv/index.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)

    # [方法一] 手动设定响应数据的编码格式
    response.encoding = response.apparent_encoding

    page_text = response.text

    # 数据解析： src的属性  alt属性
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="slist"]//li')
    for li in li_list:
        img_src = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
        img_alt = li.xpath('./a/img/@alt')[0] + '.jpg'
        img_href = 'http://pic.netbian.com' + li.xpath('./a/@href')[0]
        # 方法二 通用解决中文乱码的方案
        # img_alt = img_alt.encode('iso-8859-1').decode('gbk')
        # print(img_src, img_alt, img_href)
        page = requests.get(url=img_href, headers=headers).text
        tree2 = etree.HTML(page)
        div_list = tree2.xpath('//div[@class="photo-pic"]/a/img/@src')
        for meinv_url in div_list:
            meinv_url = 'http://pic.netbian.com'+ meinv_url
            img_data = requests.get(url=meinv_url, headers=headers).content
            img_path = './picture/' + img_alt
            with open(img_path, 'wb') as fp:
                fp.write(img_data)
                print(img_alt, '下载成功！！！')


