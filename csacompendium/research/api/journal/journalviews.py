from csacompendium.research.models import Journal
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import JournalListFilter
from csacompendium.research.api.journal.journalserializers import journal_serializers


def journal_views():
    """
    Journal views
    :return: All journal views
    :rtype: Object
    """
    journal_serializer = journal_serializers()

    class JournalCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = Journal.objects.all()
        serializer_class = journal_serializer['JournalDetailSerializer']
        permission_classes = [IsAuthenticated]

    class JournalListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = Journal.objects.all()
        serializer_class = journal_serializer['JournalListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = JournalListFilter
        pagination_class = APILimitOffsetPagination

    class JournalDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = Journal.objects.all()
        serializer_class = journal_serializer['JournalDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'slug'

    return {
        'JournalListAPIView': JournalListAPIView,
        'JournalDetailAPIView': JournalDetailAPIView,
        'JournalCreateAPIView': JournalCreateAPIView
    }
