from django_filters import CharFilter
from rest_framework.filters import (
    FilterSet
)
from csacompendium.locations.models import Location


class LocationListFilter(FilterSet):
    """
    Filter query list from country database
    """
    country_name = CharFilter(name='location_name', lookup_expr='iexact')

    class Meta:
        model = Location
        fields = ['country_name']
        order_by = ['country_name']
