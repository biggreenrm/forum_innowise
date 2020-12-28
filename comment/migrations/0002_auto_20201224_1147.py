# Generated by Django 3.1.4 on 2020-12-24 11:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [("comment", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="created_date",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 12, 24, 11, 47, 37, 831933, tzinfo=utc)
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="published_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
