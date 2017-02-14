from csacompendium.csa_practice.models import ResearchCsaPractice
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, get_http_request
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import ResearchCsaPracticeListFilter
from csacompendium.csa_practice.api.serializers import research_csa_practice_serializers


def research_csa_practice_views():
    """
    Research CSA practice views
    :return: All research CSA practice views
    :rtype: Object
    """
    class ResearchCsaPracticeCreateAPIView(CreateAPIView):
        """
        Creates a single record.
        """
        queryset = ResearchCsaPractice.objects.all()
        permission_classes = [IsAuthenticated]

        def get_serializer_class(self):
            """
            Gets serializer class
            :return: Research CSA practice object
            :rtype: Object
            """
            model_type, url_parameter, user = get_http_request(self.request, slug=False)
            create_research_csa_practice_serializer = research_csa_practice_serializers[
                'create_research_csa_practice_serializer'
            ]
            return create_research_csa_practice_serializer(model_type, url_parameter, user)

    class ResearchCsaPracticeListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = ResearchCsaPractice.objects.all()
        serializer_class = research_csa_practice_serializers['ResearchCsaPracticeListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = ResearchCsaPracticeListFilter
        pagination_class = APILimitOffsetPagination

    class ResearchCsaPracticeDetailAPIView(DetailViewUpdateDelete):
        """
        Creates, deletes and updates a record.
        """
        queryset = ResearchCsaPractice.objects.all()
        serializer_class = research_csa_practice_serializers['ResearchCsaPracticeDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

    return {
        'ResearchCsaPracticeCreateAPIView': ResearchCsaPracticeCreateAPIView,
        'ResearchCsaPracticeListAPIView': ResearchCsaPracticeListAPIView,
        'ResearchCsaPracticeDetailAPIView': ResearchCsaPracticeDetailAPIView
    }
