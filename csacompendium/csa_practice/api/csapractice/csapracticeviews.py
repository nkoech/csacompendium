from csacompendium.csa_practice.models import CsaPractice
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import CsaPracticeListFilter
from csacompendium.csa_practice.api.csapractice.csapracticeserializers import csa_practice_serializers


def csa_practice_views():
    """
    CSA practice views
    :return: All CSA practice views
    :rtype: Object
    """
    csa_practice_serializer = csa_practice_serializers()

    class CsaPracticeCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = CsaPractice.objects.all()
        serializer_class = csa_practice_serializer['CsaPracticeDetailSerializer']
        permission_classes = [IsAuthenticated]

    class CsaPracticeListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = CsaPractice.objects.all()
        serializer_class = csa_practice_serializer['CsaPracticeListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = CsaPracticeListFilter
        pagination_class = APILimitOffsetPagination

    class CsaPracticeDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = CsaPractice.objects.all()
        serializer_class = csa_practice_serializer['CsaPracticeDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'slug'

    return {
        'CsaPracticeListAPIView': CsaPracticeListAPIView,
        'CsaPracticeDetailAPIView': CsaPracticeDetailAPIView,
        'CsaPracticeCreateAPIView': CsaPracticeCreateAPIView
    }
