# First-party
from .models import LikeDislike
# Django
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType


User = get_user_model()


def add_like(obj, user):
    vote = 1
    content_type = ContentType.objects.get_for_model(obj)
    like, is_created = LikeDislike.objects.get_or_create(
        content_type=content_type, object_id=obj.id, user=user, vote=vote)
    return like

def add_dislike(obj, user):
    vote = -1
    content_type = ContentType.objects.get_for_model(obj)
    dislike, is_created = LikeDislike.objects.get_or_create(
        content_type=content_type, object_id=obj.id, user=user, vote=vote)
    return dislike

def remove_like_dislike(obj, user):
    content_type = ContentType.objects.get_for_model(obj)
    LikeDislike.objects.filter(
        content_type=content_type, object_id=obj.id, user=user
    ).delete()

def is_voted(obj, user) -> bool:
    if not user.is_authenticated:
        return False
    content_type = ContentType.objects.get_for_model(obj)
    likes = LikeDislike.objects.filter(
        content_type=content_type, object_id=obj.id, user=user)
    return likes.exists()


def get_liked_persons(obj):
    content_type = ContentType.objects.get_for_model(obj)
    return User.objects.filter(likedislike__content_type=content_type, likedislike__object_id=obj.id)