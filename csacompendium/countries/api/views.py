from django.db.models import Q
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)
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
    serializer_class = CountryListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['country_code', 'country_name']

    def get_queryset(self, *args, **kwargs):
        """
        Overwritten method that handles client query.
        :return: Query results
        :rtype: List
        """
        queryset_list = Country.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(country_code__icontains=query) |
                Q(country_name__icontains=query)
            ).distinct()
        return queryset_list


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

