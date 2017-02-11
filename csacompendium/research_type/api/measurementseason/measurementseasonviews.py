from csacompendium.research_type.models import MeasurementSeason
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import MeasurementSeasonListFilter
from csacompendium.research.api.measurementseason.measurementseasonserializers import measurement_season_serializers


def measurement_season_views():
    """
    measurement season views
    :return: All measurement season views
    :rtype: Object
    """
    measurement_season_serializer = measurement_season_serializers()

    class MeasurementSeasonCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = MeasurementSeason.objects.all()
        serializer_class = measurement_season_serializer['MeasurementSeasonDetailSerializer']
        permission_classes = [IsAuthenticated]

    class MeasurementSeasonListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = MeasurementSeason.objects.all()
        serializer_class = measurement_season_serializer['MeasurementSeasonListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = MeasurementSeasonListFilter
        pagination_class = APILimitOffsetPagination

    class MeasurementSeasonDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = MeasurementSeason.objects.all()
        serializer_class = measurement_season_serializer['MeasurementSeasonDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'slug'

    return {
        'MeasurementSeasonListAPIView': MeasurementSeasonListAPIView,
        'MeasurementSeasonDetailAPIView': MeasurementSeasonDetailAPIView,
        'MeasurementSeasonCreateAPIView': MeasurementSeasonCreateAPIView
    }
