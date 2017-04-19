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
)
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse


class IndicatorType(AuthUserDetail, CreateUpdateTime):
    """
    Indicator type model.  Creates indicator type entity.
    """
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    indicator_type = models.CharField(max_length=120, unique=True, verbose_name='Indicator category')

    def __unicode__(self):
        return self.indicator_type

    def __str__(self):
        return self.indicator_type

    def get_api_url(self):
        """
        Get indicator type URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('indicator_outcome_api:indicator_type_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Indicator Types'

    @property
    def outcome_indicator_relation(self):
        """
        Get related outcome indicator
        :return: Query result from the outcome indicator model
        :rtype: object/record
        """
        instance = self
        qs = OutcomeIndicator.objects.filter_by_model_type(instance)
        return qs


@receiver(pre_save, sender=IndicatorType)
def pre_save_indicator_type_receiver(sender, instance, *args, **kwargs):
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
        instance.slug = create_slug(instance, IndicatorType, instance.indicator_type)


class Subpillar(AuthUserDetail, CreateUpdateTime):
    """
    Subpillar model
    """
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    subpillar = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.subpillar

    def __str__(self):
        return self.subpillar

    def get_api_url(self):
        """
        Get subpillar URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('indicator_outcome_api:subpillar_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Subpillars'

    @property
    def indicator_relation(self):
        """
        Get related indicator properties
        :return: Query result from the indicator model
        :rtype: object/record
        """
        instance = self
        qs = Indicator.objects.filter_by_model_type(instance)
        return qs


@receiver(pre_save, sender=Subpillar)
def pre_save_subpillar_receiver(sender, instance, *args, **kwargs):
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
        instance.slug = create_slug(instance, Subpillar, instance.subpillar)


class IndicatorManager(models.Manager):
    """
    Indicator model manager
    """
    def filter_by_model_type(self, instance):
        """
        Query related objects/model type
        :param instance: Object instance
        :return: Matching object else none
        :rtype: Object/record
        """
        obj_qs = model_foreign_key_qs(instance, self, IndicatorManager)
        if obj_qs.exists():
            return model_type_filter(self, obj_qs, IndicatorManager)


class Indicator(AuthUserDetail, CreateUpdateTime):
    """
    Indicator model.  Creates indicator entity.
    """
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    subpillar = models.ForeignKey(Subpillar, on_delete=models.PROTECT, verbose_name='Indicator subpillar')
    indicator = models.CharField(max_length=120, unique=True)
    objects = IndicatorManager()

    def __unicode__(self):
        return self.indicator

    def __str__(self):
        return self.indicator

    def get_api_url(self):
        """
        Get indicator URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('indicator_outcome_api:indicator_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Indicators'

    @property
    def outcome_indicator_relation(self):
        """
        Get related outcome indicator
        :return: Query result from the outcome indicator model
        :rtype: object/record
        """
        instance = self
        qs = OutcomeIndicator.objects.filter_by_model_type(instance)
        return qs


@receiver(pre_save, sender=Indicator)
def pre_save_indicator_receiver(sender, instance, *args, **kwargs):
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
        instance.slug = create_slug(instance, Indicator, instance.indicator)


class OutcomeIndicatorManager(models.Manager):
    """
    Outcome indicator model manager
    """
    def filter_by_model_type(self, instance):
        """
        Query related objects/model type
        :param instance: Object instance
        :return: Matching object else none
        :rtype: Object/record
        """
        obj_qs = model_foreign_key_qs(instance, self, OutcomeIndicatorManager)
        if obj_qs.exists():
            return model_type_filter(self, obj_qs, OutcomeIndicatorManager)


class OutcomeIndicator(AuthUserDetail, CreateUpdateTime):
    """
    Outcome indicator model. Creates outcome indicator entity
    """
    slug = models.SlugField(unique=True, blank=True)
    indicator_code = models.PositiveSmallIntegerField(help_text='User defined indicator code')
    indicator = models.ForeignKey(Indicator, on_delete=models.PROTECT)
    subindicator = models.CharField(max_length=150, blank=True, null=True, verbose_name='Sub indicator')
    definition = models.TextField(blank=True, null=True)
    common_uom = models.CharField(max_length=450, blank=True, null=True)
    indicatortype = models.ForeignKey(IndicatorType, on_delete=models.PROTECT, verbose_name='Indicator Type')
    objects = OutcomeIndicatorManager()

    def __unicode__(self):
        str_format = '{0} - {1}'.format(self.indicator_code, self.subindicator)
        return str(str_format)

    def __str__(self):
        str_format = '{0} - {1}'.format(self.indicator_code, self.subindicator)
        return str(str_format)

    def get_api_url(self):
        """
        Get outcome indicator URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('indicator_outcome_api:outcome_indicator_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Outcome Indicators'

    @property
    def research_outcome_indicator(self):
        """
        Get related research outcome indicator object/record
        :return: Query result from the research outcome indicator model
        :rtype: object/record
        """
        instance = self
        qs = ResearchOutcomeIndicator.objects.filter_by_model_type(instance)
        return qs


@receiver(pre_save, sender=OutcomeIndicator)
def pre_save_outcome_indicator_receiver(sender, instance, *args, **kwargs):
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
        instance.slug = create_slug(instance, OutcomeIndicator, instance.indicator_code)


class SoilMeasurement(AuthUserDetail, CreateUpdateTime):
    """
    Soil measurement model
    """
    upper_soil_depth = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    lower_soil_depth = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    depth_uom = models.CharField(max_length=8, blank=True, null=True, default='cm')
    incubation_days = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    def __unicode__(self):
        str_format = 'Upper Soil: {0},  Lower Soil: {1}, Days: {2}'.format(
            self.upper_soil_depth, self.lower_soil_depth, self.incubation_days
        )
        return str(str_format)

    def __str__(self):
        str_format = 'Upper Soil: {0},  Lower Soil: {1}, Days: {2}'.format(
            self.upper_soil_depth, self.lower_soil_depth, self.incubation_days
        )
        return str(str_format)

    def get_api_url(self):
        """
        Get soil measurement URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('indicator_outcome_api:soil_measurement_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Soil measurements'

    @property
    def research_outcome_indicator_relation(self):
        """
        Get related research outcome indicator properties
        :return: Query result from the research outcome indicator model
        :rtype: object/record
        """
        instance = self
        qs = ResearchOutcomeIndicator.objects.filter_by_model_type(instance)
        return qs


class ExperimentOutcome(AuthUserDetail, CreateUpdateTime):
    """
    Experiment outcome model
    """
    mean_outcome = models.DecimalField(max_digits=8, decimal_places=2)
    std_outcome = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    outcome_uom = models.CharField(max_length=100, default='kg/ha')

    def __unicode__(self):
        str_format = 'Mean Outcome: {0},  STD Outcome: {1}'.format(self.mean_outcome, self.std_outcome)
        return str(str_format)

    def __str__(self):
        str_format = 'Mean Outcome: {0},  STD Outcome: {1}'.format(self.mean_outcome, self.std_outcome)
        return str(str_format)

    def get_api_url(self):
        """
        Get experiment outcome URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('indicator_outcome_api:experiment_outcome_detail', kwargs={'pk': self.pk})

    class Meta:
        unique_together = ['mean_outcome', 'std_outcome']
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Experiment Outcomes'

    @property
    def research_outcome_indicator_relation(self):
        """
        Get related research outcome indicator properties
        :return: Query result from the research outcome indicator model
        :rtype: object/record
        """
        instance = self
        qs = ResearchOutcomeIndicator.objects.filter_by_model_type(instance)
        return qs


class ResearchOutcomeIndicatorManager(models.Manager):
    """
    Research outcome indicator model manager
    """
    def filter_by_instance(self, instance):
        """
        Query a related research outcome indicator object/record from another model's object
        :param instance: Object instance
        :return: Query result from content type/model
        :rtye: object/record
        """
        return model_instance_filter(instance, self, ResearchOutcomeIndicatorManager)

    def filter_by_model_type(self, instance):
        """
        Query related objects/model type
        :param instance: Object instance
        :return: Matching object else none
        :rtype: Object/record
        """
        obj_qs = model_foreign_key_qs(instance, self, ResearchOutcomeIndicatorManager)
        if obj_qs.exists():
            return model_type_filter(self, obj_qs, ResearchOutcomeIndicatorManager)

    def create_by_model_type(self, model_type, pk, **kwargs):
        """
        Create object by model type
        :param model_type: Content/model type
        :param pk: Primary key
        :param kwargs: Fields to be created
        :return: Data object
        :rtype: Object
        """
        return create_model_type(self, model_type, pk, slugify=False, **kwargs)


class ResearchOutcomeIndicator(AuthUserDetail, CreateUpdateTime):
    """
    Research outcome indicator entry relationship model. A many to many bridge
    table between research and other models
    """
    limit = models.Q(app_label='research', model='research')
    outcomeindicator = models.ForeignKey(OutcomeIndicator, on_delete=models.PROTECT,  verbose_name='Outcome indicator')
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    soilmeasurement = models.ForeignKey(
        SoilMeasurement, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Soil measurement'
    )
    experimentoutcome = models.ForeignKey(
        ExperimentOutcome, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Experiment Outcome'
    )
    objects = ResearchOutcomeIndicatorManager()

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Research Outcome Indicators'
