from  csacompendium.research.models import ExperimentUnit
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import ExperimentUnitListFilter
from csacompendium.research.api.experimentunit.experimentunitserializers import experiment_unit_serializers


def experiment_unit_views():
    """
    Experiment unit views
    :return: All experiment unit views
    :rtype: Object
    """
    experiment_unit_serializer = experiment_unit_serializers()

    class ExperimentUnitCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = ExperimentUnit.objects.all()
        serializer_class = experiment_unit_serializer['ExperimentUnitDetailSerializer']
        permission_classes = [IsAuthenticated]

    class ExperimentUnitListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = ExperimentUnit.objects.all()
        serializer_class = experiment_unit_serializer['ExperimentUnitListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = ExperimentUnitListFilter
        pagination_class = APILimitOffsetPagination

    class ExperimentUnitDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = ExperimentUnit.objects.all()
        serializer_class = experiment_unit_serializer['ExperimentUnitDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'slug'

    return {
        'ExperimentUnitListAPIView': ExperimentUnitListAPIView,
        'ExperimentUnitDetailAPIView': ExperimentUnitDetailAPIView,
        'ExperimentUnitCreateAPIView': ExperimentUnitCreateAPIView
    }

