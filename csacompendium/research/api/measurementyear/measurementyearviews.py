from csacompendium.research.models import MeasurementYear
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
from .filters import MeasurementYearListFilter
from csacompendium.research.api.serializers import measurement_year_serializers


def measurement_year_views():
    """
    Measurement year views
    :return: All  measurement year views
    :rtype: Object
    """
    class MeasurementYearCreateAPIView(CreateAPIView):
        """
        Creates a single record.
        """
        queryset = MeasurementYear.objects.all()
        permission_classes = [IsAuthenticated]

        def get_serializer_class(self):
            """
            Gets serializer class
            :return: Measurement year object
            :rtype: Object
            """
            model_type = self.request.GET.get('type')
            pk = self.request.GET.get('pk')
            user = self.request.user
            create_measurement_year_serializer = measurement_year_serializers['create_measurement_year_serializer']
            return create_measurement_year_serializer(model_type, pk, user)

    class MeasurementYearListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = MeasurementYear.objects.all()
        serializer_class = measurement_year_serializers['MeasurementYearListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = MeasurementYearListFilter
        pagination_class = APILimitOffsetPagination

    class MeasurementYearDetailAPIView(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
        """
        Updates a record.
        """
        queryset = MeasurementYear.objects.all()
        serializer_class = measurement_year_serializers['MeasurementYearDetailSerializer']
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
            Update individual value
            :param serializer: Serializer object
            :return:
            """
            serializer.save(modified_by=self.request.user)

    return {
        'MeasurementYearCreateAPIView': MeasurementYearCreateAPIView,
        'MeasurementYearListAPIView': MeasurementYearListAPIView,
        'MeasurementYearDetailAPIView': MeasurementYearDetailAPIView
    }