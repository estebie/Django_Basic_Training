# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-26 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_auto_20180724_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
