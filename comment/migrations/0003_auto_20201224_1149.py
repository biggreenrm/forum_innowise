# Generated by Django 3.1.4 on 2020-12-24 11:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20201224_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 24, 11, 49, 33, 496799, tzinfo=utc)),
        ),
    ]