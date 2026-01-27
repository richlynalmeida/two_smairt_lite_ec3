from django.db import models
# from django.core.validators import MinValueValidator, MaxValueValidator
from utils.mixins import MixinsModel


class ProjectAsset(MixinsModel):
    project_asset_id = models.BigAutoField(
        primary_key=True,
        db_column='project_asset_id',
        verbose_name='Project Asset ID'
    )

    project_id = models.CharField(
        max_length=5,
        db_column='project_id',
        verbose_name='Project ID'
    )

    asset_code = models.CharField(
        max_length=64,
        db_column='asset_code',
        verbose_name='Asset Code'
    )

    asset_title = models.CharField(
        max_length=255,
        db_column='asset_title',
        verbose_name='Asset Title'
    )

    asset_role_code = models.CharField(
        max_length=32,
        db_column='asset_role_code',
        verbose_name='Asset Role Code',
        help_text='E.g. COMM, INSPECT, OPERATE'
    )

    ASSET_ORIGIN_CHOICES = [
        ('QUANTUM', 'From Quantum'),
        ('DIRECT', 'Direct / Discovery'),
    ]
    asset_origin = models.CharField(
        max_length=16,
        choices=ASSET_ORIGIN_CHOICES,
        default='QUANTUM',
        db_column='asset_origin',
        verbose_name='Asset Origin'
    )

    ASSET_STATUS_CHOICES = [
        ('PLANNED', 'Planned'),
        ('INSTALLED', 'Installed'),
        ('UNDER_TEST', 'Under Test'),
        ('COMPLETED', 'Completed'),
        ('ACCEPTED', 'Accepted'),
    ]
    asset_status = models.CharField(
        max_length=16,
        choices=ASSET_STATUS_CHOICES,
        default='PLANNED',
        db_column='asset_status',
        verbose_name='Asset Status'
    )

    comments = models.CharField(
        max_length=2000,
        db_column='comments',
        verbose_name='Comments',
        blank=True,
        null=True
    )

    IS_ACTIVE_CHOICES = [('Y', 'Y'), ('N', 'N')]
    is_active = models.CharField(
        max_length=1,
        choices=IS_ACTIVE_CHOICES,
        default='Y',
        db_column='is_active',
        verbose_name='Is Active Check'
    )

    class Meta:
        managed = True
        db_table = 'project_asset'
        app_label = 'or'
        verbose_name_plural = 'A | Project Assets'
        ordering = ['project_id', 'asset_code']
        unique_together = (
            ('project_id', 'asset_code'),
        )