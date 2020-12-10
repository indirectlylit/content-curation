# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-17 22:21
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('contentcuration', '0123_auto_20200921_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='disk_space_used',
            field=models.FloatField(blank=True, help_text='How many bytes a user has uploaded', null=True),
        ),
    ]
