from csacompendium.research.models import MeasurementYear
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import (
    DetailViewUpdateDelete,
    get_http_request
)
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import MeasurementYearListFilter
from csacompendium.research.api.serializers import measurement_year_serializers


def measurement_year_views():
    """
    Measurement year views
    :return: All  measurement year views
    :rtype: Object
    """
    class MeasurementYearCreateAPIView(CreateAPIView):
        """
        Creates a single record.
        """
        queryset = MeasurementYear.objects.all()
        permission_classes = [IsAuthenticated]

        def get_serializer_class(self):
            """
            Gets serializer class
            :return: Measurement year object
            :rtype: Object
            """
            model_type, url_parameter, user = get_http_request(self.request, slug=False)
            create_measurement_year_serializer = measurement_year_serializers['create_measurement_year_serializer']
            return create_measurement_year_serializer(model_type, url_parameter, user)

    class MeasurementYearListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = MeasurementYear.objects.all()
        serializer_class = measurement_year_serializers['MeasurementYearListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = MeasurementYearListFilter
        pagination_class = APILimitOffsetPagination

    class MeasurementYearDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = MeasurementYear.objects.all()
        serializer_class = measurement_year_serializers['MeasurementYearDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

    return {
        'MeasurementYearCreateAPIView': MeasurementYearCreateAPIView,
        'MeasurementYearListAPIView': MeasurementYearListAPIView,
        'MeasurementYearDetailAPIView': MeasurementYearDetailAPIView
    }