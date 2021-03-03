#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/19 18:52
# @Author  : name
# @File    : 03.xpath解析基础.py
from lxml import etree
if __name__ == "__main__":
    tree = etree.parse('test.html')
    # r = tree.xpath('/html/head/title')
    # r = tree.xpath('/html//title')
    # r = tree.xpath('//title')
    # r = tree.xpath('//div[@class="song"]/p[3]')
    # r = tree.xpath('//div[@class="tang"]//li[5]/a/text()')
    # r = tree.xpath('//div[@class="tang"]//li[7]//text()')
    r = tree.xpath('//div[@class="song"]//img/@src')
    print(r)