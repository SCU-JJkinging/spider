#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/22 14:44
# @Author  : JJkinging
# @File    : 04.动作链和iframe的处理.py
from selenium import webdriver
import time
from selenium.webdriver import ActionChains

bro = webdriver.Chrome(executable_path=r'D:\DevelopmentSoftware\anaconda3\chromedriver')
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
#如果定位的标签是存在于iframe标签之中的则必须通过如下操作在进行标签定位
bro.switch_to.frame('iframeResult')#切换浏览器标签定位的作用域
div = bro.find_element_by_id('draggable')

# 动作链
action = ActionChains(bro)

# 点击长按指定的标签
action.click_and_hold(div)

for i in range(5):
    # perform()立即执行动作链操作
    # move_by_offset(x,y):x水平方向 y竖直方向
    action.move_by_offset(17, 0).perform()

# 释放动作链
action.release()

# 关闭浏览器
time.sleep(5)
bro.quit()