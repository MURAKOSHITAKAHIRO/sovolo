# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 22:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0028_auto_20170818_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreviewlist',
            name='post_day',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 17, 22, 48, 28, 535129, tzinfo=utc), editable=False, null=True),
        ),
    ]