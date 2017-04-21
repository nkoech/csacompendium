from csacompendium.research.models import ResearchMeasurementYear
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, get_http_request
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import ResearchMeasurementYearListFilter
from csacompendium.research.api.serializers import research_measurement_year_serializers


def research_measurement_year_views():
    """
    Research measurement year views
    :return: All research measurement year views
    :rtype: Object
    """
    class ResearchMeasurementYearCreateAPIView(CreateAPIView):
        """
        Creates a single record.
        """
        queryset = ResearchMeasurementYear.objects.all()
        permission_classes = [IsAuthenticated]

        def get_serializer_class(self):
            """
            Gets serializer class
            :return: Research measurement year object
            :rtype: Object
            """
            model_type, url_parameter, user = get_http_request(self.request, slug=False)
            create_research_measurement_year_serializer = research_measurement_year_serializers[
                'create_research_measurement_year_serializer'
            ]
            return create_research_measurement_year_serializer(model_type, url_parameter, user)

    class ResearchMeasurementYearListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = ResearchMeasurementYear.objects.all()
        serializer_class = research_measurement_year_serializers['ResearchMeasurementYearListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = ResearchMeasurementYearListFilter
        pagination_class = APILimitOffsetPagination

    class ResearchMeasurementYearDetailAPIView(DetailViewUpdateDelete):
        """
        Creates, deletes and updates a record.
        """
        queryset = ResearchMeasurementYear.objects.all()
        serializer_class = research_measurement_year_serializers['ResearchMeasurementYearDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'pk'

    return {
        'ResearchMeasurementYearCreateAPIView': ResearchMeasurementYearCreateAPIView,
        'ResearchMeasurementYearListAPIView': ResearchMeasurementYearListAPIView,
        'ResearchMeasurementYearDetailAPIView': ResearchMeasurementYearDetailAPIView
    }
