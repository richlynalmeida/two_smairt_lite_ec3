
from django.contrib import admin
from .InspectionEvidence_model import InspectionEvidence


@admin.register(InspectionEvidence)
class InspectionEvidenceAdmin(admin.ModelAdmin):
    """
    Browse/debug only.
    Evidence should normally be added via InspectionItemResult.
    """

    list_display = (
        'inspection_evidence_id',
        'inspection_item_result_id',
        'evidence_type_code',
    )

    list_filter = (
        'evidence_type_code',
    )

    ordering = (
        'inspection_evidence_id',
    )

    readonly_fields = (
        'inspection_item_result_id',
        'evidence_type_code',
        'file_path',
        'comments',
    )
