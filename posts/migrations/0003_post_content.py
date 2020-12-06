# Generated by Django 3.1.3 on 2020-11-14 09:56

import datetime
from django.db import migrations
from django.utils.timezone import utc
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default=datetime.datetime(2020, 11, 14, 9, 56, 21, 281981, tzinfo=utc)),
            preserve_default=False,
        ),
    ]