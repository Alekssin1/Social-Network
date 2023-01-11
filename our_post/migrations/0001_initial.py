# Generated by Django 4.0 on 2023-01-11 22:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentText', models.TextField()),
                ('createdAt', models.DateTimeField(default=datetime.datetime(2023, 1, 12, 0, 8, 8, 470745))),
            ],
            options={
                'db_table': 'post_comment',
            },
        ),
        migrations.CreateModel(
            name='UserPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(null=True)),
                ('createdAt', models.DateTimeField(default=datetime.datetime(2023, 1, 12, 0, 8, 8, 468750))),
                ('comment', models.ManyToManyField(blank=True, to='our_post.PostComment')),
                ('content', models.ManyToManyField(to='our_post.Photo')),
            ],
            options={
                'db_table': 'user_post',
            },
        ),
    ]
