from csacompendium.research_type.models import ControlResearch
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
from .filters import ControlResearchListFilter
from csacompendium.research_type.api.serializers import control_research_serializers


def control_research_views():
    """
    Control research views
    :return: All control research views
    :rtype: Object
    """
    class ControlResearchCreateAPIView(CreateAPIView):
        """
        Creates a single record.
        """
        queryset = ControlResearch.objects.all()
        permission_classes = [IsAuthenticated]

        def get_serializer_class(self):
            """
            Gets serializer class
            :return: ControlResearch object
            :rtype: Object
            """
            model_type = None
            url_parameter = None
            user = None
            if validate_request_key(self.request) == 'pk':
                model_type, url_parameter, user = get_http_request(self.request, slug=False)
            elif validate_request_key(self.request) == 'slug':
                model_type, url_parameter, user = get_http_request(self.request, slug=True)
            create_control_research_serializer = control_research_serializers['create_control_research_serializer']
            return create_control_research_serializer(model_type, url_parameter, user)

    class ControlResearchListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = ControlResearch.objects.all()
        serializer_class = control_research_serializers['ControlResearchListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = ControlResearchListFilter
        pagination_class = APILimitOffsetPagination

    class ControlResearchDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = ControlResearch.objects.all()
        serializer_class = control_research_serializers['ControlResearchDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

    return {
        'ControlResearchCreateAPIView': ControlResearchCreateAPIView,
        'ControlResearchListAPIView': ControlResearchListAPIView,
        'ControlResearchDetailAPIView': ControlResearchDetailAPIView
    }
