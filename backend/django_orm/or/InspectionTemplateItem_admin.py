
from django.contrib import admin
from .InspectionTemplateItem_model import InspectionTemplateItem
from .InspectionTemplateVersion_model import InspectionTemplateVersion


class InspectionTemplateVersionInline(admin.TabularInline):
    model = InspectionTemplateVersion
    fk_name = 'inspection_template_id'
    extra = 0
    fields = ('version_code', 'is_published')
    ordering = ('version_code',)


# @admin.register(InspectionTemplate)
class InspectionTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'inspection_template_code',
        'inspection_template_title',
    )
    search_fields = (
        'inspection_template_code',
        'inspection_template_title',
    )
    ordering = ('inspection_template_code',)

    fields = (
        'inspection_template_code',
        'inspection_template_title',
        'description',
    )

    inlines = [InspectionTemplateVersionInline]
