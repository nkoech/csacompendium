from csacompendium.research.models import ExperimentRep
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import ExperimentRepListFilter
from csacompendium.research.api.experimentrep.experimentrepserializers import experiment_rep_serializers


def experiment_rep_views():
    """
    Experiment replication views
    :return: All experiment replication views
    :rtype: Object
    """
    experiment_rep_serializer = experiment_rep_serializers()

    class ExperimentRepCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = ExperimentRep.objects.all()
        serializer_class = experiment_rep_serializer['ExperimentRepDetailSerializer']
        permission_classes = [IsAuthenticated]

    class ExperimentRepListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = ExperimentRep.objects.all()
        serializer_class = experiment_rep_serializer['ExperimentRepListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = ExperimentRepListFilter
        pagination_class = APILimitOffsetPagination

    class ExperimentRepDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = ExperimentRep.objects.all()
        serializer_class = experiment_rep_serializer['ExperimentRepDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

    return {
        'ExperimentRepListAPIView': ExperimentRepListAPIView,
        'ExperimentRepDetailAPIView': ExperimentRepDetailAPIView,
        'ExperimentRepCreateAPIView': ExperimentRepCreateAPIView
    }
