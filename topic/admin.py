# First-party
from .models import Topic

# Django
from django.contrib import admin


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
        "title",
        "theme",
        "created_date",
        "published_status",
    )
    list_filter = ("author", "title", "theme", "created_date", "published_status")
    search_fields = ("text",)
    ordering = ("created_date", "author")
