# Generated by Django 4.0.4 on 2022-05-12 00:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_follower_users_alter_profile_following_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='follower_users',
            field=models.ManyToManyField(blank=True, default=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL), related_name='users_that_follow', to='users.profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='following_users',
            field=models.ManyToManyField(blank=True, default=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL), related_name='users_following', to='users.profile'),
        ),
    ]
