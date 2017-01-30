from csacompendium.csa_practice.models import PracticeLevel
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import PracticeLevelListFilter
from csacompendium.csa_practice.api.practicelevel.practicelevelserializers import practice_level_serializers


def practice_level_views():
    """
    Practice level views
    :return: All practice level views
    :rtype: Object
    """
    practice_level_serializer = practice_level_serializers()

    class PracticeLevelCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = PracticeLevel.objects.all()
        serializer_class = practice_level_serializer['PracticeLevelDetailSerializer']
        permission_classes = [IsAuthenticated]

    class PracticeLevelListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = PracticeLevel.objects.all()
        serializer_class = practice_level_serializer['PracticeLevelListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = PracticeLevelListFilter
        pagination_class = APILimitOffsetPagination

    class PracticeLevelDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = PracticeLevel.objects.all()
        serializer_class = practice_level_serializer['PracticeLevelDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'slug'

    return {
        'PracticeLevelListAPIView': PracticeLevelListAPIView,
        'PracticeLevelDetailAPIView': PracticeLevelDetailAPIView,
        'PracticeLevelCreateAPIView': PracticeLevelCreateAPIView
    }
