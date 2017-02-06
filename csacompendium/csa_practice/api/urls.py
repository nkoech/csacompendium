from django.conf.urls import url
from .views import (
    csa_theme_views,
    practice_level_views,
    practice_type_views,
    csa_practice_views,
)

# CSA theme URLs
urlpatterns = [
    url(
        r'^csatheme/$',
        csa_theme_views['CsaThemeListAPIView'].as_view(),
        name='csa_theme_list'
    ),
    url(
        r'^csatheme/create/$',
        csa_theme_views['CsaThemeCreateAPIView'].as_view(),
        name='csa_theme_create'
    ),
    url(
        r'^csatheme/(?P<slug>[\w-]+)/$',
        csa_theme_views['CsaThemeDetailAPIView'].as_view(),
        name='csa_theme_detail'
    ),
]

# Practice level URLs
urlpatterns += [
    url(
        r'^practicelevel/$',
        practice_level_views['PracticeLevelListAPIView'].as_view(),
        name='practice_level_list'
    ),
    url(
        r'^practicelevel/create/$',
        practice_level_views['PracticeLevelCreateAPIView'].as_view(),
        name='practice_level_create'
    ),
    url(
        r'^practicelevel/(?P<slug>[\w-]+)/$',
        practice_level_views['PracticeLevelDetailAPIView'].as_view(),
        name='practice_level_detail'
    ),
]

# Practice type URLs
urlpatterns += [
    url(
        r'^practicetype/$',
        practice_type_views['PracticeTypeListAPIView'].as_view(),
        name='practice_type_list'
    ),
    url(
        r'practicetype/create/$',
        practice_type_views['PracticeTypeCreateAPIView'].as_view(),
        name='practice_type_create'
    ),
    url(
        r'^practicetype/(?P<slug>[\w-]+)/$',
        practice_type_views['PracticeTypeDetailAPIView'].as_view(),
        name='practice_type_detail'
    ),
]

# CSA practice URLs
urlpatterns += [
    url(
        r'^$',
        csa_practice_views['CsaPracticeListAPIView'].as_view(),
        name='csa_practice_list'
    ),
    url(
        r'^create/$',
        csa_practice_views['CsaPracticeCreateAPIView'].as_view(),
        name='csa_practice_create'
    ),
    url(
        r'^(?P<slug>[\w-]+)/$',
        csa_practice_views['CsaPracticeDetailAPIView'].as_view(),
        name='csa_practice_detail'
    ),
]

