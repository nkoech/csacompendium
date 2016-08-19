from __future__ import unicode_literals

from django.conf import settings
from django.db import models


class Country(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    country_code = models.CharField(max_length=2, unique=True, help_text='Country abbreviated name')
    country_name = models.CharField(max_length=50, unique=True)
    last_update = models.DateTimeField(auto_now=True, auto_now_add=False)
    time_created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return '{0} - {1}'.format(self.country_name, self.country_code)

    def __str__(self):
        return '{0} - {1}'.format(self.country_name, self.country_code)

    class Meta:
        ordering = ["-time_created", "-last_update"]
        verbose_name_plural = "Countries"
