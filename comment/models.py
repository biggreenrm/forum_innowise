from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Comment(models.Model):
    """
    Модель для комментариев к темам на форуме, а также к самим комментариям.
    """

    user = models.ForeignKey('auth.User', db_index=True, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    text = models.CharField(max_length=1000, default="")
    created_date = models.DateTimeField(default=timezone.now)
    published_status = models.BooleanField(default=False)

    class Meta:
        ordering = ("created_date",)

    def publish(self):
        if not self.published_status:
            self.published_status = True