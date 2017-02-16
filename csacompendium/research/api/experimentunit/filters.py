# from rest_framework.filters import FilterSet
# from csacompendium.research.models import ExperimentObject
#
#
# class ExperimentObjectListFilter(FilterSet):
#     """
#     Filter query list from experiment object database table
#     """
#     class Meta:
#         model = ExperimentObject
#         fields = {'exp_object_code': ['iexact', 'icontains'],
#                   'objectcategory': ['exact'],
#                   'object_name': ['iexact', 'icontains'],
#                   'latin_name': ['iexact', 'icontains'],
#                   }
#         order_by = ['exp_object_code']
