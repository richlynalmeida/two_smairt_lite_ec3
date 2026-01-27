from django.db import models
from django.conf import settings
from utils.mixins import MixinsModel

class Inspection(MixinsModel):
    inspection_id = models.AutoField(
        primary_key=True,
        verbose_name='Inspection ID'
    )
    inspection_template_version_id = models.ForeignKey(
        'or.InspectionTemplateVersion',
        on_delete=models.RESTRICT,
        db_column='inspection_template_version_id',
        related_name='itv_j_i',
        verbose_name='Inspection Template Version'
    )
    inspected_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name='Inspected By'
    )
    inspection_date = models.DateField(
        verbose_name='Inspection Date'
    )
    location = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Location'
    )

    class Meta:
        managed = True
        db_table = 'inspection'
        app_label = 'or'
        verbose_name_plural = "C | Inspections"
        ordering = ['inspection_date']

    def __str__(self):
        return f"Inspection {self.inspection_id}"

    def __repr__(self):
        return f"<Inspection {self.inspection_id}>"

    def __label__(self):
        return f"Inspection {self.inspection_id}"

