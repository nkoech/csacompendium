# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-20 20:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0034_auto_20170420_2259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurementyear',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='measurementyear',
            name='user',
        ),
        migrations.RemoveField(
            model_name='research',
            name='measurementyear',
        ),
        migrations.DeleteModel(
            name='MeasurementYear',
        ),
    ]
