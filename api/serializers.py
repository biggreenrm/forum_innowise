from rest_framework import serializers
from topic.models import Topic
from comment.models import Comment
from likedislike.models import LikeDislike


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class LikeDislikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LikeDislike
        fields = "__all__"