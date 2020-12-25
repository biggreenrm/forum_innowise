# First-party
from topic.models import Topic
from comment.models import Comment
from likedislike.models import LikeDislike
from .serializers import TopicSerializer, CommentSerializer, LikeDislikeSerializer, UserSerializer
# Django
from django.shortcuts import render
from django.contrib.auth import get_user_model
# Third-party
from rest_framework import viewsets
from django_filters import rest_framework as filters


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ('author', 'title', 'theme', 'created_date')

# добавить фильтры, если получится
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class LikeDislikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeDislikeSerializer
    queryset = LikeDislike.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ('user', 'vote', 'content_object')
