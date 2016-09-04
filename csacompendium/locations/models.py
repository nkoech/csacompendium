from __future__ import unicode_literals

from csacompendium.utils.abstractmodels import (
    AuthUserDetail,
    CreateUpdateTime,
)
from csacompendium.utils.createslug import create_slug
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class LocationManager(models.Manager):
    """
    Location model manager
    """
    def filter_by_instance(self, instance):
        """
        Query a related location object/record from another model's object
        :param instance: Object instance
        :return: Query result from content type/model
        :rtye: object/record
        """
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(LocationManager, self).filter(content_type=content_type, object_id=obj_id)
        return qs

    def create_by_model_type(self, model_type, slug, location_name, latitude, longitude, elevation, user):
        model_qs = ContentType.objects.filter(model=model_type)
        if model_qs.exists():
            any_model = model_qs.first().model_class()
            obj_qs = any_model.objects.filter(slug=slug)
            if obj_qs.exists() and obj_qs.count() == 1:
                instance = self.model()
                instance.content_type = model_qs.first()
                instance.object_id = obj_qs.first().id
                instance.location_name = location_name
                instance.latitude = latitude
                instance.longitude = longitude
                instance.elevation = elevation
                instance.user = user
                instance.modified_by = user
                instance.save()
                return instance
            return None


class Location(AuthUserDetail, CreateUpdateTime):
    """
    Location model.  Creates location entity.
    """
    slug = models.SlugField(unique=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    location_name = models.CharField(max_length=256, blank=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=6, unique=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, unique=True)
    elevation = models.FloatField(blank=True, null=True)

    objects = LocationManager()

    def __unicode__(self):
        return self.location_name

    def __str__(self):
        return self.location_name

    class Meta:
        unique_together = ['latitude', 'longitude']
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Locations'


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
