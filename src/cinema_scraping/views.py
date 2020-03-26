from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from scrapyd_api import ScrapydAPI

from . import tasks


# connect scrapyd service
scrapyd_service = ScrapydAPI('http://localhost:6800')
scrapyd_service.schedule('web', 'cinemar_crawler')

def is_valid_url(url):
    validate = URLValidator()
    try:
        validate(url) # check format of url
    except ValidationError:
        return False
    return True


@csrf_exempt
@api_view(['GET'])
def get_movie_time(request):
    """
    request's body:
    {
        "site_name": "CGV"
    }
    return:
    {
        "status_code": 200
        "message": "SUCCEEDED"
        "body": {
            "data": "..."
        }
    }
    """
    tasks.shared_task.delay(request.get('site_name', 'CGV'))
