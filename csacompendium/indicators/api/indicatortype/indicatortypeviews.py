from csacompendium.indicators.models import IndicatorType
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import IndicatorTypeListFilter
from csacompendium.indicators.api.indicatortype.indicatortypeserializers import indicator_type_serializers


def indicator_type_views():
    """
    Indicator type views
    :return: All indicator type views
    :rtype: Object
    """
    indicator_type_serializer = indicator_type_serializers()

    class IndicatorTypeCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = IndicatorType.objects.all()
        serializer_class = indicator_type_serializer['IndicatorTypeDetailSerializer']
        permission_classes = [IsAuthenticated]

    class IndicatorTypeListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = IndicatorType.objects.all()
        serializer_class = indicator_type_serializer['IndicatorTypeListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = IndicatorTypeListFilter
        pagination_class = APILimitOffsetPagination

    class IndicatorTypeDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = IndicatorType.objects.all()
        serializer_class = indicator_type_serializer['IndicatorTypeDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'slug'

    return {
        'IndicatorTypeListAPIView': IndicatorTypeListAPIView,
        'IndicatorTypeDetailAPIView': IndicatorTypeDetailAPIView,
        'IndicatorTypeCreateAPIView': IndicatorTypeCreateAPIView
    }
