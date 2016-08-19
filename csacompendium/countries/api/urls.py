__author__ = "Koech Nicholas"
__copyright__ = "Copyright 2016"
__email__ = "koechnicholas@gmail.com"
__status__ = "draft"

from django.conf.urls import url
from django.contrib import admin

from.views import (
    CountryListAPIView
)

urlpatterns = [
    url(r'^$', CountryListAPIView.as_view(), name='list'),
]