from csacompendium.soils.models import SoilType
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import SoilTypeListFilter
from csacompendium.soils.api.soiltype.soiltypeserializers import soil_type_serializers
soil_type_serializers = soil_type_serializers()


def soil_type_views():
    """
    Soil type views
    :return: All soil type views
    :rtype: Object
    """

    class SoilTypeCreateAPIView(CreateAPIView):
        """
        Creates a single record.
        """
        queryset = SoilType.objects.all()
        serializer_class = soil_type_serializers['SoilTypeDetailSerializer']
        permission_classes = [IsAuthenticated]

        def perform_create(self, serializer):
            """
            Creates a new value on the user field
            :param serializer: Serializer object
            :return: None
            :rtype: None
            """
            serializer.save(user=self.request.user)

    class SoilTypeListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = SoilType.objects.all()
        serializer_class = soil_type_serializers['SoilTypeListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = SoilTypeListFilter
        pagination_class = APILimitOffsetPagination

    class SoilTypeDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = SoilType.objects.all()
        serializer_class = soil_type_serializers['SoilTypeDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'slug'

    return {
        'SoilTypeListAPIView': SoilTypeListAPIView,
        'SoilTypeDetailAPIView': SoilTypeDetailAPIView,
        'SoilTypeCreateAPIView': SoilTypeCreateAPIView
    }
