from csacompendium.research.models import Breed
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import BreedListFilter
from csacompendium.research.api.breed.breedserializers import breed_serializers


def breed_views():
    """
    Breed views
    :return: All breed views
    :rtype: Object
    """
    breed_serializer = breed_serializers()

    class BreedCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = Breed.objects.all()
        serializer_class = breed_serializer['BreedDetailSerializer']
        permission_classes = [IsAuthenticated]

    class BreedListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = Breed.objects.all()
        serializer_class = breed_serializer['BreedListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = BreedListFilter
        pagination_class = APILimitOffsetPagination

    class BreedDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = Breed.objects.all()
        serializer_class = breed_serializer['BreedDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'slug'

    return {
        'BreedListAPIView': BreedListAPIView,
        'BreedDetailAPIView': BreedDetailAPIView,
        'BreedCreateAPIView': BreedCreateAPIView
    }
