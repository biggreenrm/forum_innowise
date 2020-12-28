# First-party
from .models import LikeDislike

# Django
from django.contrib import admin


@admin.register(LikeDislike)
class LikeDislikeAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "content_object", "vote")
