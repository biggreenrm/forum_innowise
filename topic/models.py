from django.db import models
from django.utils import timezone
from django.urls import reverse
from likedislike.models import LikeDislike
from django.contrib.contenttypes.fields import GenericRelation


class Topic(models.Model):
    """
    Модель для темы на форуме
    """

    author = models.ForeignKey('auth.User', db_index=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    theme = models.CharField(max_length=200)
    text = models.TextField() # нужна ли максимальная длина? какие-нибудь другие параметры?
    created_date = models.DateTimeField(default=timezone.now)
    published_status = models.BooleanField(default=False)
    likes_dislikes = GenericRelation(LikeDislike)


    class Meta:
        ordering = ("created_date",)

    def publish(self):
        if not self.published_status:
            self.published_status = True

    def __str__(self):
        return self.title
    
    @property
    def total_likes_dislikes(self):
        return self.likes_dislikes.count()

    def get_absolute_url(self):
        return reverse("topic_detail", args=[self.id])