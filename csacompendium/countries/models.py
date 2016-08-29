from __future__ import unicode_literals

from csacompendium.locations.models import Location
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


class Country(models.Model):
    """
    Country model.  Creates country entity.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(app_label)s_%(class)s', default=1)
    country_code = models.CharField(max_length=2, unique=True, help_text='Country abbreviated name')
    country_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    last_update = models.DateTimeField(auto_now=True, auto_now_add=False)
    time_created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return '{0} - {1}'.format(self.country_name, self.country_code)

    def __str__(self):
        return '{0} - {1}'.format(self.country_name, self.country_code)

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


def create_slug(instance, new_slug=None):
    """
    Create a slug from country name.
    :param instance: Object instance
    :param new_slug: Newly created slug
    :return: Unique slug
    :rtype: string
    """
    slug = slugify(instance.country_name)
    if new_slug is not None:
        slug = new_slug
    qs = Country.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = '{0}-{1}'.format(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


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
        instance.slug = create_slug(instance)