from django_filters import CharFilter
from rest_framework.filters import (
    FilterSet
)
from csacompendium.countries.models import Country


class CountryListFilter(FilterSet):
    """
    Filter query list from country database
    """
    country_code = CharFilter(name='country_code', lookup_expr='iexact')
    country_name = CharFilter(name='country_name', lookup_expr='iexact')

    class Meta:
        model = Country
        fields = ['country_code', 'country_name']
        order_by = ['country_name']
