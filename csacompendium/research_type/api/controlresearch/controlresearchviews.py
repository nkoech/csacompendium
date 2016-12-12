# from csacompendium.soils.models import Soil
# from csacompendium.utils.pagination import APILimitOffsetPagination
# from csacompendium.utils.permissions import IsOwnerOrReadOnly
# from csacompendium.utils.viewsutils import DetailViewUpdateDelete, get_http_request
# from rest_framework.filters import DjangoFilterBackend
# from rest_framework.generics import CreateAPIView, ListAPIView
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from .filters import SoilListFilter
# from csacompendium.soils.api.serializers import soil_serializers
#
#
# def soil_views():
#     """
#     Soil views
#     :return: All soil views
#     :rtype: Object
#     """
#     class SoilCreateAPIView(CreateAPIView):
#         """
#         Creates a single record.
#         """
#         queryset = Soil.objects.all()
#         permission_classes = [IsAuthenticated]
#
#         def get_serializer_class(self):
#             """
#             Gets serializer class
#             :return: Soil object
#             :rtype: Object
#             """
#             model_type, url_parameter, user = get_http_request(self.request, slug=True)
#             create_soil_serializer = soil_serializers['create_soil_serializer']
#             return create_soil_serializer(model_type, url_parameter, user)
#
#     class SoilListAPIView(ListAPIView):
#         """
#         API list view. Gets all records API.
#         """
#         queryset = Soil.objects.all()
#         serializer_class = soil_serializers['SoilListSerializer']
#         filter_backends = (DjangoFilterBackend,)
#         filter_class = SoilListFilter
#         pagination_class = APILimitOffsetPagination
#
#     class SoilDetailAPIView(DetailViewUpdateDelete):
#         """
#         Updates a record.
#         """
#         queryset = Soil.objects.all()
#         serializer_class = soil_serializers['SoilDetailSerializer']
#         permission_classes = [IsAuthenticated, IsAdminUser]
#         lookup_field = 'pk'
#
#     return {
#         'SoilCreateAPIView': SoilCreateAPIView,
#         'SoilListAPIView': SoilListAPIView,
#         'SoilDetailAPIView': SoilDetailAPIView
#     }
