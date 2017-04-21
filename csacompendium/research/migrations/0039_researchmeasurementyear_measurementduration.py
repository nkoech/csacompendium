# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-21 05:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0038_measurementduration'),
    ]

    operations = [
        migrations.AddField(
            model_name='researchmeasurementyear',
            name='measurementduration',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='research.MeasurementDuration'),
        ),
    ]
