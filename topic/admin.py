# First-party
from .models import Topic

# Django
from django.contrib import admin


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "theme", "text", "created_date", "published_date")
    list_filter = ("author", "title", "theme", "text", "created_date", "published_date")
    search_fields = ("text",)
    ordering = ("created_date", "author")


# To-do:
#   1. Сделать так, чтобы текст в админке сокращался