from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from likedislike.models import LikeDislike


class Comment(models.Model):
    """
    Модель для комментариев к темам на форуме, а также к самим комментариям.
    """

    user = models.ForeignKey("auth.User", db_index=True, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    text = models.CharField(max_length=1000, default="")
    created_date = models.DateTimeField(default=timezone.now)
    published_status = models.BooleanField(default=False)
    likes_dislikes = GenericRelation(LikeDislike)

    class Meta:
        ordering = ("created_date",)

    def publish(self):
        if not self.published_status:
            self.published_status = True

    @property
    def total_likes_dislikes(self):
        return self.likes_dislikes.count()

    @property
    def total_likes(self):
        return self.likes_dislikes.filter(vote__gt=0).count()

    @property
    def total_dislikes(self):
        return self.likes_dislikes.filter(vote__lt=0).count()

    @property
    def sum_rating(self):
        return self.likes_dislikes.aggregate(Sum("vote")).get("vote__sum") or 0
