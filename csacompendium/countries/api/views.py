
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView
)
from csacompendium.countries.models import Country
from .serializers import (
    CountryCreateUpdateSerializer,
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


class CountryCreateAPIView(CreateAPIView):
    """
    Gets information on a single record.
    """
    queryset = Country.objects.all()
    serializer_class = CountryCreateUpdateSerializer


class CountryUpdateAPIView(UpdateAPIView):
    """
    Updates a record.
    """
    queryset = Country.objects.all()
    serializer_class = CountryCreateUpdateSerializer
    lookup_field = 'slug'


class CountryDeleteAPIView(DestroyAPIView):
    """
    Destroys/deletes a record.
    """
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializer
    lookup_field = 'slug'

