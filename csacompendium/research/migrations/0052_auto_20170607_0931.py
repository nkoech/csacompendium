# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-07 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0051_research_research_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research',
            name='research_code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
