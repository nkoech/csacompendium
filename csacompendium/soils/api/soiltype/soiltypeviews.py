from csacompendium.soils.models import SoilType
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import SoilTypeListFilter
from csacompendium.soils.api.soiltype.soiltypeserializers import soil_type_serializers


def soil_type_views():
    """
    Soil type views
    :return: All soil type views
    :rtype: Object
    """
    soil_type_serializer = soil_type_serializers()

    class SoilTypeCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = SoilType.objects.all()
        serializer_class = soil_type_serializer['SoilTypeDetailSerializer']
        permission_classes = [IsAuthenticated]

    class SoilTypeListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = SoilType.objects.all()
        serializer_class = soil_type_serializer['SoilTypeListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = SoilTypeListFilter
        pagination_class = APILimitOffsetPagination

    class SoilTypeDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = SoilType.objects.all()
        serializer_class = soil_type_serializer['SoilTypeDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'slug'

    return {
        'SoilTypeListAPIView': SoilTypeListAPIView,
        'SoilTypeDetailAPIView': SoilTypeDetailAPIView,
        'SoilTypeCreateAPIView': SoilTypeCreateAPIView
    }
