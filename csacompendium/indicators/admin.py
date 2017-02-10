from django.contrib import admin

# Register your models here.
from .models import (
    OutcomeIndicator,
    IndicatorType,
    Indicator,
    Subpillar,
)

class OutcomeIndicatorModelAdmin(admin.ModelAdmin):
    """
    Outcome indicator model admin settings
    """
    list_display = [
        'indicator_code', 'indicator', 'subindicator', 'definition',
        'common_uom', 'indicatortype', 'last_update', 'modified_by'
    ]
    list_display_links = ['indicator_code']
    list_filter = ['indicator', 'subindicator', 'indicatortype', 'last_update', 'modified_by']

    class Meta:
        model = OutcomeIndicator

class IndicatorTypeModelAdmin(admin.ModelAdmin):
    """
    Indicator type model admin settings
    """
    list_display = ['indicator_type', 'last_update', 'modified_by']
    list_display_links = ['indicator_type']
    list_filter = ['indicator_type', 'last_update', 'modified_by']

    class Meta:
        model = IndicatorType


class IndicatorModelAdmin(admin.ModelAdmin):
    """
    Indicator model admin settings
    """
    list_display = ['subpillar', 'indicator', 'last_update', 'modified_by']
    list_display_links = ['indicator']
    list_filter = ['indicator', 'subpillar', 'last_update', 'modified_by']

    class Meta:
        model = Indicator


class SubpillarModelAdmin(admin.ModelAdmin):
    """
    Subpillar model admin settings
    """
    list_display = ['subpillar', 'last_update', 'modified_by']
    list_display_links = ['subpillar']
    list_filter = ['subpillar', 'last_update', 'modified_by']

    class Meta:
        model = Subpillar


admin.site.register(OutcomeIndicator, OutcomeIndicatorModelAdmin)
admin.site.register(IndicatorType, IndicatorTypeModelAdmin)
admin.site.register(Indicator, IndicatorModelAdmin)
admin.site.register(Subpillar, SubpillarModelAdmin)
