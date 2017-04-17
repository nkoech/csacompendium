# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-17 22:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0019_journal_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researchauthor',
            name='journal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='research.Journal'),
        ),
    ]
