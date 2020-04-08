from django.contrib import admin
from . import models


class BookAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "price", "rating")
    search_fields = ("name",)
    ordering = ['name']

admin.site.register(models.Book, BookAdmin)