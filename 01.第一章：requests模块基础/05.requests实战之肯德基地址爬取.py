#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/19 0:45
# @Author  : name
# @File    : 05.requests实战之肯德基地址爬取.py
import requests
import json
import ast

if __name__ == "__main__":
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'
    word = input('please input the addr:')
    data = {
        'op': 'keyword',
        'cname': '',
        'pid': '',
        'keyword': word,
        'pageIndex': '1',
        'pageSize': '10',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }
    response = requests.post(url, data, headers)
    addr_list = response.text
    addr_list = ast.literal_eval(addr_list)  # 将str类型的数据转为json类型
    fp = open('./kengdeji.json', 'w', encoding='utf-8')
    json.dump(addr_list, fp, ensure_ascii=False)
    print('over!!!')