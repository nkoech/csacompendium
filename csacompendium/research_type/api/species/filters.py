from rest_framework.filters import (
    FilterSet
)
from csacompendium.research_type.models import Species


class SpeciesListFilter(FilterSet):
    """
    Filter query list from species database
    """
    class Meta:
        model = Species
        fields = {'species': ['iexact', 'icontains'], }
        order_by = ['species']