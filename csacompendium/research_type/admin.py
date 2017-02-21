from django.contrib import admin

# Register your models here.
from .models import (
    ExperimentRep,
    NitrogenApplied,
    ExperimentDetails,
    ExperimentDuration,
    MeasurementSeason,
    MeasurementYear,
    Author,
    ResearchAuthor,
    Species,
    ResearchSpecies,
    ControlResearch,
    TreatmentResearch,
    ExperimentUnitCategory,
    ExperimentUnit,
    ResearchExperimentUnit,
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


class ResearchAuthorInline(admin.TabularInline):
    """
    Easy editing of research author entry relations from the author entry page
    """
    model = ResearchAuthor


class AuthorModelAdmin(admin.ModelAdmin):
    """
    Author model admin settings
    """
    list_display = ['author_code', 'first_name', 'middle_name', 'last_name', 'author_bio', 'last_update', 'modified_by']
    list_display_links = ['first_name']
    list_filter = ['author_code', 'first_name', 'last_name', 'last_update', 'modified_by']
    inlines = [ResearchAuthorInline, ]

    class Meta:
        model = Author


class ResearchSpeciesInline(admin.TabularInline):
    """
    Easy editing of research species entry relations from the species entry page
    """
    model = ResearchSpecies


class SpeciesModelAdmin(admin.ModelAdmin):
    """
    Species model admin settings
    """
    list_display = ['species', 'last_update', 'modified_by']
    list_display_links = ['species']
    list_filter = ['species', 'last_update', 'modified_by']
    inlines = [ResearchSpeciesInline, ]

    class Meta:
        model = Species


class ExperimentUnitCategoryModelAdmin(admin.ModelAdmin):
    """
    Experiment unit category model admin settings
    """
    list_display = ['unit_category', 'last_update', 'modified_by']
    list_display_links = ['unit_category']
    list_filter = ['unit_category', 'last_update', 'modified_by']

    class Meta:
        model = ExperimentUnitCategory


class ExperimentUnitModelAdmin(admin.ModelAdmin):
    """
    Experiment unit model admin settings
    """
    list_display = [
        'exp_unit_code', 'experimentunitcategory', 'common_name', 'latin_name', 'last_update', 'modified_by'
    ]
    list_display_links = ['common_name']
    list_filter = ['common_name', 'exp_unit_code', 'experimentunitcategory', 'last_update', 'modified_by']

    class Meta:
        model = ExperimentUnit


class ResearchExperimentUnitModelAdmin(admin.ModelAdmin):
    """
    Research experiment unit model admin settings
    """
    list_display = [
        'experimentunit', 'upper_soil_depth', 'upper_soil_depth', 'incubation_days', 'last_update', 'modified_by'
    ]
    list_display_links = ['experimentunit']
    list_filter = ['experimentunit', 'upper_soil_depth', 'upper_soil_depth', 'last_update', 'modified_by']

    class Meta:
        model = ResearchExperimentUnit


admin.site.register(TreatmentResearch, TreatmentResearchModelAdmin)
admin.site.register(ControlResearch, ControlResearchModelAdmin)
admin.site.register(ExperimentDetails, ExperimentDetailsModelAdmin)
admin.site.register(NitrogenApplied, NitrogenAppliedModelAdmin)
admin.site.register(ExperimentRep, ExperimentRepModelAdmin)
admin.site.register(ExperimentDuration, ExperimentDurationModelAdmin)
admin.site.register(MeasurementYear, MeasurementYearModelAdmin)
admin.site.register(MeasurementSeason, MeasurementSeasonModelAdmin)
admin.site.register(Author, AuthorModelAdmin)
admin.site.register(Species, SpeciesModelAdmin)
admin.site.register(ExperimentUnitCategory, ExperimentUnitCategoryModelAdmin)
admin.site.register(ExperimentUnit, ExperimentUnitModelAdmin)
admin.site.register(ResearchExperimentUnit, ResearchExperimentUnitModelAdmin)
