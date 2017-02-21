from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from decimal import Decimal


class AuthUserDetail(models.Model):
    """
    Abstract model
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(app_label)s_%(class)s', default=1)

    class Meta:
        abstract = True


class ResearchOutcome(models.Model):
    """
    Abstract model for control and treatment research outcome.
    """
    mean_outcome = models.DecimalField(
        max_digits=8, decimal_places=2, default=Decimal('0.0'), verbose_name='Mean outcome'
    )
    std_outcome = models.DecimalField(
        max_digits=8, decimal_places=2, default=Decimal('0.0'),  verbose_name='Standard outcome'
    )
    outcome_uom = models.CharField(max_length=200, default='kg/ha')

    class Meta:
        abstract = True


class CreateUpdateTime(models.Model):
    """
    Model update and creation time abstract model.
    """
    last_update = models.DateTimeField(auto_now=True, auto_now_add=False)
    time_created = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        abstract = True
