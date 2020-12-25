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


class CommentedObjectRelatedField(serializers.RelatedField):
    """
    A custom field to use for 'content_object' generic relationship in CommentSerializer.
    """

    def to_representation(self, value):
        """
        Serialize commented objects to simple textual representation.
        """

        if isinstance(value, Comment):
            return 'Comment: ' + value.id
        elif isinstance(value, Topic):
            return 'Topic: ' + value.id
        raise Exception('Unexpected type of commented object')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    commented_object = CommentedObjectRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('user', 'commented_object', 'text')


class LikeDislikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LikeDislike
        fields = ('vote', 'user', 'object_id')