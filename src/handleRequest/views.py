from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import time
from .tasks import run_double
from celery import current_app
from redis import Redis

# Create your views here.
@csrf_exempt
def handle(request):
    if request.method == 'POST':
        all_task = []
        for i in json.loads(request.body).get('tasks', []):
            task = run_double.delay(i)
            all_task.append({'id': task.id, 'status': task.status})
        return HttpResponse(all_task)


@csrf_exempt
def get_result(request, task_id):
    if request.method == 'GET':
        task = current_app.AsyncResult(task_id)
        response_data = {'task_status': task.status, 'task_id': task.id}

        if task.status == 'SUCCESS':
            response_data['results'] = task.get()
        return JsonResponse(response_data)
