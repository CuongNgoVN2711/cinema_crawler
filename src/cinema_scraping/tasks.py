import scrapy
from celery import shared_task
# from . import cinema_crawler

@shared_task()
def crawl_movie_time(site_name):
    pass
    # return cinema_crawler.crawl(site_name)

