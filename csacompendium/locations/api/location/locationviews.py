from csacompendium.locations.models import Location
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import (
    DetailViewUpdateDelete,
    get_http_request
)

from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import LocationListFilter
from csacompendium.locations.api.serializers import location_serializers


def location_views():
    """
    Location views
    :return: All location views
    :rtype: Object
    """
    class LocationCreateAPIView(CreateAPIView):
        """
        Creates a single record.
        """
        queryset = Location.objects.all()
        permission_classes = [IsAuthenticated]

        def get_serializer_class(self):
            """
            Gets serializer class
            :return: Location object
            :rtype: Object
            """
            model_type, url_parameter, user = get_http_request(self.request, slug=True)
            create_location_serializer = location_serializers['create_location_serializer']
            return create_location_serializer(model_type, url_parameter, user)

    class LocationListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = Location.objects.all()
        serializer_class = location_serializers['LocationListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = LocationListFilter
        pagination_class = APILimitOffsetPagination

    class LocationDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = Location.objects.all()
        serializer_class = location_serializers['LocationDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'slug'

    return {
        'LocationCreateAPIView': LocationCreateAPIView,
        'LocationListAPIView': LocationListAPIView,
        'LocationDetailAPIView': LocationDetailAPIView
    }