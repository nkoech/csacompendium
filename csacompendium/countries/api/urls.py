from django.conf.urls import url
from .views import (
    CountryCreateAPIView,
    CountryDeleteAPIView,
    CountryDetailAPIView,
    CountryListAPIView,
    CountryUpdateAPIView
)

urlpatterns = [
    url(r'^$', CountryListAPIView.as_view(), name='list'),
    url(r'^create$', CountryCreateAPIView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', CountryDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', CountryUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', CountryDeleteAPIView.as_view(), name='delete'),
]
