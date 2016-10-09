from rest_framework.filters import (
    FilterSet
)
from csacompendium.locations.models import LocationRelation


class LocationRelationListFilter(FilterSet):
    """
    Filter query list from location relation database table
    """
    class Meta:
        model = LocationRelation
        fields = {'location': ['exact'],
                  'object_id': ['exact'],
                  'content_type': ['exact'],
                  }
        order_by = ['location']
