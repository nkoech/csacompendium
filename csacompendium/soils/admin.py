from django.contrib import admin

# Register your models here.
from .models import (
    Soil,
    SoilType,
    SoilTexture,
)


class SoilModelAdmin(admin.ModelAdmin):
    """
    Soil model admin settings
    """
    list_display = ['soiltype', 'soiltexture', 'som', 'som_uom', 'soil_ph', 'soil_years', 'last_update', 'modified_by']
    list_display_links = ['soiltype']
    list_filter = ['soiltype', 'soiltexture', 'som', 'last_update', 'modified_by']

    class Meta:
        model = Soil


class SoilTypeModelAdmin(admin.ModelAdmin):
    """
    Soil type model admin settings
    """
    list_display = ['soil_type', 'classification', 'last_update', 'modified_by']
    list_display_links = ['soil_type']
    list_filter = ['soil_type', 'classification', 'last_update', 'modified_by']

    class Meta:
        model = SoilType


class SoilTextureModelAdmin(admin.ModelAdmin):
    """
    Soil texture model admin settings
    """
    list_display = ['soil_texture', 'last_update', 'modified_by']
    list_display_links = ['soil_texture']
    list_filter = ['soil_texture', 'last_update', 'modified_by']

    class Meta:
        model = SoilTexture


admin.site.register(Soil, SoilModelAdmin)
admin.site.register(SoilType, SoilTypeModelAdmin)
admin.site.register(SoilTexture, SoilTextureModelAdmin)