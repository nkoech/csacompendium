# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from csacompendium.utils.abstractmodels import (
    AuthUserDetail,
    CreateUpdateTime,
)
from csacompendium.utils.createslug import create_slug
from csacompendium.utils.modelmanagers import (
    model_instance_filter,
    model_type_filter,
    create_model_type,
)
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse


class SoilType(AuthUserDetail, CreateUpdateTime):
    """
    Soil type model.  Creates soil type entity.
    """
    slug = models.SlugField(unique=True, blank=True)
    soil_type = models.TextField()
    classification = models.TextField()

    def __unicode__(self):
        return self.soil_type

    def __str__(self):
        return self.soil_type

    def get_api_url(self):
        """
        Get soil type URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('soil_api:soil_type_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Soil Types'

@receiver(pre_save, sender=SoilType)
def pre_save_location_receiver(sender, instance, *args, **kwargs):
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
        instance.slug = create_slug(instance, SoilType, instance.soil_type)


class SoilManager(models.Manager):
    """
    Soil model manager
    """
    def filter_by_instance(self, instance):
        """
        Query a related soil object/record from another model's object
        :param instance: Object instance
        :return: Query result from content type/model
        :rtye: object/record
        """
        return model_instance_filter(instance, self, SoilManager)

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


class Soil(AuthUserDetail, CreateUpdateTime):
    """
    Soil model.  Creates soil entity.
    """
    limit = models.Q(app_label='locations', model='location')
    soil_type = models.ForeignKey(SoilType, on_delete=models.PROTECT)
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    som = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='Soil Organic Matter')
    som_uom = models.CharField(max_length=6, blank=True, null=True, verbose_name='Soil Organic Matter UOM')
    initial_soc = models.DecimalField(
        max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='Initial Soil Organic Carbon'
    )
    soil_ph = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True)
    soil_years = models.SmallIntegerField(blank=True, null=True)
    objects = SoilManager()

    def __unicode__(self):
        return str(self.som)

    def __str__(self):
        return self.som

    # def get_api_url(self):
    #     """
    #     Get soil URL as a reverse from model
    #     :return: URL
    #     :rtype: String
    #     """
    #     return reverse('soil_api:soil_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Soils'
