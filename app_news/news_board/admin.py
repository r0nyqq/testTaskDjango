from django.contrib import admin
from .models import NewsModel


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']