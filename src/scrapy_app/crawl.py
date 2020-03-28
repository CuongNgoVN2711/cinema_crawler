from django.core.management.base import BaseCommand
from .spiders import cinema_crawler
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())
        process.crawl(cinema_crawler.CinemaCrawlerSpider)
        process.start()
# def crawl():
#     process = CrawlerProcess(get_project_settings())
#     process.crawl(cinema_crawler.CinemaCrawlerSpider)
#     process.start()
#
# crawl()