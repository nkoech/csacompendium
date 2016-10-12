from csacompendium.soils.models import SoilTexture
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import SoilTextureListFilter
from csacompendium.soils.api.soiltexture.soiltextureserializers import soil_texture_serializers


def soil_texture_views():
    """
    Soil texture views
    :return: All soil texture views
    :rtype: Object
    """
    soil_texture_serializer = soil_texture_serializers()

    class SoilTextureCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = SoilTexture.objects.all()
        serializer_class = soil_texture_serializer['SoilTextureDetailSerializer']
        permission_classes = [IsAuthenticated]

    class SoilTextureListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = SoilTexture.objects.all()
        serializer_class = soil_texture_serializer['SoilTextureListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = SoilTextureListFilter
        pagination_class = APILimitOffsetPagination

    class SoilTextureDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = SoilTexture.objects.all()
        serializer_class = soil_texture_serializer['SoilTextureDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'slug'

    return {
        'SoilTextureListAPIView': SoilTextureListAPIView,
        'SoilTextureDetailAPIView': SoilTextureDetailAPIView,
        'SoilTextureCreateAPIView': SoilTextureCreateAPIView
    }
