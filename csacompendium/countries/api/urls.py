from django.conf.urls import url
from .views import (
    CountryDetailAPIView,
    CountryListAPIView
)

urlpatterns = [
    url(r'^$', CountryListAPIView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', CountryDetailAPIView.as_view(), name='detail'),
]
