# First-party
from topic.models import Topic
from comment.models import Comment
from likedislike.models import LikeDislike
from .serializers import TopicSerializer, CommentSerializer, LikeDislikeSerializer
# Django
from django.shortcuts import render
# Third-party
from rest_frameworl import viewsets
from django_filters import rest_framework as filters


class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ('author', 'title', 'theme', 'created_date')


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ('user', 'content_object', 'created_date')


class LikeDislikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeDislikeSerializer
    queryset = LikeDislike.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ('user', 'vote', 'content_object')
