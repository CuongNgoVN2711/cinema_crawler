# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from cinema_scraping import models


class CinemaItem(DjangoItem):
    django_model = models.ScrapedDate
