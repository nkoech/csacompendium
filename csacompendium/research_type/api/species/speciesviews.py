# from csacompendium.research.models import Species
# from csacompendium.utils.pagination import APILimitOffsetPagination
# from csacompendium.utils.permissions import IsOwnerOrReadOnly
# from csacompendium.utils.viewsutils import DetailViewUpdateDelete, CreateAPIViewHook
# from rest_framework.filters import DjangoFilterBackend
# from rest_framework.generics import ListAPIView
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from .filters import SpeciesListFilter
# from csacompendium.research.api.species.speciesserializers import species_serializers
#
#
# def species_views():
#     """
#     Species views
#     :return: All species views
#     :rtype: Object
#     """
#     species_serializer = species_serializers()
#
#     class SpeciesCreateAPIView(CreateAPIViewHook):
#         """
#         Creates a single record.
#         """
#         queryset = Species.objects.all()
#         serializer_class = species_serializer['SpeciesDetailSerializer']
#         permission_classes = [IsAuthenticated]
#
#     class SpeciesListAPIView(ListAPIView):
#         """
#         API list view. Gets all records API.
#         """
#         queryset = Species.objects.all()
#         serializer_class = species_serializer['SpeciesListSerializer']
#         filter_backends = (DjangoFilterBackend,)
#         filter_class = SpeciesListFilter
#         pagination_class = APILimitOffsetPagination
#
#     class SpeciesDetailAPIView(DetailViewUpdateDelete):
#         """
#         Updates a record
#         """
#         queryset = Species.objects.all()
#         serializer_class = species_serializer['SpeciesDetailSerializer']
#         permission_classes = [IsAuthenticated, IsAdminUser]
#         lookup_field = 'slug'
#
#     return {
#         'SpeciesListAPIView': SpeciesListAPIView,
#         'SpeciesDetailAPIView': SpeciesDetailAPIView,
#         'SpeciesCreateAPIView': SpeciesCreateAPIView
#     }
#
