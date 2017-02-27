from csacompendium.research.models import Author
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import AuthorListFilter
from csacompendium.research.api.author.authorserializers import author_serializers


def author_views():
    """
    Author views
    :return: All author views
    :rtype: Object
    """
    author_serializer = author_serializers()

    class AuthorCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = Author.objects.all()
        serializer_class = author_serializer['AuthorDetailSerializer']
        permission_classes = [IsAuthenticated]

    class AuthorListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = Author.objects.all()
        serializer_class = author_serializer['AuthorListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = AuthorListFilter
        pagination_class = APILimitOffsetPagination

    class AuthorDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = Author.objects.all()
        serializer_class = author_serializer['AuthorDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'slug'

    return {
        'AuthorListAPIView': AuthorListAPIView,
        'AuthorDetailAPIView': AuthorDetailAPIView,
        'AuthorCreateAPIView': AuthorCreateAPIView
    }

