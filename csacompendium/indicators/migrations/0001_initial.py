# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-10 17:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=120, unique=True)),
                ('indicator', models.CharField(max_length=120)),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='indicators_indicator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time_created', '-last_update'],
                'verbose_name_plural': 'Indicators',
            },
        ),
        migrations.CreateModel(
            name='IndicatorType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=120, unique=True)),
                ('indicator_type', models.CharField(max_length=120, unique=True, verbose_name='Indicator category')),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='indicators_indicatortype', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time_created', '-last_update'],
                'verbose_name_plural': 'Indicator Types',
            },
        ),
        migrations.CreateModel(
            name='OutcomeIndicator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('indicator_code', models.PositiveSmallIntegerField(help_text='User defined indicator code')),
                ('subindicator', models.CharField(blank=True, max_length=150, null=True)),
                ('definition', models.TextField(blank=True, null=True)),
                ('common_uom', models.CharField(blank=True, max_length=450, null=True)),
                ('indicator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='indicators.Indicator')),
                ('indicatortype', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='indicators.IndicatorType', verbose_name='Indicator Type')),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='indicators_outcomeindicator', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time_created', '-last_update'],
                'verbose_name_plural': 'Outcome Indicators',
            },
        ),
        migrations.CreateModel(
            name='Subpillar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('subpillar', models.CharField(max_length=50, unique=True)),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='indicators_subpillar', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time_created', '-last_update'],
                'verbose_name_plural': 'Subpillars',
            },
        ),
        migrations.AddField(
            model_name='indicator',
            name='subpillar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='indicators.Subpillar', verbose_name='Indicator subpillar'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]