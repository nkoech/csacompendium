from csacompendium.research.models import Research
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import (
    DetailViewUpdateDelete,
    get_http_request,
    validate_request_key,
)
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import ResearchListFilter
from csacompendium.research.api.serializers import research_serializers


def research_views():
    """
    Research views
    :return: All research views
    :rtype: Object
    """
    class ResearchCreateAPIView(CreateAPIView):
        """
        Creates a single record.
        """
        queryset = Research.objects.all()
        permission_classes = [IsAuthenticated]

        def get_serializer_class(self):
            """
            Gets serializer class
            :return: Research object
            :rtype: Object
            """
            model_type = None
            url_parameter = None
            user = None
            if validate_request_key(self.request) == 'pk':
                model_type, url_parameter, user = get_http_request(self.request, slug=False)
            elif validate_request_key(self.request) == 'slug':
                model_type, url_parameter, user = get_http_request(self.request, slug=True)
            create_research_serializer = research_serializers['create_research_serializer']
            return create_research_serializer(model_type, url_parameter, user)

    class ResearchListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = Research.objects.all()
        serializer_class = research_serializers['ResearchListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = ResearchListFilter
        pagination_class = APILimitOffsetPagination

    class ResearchDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = Research.objects.all()
        serializer_class = research_serializers['ResearchDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

    return {
        'ResearchCreateAPIView': ResearchCreateAPIView,
        'ResearchListAPIView': ResearchListAPIView,
        'ResearchDetailAPIView': ResearchDetailAPIView
    }
