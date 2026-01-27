from django.db import models
from django.conf import settings
from utils.mixins import MixinsModel

class InspectionEvidence(MixinsModel):
    inspection_evidence_id = models.AutoField(
        primary_key=True,
        verbose_name='Inspection Evidence ID'
    )
    inspection_item_result_id = models.ForeignKey(
        'or.InspectionItemResult',
        on_delete=models.RESTRICT,
        db_column='inspection_item_result_id',
        related_name='iir_j_ie',
        verbose_name='Inspection Item Result'
    )
    evidence_type_code = models.CharField(
        max_length=20,
        verbose_name='Evidence Type Code'
    )
    file_path = models.FileField(
        upload_to='inspection_evidence/',
        blank=True,
        null=True,
        verbose_name='File'
    )
    comments = models.CharField(
        max_length=2000,
        blank=True,
        null=True,
        verbose_name='Comments'
    )

    class Meta:
        managed = True
        db_table = 'inspection_evidence'
        app_label = 'or'
        verbose_name_plural = "D | 02 | Inspection Evidence"
        ordering = ['inspection_evidence_id']

    def __str__(self):
        return f"Evidence {self.inspection_evidence_id}"

    def __repr__(self):
        return f"<InspectionEvidence {self.inspection_evidence_id}>"

    def __label__(self):
        return f"Evidence {self.inspection_evidence_id}"


