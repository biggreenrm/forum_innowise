# First-party
from .models import Topic
# Django
from django.shortcuts import render, get_object_or_404
from django.utils import timezone


def topic_list(request):
    # такой фильтр позволяет отсеить неопубликованные топики
    topics = Topic.objects.all()
    #import pdb; pdb.set_trace()
    return render(request, "topic/topic_list.html", {"topics": topics})