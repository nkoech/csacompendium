from django.conf.urls import url
from .views import (
    experiment_duration_views,
    measurement_season_views,
    measurement_year_views,
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
