# Generated by Django 4.0 on 2023-01-13 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_is_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_time_online',
            field=models.DateTimeField(null=True),
        ),
    ]
