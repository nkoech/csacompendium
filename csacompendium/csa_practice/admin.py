from django.contrib import admin

# Register your models here.
from .models import (
    CsaPractice,
    ResearchCsaPractice,
    CsaTheme,
    PracticeLevel,
    PracticeType,
)


class ResearchCsaPracticeInline(admin.TabularInline):
    """
    Inline for easy editing of in the admin in relation to the CSA practices admin
    """
    model = ResearchCsaPractice


class CsaPracticeModelAdmin(admin.ModelAdmin):
    """
    CSA practice model admin settings
    """
    list_display = [
        'practice_code', 'csatheme', 'practicelevel', 'sub_practice_level',
        'sub_subpractice_level', 'last_update', 'modified_by'
    ]
    list_display_links = ['practice_code']
    list_filter = ['csatheme', 'practicelevel', 'sub_practice_level', 'last_update', 'modified_by']
    inlines = [ResearchCsaPracticeInline, ]

    class Meta:
        model = CsaPractice


class CsaThemeModelAdmin(admin.ModelAdmin):
    """
    CSA theme model admin settings
    """
    list_display = ['csa_theme', 'last_update', 'modified_by']
    list_display_links = ['csa_theme']
    list_filter = ['csa_theme', 'last_update', 'modified_by']

    class Meta:
        model = CsaTheme


class PracticeLevelModelAdmin(admin.ModelAdmin):
    """
    CSA practice level model admin settings
    """
    list_display = ['practice_level', 'last_update', 'modified_by']
    list_display_links = ['practice_level']
    list_filter = ['practice_level', 'last_update', 'modified_by']

    class Meta:
        model = PracticeLevel


class PracticeTypeModelAdmin(admin.ModelAdmin):
    """
    CSA practice type model admin settings
    """
    list_display = ['practice_type', 'last_update', 'modified_by']
    list_display_links = ['practice_type']
    list_filter = ['practice_type', 'last_update', 'modified_by']

    class Meta:
        model = PracticeType

admin.site.register(CsaPractice, CsaPracticeModelAdmin)
admin.site.register(CsaTheme, CsaThemeModelAdmin)
admin.site.register(PracticeLevel, PracticeLevelModelAdmin)
admin.site.register(PracticeType, PracticeTypeModelAdmin)
