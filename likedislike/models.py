# Django
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTES = ((DISLIKE, "Dislike"), (LIKE, "Like"))

    vote = models.SmallIntegerField(verbose_name=("Vote"), choices=VOTES)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
