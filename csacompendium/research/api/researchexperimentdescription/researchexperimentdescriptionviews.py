from csacompendium.research.models import ResearchExperimentDescription
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, get_http_request
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import ResearchExperimentDescriptionListFilter
from csacompendium.research.api.serializers import research_experiment_description_serializers


def research_experiment_description_views():
    """
    Research experiment description views
    :return: All research experiment description views
    :rtype: Object
    """
    class ResearchExperimentDescriptionCreateAPIView(CreateAPIView):
        """
        Creates a single record.
        """
        queryset = ResearchExperimentDescription.objects.all()
        permission_classes = [IsAuthenticated]

        def get_serializer_class(self):
            """
            Gets serializer class
            :return: Research experiment description object
            :rtype: Object
            """
            model_type, url_parameter, user = get_http_request(self.request, slug=False)
            create_research_experiment_description_serializer = research_experiment_description_serializers[
                'create_research_experiment_description_serializer'
            ]
            return create_research_experiment_description_serializer(model_type, url_parameter, user)

    class ResearchExperimentDescriptionListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = ResearchExperimentDescription.objects.all()
        serializer_class = research_experiment_description_serializers['ResearchExperimentDescriptionListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = ResearchExperimentDescriptionListFilter
        pagination_class = APILimitOffsetPagination

    class ResearchExperimentDescriptionDetailAPIView(DetailViewUpdateDelete):
        """
        Creates, deletes and updates a record.
        """
        queryset = ResearchExperimentDescription.objects.all()
        serializer_class = research_experiment_description_serializers['ResearchExperimentDescriptionDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

    return {
        'ResearchExperimentDescriptionCreateAPIView': ResearchExperimentDescriptionCreateAPIView,
        'ResearchExperimentDescriptionListAPIView': ResearchExperimentDescriptionListAPIView,
        'ResearchExperimentDescriptionDetailAPIView': ResearchExperimentDescriptionDetailAPIView
    }
