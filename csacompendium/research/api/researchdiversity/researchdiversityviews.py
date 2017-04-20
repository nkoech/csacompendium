from csacompendium.research.models import ResearchDiversity
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, get_http_request
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import ResearchDiversityListFilter
from csacompendium.research.api.serializers import research_diversity_serializers


def research_diversity_views():
    """
    Research diversity views
    :return: All research diversity views
    :rtype: Object
    """
    class ResearchDiversityCreateAPIView(CreateAPIView):
        """
        Creates a single record.
        """
        queryset = ResearchDiversity.objects.all()
        permission_classes = [IsAuthenticated]

        def get_serializer_class(self):
            """
            Gets serializer class
            :return: Research diversity object
            :rtype: Object
            """
            model_type, url_parameter, user = get_http_request(self.request, slug=False)
            create_research_diversity_serializer = research_diversity_serializers[
                'create_research_diversity_serializer'
            ]
            return create_research_diversity_serializer(model_type, url_parameter, user)

    class ResearchDiversityListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = ResearchDiversity.objects.all()
        serializer_class = research_diversity_serializers['ResearchDiversityListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = ResearchDiversityListFilter
        pagination_class = APILimitOffsetPagination

    class ResearchDiversityDetailAPIView(DetailViewUpdateDelete):
        """
        Creates, deletes and updates a record.
        """
        queryset = ResearchDiversity.objects.all()
        serializer_class = research_diversity_serializers['ResearchDiversityDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

    return {
        'ResearchDiversityCreateAPIView': ResearchDiversityCreateAPIView,
        'ResearchDiversityListAPIView': ResearchDiversityListAPIView,
        'ResearchDiversityDetailAPIView': ResearchDiversityDetailAPIView
    }
