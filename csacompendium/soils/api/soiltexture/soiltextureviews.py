from csacompendium.soils.models import SoilTexture
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
from .filters import SoilTextureListFilter
from csacompendium.soils.api.soiltexture.soiltextureserializers import soil_texture_serializers
soil_texture_serializers = soil_texture_serializers()


def soil_texture_views():
    """
    Soil texture views
    :return: All soil texture views
    :rtype: Object
    """

    class SoilTextureCreateAPIView(CreateAPIView):
        """
        Creates a single record.
        """
        queryset = SoilTexture.objects.all()
        serializer_class = soil_texture_serializers['SoilTextureDetailSerializer']
        permission_classes = [IsAuthenticated]

        def perform_create(self, serializer):
            """
            Creates a new value on the user field
            :param serializer: Serializer object
            :return: None
            :rtype: None
            """
            serializer.save(user=self.request.user)

    class SoilTextureListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = SoilTexture.objects.all()
        serializer_class = soil_texture_serializers['SoilTextureListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = SoilTextureListFilter
        pagination_class = APILimitOffsetPagination

    class SoilTextureDetailAPIView(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
        """
        Updates a record.
        """
        queryset = SoilTexture.objects.all()
        serializer_class = soil_texture_serializers['SoilTextureDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'slug'

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
        'SoilTextureListAPIView': SoilTextureListAPIView,
        'SoilTextureDetailAPIView': SoilTextureDetailAPIView,
        'SoilTextureCreateAPIView': SoilTextureCreateAPIView
    }
