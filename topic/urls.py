# First-party
from . import views
# Django
from django.urls import path


urlpatterns = [
    path("", views.topic_list, name="topics_list"),
]