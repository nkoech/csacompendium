# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from csacompendium.utils.abstractmodels import (
    AuthUserDetail,
    CreateUpdateTime,
)
from csacompendium.research_type.models import (
    ControlResearch,
    TreatmentResearch
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


# class Author(AuthUserDetail, CreateUpdateTime):
#     """
#     Research author model
#     """
#     slug = models.SlugField(unique=True, blank=True)
#     author_code = models.CharField(max_length=6, unique=True)
#     first_name = models.CharField(max_length=64)
#     middle_name = models.CharField(max_length=64, null=True, blank=True)
#     last_name = models.CharField(max_length=64)
#     author_bio = models.TextField(null=True, blank=True)
#
#     def __unicode__(self):
#         return self.first_name
#
#     def __str__(self):
#         return self.first_name
#
#     def get_api_url(self):
#         """
#         Get author URL as a reverse from model
#         :return: URL
#         :rtype: String
#         """
#         return reverse('research_api:author_detail', kwargs={'slug': self.slug})
#
#     class Meta:
#         ordering = ['-time_created', '-last_update']
#         verbose_name_plural = 'Authors'
#
#     @property
#     def research_relation(self):
#         """
#         Get related research properties
#         :return: Query result from the research model
#         :rtye: object/record
#         """
#         instance = self
#         qs = Research.objects.filter_by_model_type(instance)
#         return qs
#
#
# @receiver(pre_save, sender=Author)
# def pre_save_author_receiver(sender, instance, *args, **kwargs):
#     """
#     Create a slug before save.
#     :param sender: Signal sending object
#     :param instance: Object instance
#     :param args: Any other argument
#     :param kwargs: Keyword arguments
#     :return: None
#     :rtype: None
#     """
#     if not instance.slug:
#         instance_fields = [instance.first_name, instance.last_name]
#         instance.slug = create_slug(instance, Author, instance_fields)


class ResearchManager(models.Manager):
    """
    Research model manager
    """
    def filter_by_instance(self, instance):
        """
        Query a related research object/record from another model's object
        :param instance: Object instance
        :return: Query result from content type/model
        :rtye: object/record
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


class Research(AuthUserDetail, CreateUpdateTime):
    """
    Creates research entity.
    """
    limit = models.Q(app_label='locations', model='location')
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    research_year = models.SmallIntegerField(choices=get_year_choices(), default=get_datetime_now())
    # author = models.ForeignKey(Author, on_delete=models.PROTECT)
    research_type = models.CharField(max_length=120, blank=True, null=True)
    objects = ResearchManager()

    def __unicode__(self):
        return str(self.research_year)

    def __str__(self):
        return str(self.research_year)

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

    # @property
    # def measurement_year(self):
    #     """
    #     Get related measurement year object/record
    #     :return: Query result from the measurement year model
    #     :rtye: object/record
    #     """
    #     instance = self
    #     qs = MeasurementYear.objects.filter_by_instance(instance)
    #     return qs

    # @property
    # def research_species_relation(self):
    #     """
    #     Get related research species object/record
    #     :return: Query result from the research species model
    #     :rtye: object/record
    #     """
    #     instance = self
    #     qs = ResearchSpecies.objects.filter_by_model_type(instance)
    #     return qs


    @property
    def research_outcome_indicator_relation(self):
        """
        Get related research outcome object/record
        :return: Query result from the research outcome model
        :rtye: object/record
        """
        instance = self
        qs = ResearchOutcomeIndicator.objects.filter_by_model_type(instance)
        return qs

    @property
    def research_object(self):
        """
        Get related research object object/record
        :return: Query result from the research object model
        :rtype: object/record
        """
        instance = self
        qs = ResearchObject.objects.filter_by_instance(instance)
        return qs

    @property
    def control_research(self):
        """
        Get related control research object/record
        :return: Query result from the control research model
        :rtype: object/record
        """
        instance = self
        qs = ControlResearch.objects.filter_by_instance(instance)
        return qs


    @property
    def treatment_research(self):
        """
        Get related treatment research object/record
        :return: Query result from the treatment research model
        :rtype: object/record
        """
        instance = self
        qs = TreatmentResearch.objects.filter_by_instance(instance)
        return qs


# class MeasurementSeason(AuthUserDetail, CreateUpdateTime):
#     """
#     Measurement season model
#     """
#     RAIN_SEASONS = (
#         ('Long Rains', 'Long Rains'),
#         ('Short Rains', 'Short Rains'),
#     )
#
#     slug = models.SlugField(unique=True, blank=True)
#     meas_season = models.CharField(max_length=22, choices=RAIN_SEASONS, unique=True, verbose_name='Measurement season')
#
#     def __unicode__(self):
#         return self.meas_season
#
#     def __str__(self):
#         return self.meas_season
#
#     def get_api_url(self):
#         """
#         Get measurement season URL as a reverse from model
#         :return: URL
#         :rtype: String
#         """
#         return reverse('research_api:measurement_season_detail', kwargs={'slug': self.slug})
#
#     class Meta:
#         ordering = ['-time_created', '-last_update']
#         verbose_name_plural = 'Measurement Seasons'
#
#     @property
#     def measurement_year_relation(self):
#         """
#         Get related measurement year properties
#         :return: Query result from the measurement year model
#         :rtye: object/record
#         """
#         instance = self
#         qs = MeasurementYear.objects.filter_by_model_type(instance)
#         return qs
#
#
# @receiver(pre_save, sender=MeasurementSeason)
# def pre_save_measurement_season_receiver(sender, instance, *args, **kwargs):
#     """
#     Create a slug before save.
#     :param sender: Signal sending object
#     :param instance: Object instance
#     :param args: Any other argument
#     :param kwargs: Keyword arguments
#     :return: None
#     :rtype: None
#     """
#     if not instance.slug:
#         instance.slug = create_slug(instance, MeasurementSeason, instance.meas_season)
#
#
# class MeasurementYearManager(models.Manager):
#     """
#     Measurement year model manager
#     """
#     def filter_by_instance(self, instance):
#         """
#         Query a related measurement year object/record from another model's object
#         :param instance: Object instance
#         :return: Query result from content type/model
#         :rtye: object/record
#         """
#         return model_instance_filter(instance, self, MeasurementYearManager)
#
#     def filter_by_model_type(self, instance):
#         """
#         Query related objects/model type
#         :param instance: Object instance
#         :return: Matching object else none
#         :rtype: Object/record
#         """
#         obj_qs = model_foreign_key_qs(instance, self, MeasurementYearManager)
#         if obj_qs.exists():
#             return model_type_filter(self, obj_qs, MeasurementYearManager)
#
#     def create_by_model_type(self, model_type, pk, **kwargs):
#         """
#         Create object by model type
#         :param model_type: Content/model type
#         :param pk: Primary Key
#         :param kwargs: Fields to be created
#         :return: Data object
#         :rtype: Object
#         """
#         return create_model_type(self, model_type, pk, slugify=False, **kwargs)
#
#
# class MeasurementYear(AuthUserDetail, CreateUpdateTime):
#     """
#     Creates measurement year entity.
#     """
#
#     limit = models.Q(app_label='research', model='research')
#     content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, limit_choices_to=limit)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')
#     meas_year = models.SmallIntegerField(
#         choices=get_year_choices(), default=get_datetime_now(), verbose_name='Measurement Year'
#     )
#     measurementseason = models.ForeignKey(
#         MeasurementSeason, on_delete=models.PROTECT, verbose_name='Measurement season'
#     )
#     objects = MeasurementYearManager()
#
#     def __unicode__(self):
#         return str(self.meas_year)
#
#     def __str__(self):
#         return str(self.meas_year)
#
#     class Meta:
#         ordering = ['-time_created', '-last_update']
#         verbose_name_plural = 'Measurement Years'


# class Species(AuthUserDetail, CreateUpdateTime):
#     """
#     Species model
#     """
#     slug = models.SlugField(max_length=100, unique=True, blank=True)
#     species = models.CharField(max_length=200, unique=True)
#
#     def __unicode__(self):
#         return self.species
#
#     def __str__(self):
#         return self.species
#
#     def get_api_url(self):
#         """
#         Get species URL as a reverse from model
#         :return: URL
#         :rtype: String
#         """
#         return reverse('research_api:species_detail', kwargs={'slug': self.slug})
#
#     class Meta:
#         ordering = ['-time_created', '-last_update']
#         verbose_name_plural = 'Species'
#
#     @property
#     def research_species(self):
#         """
#         Get related research species object/record
#         :return: Query result from the research species model
#         :rtype: object/record
#         """
#         instance = self
#         qs = ResearchSpecies.objects.filter_by_instance(instance)
#         return qs
#
#
# @receiver(pre_save, sender=Species)
# def pre_save_species_receiver(sender, instance, *args, **kwargs):
#     """
#     Create a slug before save.
#     :param sender: Signal sending object
#     :param instance: Object instance
#     :param args: Any other argument
#     :param kwargs: Keyword arguments
#     :return: None
#     :rtype: None
#     """
#     if not instance.slug:
#         instance.slug = create_slug(instance, Species, instance.species)


# class ResearchSpeciesManager(models.Manager):
#     """
#     Research species model manager
#     """
#     def filter_by_instance(self, instance):
#         """
#         Query a related research species object/record from another model's object
#         :param instance: Object instance
#         :return: Query result from content type/model
#         :rtye: object/record
#         """
#         return model_instance_filter(instance, self, ResearchSpeciesManager)
#
#     def filter_by_model_type(self, instance):
#         """
#         Query related objects/model type
#         :param instance: Object instance
#         :return: Matching object else none
#         :rtype: Object/record
#         """
#         obj_qs = model_foreign_key_qs(instance, self, ResearchSpeciesManager)
#         if obj_qs.exists():
#             return model_type_filter(self, obj_qs, ResearchSpeciesManager)
#
#     def create_by_model_type(self, model_type, slug, **kwargs):
#         """
#         Create object by model type
#         :param model_type: Content/model type
#         :param slug: Slug
#         :param kwargs: Fields to be created
#         :return: Data object
#         :rtype: Object
#         """
#         return create_model_type(self, model_type, slug, slugify=True, **kwargs)


# class ResearchSpecies(AuthUserDetail, CreateUpdateTime):
#     """
#     Research species entry relationship model. A many to many bridge table between research and other models
#     """
#     limit = models.Q(app_label='research', model='species')
#     research = models.ForeignKey(Research, on_delete=models.PROTECT)
#     content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, limit_choices_to=limit)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')
#     objects = ResearchSpeciesManager()
#
#     class Meta:
#         ordering = ['-time_created', '-last_update']
#         verbose_name_plural = 'Research Species'


class ResearchOutcomeIndicatorManager(models.Manager):
    """
    Research outcome model manager
    """
    def filter_by_instance(self, instance):
        """
        Query a related research outcome object/record from another model's object
        :param instance: Object instance
        :return: Query result from content type/model
        :rtye: object/record
        """
        return model_instance_filter(instance, self, ResearchOutcomeIndicatorManager)

    def filter_by_model_type(self, instance):
        """
        Query related objects/model type
        :param instance: Object instance
        :return: Matching object else none
        :rtype: Object/record
        """
        obj_qs = model_foreign_key_qs(instance, self, ResearchOutcomeIndicatorManager)
        if obj_qs.exists():
            return model_type_filter(self, obj_qs, ResearchOutcomeIndicatorManager)

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


class ResearchOutcomeIndicator(AuthUserDetail, CreateUpdateTime):
    """
    Research outcome entry relationship model. A many to many bridge table between research and other models
    """
    # limit = models.Q(app_label='indicators', model='outcomeindicator')
    research = models.ForeignKey(Research, on_delete=models.PROTECT)
    # content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, limit_choices_to=limit)
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    objects = ResearchOutcomeIndicatorManager()

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Research Outcome Indicators'


class ObjectCategory(AuthUserDetail, CreateUpdateTime):
    """
    Experiment object model. Creates experiment object entity.
    """
    slug = models.SlugField(unique=True, blank=True)
    object_category = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.object_category

    def __str__(self):
        return self.object_category

    def get_api_url(self):
        """
        Get object category URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('research_api:object_category_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Object Categories'

    @property
    def experiment_object_relation(self):
        """
        Get related experiment object properties
        :return: Query result from the experiment object model
        :rtype: object/record
        """
        instance = self
        qs = ExperimentObject.objects.filter_by_model_type(instance)
        return qs


@receiver(pre_save, sender=ObjectCategory)
def pre_save_object_category_receiver(sender, instance, *args, **kwargs):
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
        instance.slug = create_slug(instance, ObjectCategory, instance.object_category)


class ExperimentObjectManager(models.Manager):
    """
    Experiment object model manager
    """
    def filter_by_model_type(self, instance):
        """
        Query related objects/model type
        :param instance: Object instance
        :return: Matching object else none
        :rtype: Object/record
        """
        obj_qs = model_foreign_key_qs(instance, self, ExperimentObjectManager)
        if obj_qs.exists():
            return model_type_filter(self, obj_qs, ExperimentObjectManager)


class ExperimentObject(AuthUserDetail, CreateUpdateTime):
    """
    Experiment object model. Creates experiment object entity.
    """
    slug = models.SlugField(unique=True, blank=True)
    exp_object_code = models.CharField(max_length=20, unique=True, verbose_name='Experiment Object Code')
    objectcategory = models.ForeignKey(ObjectCategory, on_delete=models.PROTECT, verbose_name='Object Category')
    object_name = models.CharField(max_length=250)
    latin_name = models.CharField(max_length=250, blank=True, null=True)
    objects = ExperimentObjectManager()

    def __unicode__(self):
        return self.object_name

    def __str__(self):
        return self.object_name

    def get_api_url(self):
        """
        Get experiment object URL as a reverse from model
        :return: URL
        :rtype: String
        """
        return reverse('research_api:experiment_object_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-time_created', '-last_update']

    @property
    def research_object_relation(self):
        """
        Get related research object properties
        :return: Query result from the research object model
        :rtype: object/record
        """
        instance = self
        qs = ResearchObject.objects.filter_by_model_type(instance)
        return qs


@receiver(pre_save, sender=ExperimentObject)
def pre_save_experiment_object_receiver(sender, instance, *args, **kwargs):
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
        instance.slug = create_slug(instance, ExperimentObject, instance.object_name)


class ResearchObjectManager(models.Manager):
    """
    Research object model manager
    """
    def filter_by_instance(self, instance):
        """
        Query a related research object object/record from another model's object
        :param instance: Object instance
        :return: Query result from content type/model
        :rtype: object/record
        """
        return model_instance_filter(instance, self, ResearchObjectManager)

    def filter_by_model_type(self, instance):
        """
        Query related objects/model type
        :param instance: Object instance
        :return: Matching object else none
        :rtype: Object/record
        """
        obj_qs = model_foreign_key_qs(instance, self, ResearchObjectManager)
        if obj_qs.exists():
            return model_type_filter(self, obj_qs, ResearchObjectManager)

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


class ResearchObject(AuthUserDetail, CreateUpdateTime):
    """
    Research object model.  Creates research object entity.
    """
    limit = models.Q(app_label='research', model='research')
    experimentobject = models.ForeignKey(ExperimentObject, on_delete=models.PROTECT, verbose_name='Experiment Object')
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    upper_soil_depth = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    lower_soil_depth = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    objects = ResearchObjectManager()

    def __unicode__(self):
        return str(self.upper_soil_depth)

    def __str__(self):
        return str(self.upper_soil_depth)

    class Meta:
        ordering = ['-time_created', '-last_update']

