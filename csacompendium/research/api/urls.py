from django.conf.urls import url
from .views import (
    measurement_season_views,
    measurement_year_views,
    experiment_duration_views,
    author_views,
    object_category_views,
    experiment_object_views,
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

# Experiment Duration URLs
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