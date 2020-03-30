# -*- coding: utf-8 -*-
# import scrapy
# from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# from scrapy_app.items import CinemaItem


class CinemaCrawlerSpider(CrawlSpider):
    name = 'cinema_crawler'
    start_urls = ['https://www.cgv.vn/en/cinox/site/cgv-vinh-trung-plaza/']

    def parse(self, response):
        SET_SELECTOR = '.day'
        data = response.css(SET_SELECTOR)
        for brickset in data:
            yield {
                'app': 'cinema',
                'data': {
                    'month': int(brickset.css('span::text').get().strip()),
                    'day_of_week': str(brickset.css('em::text').get().strip()),
                    'day_of_month': int(brickset.css('strong::text').get().strip())
                }
            }
