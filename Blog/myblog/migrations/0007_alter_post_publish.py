# Generated by Django 4.0 on 2023-10-02 02:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_post_category_alter_post_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 2, 2, 37, 58, 179933, tzinfo=utc)),
        ),
    ]
