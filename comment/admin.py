# First-party
from .models import Comment
# Django
from django.contrib import admin


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "content_type", "object_id", "content_object", "created_date", "published_date")