from csacompendium.locations.models import Temperature
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from rest_framework.filters import (
    DjangoFilterBackend,
)
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
# from .filters import TemperatureListFilter
from csacompendium.locations.api.serializers import (
    # TemperatureDetailSerializer,
    TemperatureListSerializer,
    # create_temperature_serializer,
)


def temperature_views():
    """
    Temperature views
    :return: All temperature views
    :rtype: Object
    """

    class TemperatureListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = Temperature.objects.all()
        serializer_class = TemperatureListSerializer
        # filter_backends = (DjangoFilterBackend,)
        # filter_class = LocationListFilter
        # pagination_class = APILimitOffsetPagination

    return TemperatureListAPIView
