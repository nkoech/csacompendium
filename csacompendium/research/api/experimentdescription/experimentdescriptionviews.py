from csacompendium.research.models import ExperimentDescription
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import ExperimentDescriptionListFilter
from csacompendium.research.api.experimentdescription.experimentdescriptionserializers import \
    experiment_description_serializers


def experiment_description_views():
    """
    Experiment description views
    :return: All experiment description views
    :rtype: Object
    """
    experiment_description_serializer = experiment_description_serializers()

    class ExperimentDescriptionCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = ExperimentDescription.objects.all()
        serializer_class = experiment_description_serializer['ExperimentDescriptionDetailSerializer']
        permission_classes = [IsAuthenticated]

    class ExperimentDescriptionListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = ExperimentDescription.objects.all()
        serializer_class = experiment_description_serializer['ExperimentDescriptionListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = ExperimentDescriptionListFilter
        pagination_class = APILimitOffsetPagination

    class ExperimentDescriptionDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = ExperimentDescription.objects.all()
        serializer_class = experiment_description_serializer['ExperimentDescriptionDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'slug'

    return {
        'ExperimentDescriptionListAPIView': ExperimentDescriptionListAPIView,
        'ExperimentDescriptionDetailAPIView': ExperimentDescriptionDetailAPIView,
        'ExperimentDescriptionCreateAPIView': ExperimentDescriptionCreateAPIView
    }

