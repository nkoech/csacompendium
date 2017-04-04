from csacompendium.research.models import Breed
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, get_http_request
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import BreedListFilter
from csacompendium.research.api.serializers import breed_serializers


def breed_views():
    """
    Breed views
    :return: All breed views
    :rtype: Object
    """
    class BreedCreateAPIView(CreateAPIView):
        """
        Creates a single record.
        """
        queryset = Breed.objects.all()
        permission_classes = [IsAuthenticated]

        def get_serializer_class(self):
            """
            Gets serializer class
            :return: Breed object
            :rtype: Object
            """
            model_type, url_parameter, user = get_http_request(self.request, slug=True)
            create_breed_serializer = breed_serializers['create_breed_serializer']
            return create_breed_serializer(model_type, url_parameter, user)

    class BreedListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = Breed.objects.all()
        serializer_class = breed_serializers['BreedListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = BreedListFilter
        pagination_class = APILimitOffsetPagination

    class BreedDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = Breed.objects.all()
        serializer_class = breed_serializers['BreedDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'slug'

    return {
        'BreedCreateAPIView': BreedCreateAPIView,
        'BreedListAPIView': BreedListAPIView,
        'BreedDetailAPIView': BreedDetailAPIView
    }