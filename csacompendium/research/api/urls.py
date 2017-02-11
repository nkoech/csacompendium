from django.conf.urls import url
from .views import (
    measurement_season_views,
    measurement_year_views,
    author_views,
    object_category_views,
    experiment_object_views,
    research_object_views,
    species_views,
    research_species_views,
    research_outcome_indicator_views,
    # soil_views,
)

# Measurement Season URLs
urlpatterns = [
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
        r'^measurementyear/(?P<pk>[\w-]+)/$',
        measurement_year_views['MeasurementYearDetailAPIView'].as_view(),
        name='measurement_year_detail'
    ),
]

# Author URLs
urlpatterns += [
    url(r'^author/$', author_views['AuthorListAPIView'].as_view(), name='author_list'),
    url(r'^author/create/$', author_views['AuthorCreateAPIView'].as_view(), name='author_create'),
    url(r'^author/(?P<slug>[\w-]+)/$', author_views['AuthorDetailAPIView'].as_view(), name='author_detail'),
]

# Object category URLs
urlpatterns += [
    url(
        r'^objectcategory/$',
        object_category_views['ObjectCategoryListAPIView'].as_view(),
        name='object_category_list'
    ),
    url(
        r'^objectcategory/create/$',
        object_category_views['ObjectCategoryCreateAPIView'].as_view(),
        name='object_category_create'
    ),
    url(
        r'^objectcategory/(?P<slug>[\w-]+)/$',
        object_category_views['ObjectCategoryDetailAPIView'].as_view(),
        name='object_category_detail'
    ),
]

# Experiment object URLs
urlpatterns += [
    url(
        r'^experimentobject/$',
        experiment_object_views['ExperimentObjectListAPIView'].as_view(),
        name='experiment_object_list'
    ),
    url(
        r'^experimentobject/create/$',
        experiment_object_views['ExperimentObjectCreateAPIView'].as_view(),
        name='experiment_object_create'
    ),
    url(
        r'^experimentobject/(?P<slug>[\w-]+)/$',
        experiment_object_views['ExperimentObjectDetailAPIView'].as_view(),
        name='experiment_object_detail'
    ),
]

# Research object URLs
urlpatterns += [
    url(
        r'^researchobject/$',
        research_object_views['ResearchObjectListAPIView'].as_view(),
        name='research_object_list'
    ),
    url(
        r'^researchobject/create/$',
        research_object_views['ResearchObjectCreateAPIView'].as_view(),
        name='research_object_create'
    ),
    url(
        r'^researchobject/(?P<pk>[\w-]+)/$',
        research_object_views['ResearchObjectDetailAPIView'].as_view(),
        name='research_object_detail'
    ),
]

# Species object URLs
urlpatterns += [
    url(r'^species/$', species_views['SpeciesListAPIView'].as_view(), name='species_list'),
    url(r'^species/create/$', species_views['SpeciesCreateAPIView'].as_view(), name='species_create'),
    url(r'^species/(?P<slug>[\w-]+)/$', species_views['SpeciesDetailAPIView'].as_view(), name='species_detail'),
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

# Research outcome indicator URLs
urlpatterns += [
    url(
        r'^researchoutcomeindicator/$',
        research_outcome_indicator_views['ResearchOutcomeIndicatorListAPIView'].as_view(),
        name='research_outcome_indicator_list'
    ),
    url(
        r'^researchoutcomeindicator/create/$',
        research_outcome_indicator_views['ResearchOutcomeIndicatorCreateAPIView'].as_view(),
        name='research_outcome_indicator_create'
    ),
    url(
        r'^researchoutcomeindicator/(?P<pk>[\w-]+)/$',
        research_outcome_indicator_views['ResearchOutcomeIndicatorDetailAPIView'].as_view(),
        name='research_outcome_indicator_detail'
    ),
]
