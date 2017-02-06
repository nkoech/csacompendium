from csacompendium.indicators.models import Indicator
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import IndicatorListFilter
from csacompendium.indicators.api.indicator.indicatorserializers import indicator_serializers


def indicator_views():
    """
    Indicator views
    :return: All indicator views
    :rtype: Object
    """
    indicator_serializer = indicator_serializers()

    class IndicatorCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = Indicator.objects.all()
        serializer_class = indicator_serializer['IndicatorDetailSerializer']
        permission_classes = [IsAuthenticated]

    class IndicatorListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = Indicator.objects.all()
        serializer_class = indicator_serializer['IndicatorListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = IndicatorListFilter
        pagination_class = APILimitOffsetPagination

    class IndicatorDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = Indicator.objects.all()
        serializer_class = indicator_serializer['IndicatorDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'slug'

    return {
        'IndicatorListAPIView': IndicatorListAPIView,
        'IndicatorDetailAPIView': IndicatorDetailAPIView,
        'IndicatorCreateAPIView': IndicatorCreateAPIView
    }
