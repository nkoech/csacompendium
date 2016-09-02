from django.conf.urls import url
from .views import (
    LocationCreateAPIView,
    LocationDetailAPIView,
    LocationListAPIView,
)

urlpatterns = [
    url(r'^$', LocationListAPIView.as_view(), name='list'),
    url(r'^create/$', LocationCreateAPIView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', LocationDetailAPIView.as_view(), name='detail'),
]
