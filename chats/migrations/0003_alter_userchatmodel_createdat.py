# Generated by Django 4.1.1 on 2023-01-23 14:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userchatmodel',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 23, 16, 15, 55, 386142)),
        ),
    ]
