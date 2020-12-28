# First-party
from topic.models import Topic
from comment.models import Comment
from likedislike.models import LikeDislike
from likedislike import services as likes_dislikes_services
# Django
from django.contrib.auth import get_user_model
# Third-party
from rest_framework import serializers
from generic_relations.relations import GenericRelatedField


User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'first_name', 'last_name', 'is_superuser')


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    is_voted = serializers.SerializerMethodField()
    all_comments = serializers.HyperlinkedIdentityField(view_name="api:comment-detail", many=True)

    class Meta:
        model = Topic
        fields = ('id', 'author', 'title', 'text', 'created_date', 'total_likes_dislikes', 'total_likes', 'total_dislikes', 'sum_rating', 'is_voted', 'all_comments')
    
    def get_is_voted(self, obj) -> bool:
        user = self.context.get('request').user
        return likes_dislikes_services.is_voted(obj, user)


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    is_voted = serializers.SerializerMethodField()

    content_object = GenericRelatedField({
        Topic: serializers.HyperlinkedRelatedField(queryset = Topic.objects.all(),
                                                    view_name='topic-detail',),
        Comment: serializers.HyperlinkedRelatedField(queryset = Comment.objects.all(),
                                                    view_name='comment-detail',),
    })

    class Meta:
        model = Comment
        fields = ('id', 'user', 'content_object', 'text', 'total_likes_dislikes', 'total_likes', 'total_dislikes', 'is_voted',)
    
    def get_is_voted(self, obj) -> bool:
        user = self.context.get('request').user
        return likes_dislikes_services.is_voted(obj, user)


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