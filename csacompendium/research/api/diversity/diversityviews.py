from csacompendium.research.models import Diversity
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import DiversityListFilter
from csacompendium.research.api.diversity.diversityserializers import \
    diversity_serializers


def diversity_views():
    """
    Diversity views
    :return: All diversity views
    :rtype: Object
    """
    diversity_serializer = diversity_serializers()

    class DiversityCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = Diversity.objects.all()
        serializer_class = diversity_serializer['DiversityDetailSerializer']
        permission_classes = [IsAuthenticated]

    class DiversityListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = Diversity.objects.all()
        serializer_class = diversity_serializer['DiversityListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = DiversityListFilter
        pagination_class = APILimitOffsetPagination

    class DiversityDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = Diversity.objects.all()
        serializer_class = diversity_serializer['DiversityDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'slug'

    return {
        'DiversityListAPIView': DiversityListAPIView,
        'DiversityDetailAPIView': DiversityDetailAPIView,
        'DiversityCreateAPIView': DiversityCreateAPIView
    }

