from django_filters import CharFilter, NumberFilter
from rest_framework.filters import (
    FilterSet
)
from csacompendium.locations.models import Location


class LocationListFilter(FilterSet):
    """
    Filter query list from country database
    """
    class Meta:
        model = Location
        fields = {'location_name': ['iexact', 'icontains'],
                  'elevation': ['exact', 'gte', 'lte'],
                  }
        order_by = ['location_name']
