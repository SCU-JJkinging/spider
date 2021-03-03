#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 16:10
# @Author  : name
# @File    : 01.古诗文网验证码识别.py

import requests
from lxml import etree
from Chaojiying_Python.chaojiying import Chaojiying_Client  # 导入第三方打码助手


def get_codeText(img_name, code_type):
    chaojiying = Chaojiying_Client('2452393862', '098323610A1Mn4', '913086')  # 普通用户名  密码  软件ID
    im = open(img_name, 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    result_json = chaojiying.PostPic(im, code_type)  # code_type: 验证码类型
    result = result_json['pic_str']
    return result

if __name__ == "__main__":
    # 将验证码图片下载到本地
    url = 'https://so.gushiwen.org/user/login.aspx'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    # 解析验证码图片img中src属性值
    img_src = 'https://so.gushiwen.org' + tree.xpath('//*[@id="imgCode"]/@src')[0]  # 得到验证码图片的url
    img_data = requests.get(url=img_src, headers=headers).content # 得到验证码图片
    # 将验证码图片保存到本地
    with open('./code.jpg', 'wb') as fp:
        fp.write(img_data)
    # 调用打码平台的示例程序进行验证码图片识别
    result = get_codeText('code.jpg', 1004)
    print('识别结果：', result)