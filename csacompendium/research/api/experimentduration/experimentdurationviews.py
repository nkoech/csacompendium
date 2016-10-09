from csacompendium.research.models import ExperimentDuration
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
)
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

    class ExperimentDurationDetailAPIView(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
        """
        Updates a record.
        """
        queryset = ExperimentDuration.objects.all()
        serializer_class = experiment_duration_serializers['ExperimentDurationDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

        def put(self, request, *args, **kwargs):
            """
            Update record
            :param request: Client request
            :param args: List arguments
            :param kwargs: Keyworded arguments
            :return: Updated record
            :rtype: Object
            """
            return self.update(request, *args, **kwargs)

        def delete(self, request, *args, **kwargs):
            """
            Delete record
            :param request: Client request
            :param args: List arguments
            :param kwargs: Keyworded arguments
            :return: Updated record
            :rtype: Object
            """
            return self.destroy(request, *args, **kwargs)

        def perform_update(self, serializer):
            """
            Update a field
            :param serializer: Serializer object
            :return:
            """
            serializer.save(modified_by=self.request.user)

    return {
        'ExperimentDurationListAPIView': ExperimentDurationListAPIView,
        'ExperimentDurationDetailAPIView': ExperimentDurationDetailAPIView,
        'ExperimentDurationCreateAPIView': ExperimentDurationCreateAPIView
    }
