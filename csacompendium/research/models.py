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


class ExperimentRep(AuthUserDetail, CreateUpdateTime):
    """
    Experiment replication model
    """
    no_replication = models.SmallIntegerField(default=0, verbose_name='Experiment Replication Number')

    def __unicode__(self):
        return str(self.no_replication)

    def __str__(self):
        return str(self.no_replication)

    def get_api_url(self):
        """
        Get experiment replication URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('research_api:experiment_rep_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Experiment Replications'

    @property
    def research_relation(self):
        """
        Get related research properties
        :return: Query result from the research model
        :rtype: object/record
        """
        instance = self
        qs = Research.objects.filter_by_model_type(instance)
        return qs


class NitrogenApplied(AuthUserDetail, CreateUpdateTime):
    """
    Nitrogen applied model
    """
    NITROGEN_SOURCE = (
        ('Organic', 'Organic'),
        ('Inorganic', 'Inorganic'),
    )

    nitrogen_amount = models.DecimalField(max_digits=6, decimal_places=2,  unique=True, default=Decimal('0.0'))
    amount_uom = models.CharField(max_length=12, verbose_name='Nitrogen UOM', default='kg/ha')
    nitrogen_source = models.CharField(max_length=30, blank=True, null=True, choices=NITROGEN_SOURCE)

    def __unicode__(self):
        return str(self.nitrogen_amount)

    def __str__(self):
        return str(self.nitrogen_amount)

    def get_api_url(self):
        """
        Get nitrogen applied URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('research_api:nitrogen_applied_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Nitrogen Applied'

    @property
    def research_relation(self):
        """
        Get related research properties
        :return: Query result from the research model
        :rtype: object/record
        """
        instance = self
        qs = Research.objects.filter_by_model_type(instance)
        return qs


class ExperimentDuration(AuthUserDetail, CreateUpdateTime):
    """
    Experiment duration model
    """
    exp_duration = models.DecimalField(
        max_digits=4, decimal_places=2, unique=True, default=Decimal('0.0'), verbose_name='Experiment Duration'
    )

    def __unicode__(self):
        return str(self.exp_duration)

    def __str__(self):
        return str(self.exp_duration)

    def get_api_url(self):
        """
        Get experiment duration URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('research_api:experiment_duration_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Experiment Durations'

    @property
    def research_relation(self):
        """
        Get related research properties
        :return: Query result from the research model
        :rtype: object/record
        """
        instance = self
        qs = Research.objects.filter_by_model_type(instance)
        return qs


class MeasurementSeason(AuthUserDetail, CreateUpdateTime):
    """
    Measurement season model
    """
    RAIN_SEASONS = (
        ('Long Rains', 'Long Rains'),
        ('Short Rains', 'Short Rains'),
    )

    slug = models.SlugField(unique=True, blank=True)
    meas_season = models.CharField(max_length=22, choices=RAIN_SEASONS, unique=True, verbose_name='Measurement season')

    def __unicode__(self):
        return self.meas_season

    def __str__(self):
        return self.meas_season

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
    def measurement_year_relation(self):
        """
        Get related measurement year properties
        :return: Query result from the measurement year model
        :rtye: object/record
        """
        instance = self
        qs = MeasurementYear.objects.filter_by_model_type(instance)
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
        instance.slug = create_slug(instance, MeasurementSeason, instance.meas_season)


class MeasurementYearManager(models.Manager):
    """
    Measurement year model manager
    """
    def filter_by_model_type(self, instance):
        """
        Query related objects/model type
        :param instance: Object instance
        :return: Matching object else none
        :rtype: Object/record
        """
        obj_qs = model_foreign_key_qs(instance, self, MeasurementYearManager)
        if obj_qs.exists():
            return model_type_filter(self, obj_qs, MeasurementYearManager)


class MeasurementYear(AuthUserDetail, CreateUpdateTime):
    """
    Creates measurement year entity.
    """
    slug = models.SlugField(unique=True, blank=True)
    meas_year = models.SmallIntegerField(
        choices=get_year_choices(), default=get_datetime_now(), verbose_name='Measurement year'
    )
    measurementseason = models.ForeignKey(
        MeasurementSeason, on_delete=models.PROTECT, verbose_name='Measurement season'
    )
    objects = MeasurementYearManager()

    def __unicode__(self):
        return str(self.meas_year)

    def __str__(self):
        return str(self.meas_year)

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
    def research_relation(self):
        """
        Get related research properties
        :return: Query result from the research model
        :rtype: object/record
        """
        instance = self
        qs = Research.objects.filter_by_model_type(instance)
        return qs


@receiver(pre_save, sender=MeasurementYear)
def pre_save_indicator_receiver(sender, instance, *args, **kwargs):
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
        instance.slug = create_slug(instance, MeasurementYear, instance.meas_year)


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
        return self.first_name

    def __str__(self):
        return self.first_name

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
        instance_fields = [instance.first_name, instance.last_name]
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
    journal = models.ForeignKey(Journal, on_delete=models.PROTECT, blank=True, null=True)
    objects = ResearchAuthorManager()

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Research Authors'


class BreedManager(models.Manager):
    """
    Breed model manager
    """
    def filter_by_instance(self, instance):
        """
        Query a related breed object/record from another model's object
        :param instance: Object instance
        :return: Query result from content type/model
        :rtye: object/record
        """
        return model_instance_filter(instance, self, BreedManager)

    def create_by_model_type(self, model_type, slug, **kwargs):
        """
        Create object by model type
        :param model_type: Content/model type
        :param slug: Slug
        :param kwargs: Fields to be created
        :return: Data object
        :rtype: Object
        """
        return create_model_type(self, model_type, slug, slugify=True, **kwargs)


class Breed(AuthUserDetail, CreateUpdateTime):
    """
    Breed model.  Creates Breed entity.
    """
    limit = models.Q(app_label='research', model='experimentunit')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    breed = models.CharField(max_length=200, unique=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    objects = BreedManager()

    def __unicode__(self):
        return str(self.breed)

    def __str__(self):
        return str(self.breed)

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Breeds'


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

    @property
    def breeds(self):
        """
        Get related breed object/record
        :return: Query result from the breed model
        :rtype: object/record
        """
        instance = self
        qs = Breed.objects.filter_by_instance(instance)
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
    upper_soil_depth = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True, default=Decimal('0.0')
    )
    lower_soil_depth = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True, default=Decimal('0.0')
    )
    incubation_days = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, null=True, verbose_name='Incubation Days', default=Decimal('0.0')
    )
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
    experimentrep = models.ForeignKey(
        ExperimentRep, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Experiment Replications'
    )
    experiment_description = models.TextField(blank=True, null=True)
    nitrogenapplied = models.ForeignKey(
        NitrogenApplied, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Nitrogen Applied'
    )
    experimentduration = models.ForeignKey(
        ExperimentDuration, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Experiment Duration'
    )
    measurementyear = models.ForeignKey(
        MeasurementYear, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Measurement Year'
    )
    mean_outcome = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True,
        default=Decimal('0.0'), verbose_name='Mean outcome'
    )
    std_outcome = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True,
        default=Decimal('0.0'),  verbose_name='Standard outcome'
    )
    outcome_uom = models.CharField(max_length=200, blank=True, null=True, default='kg/ha')
    objects = ResearchManager()

    def __unicode__(self):
        return str(self.experiment_description)

    def __str__(self):
        return str(self.experiment_description)

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
