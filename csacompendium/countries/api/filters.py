from rest_framework.filters import (
    FilterSet
)
from csacompendium.countries.models import Country


class CountryListFilter(FilterSet):
    """
    Filter query list from country database
    """
    class Meta:
        model = Country
        fields = ['country_code', 'country_name']

