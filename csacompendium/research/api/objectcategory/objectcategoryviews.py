from csacompendium.research.models import ObjectCategory
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import ObjectCategoryListFilter
from csacompendium.research.api.objectcategory.objectcategoryserializers import object_category_serializers


def object_category_views():
    """
    Object category views
    :return: All object category views
    :rtype: Object
    """
    object_category_serializer = object_category_serializers()

    class ObjectCategoryCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = ObjectCategory.objects.all()
        serializer_class = object_category_serializer['ObjectCategoryDetailSerializer']
        permission_classes = [IsAuthenticated]

    class ObjectCategoryListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = ObjectCategory.objects.all()
        serializer_class = object_category_serializer['ObjectCategoryListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = ObjectCategoryListFilter
        pagination_class = APILimitOffsetPagination

    class ObjectCategoryDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = ObjectCategory.objects.all()
        serializer_class = object_category_serializer['ObjectCategoryDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'slug'

    return {
        'ObjectCategoryListAPIView': ObjectCategoryListAPIView,
        'ObjectCategoryDetailAPIView': ObjectCategoryDetailAPIView,
        'ObjectCategoryCreateAPIView': ObjectCategoryCreateAPIView
    }
