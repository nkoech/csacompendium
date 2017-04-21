from csacompendium.research.models import MeasurementDuration
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import MeasurementDurationListFilter
from csacompendium.research.api.measurementduration.measurementdurationserializers import \
    measurement_duration_serializers


def measurement_duration_views():
    """
    Measurement duration views
    :return: All measurement duration views
    :rtype: Object
    """
    measurement_duration_serializer = measurement_duration_serializers()

    class MeasurementDurationCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = MeasurementDuration.objects.all()
        serializer_class = measurement_duration_serializer['MeasurementDurationDetailSerializer']
        permission_classes = [IsAuthenticated]

    class MeasurementDurationListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = MeasurementDuration.objects.all()
        serializer_class = measurement_duration_serializer['MeasurementDurationListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = MeasurementDurationListFilter
        pagination_class = APILimitOffsetPagination

    class MeasurementDurationDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = MeasurementDuration.objects.all()
        serializer_class = measurement_duration_serializer['MeasurementDurationDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

    return {
        'MeasurementDurationListAPIView': MeasurementDurationListAPIView,
        'MeasurementDurationDetailAPIView': MeasurementDurationDetailAPIView,
        'MeasurementDurationCreateAPIView': MeasurementDurationCreateAPIView
    }
