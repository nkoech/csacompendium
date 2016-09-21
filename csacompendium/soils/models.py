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
    soil_type = models.CharField(max_length=80)
    classification = models.CharField(max_length=80, blank=True, null=True)

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
        return reverse('soil_api:soil_type_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Soil Types'

    @property
    def model_type_relation(self):
        """
        Get related soil properties
        :return: Query result from the soil model
        :rtye: object/record
        """
        instance = self
        qs = Soil.objects.filter_by_model_type(instance)
        return qs

@receiver(pre_save, sender=SoilType)
def pre_save_soil_type_receiver(sender, instance, *args, **kwargs):
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


class SoilTexture(AuthUserDetail, CreateUpdateTime):
    """
    Soil texture model.  Creates soil type entity.
    """
    slug = models.SlugField(unique=True, blank=True)
    soil_texture = models.CharField(max_length=50)

    def __unicode__(self):
        return self.soil_texture

    def __str__(self):
        return self.soil_texture

    def get_api_url(self):
        """
        Get soil texture URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('soil_api:soil_texture_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Soil Textures'

    @property
    def model_type_relation(self):
        """
        Get related soil textures
        :return: Query result from the soil model
        :rtye: object/record
        """
        instance = self
        qs = Soil.objects.filter_by_model_type(instance)
        return qs

@receiver(pre_save, sender=SoilType)
def pre_save_soil_texture_receiver(sender, instance, *args, **kwargs):
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

    def filter_by_model_type(self, instance):
        """
        Query related objects/model type
        :param instance: Object instance
        :return: Matching object else none
        :rtype: Object/record
        """
        soil_type_obj_qs = super(SoilManager, self).filter(soil_type=instance.id)
        soil_texture_obj_qs = super(SoilManager, self).filter(soil_texture=instance.id)
        if soil_type_obj_qs.exists():
            return model_type_filter(self, soil_type_obj_qs, SoilManager)
        else:
            return model_type_filter(self, soil_texture_obj_qs, SoilManager)

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
    soil_texture = models.ForeignKey(SoilTexture, on_delete=models.PROTECT)
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    som = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='Soil Organic Matter (SOM)')
    som_uom = models.CharField(max_length=6, blank=True, null=True, verbose_name='SOM UOM')
    initial_soc = models.DecimalField(
        max_digits=6, decimal_places=4, blank=True, null=True, verbose_name='Initial SOM'
    )
    soil_ph = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True)
    soil_years = models.SmallIntegerField(blank=True, null=True)
    objects = SoilManager()

    def __unicode__(self):
        return str(self.som)

    def __str__(self):
        return self.som

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Soils'
