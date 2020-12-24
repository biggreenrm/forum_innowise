from django.db import models
from django.utils import timezone


class Topic(models.Model):
    """
    Модель для темы на форуме
    """

    author = models.ForeignKey('auth.User', db_index=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    theme = models.CharField(max_length=200)
    text = models.TextField() # нужна ли максимальная длина? какие-нибудь другие параметры?
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ("published_date",)

    def publish(self):
        self.published_date = timezone.now()

    def __str__(self):
        return self.title