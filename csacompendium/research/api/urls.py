from django.conf.urls import url
from .views import (
    experiment_rep_views,
    nitrogen_applied_views,
    experiment_details_views,
    experiment_duration_views,
    measurement_season_views,
    measurement_year_views,
    research_author_views,
    author_views,
    research_species_views,
    species_views,
    experiment_unit_views,
    research_experiment_unit_views,
    experiment_unit_category_views,
    control_research_views,
)

# Experiment replication URLs
urlpatterns = [
    url(
        r'^experimentreplication/$',
        experiment_rep_views['ExperimentRepListAPIView'].as_view(),
        name='experiment_rep_list'
    ),
    url(
        r'^experimentreplication/create/$',
        experiment_rep_views['ExperimentRepCreateAPIView'].as_view(),
        name='experiment_rep_create'
    ),
    url(
        r'^experimentreplication/(?P<pk>[\w-]+)/$',
        experiment_rep_views['ExperimentRepDetailAPIView'].as_view(),
        name='experiment_rep_detail'
    ),
]

# Nitrogen Applied URLs
urlpatterns += [
    url(
        r'^nitrogenapplied/$',
        nitrogen_applied_views['NitrogenAppliedListAPIView'].as_view(),
        name='nitrogen_applied_list'
    ),
    url(
        r'^nitrogenapplied/create/$',
        nitrogen_applied_views['NitrogenAppliedCreateAPIView'].as_view(),
        name='nitrogen_applied_create'
    ),
    url(
        r'^nitrogenapplied/(?P<pk>[\w-]+)/$',
        nitrogen_applied_views['NitrogenAppliedDetailAPIView'].as_view(),
        name='nitrogen_applied_detail'
    ),
]

# Experiment details URLs
urlpatterns += [
    url(
        r'^experimentdetails/$',
        experiment_details_views['ExperimentDetailsListAPIView'].as_view(),
        name='experiment_details_list'
    ),
    url(
        r'^experimentdetails/create/$',
        experiment_details_views['ExperimentDetailsCreateAPIView'].as_view(),
        name='experiment_details_create'
    ),
    url(
        r'^experimentdetails/(?P<slug>[\w-]+)/$',
        experiment_details_views['ExperimentDetailsDetailAPIView'].as_view(),
        name='experiment_details_detail'
    ),
]

# Experiment duration URLs
urlpatterns += [
    url(
        r'^experimentduration/$',
        experiment_duration_views['ExperimentDurationListAPIView'].as_view(),
        name='experiment_duration_list'
    ),
    url(
        r'^experimentduration/create/$',
        experiment_duration_views['ExperimentDurationCreateAPIView'].as_view(),
        name='experiment_duration_create'
    ),
    url(
        r'^experimentduration/(?P<pk>[\w-]+)/$',
        experiment_duration_views['ExperimentDurationDetailAPIView'].as_view(),
        name='experiment_duration_detail'
    ),
]

# Measurement Season URLs
urlpatterns += [
    url(
        r'^measurementseason/$',
        measurement_season_views['MeasurementSeasonListAPIView'].as_view(),
        name='measurement_season_list'
    ),
    url(
        r'^measurementseason/create/$',
        measurement_season_views['MeasurementSeasonCreateAPIView'].as_view(),
        name='measurement_season_create'
    ),
    url(
        r'^measurementseason/(?P<slug>[\w-]+)/$',
        measurement_season_views['MeasurementSeasonDetailAPIView'].as_view(),
        name='measurement_season_detail'
    ),
]

# Measurement Year URLs
urlpatterns += [
    url(
        r'^measurementyear/$',
        measurement_year_views['MeasurementYearListAPIView'].as_view(),
        name='measurement_year_list'
    ),
    url(
        r'^measurementyear/create/$',
        measurement_year_views['MeasurementYearCreateAPIView'].as_view(),
        name='measurement_year_create'
    ),
    url(
        r'^measurementyear/(?P<slug>[\w-]+)/$',
        measurement_year_views['MeasurementYearDetailAPIView'].as_view(),
        name='measurement_year_detail'
    ),
]

# Research author URLs
urlpatterns += [
    url(
        r'^researchauthor/$',
        research_author_views['ResearchAuthorListAPIView'].as_view(),
        name='research_author_list'
    ),
    url(
        r'^researchauthor/create/$',
        research_author_views['ResearchAuthorCreateAPIView'].as_view(),
        name='research_author_create'
    ),
    url(
        r'^researchauthor/(?P<pk>[\w-]+)/$',
        research_author_views['ResearchAuthorDetailAPIView'].as_view(),
        name='research_author_detail'
    ),
]

# Author URLs
urlpatterns += [
    url(
        r'^author/$',
        author_views['AuthorListAPIView'].as_view(),
        name='author_list'
    ),
    url(
        r'^author/create/$',
        author_views['AuthorCreateAPIView'].as_view(),
        name='author_create'
    ),
    url(
        r'^author/(?P<slug>[\w-]+)/$',
        author_views['AuthorDetailAPIView'].as_view(),
        name='author_detail'
    ),
]

# Research species URLs
urlpatterns += [
    url(
        r'^researchspecies/$',
        research_species_views['ResearchSpeciesListAPIView'].as_view(),
        name='research_species_list'
    ),
    url(
        r'^researchspecies/create/$',
        research_species_views['ResearchSpeciesCreateAPIView'].as_view(),
        name='research_species_create'
    ),
    url(
        r'^researchspecies/(?P<pk>[\w-]+)/$',
        research_species_views['ResearchSpeciesDetailAPIView'].as_view(),
        name='research_species_detail'
    ),
]

# Species URLs
urlpatterns += [
    url(
        r'^species/$',
        species_views['SpeciesListAPIView'].as_view(),
        name='species_list'
    ),
    url(
        r'^species/create/$',
        species_views['SpeciesCreateAPIView'].as_view(),
        name='species_create'
    ),
    url(
        r'^species/(?P<slug>[\w-]+)/$',
        species_views['SpeciesDetailAPIView'].as_view(),
        name='species_detail'
    ),
]

# Experiment unit category URLs
urlpatterns += [
    url(
        r'^experimentunitcategory/$',
        experiment_unit_category_views['ExperimentUnitCategoryListAPIView'].as_view(),
        name='experiment_unit_category_list'
    ),
    url(
        r'^experimentunitcategory/create/$',
        experiment_unit_category_views['ExperimentUnitCategoryCreateAPIView'].as_view(),
        name='experiment_unit_category_create'
    ),
    url(
        r'^experimentunitcategory/(?P<slug>[\w-]+)/$',
        experiment_unit_category_views['ExperimentUnitCategoryDetailAPIView'].as_view(),
        name='experiment_unit_category_detail'
    ),
]

# Research experiment unit  URLs
urlpatterns += [
    url(
        r'^researchexperimentunit/$',
        research_experiment_unit_views['ResearchExperimentUnitListAPIView'].as_view(),
        name='research_experiment_unit_list'
    ),
    url(
        r'^researchexperimentunit/create/$',
        research_experiment_unit_views['ResearchExperimentUnitCreateAPIView'].as_view(),
        name='research_experiment_unit_create'
    ),
    url(
        r'^researchexperimentunit/(?P<pk>[\w-]+)/$',
        research_experiment_unit_views['ResearchExperimentUnitDetailAPIView'].as_view(),
        name='research_experiment_unit_detail'
    ),
]

# Experiment unit  URLs
urlpatterns += [
    url(
        r'^experimentunit/$',
        experiment_unit_views['ExperimentUnitListAPIView'].as_view(),
        name='experiment_unit_list'
    ),
    url(
        r'^experimentunit/create/$',
        experiment_unit_views['ExperimentUnitCreateAPIView'].as_view(),
        name='experiment_unit_create'
    ),
    url(
        r'^experimentunit/(?P<slug>[\w-]+)/$',
        experiment_unit_views['ExperimentUnitDetailAPIView'].as_view(),
        name='experiment_unit_detail'
    ),
]

# Control research URLs
urlpatterns += [
    url(
        r'^controlresearch/$',
        control_research_views['ControlResearchListAPIView'].as_view(),
        name='control_research_list'
    ),
    url(
        r'^controlresearch/create/$',
        control_research_views['ControlResearchCreateAPIView'].as_view(),
        name='control_research_create'
    ),
    url(
        r'controlresearch/(?P<pk>[\w-]+)/$',
        control_research_views['ControlResearchDetailAPIView'].as_view(),
        name='control_research_detail'
    ),
]