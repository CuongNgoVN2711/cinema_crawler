# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from .items import CinemaItem
from cinema_scraping.models import ScrapedDate

class ScrapyAppPipeline(object):
    def __init__(self):
        self.data = None

    # def close_spider(self, spider):
    #     print(self.data)

    def process_item(self, item, spider):
        print("+++++++++++++")
        print(item)
        cinema_item = CinemaItem()
        cinema_item['month'] = item['month']
        cinema_item['day_of_week'] = item['day_of_week']
        cinema_item['day_of_month'] = item['day_of_month']
        cinema_item.save()
        # item.save()
        return item
