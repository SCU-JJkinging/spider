#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/3 14:34
# @Author  : JJkinging
# @File    : FAQ问题爬取.py

from lxml import etree
import requests

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }
result_dict = {}
fp = open('./FQA.txt', 'w', encoding='utf-8')
for i in range(1, 9):
    if i == 1:
        print('开始爬取...')
        url = 'https://static.122.gov.cn/V1.22.2/static/helpMain/help-qa.html'
        page_text = requests.get(url=url, headers=headers).text
        # print(page_text)
        # 页面解析
        tree = etree.HTML(page_text)
        div = tree.xpath('/html/body/div[2]')[0]
        biaoti = div.xpath('./div[@class="title-bar"]/h3/text()')[0]
        # 题目数量
        tags_p = div.xpath('//*[@id="help-qa-basic"]/p')
        count = len(tags_p)//2
        fp.write(biaoti + '\n')
        for j in range(count):
            question = tags_p[j*2].xpath('.//text()')
            answer = tags_p[j*2+1].xpath('.//text()')
            # 去除\n\t\r
            question = question[1] + question[2].strip()
            answer2 = ''
            for k in range(len(answer)):
                answer2 += answer[k].replace('\r\n\t\t', '')
            fp.write(question+'\n'+answer2)
        print('第1类问题爬取完成')

    else:
        url = 'https://static.122.gov.cn/V1.22.2/static/helpMain/help-qa{num}.html'.format(num=str(i))
        page_text = requests.get(url=url, headers=headers).text
        # print(page_text)
        # print(page_text)
        # 页面解析
        tree = etree.HTML(page_text)
        div = tree.xpath('/html/body/div[2]')[0]
        biaoti = div.xpath('./div[@class="title-bar"]/h3/text()')[0]
        # 题目数量
        tags_p = div.xpath('//*[@id="help-qa-basic"]/p')
        count = len(tags_p) // 2
        fp.write(biaoti + '\n')
        for j in range(count):
            question = tags_p[j * 2].xpath('.//text()')
            answer = tags_p[j * 2 + 1].xpath('.//text()')
            # print(question)
            # 去除\n\t\r
            if len(question) == 2: # 处理特例
                question = question[0] + question[1].strip()
            else:
                question = question[1] + question[2].strip()
            answer2 = ''
            for k in range(len(answer)):
                answer2 += answer[k].replace('\r\n\t\t', '')
            fp.write(question + '\n' + answer2)
        print(f'第{i}类问题爬取完成')

print('爬取结束...')
fp.close()

