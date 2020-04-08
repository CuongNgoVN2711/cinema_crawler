from celery import shared_task
from django.core.management import call_command


@shared_task
def crawl_book():
    call_command('crawl_book')