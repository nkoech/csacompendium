from django.contrib import admin

# Register your models here.
from .models import (
    MeasurementSeason,
    MeasurementYear,
    ExperimentDuration,
    Research,
    Author,
)


class ResearchModelAdmin(admin.ModelAdmin):
    """
    Location model admin settings
    """
    list_display = ['author', 'experimentduration', 'research_year', 'last_update', 'modified_by']
    list_display_links = ['author']
    list_filter = ['author', 'experimentduration', 'last_update', 'modified_by', 'research_year']

    class Meta:
        model = Research


class AuthorModelAdmin(admin.ModelAdmin):
    """
    Temperature model admin settings
    """
    list_display = ['author_code', 'first_name', 'middle_name', 'last_name', 'author_bio', 'last_update', 'modified_by']
    list_display_links = ['first_name']
    list_filter = ['author_code', 'first_name', 'last_name', 'last_update', 'modified_by']

    class Meta:
        model = Author


class ExperimentDurationModelAdmin(admin.ModelAdmin):
    """
    Precipitation model admin settings
    """
    list_display = ['exp_duration', 'last_update', 'modified_by']
    list_display_links = ['exp_duration']
    list_filter = ['exp_duration', 'last_update', 'modified_by']

    class Meta:
        model = ExperimentDuration


class MeasurementYearModelAdmin(admin.ModelAdmin):
    """
    measurement year model admin settings
    """
    list_display = ['meas_year', 'measurementseason', 'last_update', 'modified_by']
    list_display_links = ['meas_year']
    list_filter = ['measurementseason', 'last_update', 'modified_by', 'meas_year']

    class Meta:
        model = MeasurementYear


class MeasurementSeasonModelAdmin(admin.ModelAdmin):
    """
    Precipitation model admin settings
    """
    list_display = ['meas_season', 'last_update', 'modified_by']
    list_display_links = ['meas_season']
    list_filter = ['meas_season', 'last_update', 'modified_by']

    class Meta:
        model = MeasurementSeason

admin.site.register(Research, ResearchModelAdmin)
admin.site.register(Author, AuthorModelAdmin)
admin.site.register(ExperimentDuration, ExperimentDurationModelAdmin)
admin.site.register(MeasurementYear, MeasurementYearModelAdmin)
admin.site.register(MeasurementSeason, MeasurementSeasonModelAdmin)
