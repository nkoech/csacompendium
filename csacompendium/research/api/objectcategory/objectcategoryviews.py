from csacompendium.research.models import ObjectCategory
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
from .filters import ObjectCategoryListFilter
from csacompendium.research.api.objectcategory.objectcategoryserializers import object_category_serializers
object_category_serializers = object_category_serializers()


def object_category_views():
    """
    Object category views
    :return: All object category views
    :rtype: Object
    """

    class ObjectCategoryCreateAPIView(CreateAPIView):
        """
        Creates a single record.
        """
        queryset = ObjectCategory.objects.all()
        serializer_class = object_category_serializers['ObjectCategoryDetailSerializer']
        permission_classes = [IsAuthenticated]

        def perform_create(self, serializer):
            """
            Creates a new value on the user field
            :param serializer: Serializer object
            :return: None
            :rtype: None
            """
            serializer.save(user=self.request.user)

    class ObjectCategoryListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = ObjectCategory.objects.all()
        serializer_class = object_category_serializers['ObjectCategoryListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = ObjectCategoryListFilter
        pagination_class = APILimitOffsetPagination

    class ObjectCategoryDetailAPIView(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
        """
        Updates a record.
        """
        queryset = ObjectCategory.objects.all()
        serializer_class = object_category_serializers['ObjectCategoryDetailSerializer']
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
        'ObjectCategoryListAPIView': ObjectCategoryListAPIView,
        'ObjectCategoryDetailAPIView': ObjectCategoryDetailAPIView,
        'ObjectCategoryCreateAPIView': ObjectCategoryCreateAPIView
    }
