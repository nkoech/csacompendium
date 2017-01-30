from csacompendium.csa_practice.models import CsaTheme
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import CsaThemeListFilter
from csacompendium.csa_practice.api.csatheme.csathemeserializers import csa_theme_serializers


def csa_theme_views():
    """
    CSA theme views
    :return: All CSA theme views
    :rtype: Object
    """
    csa_theme_serializer = csa_theme_serializers()

    class CsaThemeCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = CsaTheme.objects.all()
        serializer_class = csa_theme_serializer['CsaThemeDetailSerializer']
        permission_classes = [IsAuthenticated]

    class CsaThemeListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = CsaTheme.objects.all()
        serializer_class = csa_theme_serializer['CsaThemeListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = CsaThemeListFilter
        pagination_class = APILimitOffsetPagination

    class CsaThemeDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = CsaTheme.objects.all()
        serializer_class = csa_theme_serializer['CsaThemeDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'slug'

    return {
        'CsaThemeListAPIView': CsaThemeListAPIView,
        'CsaThemeDetailAPIView': CsaThemeDetailAPIView,
        'CsaThemeCreateAPIView': CsaThemeCreateAPIView
    }
