#! /usr/bin/env python
# -*- coding: utf-8 -*-
import scrapy
from qiubaiPro.items import QiubaiproItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    # def parse(self, response):
    #     div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
    #     all_data = []
    #     for div in div_list:
    #         # xpath返回的是列表，但是列表元素一定是Selector类型的对象
    #         # extract可以将Selector对象中data参数存储的字符串提取出来
    #         author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
    #         # 列表调用了extract之后，则表示将列表中每一个Selector对象中data对应的字符串提取了出来,返回一个列表
    #         content = div.xpath('./a/div/span//text()').extract()
    #         content = ''.join(content)
    #         dict = {
    #             'author': author,
    #             'content': content
    #         }
    #         all_data.append(dict)
    #     return all_data

    def parse(self, response):
        div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
        for div in div_list:
            # xpath返回的是列表，但是列表元素一定是Selector类型的对象
            # extract可以将Selector对象中data参数存储的字符串提取出来
            author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            # 列表调用了extract之后，则表示将列表中每一个Selector对象中data对应的字符串提取了出来,返回一个列表
            content = div.xpath('./a/div/span//text()').extract()
            content = ''.join(content)

            item = QiubaiproItem()
            item['author'] = author
            item['content'] = content
            # 将item提交给管道
            yield item

