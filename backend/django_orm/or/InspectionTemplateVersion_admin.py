from django.contrib import admin
from .InspectionTemplateVersion_model import InspectionTemplateVersion
from .InspectionTemplateItem_model import InspectionTemplateItem

class InspectionTemplateItemInline(admin.TabularInline):
    model = InspectionTemplateItem
    fk_name = 'inspection_template_version_id'
    extra = 0
    fields = (
        'item_code',
        'item_prompt',
        'item_type',
    )
    ordering = ('item_code',)

@admin.register(InspectionTemplateVersion)
class InspectionTemplateVersionAdmin(admin.ModelAdmin):
    list_display = (
        'inspection_template_id',
        'version_code',
        'is_published',
    )
    list_filter = (
        'is_published',
    )
    ordering = (
        'inspection_template_id',
        'version_code',
    )

    fields = (
        'inspection_template_id',
        'version_code',
        'is_published',
    )

    inlines = [InspectionTemplateItemInline]

