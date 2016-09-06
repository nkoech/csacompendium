from rest_framework.filters import (
    FilterSet
)
from csacompendium.locations.models import LocationRelation


class LocationRelationListFilter(FilterSet):
    """
    Filter query list from country database
    """
    class Meta:
        model = LocationRelation
        fields = ['location']
        order_by = ['location']