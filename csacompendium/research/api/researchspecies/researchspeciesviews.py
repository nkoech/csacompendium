from csacompendium.research.models import ResearchSpecies
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, get_http_request
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import ResearchSpeciesListFilter
from csacompendium.research.api.serializers import research_species_serializers


def research_species_views():
    """
    Research outcome indicator views
    :return: All research species views
    :rtype: Object
    """
    class ResearchSpeciesCreateAPIView(CreateAPIView):
        """
        Creates a single record.
        """
        queryset = ResearchSpecies.objects.all()
        permission_classes = [IsAuthenticated]

        def get_serializer_class(self):
            """
            Gets serializer class
            :return: ResearchSpecies object
            :rtype: Object
            """
            model_type, url_parameter, user = get_http_request(self.request, slug=False)
            create_research_species_serializer = research_species_serializers['create_research_species_serializer']
            return create_research_species_serializer(model_type, url_parameter, user)

    class ResearchSpeciesListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = ResearchSpecies.objects.all()
        serializer_class = research_species_serializers['ResearchSpeciesListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = ResearchSpeciesListFilter
        pagination_class = APILimitOffsetPagination

    class ResearchSpeciesDetailAPIView(DetailViewUpdateDelete):
        """
        Creates, deletes and updates a record.
        """
        queryset = ResearchSpecies.objects.all()
        serializer_class = research_species_serializers['ResearchSpeciesDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

    return {
        'ResearchSpeciesCreateAPIView': ResearchSpeciesCreateAPIView,
        'ResearchSpeciesListAPIView': ResearchSpeciesListAPIView,
        'ResearchSpeciesDetailAPIView': ResearchSpeciesDetailAPIView
    }
