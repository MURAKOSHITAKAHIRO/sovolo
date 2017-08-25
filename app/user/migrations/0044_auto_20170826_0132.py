# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 16:32
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0043_auto_20170825_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreviewlist',
            name='joined_event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Event'),
        ),
        migrations.AlterField(
            model_name='userreviewlist',
            name='post_day',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='userreviewlist',
            name='rating',
            field=models.IntegerField(choices=[(5, '5'), (4, '4'), (1, '1'), (2, '2'), (3, '3')], validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
