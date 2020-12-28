from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.urls import reverse
from likedislike.models import LikeDislike
from comment.models import Comment
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
    comments = GenericRelation(Comment)


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

    @property
    def total_likes(self):
        return self.likes_dislikes.filter(vote__gt=0).count()

    @property
    def total_dislikes(self):
        return self.likes_dislikes.filter(vote__lt=0).count()
    
    @property
    def sum_rating(self):
        return self.likes_dislikes.aggregate(Sum('vote')).get('vote__sum') or 0

    # @property
    # def all_comments(self):
    #     return self.comments.all()