from csacompendium.locations.models import Precipitation
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
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

    class PrecipitationDetailAPIView(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
        """
        Updates a record.
        """
        queryset = Precipitation.objects.all()
        serializer_class = precipitation_serializers['PrecipitationDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

        def put(self, request, *args, **kwargs):
            """
            Update record
            :param request: Client request
            :param args: List arguments
            :param kwargs: Keyworded arguments
            :return: Updated record
            :rtype: Object
            """
            return self.update(request, *args, **kwargs)

        def delete(self, request, *args, **kwargs):
            """
            Delete record
            :param request: Client request
            :param args: List arguments
            :param kwargs: Keyworded arguments
            :return: Updated record
            :rtype: Object
            """
            return self.destroy(request, *args, **kwargs)

        def perform_update(self, serializer):
            """
            Update a field
            :param serializer: Serializer object
            :return:
            """
            serializer.save(modified_by=self.request.user)

    return {
        'PrecipitationListAPIView': PrecipitationListAPIView,
        'PrecipitationDetailAPIView': PrecipitationDetailAPIView,
        'PrecipitationCreateAPIView': PrecipitationCreateAPIView
    }

