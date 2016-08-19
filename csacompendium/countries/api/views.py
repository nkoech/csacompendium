__author__ = "Koech Nicholas"
__copyright__ = "Copyright 2016"
__email__ = "koechnicholas@gmail.com"
__status__ = "draft"

from rest_framework.generics import ListAPIView
from csacompendium.countries.models import Country


class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()

