import scrapy


class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['https://www.cgv.vn/en/cinox/site/cgv-vincom-da-nang/']

    def parse(self, response):
        SET_SELECTOR = '.day'
        for brickset in response.css(SET_SELECTOR):
            yield {
                "month": brickset.css('span::text').get().strip(),
                "day of week": brickset.css('em::text').get().strip(),
                "day of month": brickset.css('strong::text').get().strip(),
            }
        #     # NAME_SELECTOR = 'h1 ::text'
        #     PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
        #     MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
        #     # IMAGE_SELECTOR = 'img ::attr(src)'
        #     yield {
        #         # 'name': brickset.css(NAME_SELECTOR).extract_first(),
        #         'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
        #         'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
        #         # 'image': brickset.css(IMAGE_SELECTOR).extract_first(),
        #     }
