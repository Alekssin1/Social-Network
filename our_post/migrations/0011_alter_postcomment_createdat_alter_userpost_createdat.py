# Generated by Django 4.0 on 2023-01-10 16:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('our_post', '0010_alter_postcomment_createdat_alter_userpost_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 10, 18, 56, 49, 625515)),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 10, 18, 56, 49, 624518)),
        ),
    ]
