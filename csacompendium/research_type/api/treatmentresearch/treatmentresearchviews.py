from csacompendium.research_type.models import TreatmentResearch
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
from .filters import TreatmentResearchListFilter
from csacompendium.research_type.api.serializers import treatment_research_serializers


def treatment_research_views():
    """
    Treatment research views
    :return: All treatment research views
    :rtype: Object
    """
    class TreatmentResearchCreateAPIView(CreateAPIView):
        """
        Creates a single record.
        """
        queryset = TreatmentResearch.objects.all()
        permission_classes = [IsAuthenticated]

        def get_serializer_class(self):
            """
            Gets serializer class
            :return: Treatment research object
            :rtype: Object
            """
            model_type = None
            url_parameter = None
            user = None
            if validate_request_key(self.request) == 'pk':
                model_type, url_parameter, user = get_http_request(self.request, slug=False)
            elif validate_request_key(self.request) == 'slug':
                model_type, url_parameter, user = get_http_request(self.request, slug=True)
            create_treatment_research_serializer = treatment_research_serializers[
                'create_treatment_research_serializer'
            ]
            return create_treatment_research_serializer(model_type, url_parameter, user)

    class TreatmentResearchListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = TreatmentResearch.objects.all()
        serializer_class = treatment_research_serializers['TreatmentResearchListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = TreatmentResearchListFilter
        pagination_class = APILimitOffsetPagination

    class TreatmentResearchDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = TreatmentResearch.objects.all()
        serializer_class = treatment_research_serializers['TreatmentResearchDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

    return {
        'TreatmentResearchCreateAPIView': TreatmentResearchCreateAPIView,
        'TreatmentResearchListAPIView': TreatmentResearchListAPIView,
        'TreatmentResearchDetailAPIView': TreatmentResearchDetailAPIView
    }
