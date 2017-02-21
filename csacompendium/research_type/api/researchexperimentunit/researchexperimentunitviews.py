from csacompendium.research_type.models import ResearchExperimentUnit
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, get_http_request
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import ResearchExperimentUnitListFilter
from csacompendium.research_type.api.serializers import research_experiment_unit_serializers


def research_outcome_indicator_views():
    """
    Research outcome indicator views
    :return: All research outcome indicator views
    :rtype: Object
    """
    class ResearchOutcomeIndicatorCreateAPIView(CreateAPIView):
        """
        Creates a single record.
        """
        queryset = ResearchOutcomeIndicator.objects.all()
        permission_classes = [IsAuthenticated]

        def get_serializer_class(self):
            """
            Gets serializer class
            :return: Research outcome indicator object
            :rtype: Object
            """
            model_type, url_parameter, user = get_http_request(self.request, slug=False)
            create_research_outcome_indicator_serializer = research_outcome_indicator_serializers[
                'create_research_outcome_indicator_serializer'
            ]
            return create_research_outcome_indicator_serializer(model_type, url_parameter, user)

    class ResearchOutcomeIndicatorListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = ResearchOutcomeIndicator.objects.all()
        serializer_class = research_outcome_indicator_serializers['ResearchOutcomeIndicatorListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = ResearchOutcomeIndicatorListFilter
        pagination_class = APILimitOffsetPagination

    class ResearchOutcomeIndicatorDetailAPIView(DetailViewUpdateDelete):
        """
        Creates, deletes and updates a record.
        """
        queryset = ResearchOutcomeIndicator.objects.all()
        serializer_class = research_outcome_indicator_serializers['ResearchOutcomeIndicatorDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

    return {
        'ResearchOutcomeIndicatorCreateAPIView': ResearchOutcomeIndicatorCreateAPIView,
        'ResearchOutcomeIndicatorListAPIView': ResearchOutcomeIndicatorListAPIView,
        'ResearchOutcomeIndicatorDetailAPIView': ResearchOutcomeIndicatorDetailAPIView
    }
