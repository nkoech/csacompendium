from csacompendium.countries.models import Country
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import CountryListFilter
from .serializers import CountryDetailSerializer, CountryListSerializer


class CountryCreateAPIView(CreateAPIView):
    """
    Creates a single record.
    """
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Creates a new value on the user field
        :param serializer: Serializer object
        :return: None
        :rtype: None
        """
        serializer.save(user=self.request.user)


class CountryListAPIView(ListAPIView):
    """
    API list view. Gets all records API.
    """
    queryset = Country.objects.all()
    serializer_class = CountryListSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = CountryListFilter
    pagination_class = APILimitOffsetPagination


class CountryDetailAPIView(DetailViewUpdateDelete):
    """
    Updates a record.
    """
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    lookup_field = 'slug'

