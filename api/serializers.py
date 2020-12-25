from rest_framework import serializers
from topic.models import Topic
from comment.models import Comment
from likedislike.models import LikeDislike
from django.contrib.auth import get_user_model
from generic_relations.relations import GenericRelatedField


User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'is_superuser')


class TopicSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Topic
        fields = ('id', 'author', 'text', 'created_date')


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    content_object = GenericRelatedField({
        Topic: serializers.HyperlinkedRelatedField(queryset = Topic.objects.all(),
                                                    view_name='topic-detail',),
        Comment: serializers.HyperlinkedRelatedField(queryset = Comment.objects.all(),
                                                    view_name='comment-detail',),
    })
    class Meta:
        model = Comment
        fields = ('user', 'content_object', 'text')


class LikeDislikeSerializer(serializers.HyperlinkedModelSerializer):

    content_object = GenericRelatedField({
        Topic: serializers.HyperlinkedRelatedField(queryset = Topic.objects.all(),
                                                    view_name='topic-detail',),
        Comment: serializers.HyperlinkedRelatedField(queryset = Comment.objects.all(),
                                                    view_name='comment-detail',),
    })

    class Meta:
        model = LikeDislike
        fields = ('vote', 'user', 'content_object')