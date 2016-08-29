from django.contrib import admin

# Register your models here.
from .models import Country


class CountryModelAdmin(admin.ModelAdmin):
    list_display = ['country_name', 'time_created', 'last_update', 'modified_by']
    list_display_links = ['country_name']
    list_filter = ['country_name', 'last_update', 'modified_by']

    class Meta:
        model = Country

admin.site.register(Country, CountryModelAdmin)
