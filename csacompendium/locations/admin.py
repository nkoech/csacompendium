from django.contrib import admin

# Register your models here.
from .models import (
    Location,
    LocationRelation,
    Temperature,
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
    list_display = ['location_name', 'latitude', 'longitude', 'last_update', 'modified_by']
    list_display_links = ['location_name']
    list_filter = ['location_name', 'last_update', 'modified_by']
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

admin.site.register(Location, LocationModelAdmin)
admin.site.register(Temperature, TemperatureModelAdmin)
