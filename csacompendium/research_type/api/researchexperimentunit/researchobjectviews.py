from csacompendium.research.models import ResearchObject
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, get_http_request
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import ResearchObjectListFilter
from csacompendium.research.api.serializers import research_object_serializers


def research_object_views():
    """
    Research object object views
    :return: All  research object views
    :rtype: Object
    """
    class ResearchObjectCreateAPIView(CreateAPIView):
        """
        Creates a single record.
        """
        queryset = ResearchObject.objects.all()
        permission_classes = [IsAuthenticated]

        def get_serializer_class(self):
            """
            Gets serializer class
            :return: Research object object
            :rtype: Object
            """
            model_type, url_parameter, user = get_http_request(self.request, slug=False)
            create_research_object_serializer = research_object_serializers['create_research_object_serializer']
            return create_research_object_serializer(model_type, url_parameter, user)

    class ResearchObjectListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = ResearchObject.objects.all()
        serializer_class = research_object_serializers['ResearchObjectListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = ResearchObjectListFilter
        pagination_class = APILimitOffsetPagination

    class ResearchObjectDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = ResearchObject.objects.all()
        serializer_class = research_object_serializers['ResearchObjectDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

    return {
        'ResearchObjectCreateAPIView': ResearchObjectCreateAPIView,
        'ResearchObjectListAPIView': ResearchObjectListAPIView,
        'ResearchObjectDetailAPIView': ResearchObjectDetailAPIView
    }