from csacompendium.research.models import Author
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
)
from .filters import AuthorListFilter
from csacompendium.research.api.author.authorserializers import author_serializers
author_serializers = author_serializers()


def author_views():
    """
    Author views
    :return: All author views
    :rtype: Object
    """

    class AuthorCreateAPIView(CreateAPIView):
        """
        Creates a single record.
        """
        queryset = Author.objects.all()
        serializer_class = author_serializers['AuthorDetailSerializer']
        permission_classes = [IsAuthenticated]

        def perform_create(self, serializer):
            """
            Creates a new value on the user field
            :param serializer: Serializer object
            :return: None
            :rtype: None
            """
            serializer.save(user=self.request.user)

    class AuthorListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = Author.objects.all()
        serializer_class = author_serializers['AuthorListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = AuthorListFilter
        pagination_class = APILimitOffsetPagination

    class AuthorDetailAPIView(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
        """
        Updates a record.
        """
        queryset = Author.objects.all()
        serializer_class = author_serializers['AuthorDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'slug'

        def put(self, request, *args, **kwargs):
            """
            Update record
            :param request: Client request
            :param args: List arguments
            :param kwargs: Keyworded arguments
            :return: Updated record
            :rtype: Object
            """
            return self.update(request, *args, **kwargs)

        def delete(self, request, *args, **kwargs):
            """
            Delete record
            :param request: Client request
            :param args: List arguments
            :param kwargs: Keyworded arguments
            :return: Updated record
            :rtype: Object
            """
            return self.destroy(request, *args, **kwargs)

        def perform_update(self, serializer):
            """
            Update a field
            :param serializer: Serializer object
            :return:
            """
            serializer.save(modified_by=self.request.user)

    return {
        'AuthorListAPIView': AuthorListAPIView,
        'AuthorDetailAPIView': AuthorDetailAPIView,
        'AuthorCreateAPIView': AuthorCreateAPIView
    }
