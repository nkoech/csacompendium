# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-20 08:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0029_auto_20170419_2312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='research',
            name='experiment_description',
        ),
    ]