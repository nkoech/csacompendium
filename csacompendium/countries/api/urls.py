from django.conf.urls import url
from .views import (
    CountryListAPIView
)

urlpatterns = [
    url(r'^$', CountryListAPIView.as_view(), name='list'),
]
