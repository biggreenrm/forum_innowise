# First-party
from .models import Topic
# Django
from django.shortcuts import render, get_object_or_404
from django.utils import timezone


def topic_list(request):
    topics = Topic.objects.all() # не забыть отфильтровать топики по дате публикации (чтобы скрыть левые)
    return render(request, "topic/topic_list.html", {"topics": topics})

def topic_detail(request, id):
    topic = get_object_or_404(Topic, id=id)
    return render(request, "topic/topic_details.html", {"topic": topic})