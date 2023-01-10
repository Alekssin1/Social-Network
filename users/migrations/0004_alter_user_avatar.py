# Generated by Django 4.0 on 2023-01-10 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ForeignKey(blank=True, default='static/default/avatar/dp.png', null=True, on_delete=django.db.models.deletion.CASCADE, to='users.avataruser'),
        ),
    ]