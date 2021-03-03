#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/22 14:16
# @Author  : JJkinging
# @File    : 03.selenium其它自动化操作.py
import time
from selenium import webdriver

bro = webdriver.Chrome(executable_path=r'D:\DevelopmentSoftware\anaconda3\chromedriver')
bro.get('https://www.bilibili.com/')

# 标签定位
search_input = bro.find_element_by_class_name('nav-search-keyword')
# 标签交互
search_input.send_keys('爬虫')

# 执行一组js程序
bro.execute_script('window.scrollTo(0, document.body.scrollHeight)')
time.sleep(4)

# 点击搜索按钮
btn = bro.find_element_by_css_selector('.bili-icon_dingdao_sousuo')
btn.click()

time.sleep(4)
bro.quit()