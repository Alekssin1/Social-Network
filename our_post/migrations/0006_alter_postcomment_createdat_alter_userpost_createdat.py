# Generated by Django 4.0 on 2023-01-13 19:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('our_post', '0005_alter_postcomment_createdat_alter_userpost_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 13, 21, 45, 8, 363120)),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 13, 21, 45, 8, 361125)),
        ),
    ]