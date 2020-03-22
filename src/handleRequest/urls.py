from django.urls import path

from . import views

urlpatterns = [
    path("handle", views.handle),
    path("get/<str:task_id>", views.get_result)
]