from django.contrib import admin

# Register your models here.
from .models import (
    OutcomeIndicator,
    SoilMeasurement,
    ResearchOutcomeIndicator,
    IndicatorType,
    Indicator,
    Subpillar,
)


class SoilMeasurementModelAdmin(admin.ModelAdmin):
    """
    Soil measurement model admin settings
    """
    list_display = ['upper_soil_depth', 'lower_soil_depth', 'incubation_days', 'last_update', 'modified_by']
    list_display_links = ['upper_soil_depth']
    list_filter = ['upper_soil_depth', 'lower_soil_depth', 'modified_by']

    class Meta:
        model = SoilMeasurement


class ResearchOutcomeIndicatorInline(admin.TabularInline):
    """
    Inline for easy editing of in the admin in relation to the outcome indicator admin
    """
    model = ResearchOutcomeIndicator


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
    inlines = [ResearchOutcomeIndicatorInline, ]

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


admin.site.register(SoilMeasurement, SoilMeasurementModelAdmin)
admin.site.register(OutcomeIndicator, OutcomeIndicatorModelAdmin)
admin.site.register(IndicatorType, IndicatorTypeModelAdmin)
admin.site.register(Indicator, IndicatorModelAdmin)
admin.site.register(Subpillar, SubpillarModelAdmin)
