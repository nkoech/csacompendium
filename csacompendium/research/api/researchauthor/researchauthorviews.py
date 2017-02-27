from csacompendium.research.models import ResearchAuthor
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, get_http_request
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import ResearchAuthorListFilter
from csacompendium.research.api.serializers import research_author_serializers


def research_author_views():
    """
    Research author views
    :return: All research author views
    :rtype: Object
    """
    class ResearchAuthorCreateAPIView(CreateAPIView):
        """
        Creates a single record.
        """
        queryset = ResearchAuthor.objects.all()
        permission_classes = [IsAuthenticated]

        def get_serializer_class(self):
            """
            Gets serializer class
            :return: Research author object
            :rtype: Object
            """
            model_type, url_parameter, user = get_http_request(self.request, slug=False)
            create_research_author_serializer = research_author_serializers['create_research_author_serializer']
            return create_research_author_serializer(model_type, url_parameter, user)

    class ResearchAuthorListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = ResearchAuthor.objects.all()
        serializer_class = research_author_serializers['ResearchAuthorListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = ResearchAuthorListFilter
        pagination_class = APILimitOffsetPagination

    class ResearchAuthorDetailAPIView(DetailViewUpdateDelete):
        """
        Creates, deletes and updates a record.
        """
        queryset = ResearchAuthor.objects.all()
        serializer_class = research_author_serializers['ResearchAuthorDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

    return {
        'ResearchAuthorCreateAPIView': ResearchAuthorCreateAPIView,
        'ResearchAuthorListAPIView': ResearchAuthorListAPIView,
        'ResearchAuthorDetailAPIView': ResearchAuthorDetailAPIView
    }
