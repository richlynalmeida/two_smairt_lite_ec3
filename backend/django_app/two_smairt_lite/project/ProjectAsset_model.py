from django.db import models
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
        # related_name='project_j_pa',
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

    # Discipline is used ONLY for filtering and slicing in C&C
    DISCIPLINE_CHOICES = [
        ('ELEC', 'Electrical'),
        ('MECH', 'Mechanical'),
        ('INST', 'Instrumentation'),
        ('CIVIL', 'Civil'),
    ]

    discipline_code = models.CharField(
        max_length=16,
        choices=DISCIPLINE_CHOICES,
        db_column='discipline_code',
        verbose_name='Discipline',
    )

    # Only energized assets are tracked for C&C
    ASSET_TYPE_CHOICES = [
        ('CABLE', 'Cable'),
        ('EQUIP', 'Equipment'),
        ('INSTR', 'Instrument'),
    ]

    asset_type_code = models.CharField(
        max_length=16,
        choices=ASSET_TYPE_CHOICES,
        db_column='asset_type_code',
        verbose_name='Asset Type',
        help_text='Only energized assets are included for C&C.',
    )

    # Asset role defines WHY the asset exists in the system
    # Fixed to COMMISSIONING for EC3 / SA Power rollout
    ASSET_ROLE_CHOICES = [
        ('COMM', 'Commissioning'),
    ]

    asset_role_code = models.CharField(
        max_length=32,
        choices=ASSET_ROLE_CHOICES,
        default='COMM',
        db_column='asset_role_code',
        verbose_name='Asset Role Code',
        help_text='Lifecycle role of the asset. Fixed to COMM for this rollout.',
        editable=False
    )

    # Asset origin indicates how the asset was introduced into the system
    # Fixed to IMPORT for EC3 / SA Power rollout
    ASSET_ORIGIN_CHOICES = [
        ('IMPORT', 'Imported'),
    ]

    asset_origin = models.CharField(
        max_length=16,
        choices=ASSET_ORIGIN_CHOICES,
        default='IMPORT',
        db_column='asset_origin',
        verbose_name='Asset Origin',
        help_text='Origin of the asset record. Fixed to IMPORT for this rollout.',
        editable=False
    )

    # Asset status reflects high-level C&C state only
    # Detailed progress is derived from activities and punches
    ASSET_STATUS_CHOICES = [
        ('IDENTIFIED', 'Identified'),
        ('IN_PROGRESS', 'In Progress'),
        ('ACCEPTED', 'Accepted'),
    ]

    asset_status = models.CharField(
        max_length=32,
        choices=ASSET_STATUS_CHOICES,
        default='IDENTIFIED',
        db_column='asset_status',
        verbose_name='Asset Status',
        help_text='High-level commissioning status (C&C only).'
    )

    # Reference-only payload captured from external registers (e.g. IS Asset Register).
    # NOTE:
    # - Read-only by convention
    # - Not used for filtering, workflows, or C&C logic
    # - Stored purely as contextual reference
    source_reference = models.JSONField(
        db_column='source_reference',
        verbose_name='Source Reference (Read-Only)',
        blank=True,
        null=True,
        help_text='Original imported asset register data for reference only.'
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
