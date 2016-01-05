# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-25 06:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='category',
            name='views',
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]