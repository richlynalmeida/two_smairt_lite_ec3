
from django.contrib import admin
from .InspectionItemResult_model import InspectionItemResult
from .InspectionEvidence_model import InspectionEvidence

class InspectionEvidenceInline(admin.TabularInline):
    model = InspectionEvidence
    fk_name = 'inspection_item_result_id'
    extra = 0
    fields = (
        'evidence_type_code',
        'file_path',
        'comments',
    )
@admin.register(InspectionItemResult)
class InspectionItemResultAdmin(admin.ModelAdmin):
    """
    Browse/debug only.
    Evidence may be added here if needed.
    """

    list_display = (
        'inspection_item_result_id',
        'inspection_id',
        'inspection_template_item_id',
        'result_code',
    )

    list_filter = (
        'result_code',
    )

    ordering = (
        'inspection_item_result_id',
    )

    readonly_fields = (
        'inspection_id',
        'inspection_template_item_id',
        'result_code',
        'measured_value',
        'comments',
    )

    inlines = [InspectionEvidenceInline]
