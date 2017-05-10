# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-10 08:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='user_type',
            field=models.CharField(choices=[('django', 'Django'), ('facebook', 'Facebook')], default='django', max_length=15),
        ),
    ]
