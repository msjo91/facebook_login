# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-11 06:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_myuser_social_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='social_id',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='user_type',
        ),
    ]
