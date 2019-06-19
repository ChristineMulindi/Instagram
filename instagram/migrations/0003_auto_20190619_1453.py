# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-06-19 11:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instagram', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_path', models.ImageField(default='images/christine.jpg', upload_to='images/')),
                ('bio', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('followers', models.ManyToManyField(blank=True, related_name='followers_profile', to='instagram.Profile')),
                ('following', models.ManyToManyField(blank=True, related_name='following_profile', to='instagram.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='editor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='user_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='instagram.Profile'),
        ),
    ]
