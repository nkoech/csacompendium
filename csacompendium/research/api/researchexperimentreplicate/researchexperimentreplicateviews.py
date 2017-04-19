from csacompendium.research.models import ResearchExperimentReplicate
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, get_http_request
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import ResearchExperimentReplicateListFilter
from csacompendium.research.api.serializers import research_experiment_replicate_serializers


def research_experiment_replicate_views():
    """
    Research experiment replicate views
    :return: All research experiment replicate views
    :rtype: Object
    """
    class ResearchExperimentReplicateCreateAPIView(CreateAPIView):
        """
        Creates a single record.
        """
        queryset = ResearchExperimentReplicate.objects.all()
        permission_classes = [IsAuthenticated]

        def get_serializer_class(self):
            """
            Gets serializer class
            :return: Research experiment replicate object
            :rtype: Object
            """
            model_type, url_parameter, user = get_http_request(self.request, slug=False)
            create_research_experiment_replicate_serializer = research_experiment_replicate_serializers[
                'create_research_experiment_replicate_serializer'
            ]
            return create_research_experiment_replicate_serializer(model_type, url_parameter, user)

    class ResearchExperimentReplicateListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = ResearchExperimentReplicate.objects.all()
        serializer_class = research_experiment_replicate_serializers['ResearchExperimentReplicateListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = ResearchExperimentReplicateListFilter
        pagination_class = APILimitOffsetPagination

    class ResearchExperimentReplicateDetailAPIView(DetailViewUpdateDelete):
        """
        Creates, deletes and updates a record.
        """
        queryset = ResearchExperimentReplicate.objects.all()
        serializer_class = research_experiment_replicate_serializers['ResearchExperimentReplicateDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

    return {
        'ResearchExperimentReplicateCreateAPIView': ResearchExperimentReplicateCreateAPIView,
        'ResearchExperimentReplicateListAPIView': ResearchExperimentReplicateListAPIView,
        'ResearchExperimentReplicateDetailAPIView': ResearchExperimentReplicateDetailAPIView
    }
