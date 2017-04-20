from django.contrib import admin

# Register your models here.
from .models import (
    NitrogenApplied,
    MeasurementSeason,
    MeasurementYear,
    ExperimentDescription,
    ResearchExperimentDescription,
    ExperimentReplicate,
    ResearchExperimentReplicate,
    Author,
    Journal,
    ResearchAuthor,
    Research,
    ExperimentUnitCategory,
    ExperimentUnit,
    Breed,
    ResearchExperimentUnit,
)


class ResearchModelAdmin(admin.ModelAdmin):
    """
    Research model admin settings
    """
    list_display = [
        'experiment_design', 'nitrogenapplied', 'last_update', 'modified_by'
    ]
    list_display_links = ['experiment_design']
    list_filter = [
        'experiment_design', 'nitrogenapplied', 'last_update', 'modified_by'
    ]

    class Meta:
        model = Research


class NitrogenAppliedModelAdmin(admin.ModelAdmin):
    """
    Nitrogen applied model admin settings
    """
    list_display = ['nitrogen_amount', 'amount_uom', 'nitrogen_source', 'last_update', 'modified_by']
    list_display_links = ['nitrogen_amount']
    list_filter = ['nitrogen_amount', 'amount_uom', 'nitrogen_source', 'last_update', 'modified_by']

    class Meta:
        model = NitrogenApplied


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


class ResearchExperimentDescriptionInline(admin.TabularInline):
    """
    Easy editing of research experiment description entry relations from
    the experiment description entry page
    """
    model = ResearchExperimentDescription


class ExperimentDescriptionModelAdmin(admin.ModelAdmin):
    """
    Experiment description model admin settings
    """
    list_display = ['experiment_description', 'last_update', 'modified_by']
    list_display_links = ['experiment_description']
    list_filter = ['experiment_description', 'last_update', 'modified_by']
    inlines = [ResearchExperimentDescriptionInline, ]

    class Meta:
        model = ExperimentReplicate


class ResearchExperimentReplicateInline(admin.TabularInline):
    """
    Easy editing of research experiment replicate entry relations from
    the experiment replicate entry page
    """
    model = ResearchExperimentReplicate


class ExperimentReplicateModelAdmin(admin.ModelAdmin):
    """
    Experiment replicate model admin settings
    """
    list_display = ['no_replicate', 'last_update', 'modified_by']
    list_display_links = ['no_replicate']
    list_filter = ['no_replicate', 'last_update', 'modified_by']
    inlines = [ResearchExperimentReplicateInline, ]

    class Meta:
        model = ExperimentReplicate


class JournalModelAdmin(admin.ModelAdmin):
    """
    Journal model admin settings
    """
    list_display = ['journal_tag', 'publication_year', 'last_update', 'modified_by']
    list_display_links = ['journal_tag']
    list_filter = ['journal_tag', 'publication_year', 'last_update', 'modified_by']

    class Meta:
        model = Journal


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


class ExperimentUnitCategoryModelAdmin(admin.ModelAdmin):
    """
    Experiment unit category model admin settings
    """
    list_display = ['unit_category', 'last_update', 'modified_by']
    list_display_links = ['unit_category']
    list_filter = ['unit_category', 'last_update', 'modified_by']

    class Meta:
        model = ExperimentUnitCategory


class BreedModelAdmin(admin.ModelAdmin):
    """
    Breed model admin settings
    """
    list_display = ['breed', 'last_update', 'modified_by']
    list_display_links = ['breed']
    list_filter = ['breed', 'last_update', 'modified_by']

    class Meta:
        model = Breed


class ResearchExperimentUnitInline(admin.TabularInline):
    """
    Easy editing of research experiment unit entry relations from the experiment unit entry page
    """
    model = ResearchExperimentUnit


class ExperimentUnitModelAdmin(admin.ModelAdmin):
    """
    Experiment unit model admin settings
    """
    list_display = [
        'exp_unit_code', 'experimentunitcategory', 'common_name', 'latin_name', 'last_update', 'modified_by'
    ]
    list_display_links = ['common_name']
    list_filter = ['common_name', 'exp_unit_code', 'experimentunitcategory', 'last_update', 'modified_by']
    inlines = [ResearchExperimentUnitInline, ]

    class Meta:
        model = ExperimentUnit

admin.site.register(Research, ResearchModelAdmin)
admin.site.register(NitrogenApplied, NitrogenAppliedModelAdmin)
admin.site.register(MeasurementYear, MeasurementYearModelAdmin)
admin.site.register(MeasurementSeason, MeasurementSeasonModelAdmin)
admin.site.register(ExperimentDescription, ExperimentDescriptionModelAdmin)
admin.site.register(ExperimentReplicate, ExperimentReplicateModelAdmin)
admin.site.register(Journal, JournalModelAdmin)
admin.site.register(Author, AuthorModelAdmin)
admin.site.register(ExperimentUnitCategory, ExperimentUnitCategoryModelAdmin)
admin.site.register(Breed, BreedModelAdmin)
admin.site.register(ExperimentUnit, ExperimentUnitModelAdmin)
