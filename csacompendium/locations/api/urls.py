from django.conf.urls import url
from .views import (
    location_views,
    location_relation_views,
    temperature_views,
    precipitation_views,
)

# Location Relation URLs
urlpatterns = [
    url(
        r'^location_relation/$',
        location_relation_views['LocationRelationListAPIView'].as_view(),
        name='location_relation_list'
    ),
    url(
        r'^location_relation/create/$',
        location_relation_views['LocationRelationCreateAPIView'].as_view(),
        name='location_relation_create'
    ),
    url(
        r'^location_relation/(?P<pk>[\w-]+)/$',
        location_relation_views['LocationRelationDetailAPIView'].as_view(),
        name='locationrelation_detail'
    ),
]

# Precipitation URLs
urlpatterns += [
    url(
        r'^precipitation/$',
        precipitation_views['PrecipitationListAPIView'].as_view(),
        name='precipitation_list'
    ),
    url(
        r'^precipitation/create/$',
        precipitation_views['PrecipitationCreateAPIView'].as_view(),
        name='precipitation_create'
    ),
    url(
        r'^precipitation/(?P<pk>[\w-]+)/$',
        precipitation_views['PrecipitationDetailAPIView'].as_view(),
        name='precipitation_detail'
    ),
]

# Temperature URLs
urlpatterns += [
    url(
        r'^temperature/$',
        temperature_views['TemperatureListAPIView'].as_view(),
        name='temperature_list'
    ),
    url(
        r'^temperature/create/$',
        temperature_views['TemperatureCreateAPIView'].as_view(),
        name='temperature_create'
    ),
    url(
        r'^temperature/(?P<pk>[\w-]+)/$',
        temperature_views['TemperatureDetailAPIView'].as_view(),
        name='temperature_detail'
    ),
]

# Location URLs
urlpatterns += [
    url(r'^$', location_views['LocationListAPIView'].as_view(), name='location_list'),
    url(r'^create/$', location_views['LocationCreateAPIView'].as_view(), name='location_create'),
    url(r'^(?P<slug>[\w-]+)/$', location_views['LocationDetailAPIView'].as_view(), name='location_detail'),
]
