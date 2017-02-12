from csacompendium.locations.models import LocationRelation
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, get_http_request
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import LocationRelationListFilter
from csacompendium.locations.api.serializers import location_relation_serializers


def location_relation_views():
    """
    Location relation views
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
            model_type, url_parameter, user = get_http_request(self.request, slug=False)
            create_location_relation_serializer = location_relation_serializers['create_location_relation_serializer']
            return create_location_relation_serializer(model_type, url_parameter, user)

    class LocationRelationListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = LocationRelation.objects.all()
        serializer_class = location_relation_serializers['LocationRelationListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = LocationRelationListFilter
        pagination_class = APILimitOffsetPagination

    class LocationRelationDetailAPIView(DetailViewUpdateDelete):
        """
        Creates, deletes and updates a record.
        """
        queryset = LocationRelation.objects.all()
        serializer_class = location_relation_serializers['LocationRelationDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

    return {
        'LocationRelationCreateAPIView': LocationRelationCreateAPIView,
        'LocationRelationListAPIView': LocationRelationListAPIView,
        'LocationRelationDetailAPIView': LocationRelationDetailAPIView
    }
