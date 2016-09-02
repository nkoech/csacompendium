from django.conf.urls import url
from .views import (
    CountryCreateAPIView,
    CountryDetailAPIView,
    CountryListAPIView,
)

urlpatterns = [
    url(r'^$', CountryListAPIView.as_view(), name='list'),
    url(r'^create$', CountryCreateAPIView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', CountryDetailAPIView.as_view(), name='detail'),
]
