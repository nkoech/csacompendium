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
    objects = ControlResearchManager()

    def __unicode__(self):
        return str(self.experimentdetails)

    def __str__(self):
        return str(self.experimentdetails)

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Control Research'
