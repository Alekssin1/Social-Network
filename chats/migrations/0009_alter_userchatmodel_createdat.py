# Generated by Django 4.0 on 2023-01-10 16:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0008_alter_userchatmodel_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userchatmodel',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 10, 18, 56, 2, 557753)),
        ),
    ]
