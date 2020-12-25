from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from .models import LikeDislike

User = get_user_model()

"""
Методы для работы с системой лайков/дизлайков.
Сюда же логично было бы запихнуть возможность посчитать все необходимое.
А потом просто раздать это через json. Нафига, в принципе, это сериализовать?
"""


def add_like_dislike(obj, user, vote):
    content_type = ContentType.objects.get_for_model(obj)
    like, is_created = LikeDislike.objects.get_or_create(
        content_type=content_type, object_id=obj.id, user=user, vote=vote)
    return like

def remove_like_dislike(obj, user):
    content_type = ContentType.objects.get_for_model(obj)
    LikeDislike.objects.filter(
        content_type=content_type, object_id=obj.id, user=user
    ).delete()

def is_liked(obj, user) -> bool:
    if not user.is_authenticated:
        return False
    content_type = ContentType.objects.get_for_model(obj)
    likes = LikeDislike.objects.filter(
        content_type=content_type, object_id=obj.id, user=user)
    return likes.exists()

# что-то похожее можно использовать, чтобы посчитать все лайки по постам для человека
def get_liked_persons(obj):
    content_type = ContentType.objects.get_for_model(obj)
    return User.objects.filter(likes__content_type=content_type, likes__object_id=obj.id)