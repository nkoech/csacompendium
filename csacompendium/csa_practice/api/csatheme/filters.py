from rest_framework.filters import (
    FilterSet
)
from csacompendium.csa_practice.models import CsaTheme


class CsaThemeListFilter(FilterSet):
    """
    Filter query list from CSA theme database
    """
    class Meta:
        model = CsaTheme
        # fields = {
        #     'soil_texture': ['iexact', 'icontains'],
        # }
        # order_by = ['soil_texture']
