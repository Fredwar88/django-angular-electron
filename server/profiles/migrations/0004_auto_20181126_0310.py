# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-26 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20171119_0224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='rank',
        ),
        migrations.AddField(
            model_name='profile',
            name='comment',
            field=models.CharField(blank=True, default='Not much to say', max_length=64),
        ),
    ]