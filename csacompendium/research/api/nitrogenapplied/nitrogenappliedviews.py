from csacompendium.research.models import NitrogenApplied
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import NitrogenAppliedListFilter
from csacompendium.research.api.nitrogenapplied.nitrogenappliedserializers import \
    nitrogen_applied_serializers


def nitrogen_applied_views():
    """
    Nitrogen applied views
    :return: All nitrogen applied views
    :rtype: Object
    """
    nitrogen_applied_serializer = nitrogen_applied_serializers()

    class NitrogenAppliedCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = NitrogenApplied.objects.all()
        serializer_class = nitrogen_applied_serializer['NitrogenAppliedDetailSerializer']
        permission_classes = [IsAuthenticated]

    class NitrogenAppliedListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = NitrogenApplied.objects.all()
        serializer_class = nitrogen_applied_serializer['NitrogenAppliedListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = NitrogenAppliedListFilter
        pagination_class = APILimitOffsetPagination

    class NitrogenAppliedDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = NitrogenApplied.objects.all()
        serializer_class = nitrogen_applied_serializer['NitrogenAppliedDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

    return {
        'NitrogenAppliedListAPIView': NitrogenAppliedListAPIView,
        'NitrogenAppliedDetailAPIView': NitrogenAppliedDetailAPIView,
        'NitrogenAppliedCreateAPIView': NitrogenAppliedCreateAPIView
    }

