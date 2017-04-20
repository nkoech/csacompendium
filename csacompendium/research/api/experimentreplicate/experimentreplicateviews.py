from csacompendium.research.models import ExperimentReplicate
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import ExperimentReplicateListFilter
from csacompendium.research.api.experimentreplicate.experimentreplicateserializers import \
    experiment_replicate_serializers


def experiment_replicate_views():
    """
    Experiment replicate views
    :return: All experiment replicate views
    :rtype: Object
    """
    experiment_replicate_serializer = experiment_replicate_serializers()

    class ExperimentReplicateCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = ExperimentReplicate.objects.all()
        serializer_class = experiment_replicate_serializer['ExperimentReplicateDetailSerializer']
        permission_classes = [IsAuthenticated]

    class ExperimentReplicateListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = ExperimentReplicate.objects.all()
        serializer_class = experiment_replicate_serializer['ExperimentReplicateListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = ExperimentReplicateListFilter
        pagination_class = APILimitOffsetPagination

    class ExperimentReplicateDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = ExperimentReplicate.objects.all()
        serializer_class = experiment_replicate_serializer['ExperimentReplicateDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

    return {
        'ExperimentReplicateListAPIView': ExperimentReplicateListAPIView,
        'ExperimentReplicateDetailAPIView': ExperimentReplicateDetailAPIView,
        'ExperimentReplicateCreateAPIView': ExperimentReplicateCreateAPIView
    }

