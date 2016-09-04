from __future__ import unicode_literals

from csacompendium.utils.abstractmodels import (
    AuthUserDetail,
    CreateUpdateTime,
)
from csacompendium.locations.models import Location
from csacompendium.utils.createslug import create_slug
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse


class Country(AuthUserDetail, CreateUpdateTime):
    """
    Country model.  Creates country entity.
    """
    country_code = models.CharField(max_length=2, unique=True, help_text='Country abbreviated name')
    country_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def __unicode__(self):
        return self.country_name

    def __str__(self):
        return self.country_name

    def get_api_url(self):
        """
        Get country URL as a reverse from another app
        :return: URL
        :rtype: String
        """
        return reverse('country_api:detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Countries'

    @property
    def locations(self):
        """
        Get related location object/record
        :return: Query result from the location model
        :rtye: object/record
        """
        instance = self
        qs = Location.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        """
        Get country content type
        :return: Content type
        :rtye: object/record
        """
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type


@receiver(pre_save, sender=Country)
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
        instance.slug = create_slug(instance, Country, instance.country_name)
