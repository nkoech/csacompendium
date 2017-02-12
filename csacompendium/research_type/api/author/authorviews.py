from csacompendium.research_type.models import Author
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import AuthorListFilter
from csacompendium.research_type.api.author.authorserializers import author_serializers


def author_views():
    """
    Author views
    :return: All author views
    :rtype: Object
    """
    author_serializer = author_serializers()

    class TemperatureCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = Temperature.objects.all()
        serializer_class = temperature_serializer['TemperatureDetailSerializer']
        permission_classes = [IsAuthenticated]

    class TemperatureListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = Temperature.objects.all()
        serializer_class = temperature_serializer['TemperatureListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = TemperatureListFilter
        pagination_class = APILimitOffsetPagination

    class TemperatureDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = Temperature.objects.all()
        serializer_class = temperature_serializer['TemperatureDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

    return {
        'TemperatureListAPIView': TemperatureListAPIView,
        'TemperatureDetailAPIView': TemperatureDetailAPIView,
        'TemperatureCreateAPIView': TemperatureCreateAPIView
    }

