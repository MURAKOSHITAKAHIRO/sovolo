# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-11 23:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_group_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='group/'),
        ),
    ]