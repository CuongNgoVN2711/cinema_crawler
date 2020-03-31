from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('get_raw_html/<str:next_page>', views.get_raw_html, name="get raw html of website"),
    path('crawl_books', views.start_crawl_book, name="trigger spider"),
    path('get_books/<str:task_id>', views.get_book, name="trigger spider")
]