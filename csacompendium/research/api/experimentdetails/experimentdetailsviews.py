from csacompendium.research.models import ExperimentDetails
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import ExperimentDetailsListFilter
from csacompendium.research.api.experimentdetails.experimentdetailsserializers import experiment_details_serializers


def experiment_details_views():
    """
    Experiment details views
    :return: All experiment details views
    :rtype: Object
    """
    experiment_details_serializer = experiment_details_serializers()

    class ExperimentDetailsCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = ExperimentDetails.objects.all()
        serializer_class = experiment_details_serializer['ExperimentDetailsDetailSerializer']
        permission_classes = [IsAuthenticated]

    class ExperimentDetailsListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = ExperimentDetails.objects.all()
        serializer_class = experiment_details_serializer['ExperimentDetailsListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = ExperimentDetailsListFilter
        pagination_class = APILimitOffsetPagination

    class ExperimentDetailsDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = ExperimentDetails.objects.all()
        serializer_class = experiment_details_serializer['ExperimentDetailsDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'slug'

    return {
        'ExperimentDetailsListAPIView': ExperimentDetailsListAPIView,
        'ExperimentDetailsDetailAPIView': ExperimentDetailsDetailAPIView,
        'ExperimentDetailsCreateAPIView': ExperimentDetailsCreateAPIView
    }
