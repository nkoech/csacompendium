from __future__ import unicode_literals

from django.conf import settings
from django.db import models


# Create your models here.

class Country(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    country_code = models.CharField(max_length=2, unique=True, help_text='Country abbreviated name')
    country_name = models.CharField(max_length=50, unique=True)
    last_update = models.DateTimeField(auto_now=True, auto_now_add=False)
    time_created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        self.country_name

    def __str__(self):
        self.country_name

    class Meta:
        ordering = ["-time_created", "-last_update"]
