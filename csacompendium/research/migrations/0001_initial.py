# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-23 14:12
from __future__ import unicode_literals

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=120, unique=True)),
                ('author_code', models.CharField(max_length=6, unique=True)),
                ('first_name', models.CharField(max_length=40)),
                ('middle_name', models.CharField(blank=True, max_length=40, null=True)),
                ('last_name', models.CharField(max_length=40)),
                ('author_bio', models.TextField(blank=True, null=True)),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='research_author', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time_created', '-last_update'],
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='ControlResearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mean_outcome', models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=8, verbose_name='Mean outcome')),
                ('std_outcome', models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=8, verbose_name='Standard outcome')),
                ('outcome_uom', models.CharField(default='kg/ha', max_length=200)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ['-time_created', '-last_update'],
                'verbose_name_plural': 'Control Research',
            },
        ),
        migrations.CreateModel(
            name='ExperimentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=250, unique=True)),
                ('exp_detail', models.CharField(max_length=250, unique=True, verbose_name='Experiment Details')),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='research_experimentdetails', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time_created', '-last_update'],
                'verbose_name_plural': 'Experiment Details',
            },
        ),
        migrations.CreateModel(
            name='ExperimentDuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('exp_duration', models.DecimalField(decimal_places=2, max_digits=4, unique=True, verbose_name='Experiment Duration')),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='research_experimentduration', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time_created', '-last_update'],
                'verbose_name_plural': 'Experiment Durations',
            },
        ),
        migrations.CreateModel(
            name='ExperimentRep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('no_replication', models.SmallIntegerField(verbose_name='Experiment Replication Number')),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='research_experimentrep', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time_created', '-last_update'],
                'verbose_name_plural': 'Experiment Replications',
            },
        ),
        migrations.CreateModel(
            name='ExperimentUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=250, unique=True)),
                ('exp_unit_code', models.CharField(max_length=20, unique=True, verbose_name='Experiment unit code')),
                ('common_name', models.CharField(max_length=250)),
                ('latin_name', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'ordering': ['-time_created', '-last_update'],
                'verbose_name_plural': 'Experiment Units',
            },
        ),
        migrations.CreateModel(
            name='ExperimentUnitCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('unit_category', models.CharField(max_length=200, unique=True)),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='research_experimentunitcategory', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time_created', '-last_update'],
                'verbose_name_plural': 'Experiment Unit Categories',
            },
        ),
        migrations.CreateModel(
            name='MeasurementSeason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('meas_season', models.CharField(choices=[('Long Rains', 'Long Rains'), ('Short Rains', 'Short Rains')], max_length=22, unique=True, verbose_name='Measurement season')),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='research_measurementseason', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time_created', '-last_update'],
                'verbose_name_plural': 'Measurement Seasons',
            },
        ),
        migrations.CreateModel(
            name='MeasurementYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('meas_year', models.SmallIntegerField(choices=[(1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017)], default=2017, verbose_name='Measurement year')),
                ('measurementseason', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='research.MeasurementSeason', verbose_name='Measurement season')),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='research_measurementyear', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time_created', '-last_update'],
                'verbose_name_plural': 'Measurement Years',
            },
        ),
        migrations.CreateModel(
            name='NitrogenApplied',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('nitrogen_amount', models.DecimalField(decimal_places=2, max_digits=6, unique=True)),
                ('amount_uom', models.CharField(default='kg/ha', max_length=12, verbose_name='Nitrogen UOM')),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='research_nitrogenapplied', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time_created', '-last_update'],
                'verbose_name_plural': 'Nitrogen Applied',
            },
        ),
        migrations.CreateModel(
            name='ResearchAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('object_id', models.PositiveIntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='research.Author')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType')),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='research_researchauthor', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time_created', '-last_update'],
                'verbose_name_plural': 'Research Authors',
            },
        ),
        migrations.CreateModel(
            name='ResearchExperimentUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('object_id', models.PositiveIntegerField()),
                ('upper_soil_depth', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('lower_soil_depth', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('incubation_days', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Incubation Days')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType')),
                ('experimentunit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='research.ExperimentUnit', verbose_name='Experiment Unit')),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='research_researchexperimentunit', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time_created', '-last_update'],
                'verbose_name_plural': 'Research Experiment Units',
            },
        ),
        migrations.CreateModel(
            name='ResearchSpecies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType')),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='research_researchspecies', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time_created', '-last_update'],
                'verbose_name_plural': 'Research Species',
            },
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('species', models.CharField(max_length=200, unique=True)),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='research_species', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time_created', '-last_update'],
                'verbose_name_plural': 'Species',
            },
        ),
        migrations.CreateModel(
            name='TreatmentResearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mean_outcome', models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=8, verbose_name='Mean outcome')),
                ('std_outcome', models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=8, verbose_name='Standard outcome')),
                ('outcome_uom', models.CharField(default='kg/ha', max_length=200)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType')),
                ('experimentdetails', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='research.ExperimentDetails', verbose_name='Experiment Details')),
                ('experimentduration', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='research.ExperimentDuration', verbose_name='Experiment Duration')),
                ('experimentrep', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='research.ExperimentRep', verbose_name='Experiment Replications')),
                ('measurementyear', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='research.MeasurementYear', verbose_name='Measurement Year')),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='research_treatmentresearch', to=settings.AUTH_USER_MODEL)),
                ('nitrogenapplied', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='research.NitrogenApplied', verbose_name='Nitrogen Applied')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time_created', '-last_update'],
                'verbose_name_plural': 'Treatment Research',
            },
        ),
        migrations.AddField(
            model_name='researchspecies',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='research.Species'),
        ),
        migrations.AddField(
            model_name='researchspecies',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='experimentunit',
            name='experimentunitcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='research.ExperimentUnitCategory', verbose_name='Unit categories'),
        ),
        migrations.AddField(
            model_name='experimentunit',
            name='modified_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='research_experimentunit', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='experimentunit',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='controlresearch',
            name='experimentdetails',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='research.ExperimentDetails', verbose_name='Experiment Details'),
        ),
        migrations.AddField(
            model_name='controlresearch',
            name='experimentduration',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='research.ExperimentDuration', verbose_name='Experiment Duration'),
        ),
        migrations.AddField(
            model_name='controlresearch',
            name='experimentrep',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='research.ExperimentRep', verbose_name='Experiment Replications'),
        ),
        migrations.AddField(
            model_name='controlresearch',
            name='measurementyear',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='research.MeasurementYear', verbose_name='Measurement Year'),
        ),
        migrations.AddField(
            model_name='controlresearch',
            name='modified_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='research_controlresearch', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='controlresearch',
            name='nitrogenapplied',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='research.NitrogenApplied', verbose_name='Nitrogen Applied'),
        ),
        migrations.AddField(
            model_name='controlresearch',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]