# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CinemaCrawlerSpider(CrawlSpider):
    name = 'cinema_crawler'
    start_urls = ['https://www.cgv.vn/en/cinox/site/cgv-vincom-da-nang/']

    def parse(self, response):
        SET_SELECTOR = '.day'
        for brickset in response.css(SET_SELECTOR):
            yield {
                "month": brickset.css('span::text').get().strip(),
                "day of week": brickset.css('em::text').get().strip(),
                "day of month": brickset.css('strong::text').get().strip(),
            }
