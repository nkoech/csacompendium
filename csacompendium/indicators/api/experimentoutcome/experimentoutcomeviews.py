from csacompendium.indicators.models import ExperimentOutcome
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import ExperimentOutcomeListFilter
from csacompendium.indicators.api.experimentoutcome.experimentoutcomeserializers import \
    experiment_outcome_serializers


def experiment_outcome_views():
    """
    Experiment outcome views
    :return: All experiment outcome views
    :rtype: Object
    """
    experiment_outcome_serializer = experiment_outcome_serializers()

    class ExperimentOutcomeCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = ExperimentOutcome.objects.all()
        serializer_class = experiment_outcome_serializer['ExperimentOutcomeDetailSerializer']
        permission_classes = [IsAuthenticated]

    class ExperimentOutcomeListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = ExperimentOutcome.objects.all()
        serializer_class = experiment_outcome_serializer['ExperimentOutcomeListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = ExperimentOutcomeListFilter
        pagination_class = APILimitOffsetPagination

    class ExperimentOutcomeDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = ExperimentOutcome.objects.all()
        serializer_class = experiment_outcome_serializer['ExperimentOutcomeDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

    return {
        'ExperimentOutcomeListAPIView': ExperimentOutcomeListAPIView,
        'ExperimentOutcomeDetailAPIView': ExperimentOutcomeDetailAPIView,
        'ExperimentOutcomeCreateAPIView': ExperimentOutcomeCreateAPIView
    }
