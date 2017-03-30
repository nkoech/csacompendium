from django.contrib import admin

# Register your models here.
from .models import (
    Location,
    LocationRelation,
    Temperature,
    Precipitation,
)


class LocationRelationInline(admin.TabularInline):
    """
    Easy editing of location entry relations from the location entry page
    """
    model = LocationRelation


class LocationModelAdmin(admin.ModelAdmin):
    """
    Location model admin settings
    """
    list_display = ['location_name', 'latitude', 'longitude', 'elevation', 'site_type', 'last_update', 'modified_by']
    list_display_links = ['location_name']
    list_filter = ['location_name', 'site_type', 'last_update', 'modified_by']
    inlines = [LocationRelationInline, ]

    class Meta:
        model = Location


class TemperatureModelAdmin(admin.ModelAdmin):
    """
    Temperature model admin settings
    """
    list_display = ['temperature', 'temperature_uom', 'last_update', 'modified_by']
    list_display_links = ['temperature']
    list_filter = ['temperature', 'last_update', 'modified_by']

    class Meta:
        model = Temperature


class PrecipitationModelAdmin(admin.ModelAdmin):
    """
    Precipitation model admin settings
    """
    list_display = ['precipitation', 'precipitation_uom', 'last_update', 'modified_by']
    list_display_links = ['precipitation']
    list_filter = ['precipitation', 'last_update', 'modified_by']

    class Meta:
        model = Precipitation

admin.site.register(Location, LocationModelAdmin)
admin.site.register(Temperature, TemperatureModelAdmin)
admin.site.register(Precipitation, PrecipitationModelAdmin)
