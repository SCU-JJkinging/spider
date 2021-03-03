#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 23:52
# @Author  : name
# @File    : 03.requests实战之破解百度翻译.py

import requests
import json
if __name__ == "__main__":
    post_url = 'https://fanyi.baidu.com/sug'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }
    word = input('please input the word:')
    # post请求参数处理（同get请求一致）,这里的data就等价于get请求的params参数
    data = {
        'kw': word
    }
    response = requests.post(url=post_url, data=data, headers=headers)
    # 获取响应数据：只有确认响应数据是json类型的，才能用json()方法
    dic_obj = response.json()
    print(dic_obj)
    # 持久化数据
    fp = open('./dog.json', 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)
    fp.close()
    print('over!!!')