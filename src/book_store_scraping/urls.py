from django.urls import path
from . import views

urlpatterns = [
    path('get_raw_html', views.get_raw_html, name="get raw html of website")
]