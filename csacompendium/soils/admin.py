from django.contrib import admin

# Register your models here.
from .models import (
    Soil,
    SoilType,
)


class SoilModelAdmin(admin.ModelAdmin):
    """
    Soil model admin settings
    """
    list_display = ['som', 'som_uom', 'initial_soc', 'soil_ph', 'soil_years', 'last_update', 'modified_by']
    list_display_links = ['som']
    list_filter = ['som', 'last_update', 'modified_by']

    class Meta:
        model = Soil


class SoilTypeModelAdmin(admin.ModelAdmin):
    """
    Soil model admin settings
    """
    list_display = ['soil_type', 'classification', 'last_update', 'modified_by']
    list_display_links = ['soil_type']
    list_filter = ['soil_type', 'classification', 'last_update', 'modified_by']

    class Meta:
        model = SoilType


admin.site.register(Soil, SoilModelAdmin)
admin.site.register(SoilType, SoilTypeModelAdmin)
