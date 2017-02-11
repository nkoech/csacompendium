from django.contrib import admin

from django.contrib import admin

# Register your models here.
from .models import (
    ExperimentRep,
    NitrogenApplied,
    ExperimentDetails,
    ExperimentDuration,
    MeasurementSeason,
    MeasurementYear,
    ControlResearch,
    TreatmentResearch,
)


class TreatmentResearchModelAdmin(admin.ModelAdmin):
    """
    Treatment research model admin settings
    """
    list_display = ['experimentdetails', 'experimentrep', 'nitrogenapplied', 'experimentduration', 'last_update', 'modified_by']
    list_display_links = ['experimentdetails']
    list_filter = ['experimentrep', 'nitrogenapplied', 'experimentduration', 'last_update', 'modified_by']

    class Meta:
        model = TreatmentResearch


class ControlResearchModelAdmin(admin.ModelAdmin):
    """
    Control research model admin settings
    """
    list_display = ['experimentdetails', 'experimentrep', 'nitrogenapplied', 'experimentduration', 'last_update', 'modified_by']
    list_display_links = ['experimentdetails']
    list_filter = ['experimentrep', 'nitrogenapplied', 'experimentduration', 'last_update', 'modified_by']

    class Meta:
        model = ControlResearch


class ExperimentDetailsModelAdmin(admin.ModelAdmin):
    """
    Experiment details model admin settings
    """
    list_display = ['exp_detail', 'last_update', 'modified_by']
    list_display_links = ['exp_detail']
    list_filter = ['exp_detail', 'last_update', 'modified_by']

    class Meta:
        model = ExperimentDetails


class NitrogenAppliedModelAdmin(admin.ModelAdmin):
    """
    Nitrogen applied model admin settings
    """
    list_display = ['nitrogen_amount', 'amount_uom', 'last_update', 'modified_by']
    list_display_links = ['nitrogen_amount']
    list_filter = ['nitrogen_amount', 'amount_uom', 'last_update', 'modified_by']

    class Meta:
        model = NitrogenApplied


class ExperimentRepModelAdmin(admin.ModelAdmin):
    """
    Experiment replication model admin settings
    """
    list_display = ['no_replication', 'last_update', 'modified_by']
    list_display_links = ['no_replication']
    list_filter = ['no_replication', 'last_update', 'modified_by']

    class Meta:
        model = ExperimentRep


class ExperimentDurationModelAdmin(admin.ModelAdmin):
    """
    Experiment details model admin settings
    """
    list_display = ['exp_duration', 'last_update', 'modified_by']
    list_display_links = ['exp_duration']
    list_filter = ['exp_duration', 'last_update', 'modified_by']

    class Meta:
        model = ExperimentDuration


class MeasurementYearModelAdmin(admin.ModelAdmin):
    """
    Measurement year model admin settings
    """
    list_display = ['meas_year', 'measurementseason', 'last_update', 'modified_by']
    list_display_links = ['meas_year']
    list_filter = ['measurementseason', 'last_update', 'modified_by', 'meas_year']

    class Meta:
        model = MeasurementYear


class MeasurementSeasonModelAdmin(admin.ModelAdmin):
    """
    Measurement season model admin settings
    """
    list_display = ['meas_season', 'last_update', 'modified_by']
    list_display_links = ['meas_season']
    list_filter = ['meas_season', 'last_update', 'modified_by']

    class Meta:
        model = MeasurementSeason

admin.site.register(TreatmentResearch, TreatmentResearchModelAdmin)
admin.site.register(ControlResearch, ControlResearchModelAdmin)
admin.site.register(ExperimentDetails, ExperimentDetailsModelAdmin)
admin.site.register(NitrogenApplied, NitrogenAppliedModelAdmin)
admin.site.register(ExperimentRep, ExperimentRepModelAdmin)
admin.site.register(ExperimentDuration, ExperimentDurationModelAdmin)
admin.site.register(MeasurementYear, MeasurementYearModelAdmin)
admin.site.register(MeasurementSeason, MeasurementSeasonModelAdmin)
