# -*- coding: utf-8 -*-
# Generated by Django 1.10rc1 on 2016-08-05 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_follow_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='follow_tag',
            field=models.ManyToManyField(related_name='follower', to='tag.Tag'),
        ),
    ]