from csacompendium.research.models import MeasurementSeason
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
from .filters import MeasurementSeasonListFilter
from csacompendium.research.api.measurementseason.measurementseasonserializers import measurement_season_serializers
measurement_season_serializers = measurement_season_serializers()


def measurement_season_views():
    """
    measurement season views
    :return: All measurement season views
    :rtype: Object
    """

    class MeasurementSeasonCreateAPIView(CreateAPIView):
        """
        Creates a single record.
        """
        queryset = MeasurementSeason.objects.all()
        serializer_class = measurement_season_serializers['MeasurementSeasonDetailSerializer']
        permission_classes = [IsAuthenticated]

        def perform_create(self, serializer):
            """
            Creates a new value on the user field
            :param serializer: Serializer object
            :return: None
            :rtype: None
            """
            serializer.save(user=self.request.user)

    class MeasurementSeasonListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = MeasurementSeason.objects.all()
        serializer_class = measurement_season_serializers['MeasurementSeasonListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = MeasurementSeasonListFilter
        pagination_class = APILimitOffsetPagination

    class MeasurementSeasonDetailAPIView(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
        """
        Updates a record.
        """
        queryset = MeasurementSeason.objects.all()
        serializer_class = measurement_season_serializers['MeasurementSeasonDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'slug'

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
        'MeasurementSeasonListAPIView': MeasurementSeasonListAPIView,
        'MeasurementSeasonDetailAPIView': MeasurementSeasonDetailAPIView,
        'MeasurementSeasonCreateAPIView': MeasurementSeasonCreateAPIView
    }
