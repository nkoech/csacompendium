from django.conf.urls import url
from .views import (
    subpillar_views,
    indicator_views,
    indicator_type_views,
)

# Subpillar URLs
urlpatterns = [
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

# Indicator type URLs
urlpatterns += [
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
