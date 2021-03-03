#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/19 13:02
# @Author  : name
# @File    : 06.requests实战之药监总局相关数据爬取.py
import requests
import json

if __name__ == "__main__":
    # 批量获取不同企业的id值
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }
    id_list = []
    for page in range(1, 6):
        page = str(page)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': '',
        }
        page_json = requests.post(url=url, data=data, headers=headers).json()
        for dict in page_json['list']:
            id_list.append(dict['ID'])

    # 根据id拼接url获取企业许可证信息
    url2 = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    data_list = []
    for id in id_list:
        data2 = {
            'id': id
        }
        data_json = requests.post(url=url2, data=data2, headers=headers).json()
        # print(data_json)
        data_list.append(data_json)
    fp = open('./yaojianzongju.json', 'w', encoding='utf-8')
    json.dump(data_list, fp, ensure_ascii=False)
    fp.close()
    print('over!')