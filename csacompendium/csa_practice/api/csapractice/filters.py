from rest_framework.filters import (
    FilterSet
)
from csacompendium.csa_practice.models import CsaPractice


class CsaThemeListFilter(FilterSet):
    """
    Filter query list from CSA practice database
    """
    class Meta:
        model = CsaPractice
        # fields = {
        #     'soil_texture': ['iexact', 'icontains'],
        # }
        # order_by = ['soil_texture']
