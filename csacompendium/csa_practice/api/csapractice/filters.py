from rest_framework.filters import (
    FilterSet
)
from csacompendium.csa_practice.models import CsaPractice


class CsaPracticeListFilter(FilterSet):
    """
    Filter query list from CSA practice database
    """
    class Meta:
        model = CsaPractice
        fields = {'practice_code': ['iexact', 'icontains'],
                  'csatheme': ['exact'],
                  'practicelevel': ['exact'],
                  'sub_practice_level': ['iexact', 'icontains'],
                  'sub_subpractice_level': ['iexact', 'icontains'],
                  'definition': ['iexact', 'icontains'],
                  'practicetype': ['exact'],
                  }
        order_by = ['practice_code']
