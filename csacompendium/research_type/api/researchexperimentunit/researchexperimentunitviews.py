from csacompendium.research_type.models import ResearchExperimentUnit
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, get_http_request
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import ResearchExperimentUnitListFilter
from csacompendium.research_type.api.serializers import research_experiment_unit_serializers


def research_experiment_unit_views():
    """
    Research experiment unit views
    :return: All research experiment unit views
    :rtype: Object
    """
    class ResearchExperimentUnitCreateAPIView(CreateAPIView):
        """
        Creates a single record.
        """
        queryset = ResearchExperimentUnit.objects.all()
        permission_classes = [IsAuthenticated]

        def get_serializer_class(self):
            """
            Gets serializer class
            :return: Research experiment unit views
            :rtype: Object
            """
            model_type, url_parameter, user = get_http_request(self.request, slug=False)
            create_research_experiment_unit_serializer = research_experiment_unit_serializers[
                'create_research_experiment_unit_serializer'
            ]
            return create_research_experiment_unit_serializer(model_type, url_parameter, user)

    class ResearchExperimentUnitListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = ResearchExperimentUnit.objects.all()
        serializer_class = research_experiment_unit_serializers['ResearchExperimentUnitListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = ResearchExperimentUnitListFilter
        pagination_class = APILimitOffsetPagination

    class ResearchExperimentUnitDetailAPIView(DetailViewUpdateDelete):
        """
        Creates, deletes and updates a record.
        """
        queryset = ResearchExperimentUnit.objects.all()
        serializer_class = research_experiment_unit_serializers['ResearchExperimentUnitDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

    return {
        'ResearchExperimentUnitCreateAPIView': ResearchExperimentUnitCreateAPIView,
        'ResearchExperimentUnitListAPIView': ResearchExperimentUnitListAPIView,
        'ResearchExperimentUnitDetailAPIView': ResearchExperimentUnitDetailAPIView
    }
