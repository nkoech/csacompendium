# from rest_framework.serializers import (
#     ModelSerializer,
#     SerializerMethodField
# )
# from csacompendium.research.api.measurementyear.measurementyearserializers import measurement_year_serializers
# from csacompendium.research.models import MeasurementSeason
# from csacompendium.utils.hyperlinkedidentity import hyperlinked_identity
# from csacompendium.utils.serializersutils import FieldMethodSerializer, get_related_content
#
#
# def measurement_season_serializers():
#     """
#     Measurement season serializers
#     :return: All measurement season serializers
#     :rtype: Object
#     """
#
#     class MeasurementSeasonListSerializer(ModelSerializer):
#         """
#         Serialize all records in given fields into an API
#         """
#         url = hyperlinked_identity('research_api:measurement_season_detail', 'slug')
#
#         class Meta:
#             model = MeasurementSeason
#             fields = [
#                 'meas_season',
#                 'url',
#             ]
#
#     class MeasurementSeasonDetailSerializer(ModelSerializer, FieldMethodSerializer):
#         """
#         Serialize single record into an API. This is dependent on fields given.
#         """
#         measurement_year_serializers = measurement_year_serializers()
#         user = SerializerMethodField()
#         modified_by = SerializerMethodField()
#         measurement_year = SerializerMethodField()
#
#         class Meta:
#             common_fields = [
#                 'user',
#                 'modified_by',
#                 'last_update',
#                 'time_created',
#                 'measurement_year',
#             ]
#             model = MeasurementSeason
#             fields = [
#                 'id',
#                 'meas_season',
#             ] + common_fields
#             read_only_fields = ['id', ] + common_fields
#
#         def get_measurement_year(self, obj):
#             """
#             :param obj: Current record object
#             :return: Measurement year of a season
#             :rtype: Object/record
#             """
#             request = self.context['request']
#             MeasurementYearListSerializer = self.measurement_year_serializers['MeasurementYearListSerializer']
#             related_content = get_related_content(
#                 obj, MeasurementYearListSerializer, obj.measurement_year_relation, request
#             )
#             return related_content
#
#     return {
#         'MeasurementSeasonListSerializer': MeasurementSeasonListSerializer,
#         'MeasurementSeasonDetailSerializer': MeasurementSeasonDetailSerializer
#     }
