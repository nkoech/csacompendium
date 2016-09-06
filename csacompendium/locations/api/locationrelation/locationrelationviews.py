from csacompendium.locations.models import LocationRelation
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
# from .filters import LocationRelationListFilter
from csacompendium.locations.api.serializers import (
    LocationRelationDetailSerializer,
    LocationRelationListSerializer,
    # create_location_relation_serializer,
)


def location_relation_views():
    """
    Location views
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
    #         return create_location_serializer(model_type, slug, user)

    class LocationRelationListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = LocationRelation.objects.all()
        serializer_class = LocationRelationListSerializer
        # filter_backends = (DjangoFilterBackend,)
        # filter_class = LocationRelationListFilter
        pagination_class = APILimitOffsetPagination

    class LocationRelationDetailAPIView(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
        """
        Creates, deletes and updates a record.
        """
        queryset = LocationRelation.objects.all()
        serializer_class = LocationRelationDetailSerializer
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
    return LocationRelationListAPIView, LocationRelationDetailAPIView
