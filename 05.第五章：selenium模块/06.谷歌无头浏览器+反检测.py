#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/22 15:26
# @Author  : JJkinging
# @File    : 06.谷歌无头浏览器+反检测.py
from selenium import webdriver
from time import sleep
# 实现无可视化界面的
from selenium.webdriver.chrome.options import Options
# 实现规避检测的
from selenium.webdriver import ChromeOptions

# 实现无可视化界面的操作
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 实现对selenum的规避检测
options = ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])

bro = webdriver.Chrome(executable_path=r'D:\DevelopmentSoftware\anaconda3\chromedriver', chrome_options=chrome_options,
                       options=options)

# 无头浏览器
bro.get('https://www.baidu.com')

print(bro.page_source)
sleep(2)
bro.quit()