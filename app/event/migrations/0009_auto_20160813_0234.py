# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-12 17:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='user',
        ),
        migrations.AddField(
            model_name='answer',
            name='participation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='event.Participation'),
            preserve_default=False,
        ),
    ]
