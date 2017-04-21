# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from csacompendium.indicators.models import ResearchOutcomeIndicator
from csacompendium.csa_practice.models import ResearchCsaPractice
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
    get_year_choices,
    get_datetime_now,
)
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse
from decimal import Decimal


class NitrogenApplied(AuthUserDetail, CreateUpdateTime):
    """
    Nitrogen applied model
    """
    NITROGEN_SOURCE = (
        ('Organic', 'Organic'),
        ('Inorganic', 'Inorganic'),
    )
    nitrogen_amount = models.DecimalField(max_digits=6, decimal_places=2,  unique=True)
    amount_uom = models.CharField(max_length=12, verbose_name='Nitrogen UOM', default='kg/ha')
    nitrogen_source = models.CharField(max_length=30, choices=NITROGEN_SOURCE)

    def __unicode__(self):
        str_format = 'Amount {0}, UoM {1}, Source {2} '.format(
            self.nitrogen_amount, self.amount_uom, self.nitrogen_source
        )
        return str(str_format)

    def __str__(self):
        str_format = 'Amount {0}, UoM {1}, Source {2} '.format(
            self.nitrogen_amount, self.amount_uom, self.nitrogen_source
        )
        return str(str_format)

    def get_api_url(self):
        """
        Get nitrogen applied URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('research_api:nitrogen_applied_detail', kwargs={'pk': self.pk})

    class Meta:
        unique_together = ['nitrogen_amount', 'nitrogen_source']
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Nitrogen Applied'

    @property
    def research_nitrogen_applied_relation(self):
        """
        Get related research nitrogen applied object/record
        :return: Query result from the research nitrogen applied model
        :rtype: object/record
        """
        instance = self
        qs = ResearchNitrogenApplied.objects.filter_by_model_type(instance)
        return qs


class ResearchNitrogenAppliedManager(models.Manager):
    """
    Research nitrogen applied model manager
    """
    def filter_by_instance(self, instance):
        """
        Query a related research nitrogen applied object/record from another model's object
        :param instance: Object instance
        :return: Query result from content type/model
        :rtype: object/record
        """
        return model_instance_filter(instance, self, ResearchNitrogenAppliedManager)

    def filter_by_model_type(self, instance):
        """
        Query related objects/model type
        :param instance: Object instance
        :return: Matching object else none
        :rtype: Object/record
        """
        obj_qs = model_foreign_key_qs(instance, self, ResearchNitrogenAppliedManager)
        if obj_qs.exists():
            return model_type_filter(self, obj_qs, ResearchNitrogenAppliedManager)

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


class ResearchNitrogenApplied(AuthUserDetail, CreateUpdateTime):
    """
    Research nitrogen applied entry relationship model.
    A many to many bridge table between research and other models
    """
    limit = models.Q(app_label='research', model='research')
    nitrogenapplied = models.ForeignKey(NitrogenApplied, on_delete=models.PROTECT)
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    objects = ResearchNitrogenAppliedManager()

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Research Nitrogen Applied'


class MeasurementYear(AuthUserDetail, CreateUpdateTime):
    """
    Measurement year model
    """
    slug = models.SlugField(max_length=10, unique=True, blank=True)
    measurement_year = models.SmallIntegerField(choices=get_year_choices(), unique=True, default=get_datetime_now())

    def __unicode__(self):
        return str(self.measurement_year)

    def __str__(self):
        return str(self.measurement_year)

    def get_api_url(self):
        """
        Get measurement year URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('research_api:measurement_year_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Measurement Years'

    @property
    def research_measurement_year_relation(self):
        """
        Get related research measurement year object/record
        :return: Query result from the research measurement year model
        :rtype: object/record
        """
        instance = self
        qs = ResearchMeasurementYear.objects.filter_by_model_type(instance)
        return qs


@receiver(pre_save, sender=MeasurementYear)
def pre_save_measurement_year_receiver(sender, instance, *args, **kwargs):
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
        instance.slug = create_slug(instance, MeasurementYear, instance.measurement_year)


class MeasurementDuration(AuthUserDetail, CreateUpdateTime):
    """
    Measurement duration model
    """
    measurement_duration = models.DecimalField(max_digits=6, decimal_places=2, unique=True)

    def __unicode__(self):
        return str(self.measurement_duration)

    def __str__(self):
        return str(self.measurement_duration)

    def get_api_url(self):
        """
        Get measurement duration URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('research_api:measurement_duration_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Measurement Duration'

    @property
    def research_measurement_year_relation(self):
        """
        Get related research measurement year properties
        :return: Query result from the research measurement year model
        :rtype: object/record
        """
        instance = self
        qs = ResearchMeasurementYear.objects.filter_by_model_type(instance)
        return qs


class MeasurementSeason(AuthUserDetail, CreateUpdateTime):
    """
    Measurement season model
    """
    SEASONS = (
        ('First Growing Season', 'First Growing Season'),
        ('Second Growing Season', 'Second Growing Season'),
    )
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    measurement_season = models.CharField(max_length=42, choices=SEASONS, unique=True, null=True)

    def __unicode__(self):
        return self.measurement_season

    def __str__(self):
        return self.measurement_season

    def get_api_url(self):
        """
        Get measurement season URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('research_api:measurement_season_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Measurement Seasons'

    @property
    def research_measurement_year_relation(self):
        """
        Get related research measurement year properties
        :return: Query result from the research measurement year model
        :rtype: object/record
        """
        instance = self
        qs = ResearchMeasurementYear.objects.filter_by_model_type(instance)
        return qs


@receiver(pre_save, sender=MeasurementSeason)
def pre_save_measurement_season_receiver(sender, instance, *args, **kwargs):
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
        instance.slug = create_slug(instance, MeasurementSeason, instance.measurement_season)


class ResearchMeasurementYearManager(models.Manager):
    """
    Research measurement year model manager
    """
    def filter_by_instance(self, instance):
        """
        Query a related research measurement year object/record from another model's object
        :param instance: Object instance
        :return: Query result from content type/model
        :rtype: object/record
        """
        return model_instance_filter(instance, self, ResearchMeasurementYearManager)

    def filter_by_model_type(self, instance):
        """
        Query related objects/model type
        :param instance: Object instance
        :return: Matching object else none
        :rtype: Object/record
        """
        obj_qs = model_foreign_key_qs(instance, self, ResearchMeasurementYearManager)
        if obj_qs.exists():
            return model_type_filter(self, obj_qs, ResearchMeasurementYearManager)

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


class ResearchMeasurementYear(AuthUserDetail, CreateUpdateTime):
    """
    Research measurement year entry relationship model.
    A many to many bridge table between research and other models
    """
    limit = models.Q(app_label='research', model='research')
    measurementyear = models.ForeignKey(MeasurementYear, on_delete=models.PROTECT)
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    measurementduration = models.ForeignKey(MeasurementDuration, on_delete=models.SET_NULL, blank=True, null=True)
    measurementseason = models.ForeignKey(MeasurementSeason, on_delete=models.SET_NULL, blank=True, null=True)
    objects = ResearchMeasurementYearManager()

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Research Measurement Years'


class Diversity(AuthUserDetail, CreateUpdateTime):
    """
    Diversity model
    """
    slug = models.SlugField(max_length=360, unique=True, blank=True)
    diversity = models.CharField(max_length=360, unique=True)

    def __unicode__(self):
        return self.diversity

    def __str__(self):
        return self.diversity

    def get_api_url(self):
        """
        Get diversity URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('research_api:diversity_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Diversity'

    @property
    def research_diversity_relation(self):
        """
        Get related research diversity object/record
        :return: Query result from the research diversity model
        :rtype: object/record
        """
        instance = self
        qs = ResearchDiversity.objects.filter_by_model_type(instance)
        return qs


@receiver(pre_save, sender=Diversity)
def pre_save_diversity_receiver(sender, instance, *args, **kwargs):
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
        instance.slug = create_slug(instance, Diversity, instance.diversity)


class ResearchDiversityManager(models.Manager):
    """
    Research diversity model manager
    """
    def filter_by_instance(self, instance):
        """
        Query a related research diversity object/record from another model's object
        :param instance: Object instance
        :return: Query result from content type/model
        :rtype: object/record
        """
        return model_instance_filter(instance, self, ResearchDiversityManager)

    def filter_by_model_type(self, instance):
        """
        Query related objects/model type
        :param instance: Object instance
        :return: Matching object else none
        :rtype: Object/record
        """
        obj_qs = model_foreign_key_qs(instance, self, ResearchDiversityManager)
        if obj_qs.exists():
            return model_type_filter(self, obj_qs, ResearchDiversityManager)

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


class ResearchDiversity(AuthUserDetail, CreateUpdateTime):
    """
    Research diversity entry relationship model.
    A many to many bridge table between research and other models
    """
    limit = models.Q(app_label='research', model='research')
    diversity = models.ForeignKey(Diversity, on_delete=models.PROTECT)
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    objects = ResearchDiversityManager()

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Research Diversity'


class ExperimentDescription(AuthUserDetail, CreateUpdateTime):
    """
    Experiment description model
    """
    slug = models.SlugField(max_length=500, unique=True, blank=True)
    experiment_description = models.TextField(unique=True)

    def __unicode__(self):
        return self.experiment_description

    def __str__(self):
        return self.experiment_description

    def get_api_url(self):
        """
        Get experiment description URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('research_api:experiment_description_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Experiment Descriptions'

    @property
    def research_experiment_description_relation(self):
        """
        Get related research experiment description object/record
        :return: Query result from the research experiment description model
        :rtype: object/record
        """
        instance = self
        qs = ResearchExperimentDescription.objects.filter_by_model_type(instance)
        return qs


@receiver(pre_save, sender=ExperimentDescription)
def pre_save_experiment_description_receiver(sender, instance, *args, **kwargs):
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
        instance.slug = create_slug(instance, ExperimentDescription, instance.experiment_description)


class ResearchExperimentDescriptionManager(models.Manager):
    """
    Research experiment description model manager
    """
    def filter_by_instance(self, instance):
        """
        Query a related research experiment description object/record from another model's object
        :param instance: Object instance
        :return: Query result from content type/model
        :rtype: object/record
        """
        return model_instance_filter(instance, self, ResearchExperimentDescriptionManager)

    def filter_by_model_type(self, instance):
        """
        Query related objects/model type
        :param instance: Object instance
        :return: Matching object else none
        :rtype: Object/record
        """
        obj_qs = model_foreign_key_qs(instance, self, ResearchExperimentDescriptionManager)
        if obj_qs.exists():
            return model_type_filter(self, obj_qs, ResearchExperimentDescriptionManager)

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


class ResearchExperimentDescription(AuthUserDetail, CreateUpdateTime):
    """
    Research experiment description entry relationship model.
    A many to many bridge table between research and other models
    """
    limit = models.Q(app_label='research', model='research')
    experimentdescription = models.ForeignKey(
        ExperimentDescription, on_delete=models.PROTECT, verbose_name='Experiment description'
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    objects = ResearchExperimentDescriptionManager()

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Research Experiment Descriptions'


class ExperimentReplicate(AuthUserDetail, CreateUpdateTime):
    """
    Experiment replicate model
    """
    no_replicate = models.PositiveSmallIntegerField(unique=True, verbose_name='Number of replicates')

    def __unicode__(self):
        str_format = 'Replicates {0} '.format(self.no_replicate)
        return str(str_format)

    def __str__(self):
        str_format = 'Replicates {0} '.format(self.no_replicate)
        return str(str_format)

    def get_api_url(self):
        """
        Get experiment replicate URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('research_api:experiment_replicate_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Experiment Replicates'

    @property
    def research_experiment_replicate_relation(self):
        """
        Get related research experiment replicate object/record
        :return: Query result from the research experiment replicate model
        :rtype: object/record
        """
        instance = self
        qs = ResearchExperimentReplicate.objects.filter_by_model_type(instance)
        return qs


class ResearchExperimentReplicateManager(models.Manager):
    """
    Research experiment replicate model manager
    """
    def filter_by_instance(self, instance):
        """
        Query a related research experiment replicate object/record from another model's object
        :param instance: Object instance
        :return: Query result from content type/model
        :rtype: object/record
        """
        return model_instance_filter(instance, self, ResearchExperimentReplicateManager)

    def filter_by_model_type(self, instance):
        """
        Query related objects/model type
        :param instance: Object instance
        :return: Matching object else none
        :rtype: Object/record
        """
        obj_qs = model_foreign_key_qs(instance, self, ResearchExperimentReplicateManager)
        if obj_qs.exists():
            return model_type_filter(self, obj_qs, ResearchExperimentReplicateManager)

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


class ResearchExperimentReplicate(AuthUserDetail, CreateUpdateTime):
    """
    Research experiment replicate entry relationship model.
    A many to many bridge table between research and other models
    """
    limit = models.Q(app_label='research', model='research')
    experimentreplicate = models.ForeignKey(
        ExperimentReplicate, on_delete=models.PROTECT, verbose_name='Experiment replicate'
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    objects = ResearchExperimentReplicateManager()

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Research Experiment Replicates'


class Author(AuthUserDetail, CreateUpdateTime):
    """
    Research author model
    """
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    author_code = models.CharField(max_length=6, unique=True)
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40, null=True, blank=True)
    last_name = models.CharField(max_length=40)
    author_bio = models.TextField(null=True, blank=True)

    def __unicode__(self):
        str_format = '{0} {1}'.format(self.last_name, self.first_name)
        return str(str_format)

    def __str__(self):
        str_format = '{0} {1}'.format(self.last_name, self.first_name)
        return str(str_format)

    def get_api_url(self):
        """
        Get author URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('research_api:author_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Authors'

    @property
    def research_author_relation(self):
        """
        Get related research author object/record
        :return: Query result from the research author model
        :rtype: object/record
        """
        instance = self
        qs = ResearchAuthor.objects.filter_by_model_type(instance)
        return qs


@receiver(pre_save, sender=Author)
def pre_save_author_receiver(sender, instance, *args, **kwargs):
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
        instance_fields = [instance.last_name, instance.first_name]
        instance.slug = create_slug(instance, Author, instance_fields)


class Journal(AuthUserDetail, CreateUpdateTime):
    """
    Journal model
    """
    slug = models.SlugField(max_length=64, unique=True, blank=True)
    journal_tag = models.CharField(max_length=60)
    publication_year = models.SmallIntegerField(choices=get_year_choices(), default=get_datetime_now())

    def __unicode__(self):
        str_format = '{0} - {1}'.format(self.journal_tag, self.publication_year)
        return str(str_format)

    def __str__(self):
        str_format = '{0} - {1}'.format(self.journal_tag, self.publication_year)
        return str(str_format)

    def get_api_url(self):
        """
        Get journal URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('research_api:journal_detail', kwargs={'slug': self.slug})

    class Meta:
        unique_together = ['journal_tag', 'publication_year']
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Journals'

    @property
    def research_author_relation(self):
        """
        Get related research author properties
        :return: Query result from the research author model
        :rtype: object/record
        """
        instance = self
        qs = ResearchAuthor.objects.filter_by_model_type(instance)
        return qs


@receiver(pre_save, sender=Journal)
def pre_save_journal_receiver(sender, instance, *args, **kwargs):
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
        instance_fields = [instance.journal_tag, instance.publication_year]
        instance.slug = create_slug(instance, Journal, instance_fields)


class ResearchAuthorManager(models.Manager):
    """
    Research author model manager
    """
    def filter_by_instance(self, instance):
        """
        Query a related research author object/record from another model's object
        :param instance: Object instance
        :return: Query result from content type/model
        :rtye: object/record
        """
        return model_instance_filter(instance, self, ResearchAuthorManager)

    def filter_by_model_type(self, instance):
        """
        Query related objects/model type
        :param instance: Object instance
        :return: Matching object else none
        :rtype: Object/record
        """
        obj_qs = model_foreign_key_qs(instance, self, ResearchAuthorManager)
        if obj_qs.exists():
            return model_type_filter(self, obj_qs, ResearchAuthorManager)

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


class ResearchAuthor(AuthUserDetail, CreateUpdateTime):
    """
    Research author entry relationship model. A many to many bridge table between research and other models
    """
    limit = models.Q(app_label='research', model='research')
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    journal = models.ForeignKey(Journal, on_delete=models.SET_NULL, blank=True, null=True)
    objects = ResearchAuthorManager()

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Research Authors'


class ExperimentUnitCategory(AuthUserDetail, CreateUpdateTime):
    """
    Experiment unit category model. Creates experiment unit category entity.
    """
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    unit_category = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return self.unit_category

    def __str__(self):
        return self.unit_category

    def get_api_url(self):
        """
        Get experiment unit category URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('research_api:experiment_unit_category_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Experiment Unit Categories'

    @property
    def experiment_unit_relation(self):
        """
        Get related experiment unit properties
        :return: Query result from the experiment unit model
        :rtype: object/record
        """
        instance = self
        qs = ExperimentUnit.objects.filter_by_model_type(instance)
        return qs


@receiver(pre_save, sender=ExperimentUnitCategory)
def pre_save_experiment_unit_category_receiver(sender, instance, *args, **kwargs):
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
        instance.slug = create_slug(instance, ExperimentUnitCategory, instance.unit_category)


class ExperimentUnitManager(models.Manager):
    """
    Experiment unit model manager
    """
    def filter_by_model_type(self, instance):
        """
        Query related objects/model type
        :param instance: Object instance
        :return: Matching object else none
        :rtype: Object/record
        """
        obj_qs = model_foreign_key_qs(instance, self, ExperimentUnitManager)
        if obj_qs.exists():
            return model_type_filter(self, obj_qs, ExperimentUnitManager)


class ExperimentUnit(AuthUserDetail, CreateUpdateTime):
    """
    Experiment unit model. Creates experiment unit entity.
    """
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    exp_unit_code = models.CharField(max_length=20, unique=True, verbose_name='Experiment unit code')
    experimentunitcategory = models.ForeignKey(
        ExperimentUnitCategory, on_delete=models.PROTECT, verbose_name='Unit categories'
    )
    common_name = models.CharField(max_length=250)
    latin_name = models.CharField(max_length=250, blank=True, null=True)
    objects = ExperimentUnitManager()

    def __unicode__(self):
        return self.common_name

    def __str__(self):
        return self.common_name

    def get_api_url(self):
        """
        Get experiment unit model URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('research_api:experiment_unit_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Experiment Units'

    @property
    def research_experiment_unit_relation(self):
        """
        Get related experiment unit object/record
        :return: Query result from the research experiment unit model
        :rtype: object/record
        """
        instance = self
        qs = ResearchExperimentUnit.objects.filter_by_model_type(instance)
        return qs


@receiver(pre_save, sender=ExperimentUnit)
def pre_save_experiment_unit_receiver(sender, instance, *args, **kwargs):
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
        instance.slug = create_slug(instance, ExperimentUnit, instance.common_name)


class Breed(AuthUserDetail, CreateUpdateTime):
    """
    Breed model
    """
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    breed = models.CharField(max_length=120, unique=True)

    def __unicode__(self):
        return self.breed

    def __str__(self):
        return self.breed

    def get_api_url(self):
        """
        Get breed URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('research_api:breed_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Breeds'

    @property
    def research_experiment_unit_relation(self):
        """
        Get related research experiment unit properties
        :return: Query result from the research experiment unit model
        :rtype: object/record
        """
        instance = self
        qs = ResearchExperimentUnit.objects.filter_by_model_type(instance)
        return qs


@receiver(pre_save, sender=Breed)
def pre_save_breed_receiver(sender, instance, *args, **kwargs):
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
        instance.slug = create_slug(instance, Breed, instance.breed)


class ResearchExperimentUnitManager(models.Manager):
    """
    Research experiment unit model manager
    """
    def filter_by_instance(self, instance):
        """
        Query a related research experiment unit object/record from another model's object
        :param instance: Object instance
        :return: Query result from content type/model
        :rtype: object/record
        """
        return model_instance_filter(instance, self, ResearchExperimentUnitManager)

    def filter_by_model_type(self, instance):
        """
        Query related objects/model type
        :param instance: Object instance
        :return: Matching object else none
        :rtype: Object/record
        """
        obj_qs = model_foreign_key_qs(instance, self, ResearchExperimentUnitManager)
        if obj_qs.exists():
            return model_type_filter(self, obj_qs, ResearchExperimentUnitManager)

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


class ResearchExperimentUnit(AuthUserDetail, CreateUpdateTime):
    """
    Research experiment unit entry relationship model. A many to many bridge table
    between research and other models
    """
    limit = models.Q(app_label='research', model='research')
    experimentunit = models.ForeignKey(ExperimentUnit, on_delete=models.PROTECT, verbose_name='Experiment Unit')
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, blank=True, null=True)
    objects = ResearchExperimentUnitManager()

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Research Experiment Units'


class ResearchManager(models.Manager):
    """
    Research model manager
    """
    def filter_by_instance(self, instance):
        """
        Query a related Research object/record from another model's object
        :param instance: Object instance
        :return: Query result from content type/model
        :rtype: object/record
        """
        return model_instance_filter(instance, self, ResearchManager)

    def filter_by_model_type(self, instance):
        """
        Query related objects/model type
        :param instance: Object instance
        :return: Matching object else none
        :rtype: Object/record
        """
        obj_qs = model_foreign_key_qs(instance, self, ResearchManager)
        if obj_qs.exists():
            return model_type_filter(self, obj_qs, ResearchManager)

    def create_by_model_type(self, model_type, pk, **kwargs):
        """
        Create object by model type
        :param model_type: Content/model type
        :param pk: Primary Key
        :param kwargs: Fields to be created
        :return: Data object
        :rtype: Object
        """
        return create_model_type(self, model_type, pk, slugify=False, **kwargs)


class Research(AuthUserDetail, CreateUpdateTime):
    """
    Creates research entity.
    """
    EXPERIMENT_DESIGN = (
        ('Control Treatment', 'Control Treatment'),
        ('Improved Treatment', 'Improved Treatment'),
    )
    limit = models.Q(app_label='locations', model='location')
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    experiment_design = models.CharField(max_length=22, choices=EXPERIMENT_DESIGN)
    objects = ResearchManager()

    def __unicode__(self):
        str_format = '{0} - {1}'.format(self.experiment_design, self.id)
        return str(str_format)

    def __str__(self):
        str_format = '{0} - {1}'.format(self.experiment_design, self.id)
        return str(str_format)

    def get_api_url(self):
        """
        Get Research URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('research_api:research_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Research'

    @property
    def research_measurement_year(self):
        """
        Get related research measurement year object/record
        :return: Query result from the research measurement year model
        :rtype: object/record
        """
        instance = self
        qs = ResearchMeasurementYear.objects.filter_by_instance(instance)
        return qs

    @property
    def research_diversity(self):
        """
        Get related research diversity object/record
        :return: Query result from the research diversity model
        :rtype: object/record
        """
        instance = self
        qs = ResearchDiversity.objects.filter_by_instance(instance)
        return qs

    @property
    def research_experiment_description(self):
        """
        Get related research experiment description object/record
        :return: Query result from the research experiment description model
        :rtype: object/record
        """
        instance = self
        qs = ResearchExperimentDescription.objects.filter_by_instance(instance)
        return qs

    @property
    def research_experiment_replicate(self):
        """
        Get related research experiment replicate object/record
        :return: Query result from the research experiment replicate model
        :rtype: object/record
        """
        instance = self
        qs = ResearchExperimentReplicate.objects.filter_by_instance(instance)
        return qs

    @property
    def research_author(self):
        """
        Get related research author object/record
        :return: Query result from the research author model
        :rtype: object/record
        """
        instance = self
        qs = ResearchAuthor.objects.filter_by_instance(instance)
        return qs

    @property
    def research_outcome_indicator(self):
        """
        Get related research outcome indicator object/record
        :return: Query result from the research outcome indicator model
        :rtype: object/record
        """
        instance = self
        qs = ResearchOutcomeIndicator.objects.filter_by_instance(instance)
        return qs

    @property
    def research_csa_practice(self):
        """
        Get related research CSA practice object/record
        :return: Query result from the research CSA practice model
        :rtype: object/record
        """
        instance = self
        qs = ResearchCsaPractice.objects.filter_by_instance(instance)
        return qs

    @property
    def research_experiment_unit(self):
        """
        Get related research experiment unit object/record
        :return: Query result from the research experiment unit model
        :rtype: object/record
        """
        instance = self
        qs = ResearchExperimentUnit.objects.filter_by_instance(instance)
        return qs
