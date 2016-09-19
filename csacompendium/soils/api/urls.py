from django.conf.urls import url
from .views import (
    soil_views,
)

# Location URLs
urlpatterns = [
    url(r'^$', soil_views['SoilListAPIView'].as_view(), name='soil_list'),
    # url(r'^create/$', location_views['LocationCreateAPIView'].as_view(), name='location_create'),
    url(r'^(?P<pk>[\w-]+)/$', soil_views['SoilDetailAPIView'].as_view(), name='soil_detail'),
]
