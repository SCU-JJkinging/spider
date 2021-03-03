# -*- coding: utf-8 -*-
import scrapy
from xiaohuaPro.items import XiaohuaproItem

class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.521609.com/daxuexiaohua/']

    #生成一个通用的url模板(不可变)
    url = 'http://www.521609.com/daxuexiaohua/list3{num}.html'
    page_num = 2

    def parse(self, response):
        li_list = response.xpath('//*[@id="content"]/div[2]/div[2]/ul/li')
        for li in li_list:
            img_name = li.xpath('./a[2]/b/text() | ./a[2]/text()').extract_first()
            print(img_name)
            item = XiaohuaproItem()
            item['img_name'] = img_name
            yield item

        if self.page_num <= 58:
            new_url = self.url.format(num=str(self.page_num))
            self.page_num += 1
            #手动请求发送:callback回调函数是专门用作于数据解析
            yield scrapy.Request(url=new_url, callback=self.parse)
