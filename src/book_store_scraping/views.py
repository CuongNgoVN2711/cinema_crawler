from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

import requests
from lxml import html


@api_view(['GET'])
@csrf_exempt
def get_raw_html(request):
    url = "https://tiki.vn/tu-sach-ceo-tran-ngoc-thai-son/c22218?src=lp-191&_lc="
    res = requests.get(url)
    # raw = html.fromstring(res.content)
    return HttpResponse(res.content)