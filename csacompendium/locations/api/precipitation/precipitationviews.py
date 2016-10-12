from csacompendium.locations.models import Precipitation
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
)
from .filters import PrecipitationListFilter

from csacompendium.locations.api.precipitation.precipitationserializers import precipitation_serializers
precipitation_serializers = precipitation_serializers()


def precipitation_views():
    """
    Precipitation views
    :return: All precipitation views
    :rtype: Object
    """

    class PrecipitationCreateAPIView(CreateAPIView):
        """
        Creates a single record.
        """
        queryset = Precipitation.objects.all()
        serializer_class = precipitation_serializers['PrecipitationDetailSerializer']
        permission_classes = [IsAuthenticated]

        def perform_create(self, serializer):
            """
            Creates a new value on the user field
            :param serializer: Serializer object
            :return: None
            :rtype: None
            """
            serializer.save(user=self.request.user)

    class PrecipitationListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = Precipitation.objects.all()
        serializer_class = precipitation_serializers['PrecipitationListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = PrecipitationListFilter
        pagination_class = APILimitOffsetPagination

    class PrecipitationDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = Precipitation.objects.all()
        serializer_class = precipitation_serializers['PrecipitationDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

    return {
        'PrecipitationListAPIView': PrecipitationListAPIView,
        'PrecipitationDetailAPIView': PrecipitationDetailAPIView,
        'PrecipitationCreateAPIView': PrecipitationCreateAPIView
    }

