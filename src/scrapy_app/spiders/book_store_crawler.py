# -*- coding: utf-8 -*-
# import scrapy
# from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy import FormRequest, Request

# from scrapy_app.items import CinemaItem, BookStoreItem


class BookStoreCrawlerSpider(CrawlSpider):
    name = 'book_store_crawler'
    # start_urls = ["https://www.cgv.vn/en/cinox/site/cgv-vincom-da-nang/"]
    start_urls = ["http://0.0.0.0:8000/book_scraping/get_raw_html/None"]

    def parse(self, response):
        SET_SELECTOR = '.product-box-list'
        data = response.css(SET_SELECTOR).css('.product-item    ')
        # content = data.css('.content ')
        for brickset in data:
            review_content = brickset.css('a').css('.review-wrap')
            rating = review_content.css(".rating").css('.rating-content').css('span::attr(style)').get()
            price = brickset.xpath('@data-price').get().strip()
            category = brickset.xpath('@data-category')
            item = {
                'app': 'book',
                'data': {
                    'name': brickset.xpath('@data-title').get().strip(),
                    'author': brickset.xpath('@data-brand').get().strip(),
                    'price': price,
                    'category': category.get().strip()[category.get().strip().rfind('/')+1:],
                    'review_number': review_content.css(".review::text").get().strip('(').strip(')'),
                    'rating': rating.strip('width:') if rating is not None else '0%'
                }
            }
            yield item

        next_page = response.css('.next::attr(href)').get()
        if next_page is not None:
            next_page = self.start_urls[0].rstrip('None') + next_page[next_page.rfind('&page=')+6:]
            yield Request(next_page, callback=self.parse)
