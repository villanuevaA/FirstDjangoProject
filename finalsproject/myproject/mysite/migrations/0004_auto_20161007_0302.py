# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-07 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20161004_0325'),
    ]

    operations = [
        migrations.AddField(
            model_name='tips',
            name='dislikes',
            field=models.TextField(default=0),
        ),
        migrations.AddField(
            model_name='tips',
            name='likes',
            field=models.TextField(default=0),
        ),
    ]