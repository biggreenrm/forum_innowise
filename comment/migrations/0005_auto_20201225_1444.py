# Generated by Django 3.1.4 on 2020-12-25 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0004_auto_20201224_1306'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created_date',)},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='published_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='published_status',
            field=models.BooleanField(default=False),
        ),
    ]