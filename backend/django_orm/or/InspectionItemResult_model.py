from django.db import models
from utils.mixins import MixinsModel


class InspectionItemResult(MixinsModel):
    inspection_item_result_id = models.AutoField(
        primary_key=True,
        verbose_name='Inspection Item Result ID'
    )

    # FK names intentionally end with _id
    inspection_id = models.ForeignKey(
        'or.Inspection',
        on_delete=models.RESTRICT,
        db_column='inspection_id',
        related_name='i_j_iir',
        verbose_name='Inspection'
    )

    inspection_template_item_id = models.ForeignKey(
        'or.InspectionTemplateItem',
        on_delete=models.RESTRICT,
        db_column='inspection_template_item_id',
        related_name='iti_j_iir',
        verbose_name='Inspection Template Item'
    )

    result_code = models.CharField(
        max_length=10,
        verbose_name='Result Code'
    )

    measured_value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name='Measured Value'
    )

    comments = models.CharField(
        max_length=2000,
        blank=True,
        null=True,
        verbose_name='Comments'
    )

    class Meta:
        managed = True
        db_table = 'inspection_item_result'
        app_label = 'or'
        verbose_name_plural = "D | 01 | Inspection Item Results"
        ordering = ['inspection_item_result_id']

    # ---------- SAFE STRING METHODS ----------

    def __str__(self):
        if hasattr(self, 'inspection_template_item_id') and self.inspection_template_item_id:
            return f"{self.inspection_template_item_id.item_code} - {self.result_code}"
        return f"Result {self.inspection_item_result_id} - {self.result_code}"

    def __repr__(self):
        return f"<InspectionItemResult id={self.inspection_item_result_id} result={self.result_code}>"

    def __label__(self):
        if hasattr(self, 'inspection_template_item_id') and self.inspection_template_item_id:
            return f"{self.inspection_template_item_id.item_code} → {self.result_code}"
        return f"Result {self.inspection_item_result_id} → {self.result_code}"
