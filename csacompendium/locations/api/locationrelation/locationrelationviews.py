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
from .filters import LocationRelationListFilter
from csacompendium.locations.api.serializers import location_relation_serializers


def location_relation_views():
    """
    Location views
    :return: All location views
    :rtype: Object
    """
    class LocationRelationCreateAPIView(CreateAPIView):
        """
        Creates a single record.
        """
        queryset = LocationRelation.objects.all()
        permission_classes = [IsAuthenticated]

        def get_serializer_class(self):
            """
            Gets serializer class
            :return: LocationRelation object
            :rtype: Object
            """
            model_type = self.request.GET.get('type')
            pk = self.request.GET.get('pk')
            user = self.request.user
            create_location_relation_serializer = location_relation_serializers['create_location_relation_serializer']
            return create_location_relation_serializer(model_type, pk, user)

    class LocationRelationListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = LocationRelation.objects.all()
        serializer_class = location_relation_serializers['LocationRelationListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = LocationRelationListFilter
        pagination_class = APILimitOffsetPagination

    class LocationRelationDetailAPIView(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
        """
        Creates, deletes and updates a record.
        """
        queryset = LocationRelation.objects.all()
        serializer_class = location_relation_serializers['LocationRelationDetailSerializer']
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
        'LocationRelationCreateAPIView': LocationRelationCreateAPIView,
        'LocationRelationListAPIView': LocationRelationListAPIView,
        'LocationRelationDetailAPIView': LocationRelationDetailAPIView
    }
