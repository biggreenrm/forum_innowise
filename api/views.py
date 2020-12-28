# First-party
from topic.models import Topic
from comment.models import Comment
from likedislike.models import LikeDislike
from .serializers import TopicSerializer, CommentSerializer, LikeDislikeSerializer, UserSerializer
from .mixins import LikedDislikedMixin
# Django
from django.shortcuts import render
from django.contrib.auth import get_user_model
# Third-party
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters import rest_framework as filters


User = get_user_model()


"""
Работа с моделями по лайтовому пути - много магии, мало гибкости (она и не нужна).
"""

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class TopicViewSet(viewsets.ModelViewSet, LikedDislikedMixin):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ('author', 'title', 'theme', 'created_date')

class CommentViewSet(viewsets.ModelViewSet, LikedDislikedMixin):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ('user',)


class LikeDislikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeDislikeSerializer
    queryset = LikeDislike.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )
