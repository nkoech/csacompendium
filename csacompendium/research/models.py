# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from csacompendium.utils.abstractmodels import (
    AuthUserDetail,
    CreateUpdateTime,
)
from csacompendium.utils.createslug import create_slug
from csacompendium.utils.modelmanagers import (
    model_instance_filter,
    model_foreign_key_qs,
    model_type_filter,
    create_model_type,
    get_year_choices,
    get_datetime_now,
)
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse


class ExperimentDuration(AuthUserDetail, CreateUpdateTime):
    """
    Experiment duration model
    """
    exp_duration = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Experiment Duration')

    def __unicode__(self):
        return str(self.exp_duration)

    def __str__(self):
        return str(self.exp_duration)

    def get_api_url(self):
        """
        Get experiment duration URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('research_api:experiment_duration_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Experiment Durations'

    @property
    def model_type_relation(self):
        """
        Get related research properties
        :return: Query result from the research model
        :rtye: object/record
        """
        instance = self
        qs = Research.objects.filter_by_model_type(instance)
        return qs


class Author(AuthUserDetail, CreateUpdateTime):
    """
    Research author model
    """
    slug = models.SlugField(unique=True, blank=True)
    author_code = models.CharField(max_length=6, unique=True)
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64)
    author_bio = models.TextField()

    def __unicode__(self):
        return self.first_name

    def __str__(self):
        return self.first_name

    def get_api_url(self):
        """
        Get author URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('research_api:author_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Authors'

    @property
    def model_type_relation(self):
        """
        Get related research properties
        :return: Query result from the research model
        :rtye: object/record
        """
        instance = self
        qs = Research.objects.filter_by_model_type(instance)
        return qs


@receiver(pre_save, sender=Author)
def pre_save_author_receiver(sender, instance, *args, **kwargs):
    """
    Create a slug before save.
    :param sender: Signal sending object
    :param instance: Object instance
    :param args: Any other argument
    :param kwargs: Keyword arguments
    :return: None
    :rtype: None
    """
    if not instance.slug:
        instance_fields = [instance.first_name, instance.last_name]
        instance.slug = create_slug(instance, Author, instance_fields)


class ResearchManager(models.Manager):
    """
    Research model manager
    """
    def filter_by_instance(self, instance):
        """
        Query a related research object/record from another model's object
        :param instance: Object instance
        :return: Query result from content type/model
        :rtye: object/record
        """
        return model_instance_filter(instance, self, ResearchManager)

    def filter_by_model_type(self, instance):
        """
        Query related objects/model type
        :param instance: Object instance
        :return: Matching object else none
        :rtype: Object/record
        """
        obj_qs = model_foreign_key_qs(instance, self, ResearchManager)
        if obj_qs.exists():
            return model_type_filter(self, obj_qs, ResearchManager)

    def create_by_model_type(self, model_type, slug, **kwargs):
        """
        Create object by model type
        :param model_type: Content/model type
        :param slug: Slug
        :param kwargs: Fields to be created
        :return: Data object
        :rtype: Object
        """
        return create_model_type(self, model_type, slug, slugify=True, **kwargs)


class Research(AuthUserDetail, CreateUpdateTime):
    """
    Creates research entity.
    """
    limit = models.Q(app_label='locations', model='location')
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    research_year = models.SmallIntegerField(max_length=4, choices=get_year_choices(), default=get_datetime_now())
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    research_type = models.CharField(max_length=120)
    experimentduration = models.ForeignKey(
        ExperimentDuration, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Experiment Duration'
    )
    objects = ResearchManager()

    def __unicode__(self):
        return str(self.research_year)

    def __str__(self):
        return str(self.research_year)

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Research'


class MeasurementSeason(AuthUserDetail, CreateUpdateTime):
    """
    Measurement season model
    """
    meas_season = models.SmallIntegerField(max_length=2, verbose_name='Measurement season')

    def __unicode__(self):
        return str(self.meas_season)

    def __str__(self):
        return str(self.meas_season)

    def get_api_url(self):
        """
        Get measurement season URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('research_api:measurement_season_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Measurement Seasons'

    @property
    def model_type_relation(self):
        """
        Get related measurement year properties
        :return: Query result from the measurement year model
        :rtye: object/record
        """
        instance = self
        qs = MeasurementYear.objects.filter_by_model_type(instance)
        return qs


class MeasurementYearManager(models.Manager):
    """
    Measurement year model manager
    """
    def filter_by_instance(self, instance):
        """
        Query a related research object/record from another model's object
        :param instance: Object instance
        :return: Query result from content type/model
        :rtye: object/record
        """
        return model_instance_filter(instance, self, MeasurementYearManager)

    def filter_by_model_type(self, instance):
        """
        Query related objects/model type
        :param instance: Object instance
        :return: Matching object else none
        :rtype: Object/record
        """
        obj_qs = model_foreign_key_qs(instance, self, MeasurementYearManager)
        if obj_qs.exists():
            return model_type_filter(self, obj_qs, MeasurementYearManager)

    def create_by_model_type(self, model_type, pk, **kwargs):
        """
        Create object by model type
        :param model_type: Content/model type
        :param pk: Primary Key
        :param kwargs: Fields to be created
        :return: Data object
        :rtype: Object
        """
        return create_model_type(self, model_type, pk, slugify=False, **kwargs)


class MeasurementYear(AuthUserDetail, CreateUpdateTime):
    """
    Creates measurement year entity.
    """
    limit = models.Q(app_label='research', model='research')
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    meas_year = models.SmallIntegerField(
        max_length=4, choices=get_year_choices(), default=get_datetime_now(), verbose_name='Measurement Year'
    )
    measurementseason = models.ForeignKey(
        MeasurementSeason, on_delete=models.PROTECT, verbose_name='Measurement season'
    )
    objects = MeasurementYearManager()

    def __unicode__(self):
        return str(self.meas_year)

    def __str__(self):
        return str(self.meas_year)

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Measurement Years'
