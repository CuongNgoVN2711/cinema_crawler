import scrapy
from celery import shared_task


@shared_task()
def crawl_movie_time(site_name):
    pass

