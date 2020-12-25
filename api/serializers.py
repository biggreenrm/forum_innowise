from rest_framework import serializers
from topic.models import Topic
from comment.models import Comment
from likedislike.models import LikeDislike
from django.contrib.auth import get_user_model


User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'is_superuser')

class TopicSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Topic
        fields = ('id', 'author', 'text')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'content_type', 'object_id', 'text')


class LikeDislikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LikeDislike
        fields = "__all__"