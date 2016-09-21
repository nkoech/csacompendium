from rest_framework.filters import (
    FilterSet
)
from csacompendium.soils.models import SoilTexture


class SoilTextureListFilter(FilterSet):
    """
    Filter query list from soil texture database
    """
    class Meta:
        model = SoilTexture
        fields = {'soil_texture': ['iexact', 'icontains'],
                  }
        order_by = ['soil_texture']
