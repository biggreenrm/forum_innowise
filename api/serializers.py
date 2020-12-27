from rest_framework import serializers
from topic.models import Topic
from comment.models import Comment
from likedislike.models import LikeDislike
from django.contrib.auth import get_user_model
from generic_relations.relations import GenericRelatedField
from likedislike import services as likes_dislikes_services


User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'first_name', 'last_name', 'is_superuser')


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    is_voted = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = ('id', 'author', 'title', 'text', 'created_date', 'total_likes_dislikes', 'total_likes', 'total_dislikes', 'sum_rating', 'is_voted')
    
    def get_is_voted(self, obj) -> bool:
        """
        Проверяет стоит ли лайк или дизлайк от юзера
        """
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
        fields = ('id', 'user', 'content_object', 'text', 'total_likes_dislikes', 'total_likes', 'total_dislikes', 'is_voted')
    
    def get_is_voted(self, obj) -> bool:
        """
        Проверяет стоит ли лайк или дизлайк от юзера
        """
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