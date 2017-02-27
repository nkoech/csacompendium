# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from csacompendium.utils.abstractmodels import (
    AuthUserDetail,
    CreateUpdateTime,
)
from csacompendium.utils.createslug import create_slug
from csacompendium.utils.modelmanagers import (
    model_instance_filter,
    model_foreign_key_qs,
    model_type_filter,
    create_model_type,
)
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse


class CsaTheme(AuthUserDetail, CreateUpdateTime):
    """
    CSA theme model. Creates CSA theme entity.
    """
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    csa_theme = models.CharField(max_length=80, unique=True, verbose_name='CSA theme')

    def __unicode__(self):
        return self.csa_theme

    def __str__(self):
        return self.csa_theme

    def get_api_url(self):
        """
        Get CSA theme URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('csa_practice_api:csa_theme_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'CSA Practice Themes'

    @property
    def csa_practice_relation(self):
        """
        Get related CSA practice
        :return: Query result from the CSA practice model
        :rtype: object/record
        """
        instance = self
        qs = CsaPractice.objects.filter_by_model_type(instance)
        return qs


@receiver(pre_save, sender=CsaTheme)
def pre_save_csa_theme_receiver(sender, instance, *args, **kwargs):
    """
    Create a slug before save.
    :param sender: Signal sending object
    :param instance: Object instance
    :param args: Any other argument
    :param kwargs: Keyword arguments
    :return: None
    :rtype: None
    """
    if not instance.slug:
        instance.slug = create_slug(instance, CsaTheme, instance.csa_theme)


class PracticeLevel(AuthUserDetail, CreateUpdateTime):
    """
    CSA level of practice model.  Creates CSA practice level entity.
    """
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    practice_level = models.CharField(max_length=150, unique=True)

    def __unicode__(self):
        return self.practice_level

    def __str__(self):
        return self.practice_level

    def get_api_url(self):
        """
        Get CSA practice level URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('csa_practice_api:practice_level_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'CSA Practice Levels'

    @property
    def csa_practice_relation(self):
        """
        Get related CSA practice
        :return: Query result from the CSA practice model
        :rtype: object/record
        """
        instance = self
        qs = CsaPractice.objects.filter_by_model_type(instance)
        return qs


@receiver(pre_save, sender=PracticeLevel)
def pre_save_practice_level_receiver(sender, instance, *args, **kwargs):
    """
    Create a slug before save.
    :param sender: Signal sending object
    :param instance: Object instance
    :param args: Any other argument
    :param kwargs: Keyword arguments
    :return: None
    :rtype: None
    """
    if not instance.slug:
        instance.slug = create_slug(instance, PracticeLevel, instance.practice_level)


class PracticeType(AuthUserDetail, CreateUpdateTime):
    """
    CSA practice type model.  Creates CSA practice type entity.
    """
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    practice_type = models.CharField(max_length=120, unique=True, verbose_name='Practice category')

    def __unicode__(self):
        return self.practice_type

    def __str__(self):
        return self.practice_type

    def get_api_url(self):
        """
        Get CSA practice type URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('csa_practice_api:practice_type_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'CSA Practice Types'

    @property
    def csa_practice_relation(self):
        """
        Get related CSA practice
        :return: Query result from the CSA practice model
        :rtype: object/record
        """
        instance = self
        qs = CsaPractice.objects.filter_by_model_type(instance)
        return qs


@receiver(pre_save, sender=PracticeType)
def pre_save_practice_type_receiver(sender, instance, *args, **kwargs):
    """
    Create a slug before save.
    :param sender: Signal sending object
    :param instance: Object instance
    :param args: Any other argument
    :param kwargs: Keyword arguments
    :return: None
    :rtype: None
    """
    if not instance.slug:
        instance.slug = create_slug(instance, PracticeType, instance.practice_type)


class CsaPracticeManager(models.Manager):
    """
    CSA practice model manager
    """
    def filter_by_model_type(self, instance):
        """
        Query related objects/model type
        :param instance: Object instance
        :return: Matching object else none
        :rtype: Object/record
        """
        obj_qs = model_foreign_key_qs(instance, self, CsaPracticeManager)
        if obj_qs.exists():
            return model_type_filter(self, obj_qs, CsaPracticeManager)


class CsaPractice(AuthUserDetail, CreateUpdateTime):
    """
    CSA practice model.  Creates CSA practice entity.
    """
    slug = models.SlugField(unique=True, blank=True)
    practice_code = models.CharField(max_length=6, unique=True, help_text='User defined CSA practice code')
    csatheme = models.ForeignKey(CsaTheme, on_delete=models.PROTECT, verbose_name='CSA theme')
    practicelevel = models.ForeignKey(PracticeLevel, on_delete=models.PROTECT, verbose_name='Practice level')
    sub_practice_level = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    practicetype = models.ForeignKey(PracticeType, on_delete=models.PROTECT, verbose_name='Practice category')
    objects = CsaPracticeManager()

    def __unicode__(self):
        return self.sub_practice_level

    def __str__(self):
        return self.sub_practice_level

    def get_api_url(self):
        """
        Get CSA practice URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('csa_practice_api:csa_practice_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'CSA Practices'

    @property
    def research_csa_practice(self):
        """
        Get related research CSA practice object/record
        :return: Query result from the research CSA practice model
        :rtype: object/record
        """
        instance = self
        qs = ResearchCsaPractice.objects.filter_by_model_type(instance)
        return qs


@receiver(pre_save, sender=CsaPractice)
def pre_save_csa_practice_receiver(sender, instance, *args, **kwargs):
    """
    Create a slug before save.
    :param sender: Signal sending object
    :param instance: Object instance
    :param args: Any other argument
    :param kwargs: Keyword arguments
    :return: None
    :rtype: None
    """
    if not instance.slug:
        instance.slug = create_slug(instance, CsaPractice, instance.practice_code)


class ResearchCsaPracticeManager(models.Manager):
    """
    Research CSA practice model manager
    """
    def filter_by_instance(self, instance):
        """
        Query a related research CSA practice object/record from another model's object
        :param instance: Object instance
        :return: Query result from content type/model
        :rtye: object/record
        """
        return model_instance_filter(instance, self, ResearchCsaPracticeManager)

    def filter_by_model_type(self, instance):
        """
        Query related objects/model type
        :param instance: Object instance
        :return: Matching object else none
        :rtype: Object/record
        """
        obj_qs = model_foreign_key_qs(instance, self, ResearchCsaPracticeManager)
        if obj_qs.exists():
            return model_type_filter(self, obj_qs, ResearchCsaPracticeManager)

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


class ResearchCsaPractice(AuthUserDetail, CreateUpdateTime):
    """
    Research CSA practice entry relationship model. A many to many bridge
    table between control/treatment research and other models
    """
    limit = models.Q(app_label='research', model='controlresearch') | \
            models.Q(app_label='research', model='treatmentresearch')
    csapractice = models.ForeignKey(CsaPractice, on_delete=models.PROTECT,  verbose_name='CSA practice')
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    objects = ResearchCsaPracticeManager()

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Research CSA Practices'








