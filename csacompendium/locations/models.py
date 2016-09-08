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


class LocationManager(models.Manager):
    """
    Location model manager
    """
    def filter_by_instance(self, instance):
        """
        Query a related Location object/record from another model's object
        :param instance: Object instance
        :return: Query result from content type/model
        :rtye: object/record
        """
        return model_instance_filter(instance, self, LocationManager)

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


class Location(AuthUserDetail, CreateUpdateTime):
    """
    Location model.  Creates location entity.
    """
    limit = models.Q(app_label='countries', model='country')
    slug = models.SlugField(unique=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    location_name = models.CharField(max_length=256, blank=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    elevation = models.FloatField(blank=True, null=True)
    objects = LocationManager()

    def __unicode__(self):
        return self.location_name

    def __str__(self):
        return self.location_name

    def get_api_url(self):
        """
        Get location URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('location_api:location_detail', kwargs={'slug': self.slug})

    class Meta:
        unique_together = ['latitude', 'longitude']
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Locations'

    @property
    def model_type_relation(self):
        """
        Get related LocationRelation object/record
        :return: Query result from the LocationRelation model
        :rtye: object/record
        """
        instance = self
        qs = LocationRelation.objects.filter_by_model_type(instance)
        return qs


@receiver(pre_save, sender=Location)
def pre_save_country_receiver(sender, instance, *args, **kwargs):
    """
    Create a slug before save.
    :param sender: Signal sending objec
    :param instance: Object instance
    :param args: Any other argument
    :param kwargs: Keyword arguments
    :return: None
    :rtype: None
    """
    if not instance.slug:
        instance.slug = create_slug(instance, Location, instance.location_name)


class LocationRelationManager(models.Manager):
    """
    Location relation model manager
    """
    def filter_by_instance(self, instance):
        """
        Query a related LocationRelation object/record from another model's object
        :param instance: Object instance
        :return: Query result from content type/model
        :rtye: object/record
        """
        return model_instance_filter(instance, self, LocationRelationManager)

    def filter_by_model_type(self, instance):
        """
        Query related objects/mode type
        :param instance: Object instance
        :return: Matching object else none
        :rtype: Object/record
        """
        obj_qs = super(LocationRelationManager, self).filter(location=instance.id)
        return model_type_filter(self, obj_qs, LocationRelationManager)

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


class LocationRelation(AuthUserDetail, CreateUpdateTime):
    """
    Location entry relationship model. A many to many bridge table between location  model
    and other models
    """
    limit = models.Q(app_label='locations', model='temperature') | models.Q(app_label='locations', model='location')
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    objects = LocationRelationManager()

    class Meta:
        ordering = ['-time_created', '-last_update']


class Temperature(AuthUserDetail, CreateUpdateTime):
    """
    Temperature model. Creates temperature entity
    """
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    temperature_uom = models.CharField(max_length=5, default='°C')

    def __unicode__(self):
        return str(self.temperature)

    def __str__(self):
        return str(self.temperature)

    def get_api_url(self):
        """
        Get temperature URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('location_api:temperature_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Temperatures'

    @property
    def location_relations(self):
        """
        Get related LocationRelation object/record
        :return: Query result from the LocationRelation model
        :rtye: object/record
        """
        instance = self
        qs = LocationRelation.objects.filter_by_instance(instance)
        return qs

