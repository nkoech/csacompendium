from django.conf.urls import url
from .views import (
    CountryDeleteAPIView,
    CountryDetailAPIView,
    CountryListAPIView,
    CountryUpdateAPIView
)

urlpatterns = [
    url(r'^$', CountryListAPIView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', CountryDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', CountryUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', CountryDeleteAPIView.as_view(), name='delete'),
]
