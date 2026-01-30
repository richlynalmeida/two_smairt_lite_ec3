from django.db import models
from django.conf import settings
from utils.mixins import MixinsModel


class InspectionTemplateVersion(MixinsModel):
    inspection_template_version_id = models.AutoField(
        primary_key=True,
        verbose_name='Inspection Template Version ID'
    )

    # NOTE: FK name intentionally ends with _id (by design)
    inspection_template_id = models.ForeignKey(
        'or.InspectionTemplate',
        on_delete=models.RESTRICT,
        db_column='inspection_template_id',
        related_name='it_j_itv',
        verbose_name='Inspection Template'
    )

    version_code = models.CharField(
        max_length=20,
        verbose_name='Version Code'
    )

    is_published = models.BooleanField(
        default=False,
        verbose_name='Is Published'
    )

    class Meta:
        managed = True
        db_table = 'inspection_template_version'
        app_label = 'or'
        unique_together = ('inspection_template_id', 'version_code')
        verbose_name_plural = "B | 02 | Inspection Template Versions"
        ordering = ['inspection_template_id', 'version_code']

    # ---------- SAFE STRING METHODS ----------

    def __str__(self):
        """
        Defensive: FK may not be hydrated (admin, PLAHO rows, queryset optimizations)
        """
        if hasattr(self, 'inspection_template_id') and self.inspection_template_id:
            return f"{self.inspection_template_id.inspection_template_code} v{self.version_code}"
        return f"Template v{self.version_code}"

    def __repr__(self):
        return f"<InspectionTemplateVersion id={self.inspection_template_version_id} v={self.version_code}>"

    def __label__(self):
        if hasattr(self, 'inspection_template_id') and self.inspection_template_id:
            return f"{self.inspection_template_id.inspection_template_code} v{self.version_code}"
        return f"Template v{self.version_code}"
