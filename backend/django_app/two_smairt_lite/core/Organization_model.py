from django.db import models
from utils.mixins import MixinsModel


class Organization(MixinsModel):
    organization_id = models.BigAutoField(
        primary_key=True,
        db_column='organization_id',
        verbose_name='Organization ID'
    )

    tenant_id = models.ForeignKey(
        'core.Tenant',
        on_delete=models.CASCADE,
        db_column='tenant_id',
        related_name='tenant_j_org',
        verbose_name='Tenant'
    )

    company_item_id = models.ForeignKey(
        'core.CompanyItem',
        on_delete=models.RESTRICT,
        db_column='company_item_id',
        related_name='ci_j_org',
        verbose_name='Company'
    )

    organization_code = models.CharField(
        max_length=20,
        db_column='organization_code',
        verbose_name='Organization Code',
        help_text='Tenant-scoped organization identifier'
    )

    IS_ACTIVE_CHOICES = [('Y', 'Y'), ('N', 'N')]
    is_active = models.CharField(
        max_length=1,
        choices=IS_ACTIVE_CHOICES,
        default='Y',
        db_column='is_active',
        verbose_name='Is Active'
    )

    comments = models.CharField(
        max_length=2000,
        blank=True,
        null=True,
        db_column='comments',
        verbose_name='Comments'
    )

    class Meta:
        managed = True
        db_table = 'organization'
        app_label = 'core'
        verbose_name_plural = 'Organizations'
        ordering = ['tenant_id', 'organization_code']
        unique_together = (
            ('tenant_id', 'organization_code'),
            ('tenant_id', 'company_item_id'),
        )
        indexes = [
            models.Index(fields=['tenant_id'], name='idx_org_tenant'),
            models.Index(fields=['company_item_id'], name='idx_org_company'),
        ]

    def __str__(self):
        return f"{self.organization_code} ({self.company_item_id.company_item_title})"

    def __repr__(self):
        return f"<Organization {self.organization_code}>"

    def __label__(self):
        return f"{self.organization_code} - {self.company_item_id.company_item_title}"
