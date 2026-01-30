from django.db import models
from django.conf import settings
from utils.mixins import MixinsModel


class InspectionTemplate(MixinsModel):
    inspection_template_id = models.AutoField(
        primary_key=True,
        verbose_name='Inspection Template ID'
    )
    inspection_template_code = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Inspection Template Code'
    )
    inspection_template_title = models.CharField(
        max_length=255,
        verbose_name='Inspection Template Title'
    )
    description = models.CharField(
        max_length=2000,
        blank=True,
        null=True,
        verbose_name='Description'
    )

    class Meta:
        managed = True
        db_table = 'inspection_template'
        app_label = 'or'
        verbose_name_plural = "B | 01 | Inspection Templates"
        ordering = ['inspection_template_code']

    def __str__(self):
        return f"{self.inspection_template_code}"

    def __repr__(self):
        return f"<InspectionTemplate {self.inspection_template_code}>"

    def __label__(self):
        return f"{self.inspection_template_code} - {self.inspection_template_title}"


