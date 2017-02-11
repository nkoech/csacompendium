# from rest_framework.filters import (
#     FilterSet
# )
# from csacompendium.research.models import MeasurementYear
#
#
# class MeasurementYearListFilter(FilterSet):
#     """
#     Filter query list from measurement year database table
#     """
#     class Meta:
#         model = MeasurementYear
#         fields = {
#             'meas_year': ['exact', 'gte', 'lte'],
#             'measurementseason': ['exact'],
#             'object_id': ['exact'],
#             'content_type': ['exact'],
#         }
#         order_by = ['meas_year']
