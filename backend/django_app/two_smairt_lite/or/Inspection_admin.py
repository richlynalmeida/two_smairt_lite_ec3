from django.contrib import admin
from .Inspection_model import Inspection
from .InspectionItemResult_model import InspectionItemResult

class InspectionItemResultInline(admin.TabularInline):
    model = InspectionItemResult
    fk_name = 'inspection_id'
    extra = 0

    fields = (
        'inspection_template_item_id',
        'result_code',
        'measured_value',
        'comments',
    )

    ordering = ('inspection_item_result_id',)

    # Optional safety: prevent changing the question mid-inspection
    readonly_fields = (
        'inspection_template_item_id',
    )


@admin.register(Inspection)
class InspectionAdmin(admin.ModelAdmin):
    list_display = (
        'inspection_id',
        'inspection_template_version_id',
        'inspection_date',
        'inspected_by',
    )

    list_filter = (
        'inspection_template_version_id',
        'inspection_date',
    )

    ordering = ('inspection_date',)

    fields = (
        'inspection_template_version_id',
        'inspection_date',
        'inspected_by',
        'location',
    )

    inlines = [InspectionItemResultInline]
