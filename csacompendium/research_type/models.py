# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from csacompendium.csa_practice.models import CsaPractice
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


class ExperimentRep(AuthUserDetail, CreateUpdateTime):
    """
    Experiment replication model
    """
    no_replication = models.SmallIntegerField(verbose_name='Experiment Replication Number')

    def __unicode__(self):
        return str(self.no_replication)

    def __str__(self):
        return str(self.no_replication)

    def get_api_url(self):
        """
        Get experiment replication URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('research_type_api:experiment_rep_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Experiment Replications'

    @property
    def control_research_relation(self):
        """
        Get related control research properties
        :return: Query result from the control research model
        :rtype: object/record
        """
        instance = self
        qs = ControlResearch.objects.filter_by_model_type(instance)
        return qs

    @property
    def treatment_research_relation(self):
        """
        Get related treatment research properties
        :return: Query result from the treatment research model
        :rtype: object/record
        """
        instance = self
        qs = TreatmentResearch.objects.filter_by_model_type(instance)
        return qs


class NitrogenApplied(AuthUserDetail, CreateUpdateTime):
    """
    Nitrogen applied model
    """
    nitrogen_amount = models.DecimalField(max_digits=6, decimal_places=2,  unique=True)
    amount_uom = models.CharField(max_length=12, default='kg/ha', verbose_name='Nitrogen UOM')

    def __unicode__(self):
        return str(self.nitrogen_amount)

    def __str__(self):
        return str(self.nitrogen_amount)

    def get_api_url(self):
        """
        Get nitrogen applied URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('research_type_api:nitrogen_applied_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Nitrogen Applied'

    @property
    def control_research_relation(self):
        """
        Get related control research properties
        :return: Query result from the control research model
        :rtype: object/record
        """
        instance = self
        qs = ControlResearch.objects.filter_by_model_type(instance)
        return qs

    @property
    def treatment_research_relation(self):
        """
        Get related treatment research properties
        :return: Query result from the treatment research model
        :rtype: object/record
        """
        instance = self
        qs = TreatmentResearch.objects.filter_by_model_type(instance)
        return qs


class ExperimentDetails(AuthUserDetail, CreateUpdateTime):
    """
    Experiment details model
    """
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    exp_detail = models.CharField(max_length=250, unique=True, verbose_name='Experiment Details')

    def __unicode__(self):
        return self.exp_detail

    def __str__(self):
        return self.exp_detail

    def get_api_url(self):
        """
        Get experiment details URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('research_type_api:experiment_details_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Experiment Details'

    @property
    def control_research_relation(self):
        """
        Get related control research properties
        :return: Query result from the control research model
        :rtype: object/record
        """
        instance = self
        qs = ControlResearch.objects.filter_by_model_type(instance)
        return qs

    @property
    def treatment_research_relation(self):
        """
        Get related treatment research properties
        :return: Query result from the treatment research model
        :rtype: object/record
        """
        instance = self
        qs = TreatmentResearch.objects.filter_by_model_type(instance)
        return qs


@receiver(pre_save, sender=ExperimentDetails)
def pre_save_experiment_details_receiver(sender, instance, *args, **kwargs):
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
        instance.slug = create_slug(instance, ExperimentDetails, instance.exp_detail)


class ExperimentDuration(AuthUserDetail, CreateUpdateTime):
    """
    Experiment duration model
    """
    exp_duration = models.DecimalField(
        max_digits=4, decimal_places=2, unique=True, verbose_name='Experiment Duration'
    )

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
        return reverse('research_type_api:experiment_duration_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Experiment Durations'

    @property
    def control_research_relation(self):
        """
        Get related control research properties
        :return: Query result from the control research model
        :rtype: object/record
        """
        instance = self
        qs = ControlResearch.objects.filter_by_model_type(instance)
        return qs

    @property
    def treatment_research_relation(self):
        """
        Get related treatment research properties
        :return: Query result from the treatment research model
        :rtype: object/record
        """
        instance = self
        qs = TreatmentResearch.objects.filter_by_model_type(instance)
        return qs


# class MeasurementSeason(AuthUserDetail, CreateUpdateTime):
#     """
#     Measurement season model
#     """
#     RAIN_SEASONS = (
#         ('Long Rains', 'Long Rains'),
#         ('Short Rains', 'Short Rains'),
#     )
#
#     slug = models.SlugField(unique=True, blank=True)
#     meas_season = models.CharField(max_length=22, choices=RAIN_SEASONS, unique=True, verbose_name='Measurement season')
#
#     def __unicode__(self):
#         return self.meas_season
#
#     def __str__(self):
#         return self.meas_season
#
#     def get_api_url(self):
#         """
#         Get measurement season URL as a reverse from model
#         :return: URL
#         :rtype: String
#         """
#         return reverse('research_type_api:measurement_season_detail', kwargs={'slug': self.slug})
#
#     class Meta:
#         ordering = ['-time_created', '-last_update']
#         verbose_name_plural = 'Measurement Seasons'
#
#     @property
#     def measurement_year_relation(self):
#         """
#         Get related measurement year properties
#         :return: Query result from the measurement year model
#         :rtye: object/record
#         """
#         instance = self
#         qs = MeasurementYear.objects.filter_by_model_type(instance)
#         return qs
#
#
# @receiver(pre_save, sender=MeasurementSeason)
# def pre_save_measurement_season_receiver(sender, instance, *args, **kwargs):
#     """
#     Create a slug before save.
#     :param sender: Signal sending object
#     :param instance: Object instance
#     :param args: Any other argument
#     :param kwargs: Keyword arguments
#     :return: None
#     :rtype: None
#     """
#     if not instance.slug:
#         instance.slug = create_slug(instance, MeasurementSeason, instance.meas_season)
#
#
# class MeasurementYearManager(models.Manager):
#     """
#     Measurement year model manager
#     """
#     def filter_by_model_type(self, instance):
#         """
#         Query related objects/model type
#         :param instance: Object instance
#         :return: Matching object else none
#         :rtype: Object/record
#         """
#         obj_qs = model_foreign_key_qs(instance, self, MeasurementYearManager)
#         if obj_qs.exists():
#             return model_type_filter(self, obj_qs, MeasurementYearManager)
#
#
# class MeasurementYear(AuthUserDetail, CreateUpdateTime):
#     """
#     Creates measurement year entity.
#     """
#     slug = models.SlugField(unique=True, blank=True)
#     meas_year = models.SmallIntegerField(
#         choices=get_year_choices(), default=get_datetime_now(), verbose_name='Measurement Year'
#     )
#     measurementseason = models.ForeignKey(
#         MeasurementSeason, on_delete=models.PROTECT, verbose_name='Measurement season'
#     )
#     objects = MeasurementYearManager()
#
#     def __unicode__(self):
#         return str(self.meas_year)
#
#     def __str__(self):
#         return str(self.meas_year)
#
#     def get_api_url(self):
#         """
#         Get measurement year URL as a reverse from model
#         :return: URL
#         :rtype: String
#         """
#         return reverse('research_type_api:measurement_year_detail', kwargs={'slug': self.slug})
#
#     class Meta:
#         ordering = ['-time_created', '-last_update']
#         verbose_name_plural = 'Measurement Years'
#
#     @property
#     def control_research_relation(self):
#         """
#         Get related control research properties
#         :return: Query result from the control research model
#         :rtype: object/record
#         """
#         instance = self
#         qs = ControlResearch.objects.filter_by_model_type(instance)
#         return qs
#
#     @property
#     def treatment_research_relation(self):
#         """
#         Get related treatment research properties
#         :return: Query result from the treatment research model
#         :rtype: object/record
#         """
#         instance = self
#         qs = TreatmentResearch.objects.filter_by_model_type(instance)
#         return qs
#
#
# @receiver(pre_save, sender=MeasurementYear)
# def pre_save_indicator_receiver(sender, instance, *args, **kwargs):
#     """
#     Create a slug before save.
#     :param sender: Signal sending object
#     :param instance: Object instance
#     :param args: Any other argument
#     :param kwargs: Keyword arguments
#     :return: None
#     :rtype: None
#     """
#     if not instance.slug:
#         instance.slug = create_slug(instance, MeasurementYear, instance.meas_year)


class ControlResearchManager(models.Manager):
    """
    Control research model manager
    """
    def filter_by_instance(self, instance):
        """
        Query a related control research object/record from another model's object
        :param instance: Object instance
        :return: Query result from content type/model
        :rtye: object/record
        """
        return model_instance_filter(instance, self, ControlResearchManager)

    def filter_by_model_type(self, instance):
        """
        Query related objects/model type
        :param instance: Object instance
        :return: Matching object else none
        :rtype: Object/record
        """
        obj_qs = model_foreign_key_qs(instance, self, ControlResearchManager)
        if obj_qs.exists():
            return model_type_filter(self, obj_qs, ControlResearchManager)

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


class ControlResearch(AuthUserDetail, CreateUpdateTime):
    """
    Creates control research entity.
    """
    limit = models.Q(app_label='research', model='research')
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    csapractice = models.ForeignKey(CsaPractice, on_delete=models.PROTECT, verbose_name='CSA Practice')
    experimentrep = models.ForeignKey(
        ExperimentRep, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Experiment Replications'
    )
    experimentdetails = models.ForeignKey(
        ExperimentDetails, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Experiment Details'
    )
    nitrogenapplied = models.ForeignKey(
        NitrogenApplied, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Nitrogen Applied'
    )
    experimentduration = models.ForeignKey(
        ExperimentDuration, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Experiment Duration'
    )
    objects = ControlResearchManager()

    def __unicode__(self):
        return str(self.experimentdetails)

    def __str__(self):
        return str(self.experimentdetails)

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Control Research'


class TreatmentResearchManager(models.Manager):
    """
    Treatment research model manager
    """
    def filter_by_instance(self, instance):
        """
        Query a related treatment research object/record from another model's object
        :param instance: Object instance
        :return: Query result from content type/model
        :rtye: object/record
        """
        return model_instance_filter(instance, self, TreatmentResearchManager)

    def filter_by_model_type(self, instance):
        """
        Query related objects/model type
        :param instance: Object instance
        :return: Matching object else none
        :rtype: Object/record
        """
        obj_qs = model_foreign_key_qs(instance, self, TreatmentResearchManager)
        if obj_qs.exists():
            return model_type_filter(self, obj_qs, TreatmentResearchManager)

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


class TreatmentResearch(AuthUserDetail, CreateUpdateTime):
    """
    Creates treatment research entity.
    """
    limit = models.Q(app_label='research', model='research')
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    csapractice = models.ForeignKey(CsaPractice, on_delete=models.PROTECT, verbose_name='CSA Practice')
    experimentrep = models.ForeignKey(
        ExperimentRep, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Experiment Replications'
    )
    experimentdetails = models.ForeignKey(
        ExperimentDetails, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Experiment Details'
    )
    nitrogenapplied = models.ForeignKey(
        NitrogenApplied, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Nitrogen Applied'
    )
    experimentduration = models.ForeignKey(
        ExperimentDuration, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Experiment Duration'
    )
    objects = TreatmentResearchManager()

    def __unicode__(self):
        return str(self.experimentdetails)

    def __str__(self):
        return str(self.experimentdetails)

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Treatment Research'
