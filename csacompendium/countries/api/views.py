
from rest_framework.generics import ListAPIView, RetrieveAPIView
from csacompendium.countries.models import Country
from .serializers import (
    CountryDetailSerializer,
    CountryListSerializer
)


class CountryListAPIView(ListAPIView):
    """
    Country API list view. Gets all country records API.
    """
    queryset = Country.objects.all()
    serializer_class = CountryListSerializer


class CountryDetailAPIView(RetrieveAPIView):
    """
    Gets information on a single record.
    """
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializer
    lookup_field = 'slug'
