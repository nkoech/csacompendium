from csacompendium.research.models import MeasurementYear
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import MeasurementYearListFilter
from csacompendium.research.api.measurementyear.measurementyearserializers import measurement_year_serializers


def measurement_year_views():
    """
    Measurement year views
    :return: All nitrogen applied views
    :rtype: Object
    """
    measurement_year_serializer = measurement_year_serializers()

    class MeasurementYearCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = MeasurementYear.objects.all()
        serializer_class = measurement_year_serializer['MeasurementYearDetailSerializer']
        permission_classes = [IsAuthenticated]

    class MeasurementYearListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = MeasurementYear.objects.all()
        serializer_class = measurement_year_serializer['MeasurementYearListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = MeasurementYearListFilter
        pagination_class = APILimitOffsetPagination

    class MeasurementYearDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = MeasurementYear.objects.all()
        serializer_class = measurement_year_serializer['MeasurementYearDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'slug'

    return {
        'MeasurementYearListAPIView': MeasurementYearListAPIView,
        'MeasurementYearDetailAPIView': MeasurementYearDetailAPIView,
        'MeasurementYearCreateAPIView': MeasurementYearCreateAPIView
    }
