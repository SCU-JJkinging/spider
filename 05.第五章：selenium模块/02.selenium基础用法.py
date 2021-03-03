#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/22 13:47
# @Author  : JJkinging
# @File    : 02.selenium基础用法.py

from selenium import webdriver
from lxml import etree
from time import sleep

# 实例化一个浏览器对象（传入浏览器的驱动程序）
bro = webdriver.Chrome(executable_path=r'D:\DevelopmentSoftware\anaconda3\chromedriver')
# 让浏览器发起一个指定url对应请求
bro.get('http://scxk.nmpa.gov.cn:81/xk/')
# 使用page_source 获取获取浏览器当前页面的页面源码数据
page_text = bro.page_source

# 解析企业名称
tree = etree.HTML(page_text)
li_list = tree.xpath('//div[@class="dzpzmain"]//ul[2]/li')
for li in li_list:
    name = li.xpath('./dl/@title')[0]
    print(name)

sleep(3)
bro.quit()