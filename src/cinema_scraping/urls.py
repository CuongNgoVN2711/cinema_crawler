from django.urls import path
from . import views

urlpatterns = [
    path('movie_time', views.get_movie_time, name="get all movie times")
]