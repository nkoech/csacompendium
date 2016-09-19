from csacompendium.locations.models import Soil
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
from .filters import SoilListFilter
from csacompendium.soils.api.serializers import soil_serializers


def soil_views():
    """
    Soil views
    :return: All location views
    :rtype: Object
    """
    # class LocationCreateAPIView(CreateAPIView):
    #     """
    #     Creates a single record.
    #     """
    #     queryset = Location.objects.all()
    #     permission_classes = [IsAuthenticated]
    #
    #     def get_serializer_class(self):
    #         """
    #         Gets serializer class
    #         :return: Location object
    #         :rtype: Object
    #         """
    #         model_type = self.request.GET.get('type')
    #         slug = self.request.GET.get('slug')
    #         user = self.request.user
    #         create_location_serializer = location_serializers['create_location_serializer']
    #         return create_location_serializer(model_type, slug, user)

    class SoilListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = Soil.objects.all()
        serializer_class = soil_serializers['SoilListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = SoilListFilter
        pagination_class = APILimitOffsetPagination

    class SoilDetailAPIView(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
        """
        Updates a record.
        """
        queryset = Soil.objects.all()
        serializer_class = soil_serializers['SoilDetailSerializer']
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
        # 'LocationCreateAPIView': LocationCreateAPIView,
        'SoilListAPIView': SoilListAPIView,
        'SoilDetailAPIView': SoilDetailAPIView
    }