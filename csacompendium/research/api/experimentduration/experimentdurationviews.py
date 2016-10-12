from csacompendium.research.models import ExperimentDuration
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import ExperimentDurationListFilter
from csacompendium.research.api.experimentduration.experimentdurationserializers import experiment_duration_serializers


def experiment_duration_views():
    """
    experiment duration views
    :return: All experiment duration views
    :rtype: Object
    """
    experiment_duration_serializer = experiment_duration_serializers()
    
    class ExperimentDurationCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = ExperimentDuration.objects.all()
        serializer_class = experiment_duration_serializer['ExperimentDurationDetailSerializer']
        permission_classes = [IsAuthenticated]

    class ExperimentDurationListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = ExperimentDuration.objects.all()
        serializer_class = experiment_duration_serializer['ExperimentDurationListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = ExperimentDurationListFilter
        pagination_class = APILimitOffsetPagination

    class ExperimentDurationDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = ExperimentDuration.objects.all()
        serializer_class = experiment_duration_serializer['ExperimentDurationDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

    return {
        'ExperimentDurationListAPIView': ExperimentDurationListAPIView,
        'ExperimentDurationDetailAPIView': ExperimentDurationDetailAPIView,
        'ExperimentDurationCreateAPIView': ExperimentDurationCreateAPIView
    }
