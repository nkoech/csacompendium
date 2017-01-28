from rest_framework.filters import (
    FilterSet
)
from csacompendium.csa_practice.models import PracticeLevel


class CsaThemeListFilter(FilterSet):
    """
    Filter query list from practice level database
    """
    class Meta:
        model = PracticeLevel
        # fields = {
        #     'soil_texture': ['iexact', 'icontains'],
        # }
        # order_by = ['soil_texture']
