#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/22 14:59
# @Author  : JJkinging
# @File    : 05.模拟登陆QQ空间.py
from time import sleep
from selenium import webdriver

bro = webdriver.Chrome(executable_path=r'D:\DevelopmentSoftware\anaconda3\chromedriver')
bro.get('https://i.qq.com/')

# 切换到iframe域
bro.switch_to.frame('login_frame')
switch = bro.find_element_by_id('switcher_plogin')
# 点击切换
switch.click()
#获取用户名和密码的输入标签
userName_tag = bro.find_element_by_id('u')
password_tag = bro.find_element_by_id('p')
sleep(1)
# 输入值
userName_tag.send_keys('2452393862')
sleep(1)
password_tag.send_keys('5412347A1Mn4')
sleep(1)

# 点击登录
submit_tag = bro.find_element_by_id('login_button')
#  点击
submit_tag.click()

sleep(20)

bro.quit()




