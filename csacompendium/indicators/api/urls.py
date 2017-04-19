from django.conf.urls import url
from .views import (
    outcome_indicator_views,
    research_outcome_indicator_views,
    soil_measurement_views,
    indicator_type_views,
    indicator_views,
    subpillar_views,
)

# Indicator type URLs
urlpatterns = [
    url(
        r'^indicatortype/$',
        indicator_type_views['IndicatorTypeListAPIView'].as_view(),
        name='indicator_type_list'
    ),
    url(
        r'^indicatortype/create/$',
        indicator_type_views['IndicatorTypeCreateAPIView'].as_view(),
        name='indicator_type_create'
    ),
    url(
        r'^indicatortype/(?P<slug>[\w-]+)/$',
        indicator_type_views['IndicatorTypeDetailAPIView'].as_view(),
        name='indicator_type_detail'
    ),
]

# Subpillar URLs
urlpatterns += [
    url(
        r'^subpillar/$',
        subpillar_views['SubpillarListAPIView'].as_view(),
        name='subpillar_list'
    ),
    url(
        r'^subpillar/create/$',
        subpillar_views['SubpillarCreateAPIView'].as_view(),
        name='subpillar_create'
    ),
    url(
        r'^subpillar/(?P<slug>[\w-]+)/$',
        subpillar_views['SubpillarDetailAPIView'].as_view(),
        name='subpillar_detail'
    ),
]

# Indicator URLs
urlpatterns += [
    url(
        r'^indicator/$',
        indicator_views['IndicatorListAPIView'].as_view(),
        name='indicator_list'
    ),
    url(
        r'^indicator/create/$',
        indicator_views['IndicatorCreateAPIView'].as_view(),
        name='indicator_create'
    ),
    url(
        r'^indicator/(?P<slug>[\w-]+)/$',
        indicator_views['IndicatorDetailAPIView'].as_view(),
        name='indicator_detail'
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

# Soil measurement URLs
urlpatterns += [
    url(
        r'^soilmeasurement/$',
        soil_measurement_views['SoilMeasurementListAPIView'].as_view(),
        name='soil_measurement_list'
    ),
    url(
        r'^soilmeasurement/create/$',
        soil_measurement_views['SoilMeasurementCreateAPIView'].as_view(),
        name='soil_measurement_create'
    ),
    url(
        r'^soilmeasurement/(?P<pk>[\w-]+)/$',
        soil_measurement_views['SoilMeasurementDetailAPIView'].as_view(),
        name='soil_measurement_detail'
    ),
]

# Outcome indicator URLs
urlpatterns += [
    url(
        r'^$',
        outcome_indicator_views['OutcomeIndicatorListAPIView'].as_view(),
        name='outcome_indicator_list'
    ),
    url(
        r'^create/$',
        outcome_indicator_views['OutcomeIndicatorCreateAPIView'].as_view(),
        name='outcome_indicator_create'
    ),
    url(
        r'^(?P<slug>[\w-]+)/$',
        outcome_indicator_views['OutcomeIndicatorDetailAPIView'].as_view(),
        name='outcome_indicator_detail'
    ),
]
