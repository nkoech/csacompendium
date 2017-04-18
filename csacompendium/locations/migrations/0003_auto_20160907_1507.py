# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-07 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_locationrelation_temperature'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='locationrelation',
            options={'ordering': ['-time_created', '-last_update']},
        ),
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=8),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
    ]