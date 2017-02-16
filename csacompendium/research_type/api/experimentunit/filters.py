from rest_framework.filters import FilterSet
from csacompendium.research_type.models import ExperimentUnit


class ExperimentUnitListFilter(FilterSet):
    """
    Filter query list from experiment unit database table
    """
    class Meta:
        model = ExperimentUnit
        fields = {'exp_unit_code': ['iexact', 'icontains'],
                  'experimentunitcategory': ['exact'],
                  'common_name': ['iexact', 'icontains'],
                  'latin_name': ['iexact', 'icontains'],
                  }
        order_by = ['exp_unit_code']


