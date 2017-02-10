from csacompendium.indicators.models import OutcomeIndicator
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import OutcomeIndicatorListFilter
from csacompendium.indicators.api.outcomeindicator.outcomeindicatorserializers import outcome_indicator_serializers


def outcome_indicator_views():
    """
    Outcome indicator views
    :return: All outcome indicator views
    :rtype: Object
    """
    outcome_indicator_serializer = outcome_indicator_serializers()

    class OutcomeIndicatorCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = OutcomeIndicator.objects.all()
        serializer_class = outcome_indicator_serializer['OutcomeIndicatorDetailSerializer']
        permission_classes = [IsAuthenticated]

    class OutcomeIndicatorListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = OutcomeIndicator.objects.all()
        serializer_class = outcome_indicator_serializer['OutcomeIndicatorListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = OutcomeIndicatorListFilter
        pagination_class = APILimitOffsetPagination

    class OutcomeIndicatorDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = OutcomeIndicator.objects.all()
        serializer_class = outcome_indicator_serializer['OutcomeIndicatorDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'slug'

    return {
        'OutcomeIndicatorListAPIView': OutcomeIndicatorListAPIView,
        'OutcomeIndicatorDetailAPIView': OutcomeIndicatorDetailAPIView,
        'OutcomeIndicatorCreateAPIView': OutcomeIndicatorCreateAPIView
    }

