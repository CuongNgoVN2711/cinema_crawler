# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from .items import CinemaItem, BookStoreItem
from cinema_scraping.models import ScrapedDate
from book_store_scraping.models import Book

class ScrapyAppPipeline(object):
    def __init__(self):
        self.data = None

    def process_item(self, item, spider):
        if item.get('app', '') == 'cinema':
            cinema_item = CinemaItem()
            cinema_item['month'] = item['data']['month']
            cinema_item['day_of_week'] = item['data']['day_of_week']
            cinema_item['day_of_month'] = item['data']['day_of_month']
            cinema_item.save()
            return item
        if item.get('app', '') == 'book':
            bs_item = BookStoreItem()
            bs_item['name'] = item['data']['name']
            bs_item['author'] = item['data']['author']
            bs_item['price'] = item['data']['price']
            bs_item['category'] = item['data']['category']
            bs_item['review_number'] = item['data']['review_number']
            bs_item['rating'] = item['data']['rating']
            bs_item.save()
            return item
