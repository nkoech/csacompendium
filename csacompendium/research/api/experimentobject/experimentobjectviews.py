from csacompendium.research.models import ExperimentObject
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import ExperimentObjectListFilter
from csacompendium.research.api.experimentobject.experimentobjectserializers import experiment_object_serializers


def experiment_object_views():
    """
    Experiment object views
    :return: All experiment object views
    :rtype: Object
    """
    experiment_object_serializer = experiment_object_serializers()

    class ExperimentObjectCreateAPIView(CreateAPIView):
        """
        Creates a single record.
        """
        queryset = ExperimentObject.objects.all()
        serializer_class = experiment_object_serializer['ExperimentObjectDetailSerializer']
        permission_classes = [IsAuthenticated]

        def perform_create(self, serializer):
            """
            Creates a new value on the user field
            :param serializer: Serializer object
            :return: None
            :rtype: None
            """
            serializer.save(user=self.request.user)

    class ExperimentObjectListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = ExperimentObject.objects.all()
        serializer_class = experiment_object_serializer['ExperimentObjectListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = ExperimentObjectListFilter
        pagination_class = APILimitOffsetPagination

    class ExperimentObjectDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = ExperimentObject.objects.all()
        serializer_class = experiment_object_serializer['ExperimentObjectDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'slug'

    return {
        'ExperimentObjectListAPIView': ExperimentObjectListAPIView,
        'ExperimentObjectDetailAPIView': ExperimentObjectDetailAPIView,
        'ExperimentObjectCreateAPIView': ExperimentObjectCreateAPIView
    }
