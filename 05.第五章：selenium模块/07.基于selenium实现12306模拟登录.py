#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/22 16:50
# @Author  : JJkinging
# @File    : 07.基于selenium实现12306模拟登录.py
from time import sleep
from selenium import webdriver
# 实现规避检测的
from selenium.webdriver import ChromeOptions
from PIL import Image
from Chaojiying_Python.chaojiying import Chaojiying_Client
from selenium.webdriver import ActionChains

# 实现对selenum的规避检测
options = ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])

bro = webdriver.Chrome(executable_path=r'D:\DevelopmentSoftware\anaconda3\chromedriver', options=options)
# 浏览器全屏显示
bro.maximize_window()
bro.get('https://kyfw.12306.cn/otn/resources/login.html')

# 切换至账号登录
# bro.switch_to.frame('login_frame')
zhanghao_tag = bro.find_elements_by_xpath('//li[@class="login-hd-account"]/a')[0]
zhanghao_tag.click()
sleep(1)

# save_screenshot就是将当前页面进行截图且保存
bro.save_screenshot('./12306.png')

# 确定验证码图片对应的左上角和右下角的坐标（裁剪的区域就确定）
img_tag = bro.find_element_by_xpath('//*[@id="J-loginImg"]')
# 验证码图片左上角的坐标 x,y       {'x': 1016, 'y': 292}
location = img_tag.location
# 验证码标签对应的长和宽           {'height': 188, 'width': 300}
size = img_tag.size
# 左上角和右下角坐标
# 这里都乘以1.25的原因是由于笔记本的默认缩放大小是125%
rangle = (
    int(location['x'] * 1.25), int(location['y'] * 1.25), int((int(location['x'] + size['width'])) * 1.25), int((int(location['y'] + size['height']) * 1.25))
)
# 至此验证码图片区域就确定下来了

i = Image.open('./12306.png')
code_img_name = './code.png'
frame = i.crop(rangle)
frame.save(code_img_name)
# print(rangle)  # (1270, 365, 1645, 600)

# 将验证码图片提交给第三方打码平台（超级鹰）进行识别
chaojiying = Chaojiying_Client('2452393862', '098323610A1Mn4', '913086')
im = open('./code.png', 'rb').read()
json = chaojiying.PostPic(im, 9004)
result = json['pic_str']
print('result:', result)

# 要存储即将被点击的点的坐标  [[x1,y1],[x2,y2]]
all_list = []
if '|' in result:
    list_1 = result.split('|')
    count_1 = len(list_1)
    for i in range(count_1):
        xy_list = []
        x = int(list_1[i].split(',')[0])
        y = int(list_1[i].split(',')[1])
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)
else:
    x = int(result.split(',')[0])
    y = int(result.split(',')[1])
    xy_list = []
    xy_list.append(x)
    xy_list.append(y)
    all_list.append(xy_list)
print('坐标:', all_list)

#遍历列表，使用动作链对每一个列表元素对应的x,y指定的位置进行点击操作
for l in all_list:
    x = l[0]
    y = l[1]
    ActionChains(bro).move_to_element_with_offset(img_tag, x, y).click().perform()
    sleep(0.5)
    print('点击一次')

# 模拟登录
userName_tag = bro.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/input')
password_tag = bro.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/input')
userName_tag.send_keys('A098323610')
sleep(1)
password_tag.send_keys('098323610A1Mn4')
sleep(1)
# 点击登录按钮
bro.find_element_by_xpath('//*[@id="J-login"]').click()
sleep(5)
# bro.quit()