from csacompendium.locations.models import Temperature
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
)
from .filters import TemperatureListFilter

from csacompendium.locations.api.temperature.temperatureserializers import temperature_serializers
temperature_serializers = temperature_serializers()


def temperature_views():
    """
    Temperature views
    :return: All temperature views
    :rtype: Object
    """

    class TemperatureCreateAPIView(CreateAPIView):
        """
        Creates a single record.
        """
        queryset = Temperature.objects.all()
        serializer_class = temperature_serializers['TemperatureDetailSerializer']
        permission_classes = [IsAuthenticated]

        def perform_create(self, serializer):
            """
            Creates a new value on the user field
            :param serializer: Serializer object
            :return: None
            :rtype: None
            """
            serializer.save(user=self.request.user)

    class TemperatureListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = Temperature.objects.all()
        serializer_class = temperature_serializers['TemperatureListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = TemperatureListFilter
        pagination_class = APILimitOffsetPagination

    class TemperatureDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = Temperature.objects.all()
        serializer_class = temperature_serializers['TemperatureDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

    return {
        'TemperatureListAPIView': TemperatureListAPIView,
        'TemperatureDetailAPIView': TemperatureDetailAPIView,
        'TemperatureCreateAPIView': TemperatureCreateAPIView
    }

