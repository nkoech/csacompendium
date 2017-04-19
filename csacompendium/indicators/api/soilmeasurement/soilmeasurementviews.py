from csacompendium.indicators.models import SoilMeasurement
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import SoilMeasurementListFilter
from csacompendium.indicators.api.soilmeasurement.soilmeasurementserializers import soil_measurement_serializers


def soil_measurement_views():
    """
    Soil measurement views
    :return: All soil measurement views
    :rtype: Object
    """
    soil_measurement_serializer = soil_measurement_serializers()

    class SoilMeasurementCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = SoilMeasurement.objects.all()
        serializer_class = soil_measurement_serializer['SoilMeasurementDetailSerializer']
        permission_classes = [IsAuthenticated]

    class SoilMeasurementListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = SoilMeasurement.objects.all()
        serializer_class = soil_measurement_serializer['SoilMeasurementListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = SoilMeasurementListFilter
        pagination_class = APILimitOffsetPagination

    class SoilMeasurementDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = SoilMeasurement.objects.all()
        serializer_class = soil_measurement_serializer['SoilMeasurementDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

    return {
        'SoilMeasurementListAPIView': SoilMeasurementListAPIView,
        'SoilMeasurementDetailAPIView': SoilMeasurementDetailAPIView,
        'SoilMeasurementCreateAPIView': SoilMeasurementCreateAPIView
    }
