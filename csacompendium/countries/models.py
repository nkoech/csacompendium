from __future__ import unicode_literals

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


def create_slug(instance, new_slug=None):
    """
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
    :param sender: Signal sending objec
    :param instance: Object instance
    :param args: Any other argument
    :param kwargs: Keyword arguments
    :return: None
    :rtype: None
    """
    if not instance.slug:
        instance.slug = create_slug(instance)