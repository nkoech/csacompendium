from csacompendium.research_type.models import ExperimentUnitCategory
from csacompendium.utils.pagination import APILimitOffsetPagination
from csacompendium.utils.permissions import IsOwnerOrReadOnly
from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import ExperimentUnitCategoryListFilter
from csacompendium.research_type.api.experimentunitcategory.experimentunitcategoryserializers \
    import experiment_unit_category_serializers


def experiment_unit_category_views():
    """
    Experiment unit category views
    :return: All experiment unit category views
    :rtype: Object
    """
    experiment_unit_category_serializer = experiment_unit_category_serializers()

    class ExperimentUnitCategoryCreateAPIView(CreateAPIViewHook):
        """
        Creates a single record.
        """
        queryset = ExperimentUnitCategory.objects.all()
        serializer_class = experiment_unit_category_serializer['ExperimentUnitCategoryDetailSerializer']
        permission_classes = [IsAuthenticated]

    class ExperimentUnitCategoryListAPIView(ListAPIView):
        """
        API list view. Gets all records API.
        """
        queryset = ExperimentUnitCategory.objects.all()
        serializer_class = experiment_unit_category_serializer['ExperimentUnitCategoryListSerializer']
        filter_backends = (DjangoFilterBackend,)
        filter_class = ExperimentUnitCategoryListFilter
        pagination_class = APILimitOffsetPagination

    class ExperimentUnitCategoryDetailAPIView(DetailViewUpdateDelete):
        """
        Updates a record.
        """
        queryset = ExperimentUnitCategory.objects.all()
        serializer_class = experiment_unit_category_serializer['ExperimentUnitCategoryDetailSerializer']
        permission_classes = [IsAuthenticated, IsAdminUser]
        lookup_field = 'slug'

    return {
        'ExperimentUnitCategoryListAPIView': ExperimentUnitCategoryListAPIView,
        'ExperimentUnitCategoryDetailAPIView': ExperimentUnitCategoryDetailAPIView,
        'ExperimentUnitCategoryCreateAPIView': ExperimentUnitCategoryCreateAPIView
    }
