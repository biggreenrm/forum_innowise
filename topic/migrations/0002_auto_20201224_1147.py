# Generated by Django 3.1.4 on 2020-12-24 11:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [("topic", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="topic",
            name="created_date",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 12, 24, 11, 47, 37, 829442, tzinfo=utc)
            ),
        )
    ]
