from django.contrib import admin

# Register your models here.
from .models import Location


class LocationModelAdmin(admin.ModelAdmin):
    list_display = ['location_name', 'latitude', 'longitude', 'last_update', 'modified_by']
    list_display_links = ['location_name']
    list_filter = ['location_name', 'last_update', 'modified_by']

    class Meta:
        model = Location

admin.site.register(Location, LocationModelAdmin)