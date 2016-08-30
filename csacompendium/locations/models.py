from __future__ import unicode_literals

from csacompendium.utils.abstractmodels import (
    AuthUserDetail,
    CreateUpdateTime,
)
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


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


def create_slug(instance, new_slug=None):
    """
    Create a slug from location name.
    :param instance: Object instance
    :param new_slug: Newly created slug
    :return: Unique slug
    :rtype: string
    """
    slug = slugify(instance.location_name)
    if new_slug is not None:
        slug = new_slug
    qs = Location.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = '{0}-{1}'.format(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


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
        instance.slug = create_slug(instance)
