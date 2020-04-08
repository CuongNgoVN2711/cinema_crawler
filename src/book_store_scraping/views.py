from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from celery import current_app
from django.core.management import call_command

from .models import  Book
from . import tasks

import requests
from lxml import html


@api_view(['GET'])
@csrf_exempt
def get_raw_html(request, next_page):
    url = "https://tiki.vn/tu-sach-ceo-tran-ngoc-thai-son/c22218?src=lp-191&_lc="
    if next_page == "None":
        res = requests.get(url)
        return HttpResponse(res.content)
    else:
        url += "&page=" + next_page
        res = requests.get(url)
        return HttpResponse(res.content)


@api_view(['POST'])
@csrf_exempt
def start_crawl_book(request):
    # task = tasks.crawl_book.delay()
    call_command('crawl_book')
    return HttpResponse("task")


@api_view(['GET'])
@csrf_exempt
def get_book(request, task_id):
    task = current_app.AsyncResult(task_id)
    response_data = {'status': task.status}
    if task.status == "SUCCESS":
        books = Book.objects.all()
        response_data['books'] = books
    return HttpResponse(response_data)