from rest_framework.filters import (
    FilterSet
)
from csacompendium.research.models import Species


class SpeciesListFilter(FilterSet):
    """
    Filter query list from precipitation database
    """
    class Meta:
        model = Species
        fields = {'species': ['iexact', 'icontains'], }
        order_by = ['species']
