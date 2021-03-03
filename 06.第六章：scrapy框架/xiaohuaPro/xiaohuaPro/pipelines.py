# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class XiaohuaproPipeline(object):
    fp = None
    def open_spider(self, spider):
        print('爬虫开始...')
        self.fp = open('./xiaohua.txt', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        img_name = item['img_name']
        self.fp.write(img_name+'\n')
        return item
    
    def close_spider(self, spider):
        print('爬虫结束...')
        self.fp.close()
