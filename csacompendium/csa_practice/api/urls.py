from django.conf.urls import url
from .views import (
    csa_theme_views,
)

# CSA theme URLs
urlpatterns = [
    url(r'^csatheme/$', csa_theme_views['CsaThemeListAPIView'].as_view(), name='csa_theme_list'),
    url(r'^csatheme/create/$', csa_theme_views['CsaThemeCreateAPIView'].as_view(), name='csa_theme_create'),
    url(r'^csatheme/(?P<slug>[\w-]+)/$', csa_theme_views['CsaThemeDetailAPIView'].as_view(), name='csa_theme_detail'),
]

# # Practice level URLs
# urlpatterns = [
#     url(r'^csatheme/$', csa_theme_views['CsaThemeListAPIView'].as_view(), name='csa_theme_list'),
#     url(r'^csatheme/create/$', csa_theme_views['CsaThemeCreateAPIView'].as_view(), name='csa_theme_create'),
#     url(r'^csatheme/(?P<slug>[\w-]+)/$', csa_theme_views['CsaThemeDetailAPIView'].as_view(), name='csa_theme_detail'),
# ]