
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView
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

    def perform_create(self, serializer):
        """
        Updates the user field
        :param serializer: Serializer object
        :return: None
        :rtype: None
        """
        serializer.save(user=self.request.user)


class CountryUpdateAPIView(RetrieveUpdateAPIView):
    """
    Updates a record.
    """
    queryset = Country.objects.all()
    serializer_class = CountryCreateUpdateSerializer
    lookup_field = 'slug'

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class CountryDeleteAPIView(RetrieveDestroyAPIView):
    """
    Destroys/deletes a record.
    """
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializer
    lookup_field = 'slug'

