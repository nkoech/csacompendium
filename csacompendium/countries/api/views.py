
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.permissions import (
    IsAuthenticated,
)
from csacompendium.countries.models import Country
from .permissions import IsOwnerOrReadOnly
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
    Creates a single record.
    """
    queryset = Country.objects.all()
    serializer_class = CountryCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = 'slug'

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)


class CountryDeleteAPIView(RetrieveDestroyAPIView):
    """
    Destroys/deletes a record.
    """
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = 'slug'

