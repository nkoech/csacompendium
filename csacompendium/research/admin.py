from django.contrib import admin

# Register your models here.
# from .models import (
#     ObjectCategory,
#     ExperimentObject,
#     ResearchObject,
#     # ResearchOutcomeIndicator,
#     # Species,
#     # ResearchSpecies,
#     # MeasurementSeason,
#     # MeasurementYear,
#     Research,
#     # Author,
# )


# class ResearchOutcomeIndicatorInline(admin.TabularInline):
#     """
#     Easy editing of research outcome indicator entry relations from the research entry page
#     """
#     model = ResearchOutcomeIndicator


# class ResearchSpeciesInline(admin.TabularInline):
#     """
#     Easy editing of research species entry relations from the research entry page
#     """
#     model = ResearchSpecies


# class ResearchModelAdmin(admin.ModelAdmin):
#     """
#     Location model admin settings
#     """
#     # list_display = ['author', 'research_year', 'last_update', 'modified_by']
#     list_display = ['research_year', 'last_update', 'modified_by']
#     # list_display_links = ['author']
#     list_display_links = ['research_year']
#     # list_filter = ['author', 'last_update', 'modified_by', 'research_year']
#     list_filter = ['last_update', 'modified_by', 'research_year']
#     # inlines = [ResearchSpeciesInline, ResearchOutcomeIndicatorInline, ]
#     # inlines = [ResearchOutcomeIndicatorInline, ]
#
#     class Meta:
#         model = Research


# class AuthorModelAdmin(admin.ModelAdmin):
#     """
#     Temperature model admin settings
#     """
#     list_display = ['author_code', 'first_name', 'middle_name', 'last_name', 'author_bio', 'last_update', 'modified_by']
#     list_display_links = ['first_name']
#     list_filter = ['author_code', 'first_name', 'last_name', 'last_update', 'modified_by']
#
#     class Meta:
#         model = Author


# class MeasurementYearModelAdmin(admin.ModelAdmin):
#     """
#     Measurement year model admin settings
#     """
#     list_display = ['meas_year', 'measurementseason', 'last_update', 'modified_by']
#     list_display_links = ['meas_year']
#     list_filter = ['measurementseason', 'last_update', 'modified_by', 'meas_year']
#
#     class Meta:
#         model = MeasurementYear


# class MeasurementSeasonModelAdmin(admin.ModelAdmin):
#     """
#     Measurement season model admin settings
#     """
#     list_display = ['meas_season', 'last_update', 'modified_by']
#     list_display_links = ['meas_season']
#     list_filter = ['meas_season', 'last_update', 'modified_by']
#
#     class Meta:
#         model = MeasurementSeason


# class SpeciesModelAdmin(admin.ModelAdmin):
#     """
#     Species model admin settings
#     """
#     list_display = ['species', 'last_update', 'modified_by']
#     list_display_links = ['species']
#     list_filter = ['species', 'last_update', 'modified_by']
#
#     class Meta:
#         model = Species


# class ObjectCategoryModelAdmin(admin.ModelAdmin):
#     """
#     Object Category model admin settings
#     """
#     list_display = ['object_category', 'last_update', 'modified_by']
#     list_display_links = ['object_category']
#     list_filter = ['object_category', 'last_update', 'modified_by']
#
#     class Meta:
#         model = ObjectCategory
#
#
# class ExperimentObjectModelAdmin(admin.ModelAdmin):
#     """
#     Experiment object model admin settings
#     """
#     list_display = ['exp_object_code', 'objectcategory', 'object_name', 'latin_name', 'last_update', 'modified_by']
#     list_display_links = ['object_name']
#     list_filter = ['object_name', 'exp_object_code', 'objectcategory', 'last_update', 'modified_by']
#
#     class Meta:
#         model = ExperimentObject
#
#
# class ResearchObjectModelAdmin(admin.ModelAdmin):
#     """
#     Research object model admin settings
#     """
#     list_display = ['experimentobject', 'upper_soil_depth', 'upper_soil_depth', 'last_update', 'modified_by']
#     list_display_links = ['experimentobject']
#     list_filter = ['experimentobject', 'upper_soil_depth', 'upper_soil_depth', 'last_update', 'modified_by']
#
#     class Meta:
#         model = ResearchObject
#
# admin.site.register(Research, ResearchModelAdmin)
# # admin.site.register(Author, AuthorModelAdmin)
# # admin.site.register(MeasurementYear, MeasurementYearModelAdmin)
# # admin.site.register(MeasurementSeason, MeasurementSeasonModelAdmin)
# # admin.site.register(Species, SpeciesModelAdmin)
# admin.site.register(ObjectCategory, ObjectCategoryModelAdmin)
# admin.site.register(ExperimentObject, ExperimentObjectModelAdmin)
# admin.site.register(ResearchObject, ResearchObjectModelAdmin)
