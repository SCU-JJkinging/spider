#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 17:39
# @Author  : name
# @File    : 02.人人网模拟登录.py
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
    url = 'http://www.renren.com/SysHome.do'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    # 解析验证码图片img中src属性值
    img_src = tree.xpath('//*[@id="verifyPic_login"]/@src')[0] # 得到验证码图片的url
    img_data = requests.get(url=img_src, headers=headers).content # 得到验证码图片
    # 将验证码图片保存到本地
    with open('./code.jpg', 'wb') as fp:
        fp.write(img_data)
    # 调用打码平台的示例程序进行验证码图片识别
    result = get_codeText('code.jpg', 1005)
    print('识别结果：', result)

    #模拟登录
    # 先在登录页面获取__VIEWSTATE和__VIEWSTATEGENERATOR的值  (针对存在这些值的情况)
    # viewState = tree.xpath('//*[@id="aspnetForm"]/div[1]/input/@value')[0]
    # viewStateGenerator = tree.xpath('//*[@id="aspnetForm"]/div[2]/input/@value')[0]
    # print(viewStateGenerator)

    # post请求的发送（模拟登录）
    login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=202116227993'
    data = {
        'email': '2452393862@qq.com',
        'icode':'',
        'origURL': 'http://www.renren.com/home',
        'domain': 'renren.com',
        'key_id': '1',
        'captcha_type': 'web_login',
        'password': '455b605153819ff286d617e1977c7dab075f61319b7074144ff8957f2296cd1c',
        'rkey': '6466b6af25f60536b4dfcf4f559dce36',
        'f': 'http%3A%2F%2Fwww.renren.com%2F976195451%2Fnewsfeed%2Fphoto'
    }
    response = requests.post(url=login_url, data=data, headers=headers)
    print(response.status_code)
    page_text2 = response.text
    with open('./人人网.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text2)
    print('over!!!')

