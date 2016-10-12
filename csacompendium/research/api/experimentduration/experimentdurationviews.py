from csacompendium.research.models import ExperimentDuration
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import ExperimentDurationListFilter
from csacompendium.research.api.experimentduration.experimentdurationserializers import experiment_duration_serializers
experiment_duration_serializers = experiment_duration_serializers()


def experiment_duration_views():
    """
    experiment duration views
    :return: All experiment duration views
    :rtype: Object
    """

    class ExperimentDurationCreateAPIView(CreateAPIView):
        """
        Creates a single record.
        """
        queryset = ExperimentDuration.objects.all()
        serializer_class = experiment_duration_serializers['ExperimentDurationDetailSerializer']
        permission_classes = [IsAuthenticated]

        def perform_create(self, serializer):
            """
            Creates a new value on the user field
            :param serializer: Serializer object
            :return: None
            :rtype: None
            """
            serializer.save(user=self.request.user)

    class ExperimentDurationListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = ExperimentDuration.objects.all()
        serializer_class = experiment_duration_serializers['ExperimentDurationListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = ExperimentDurationListFilter
        pagination_class = APILimitOffsetPagination

    class ExperimentDurationDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = ExperimentDuration.objects.all()
        serializer_class = experiment_duration_serializers['ExperimentDurationDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

    return {
        'ExperimentDurationListAPIView': ExperimentDurationListAPIView,
        'ExperimentDurationDetailAPIView': ExperimentDurationDetailAPIView,
        'ExperimentDurationCreateAPIView': ExperimentDurationCreateAPIView
    }
