from rest_framework.filters import (
    FilterSet
)
from csacompendium.csa_practice.models import PracticeType


class CsaThemeListFilter(FilterSet):
    """
    Filter query list from practice type database
    """
    class Meta:
        model = PracticeType
        # fields = {
        #     'soil_texture': ['iexact', 'icontains'],
        # }
        # order_by = ['soil_texture']
