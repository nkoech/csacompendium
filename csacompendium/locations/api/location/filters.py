from rest_framework.filters import (
    FilterSet
)
from csacompendium.locations.models import Location


class LocationListFilter(FilterSet):
    """
    Filter query list from location database table
    """
    class Meta:
        model = Location
        fields = {'location_name': ['iexact', 'icontains'],
                  'latitude': ['exact', 'gte', 'lte'],
                  'longitude': ['exact', 'gte', 'lte'],
                  'elevation': ['exact', 'gte', 'lte'],
                  'object_id': ['exact'],
                  'content_type': ['exact'],
                  }
        order_by = ['location_name']
