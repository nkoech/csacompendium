from __future__ import unicode_literals

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from django.utils.text import slugify


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


class Location(models.Model):
    """
    Location model.  Creates location entity.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(app_label)s_%(class)s', default=1)
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    location_name = models.CharField(max_length=256, blank=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=6, unique=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, unique=True)
    elevation = models.FloatField(blank=True)
    last_update = models.DateTimeField(auto_now=True, auto_now_add=False)
    time_created = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = LocationManager()

    def __unicode__(self):
        return self.location_name

    def __str__(self):
        return self.location_name

    class Meta:
        unique_together = ['latitude', 'longitude']
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Locations'
