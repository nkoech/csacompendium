from django.conf.urls import url
from .views import (
    soil_texture_views,
    soil_type_views,
    soil_views,
)

# Soil Texture URLs
urlpatterns = [
    url(r'^soiltexture/$', soil_texture_views['SoilTextureListAPIView'].as_view(), name='soil_texture_list'),
    url(r'^soiltexture/create/$', soil_texture_views['SoilTextureCreateAPIView'].as_view(), name='soil_texture_create'),
    url(r'^soiltexture/(?P<slug>[\w-]+)/$', soil_texture_views['SoilTextureDetailAPIView'].as_view(), name='soil_texture_detail'),
]

# Soil Type URLs
urlpatterns += [
    url(r'^soiltype/$', soil_type_views['SoilTypeListAPIView'].as_view(), name='soil_type_list'),
    url(r'^soiltype/create/$', soil_type_views['SoilTypeCreateAPIView'].as_view(), name='soil_type_create'),
    url(r'^soiltype/(?P<slug>[\w-]+)/$', soil_type_views['SoilTypeDetailAPIView'].as_view(), name='soil_type_detail'),
]

# Soil URLs
urlpatterns += [
    url(r'^$', soil_views['SoilListAPIView'].as_view(), name='soil_list'),
    # url(r'^create/$', location_views['LocationCreateAPIView'].as_view(), name='location_create'),
    url(r'^(?P<pk>[\w-]+)/$', soil_views['SoilDetailAPIView'].as_view(), name='soil_detail'),
]


