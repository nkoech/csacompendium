from csacompendium.research.models import ResearchNitrogenApplied
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, get_http_request
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import ResearchNitrogenAppliedListFilter
from csacompendium.research.api.serializers import research_nitrogen_applied_serializers


def research_nitrogen_applied_views():
    """
    Research nitrogen applied views
    :return: All research nitrogen applied views
    :rtype: Object
    """
    class ResearchNitrogenAppliedCreateAPIView(CreateAPIView):
        """
        Creates a single record.
        """
        queryset = ResearchNitrogenApplied.objects.all()
        permission_classes = [IsAuthenticated]

        def get_serializer_class(self):
            """
            Gets serializer class
            :return: Research nitrogen applied object
            :rtype: Object
            """
            model_type, url_parameter, user = get_http_request(self.request, slug=False)
            create_research_nitrogen_applied_serializer = research_nitrogen_applied_serializers[
                'create_research_nitrogen_applied_serializer'
            ]
            return create_research_nitrogen_applied_serializer(model_type, url_parameter, user)

    class ResearchNitrogenAppliedListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = ResearchNitrogenApplied.objects.all()
        serializer_class = research_nitrogen_applied_serializers['ResearchNitrogenAppliedListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = ResearchNitrogenAppliedListFilter
        pagination_class = APILimitOffsetPagination

    class ResearchNitrogenAppliedDetailAPIView(DetailViewUpdateDelete):
        """
        Creates, deletes and updates a record.
        """
        queryset = ResearchNitrogenApplied.objects.all()
        serializer_class = research_nitrogen_applied_serializers['ResearchNitrogenAppliedDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

    return {
        'ResearchNitrogenAppliedCreateAPIView': ResearchNitrogenAppliedCreateAPIView,
        'ResearchNitrogenAppliedListAPIView': ResearchNitrogenAppliedListAPIView,
        'ResearchNitrogenAppliedDetailAPIView': ResearchNitrogenAppliedDetailAPIView
    }
