from rest_framework.filters import (
    FilterSet
)
from csacompendium.csa_practice.models import PracticeLevel


class PracticeLevelListFilter(FilterSet):
    """
    Filter query list from practice level database
    """
    class Meta:
        model = PracticeLevel
        fields = {
            'practice_level': ['iexact', 'icontains'],
        }
        order_by = ['practice_level']
