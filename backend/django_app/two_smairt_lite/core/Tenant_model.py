from django.db import models
from utils.mixins import MixinsModel


class Tenant(MixinsModel):
    tenant_id = models.BigAutoField(
        primary_key=True,
        db_column='tenant_id',
        verbose_name='Tenant ID'
    )

    tenant_code = models.CharField(
        max_length=20,
        unique=True,
        db_column='tenant_code',
        verbose_name='Tenant Code',
        help_text='Unique system identifier for the tenant'
    )

    tenant_name = models.CharField(
        max_length=255,
        db_column='tenant_name',
        verbose_name='Tenant Name'
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
        db_table = 'tenant'
        app_label = 'core'
        verbose_name_plural = 'Tenants'
        ordering = ['tenant_code']
        indexes = [
            models.Index(fields=['tenant_code'], name='idx_tenant_code'),
        ]

    def __str__(self):
        return f"{self.tenant_code} - {self.tenant_name}"

    def __repr__(self):
        return f"<Tenant {self.tenant_code}>"

    def __label__(self):
        return f"{self.tenant_code} - {self.tenant_name}"
