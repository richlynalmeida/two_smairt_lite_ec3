from django.db import models
from django.conf import settings
from utils.mixins import MixinsModel


class InspectionTemplateItem(MixinsModel):
    inspection_template_item_id = models.AutoField(
        primary_key=True,
        verbose_name='Inspection Template Item ID'
    )
    inspection_template_version_id = models.ForeignKey(
        'or.InspectionTemplateVersion',
        on_delete=models.RESTRICT,
        db_column='inspection_template_version_id',
        related_name='itv_j_iti',
        verbose_name='Inspection Template Version'
    )
    item_code = models.CharField(
        max_length=50,
        verbose_name='Item Code'
    )
    item_prompt = models.CharField(
        max_length=500,
        verbose_name='Item Prompt'
    )
    item_type = models.CharField(
        max_length=20,
        verbose_name='Item Type'
    )

    class Meta:
        managed = True
        db_table = 'inspection_template_item'
        app_label = 'or'
        unique_together = ('inspection_template_version_id', 'item_code')
        verbose_name_plural = "C / Inspection Template Items"
        ordering = ['item_code']

    def __str__(self):
        return self.item_code

    def __repr__(self):
        return f"<InspectionTemplateItem {self.item_code}>"

    def __label__(self):
        return f"{self.item_code} - {self.item_prompt}"




