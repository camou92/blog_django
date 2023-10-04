# Generated by Django 4.0 on 2023-09-30 15:18

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_alter_post_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category_posts', to='myblog.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 30, 15, 18, 1, 843229, tzinfo=utc)),
        ),
    ]