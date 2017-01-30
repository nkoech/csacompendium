from csacompendium.csa_practice.models import PracticeType
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import PracticeTypeListFilter
from csacompendium.csa_practice.api.practicetype.practicetypeserializers import practice_type_serializers


def practice_type_views():
    """
    Practice type views
    :return: All practice type views
    :rtype: Object
    """
    practice_type_serializer = practice_type_serializers()

    class PracticeTypeCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = PracticeType.objects.all()
        serializer_class = practice_type_serializer['PracticeTypeDetailSerializer']
        permission_classes = [IsAuthenticated]

    class PracticeTypeListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = PracticeType.objects.all()
        serializer_class = practice_type_serializer['PracticeTypeListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = PracticeTypeListFilter
        pagination_class = APILimitOffsetPagination

    class PracticeTypeDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = PracticeType.objects.all()
        serializer_class = practice_type_serializer['PracticeTypeDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'slug'

    return {
        'PracticeTypeListAPIView': PracticeTypeListAPIView,
        'PracticeTypeDetailAPIView': PracticeTypeDetailAPIView,
        'PracticeTypeCreateAPIView': PracticeTypeCreateAPIView
    }
