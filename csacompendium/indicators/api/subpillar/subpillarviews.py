from csacompendium.indicators.models import Subpillar
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import SubpillarListFilter
from csacompendium.indicators.api.subpillar.subpillarserializers import subpillar_serializers


def subpillar_views():
    """
    Subpillar views
    :return: All subpillar views
    :rtype: Object
    """
    subpillar_serializer = subpillar_serializers()

    class SubpillarCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = Subpillar.objects.all()
        serializer_class = subpillar_serializer['SubpillarDetailSerializer']
        permission_classes = [IsAuthenticated]

    class SubpillarListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = Subpillar.objects.all()
        serializer_class = subpillar_serializer['SubpillarListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = SubpillarListFilter
        pagination_class = APILimitOffsetPagination

    class SubpillarDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = Subpillar.objects.all()
        serializer_class = subpillar_serializer['SubpillarDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'slug'

    return {
        'SubpillarListAPIView': SubpillarListAPIView,
        'SubpillarDetailAPIView': SubpillarDetailAPIView,
        'SubpillarCreateAPIView': SubpillarCreateAPIView
    }
