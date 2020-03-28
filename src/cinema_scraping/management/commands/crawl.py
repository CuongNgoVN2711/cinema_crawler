from django.core.management.base import BaseCommand
from scrapy_app.spiders import cinema_crawler
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.settings import Settings
from scrapy_app import settings


class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        c_settings = Settings()
        c_settings.setmodule(settings)
        process = CrawlerProcess(c_settings)
        process.crawl(cinema_crawler.CinemaCrawlerSpider)
        process.start()
