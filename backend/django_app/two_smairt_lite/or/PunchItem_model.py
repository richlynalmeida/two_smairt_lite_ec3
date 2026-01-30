from django.db import models
from utils.mixins import MixinsModel


class PunchItem(MixinsModel):
    punch_item_id = models.BigAutoField(
        primary_key=True,
        db_column='punch_item_id',
        verbose_name='Punch Item ID'
    )

    project_id = models.CharField(
        max_length=5,
        db_column='project_id',
        verbose_name='Project ID'
    )

    project_asset_id = models.ForeignKey(
        'or.ProjectAsset',
        on_delete=models.CASCADE,
        db_column='project_asset_id',
        related_name='pa_j_punch_item',
        verbose_name='Project Asset',
        db_index=False,
    )

    inspection_id = models.ForeignKey(
        'or.Inspection',
        on_delete=models.SET_NULL,
        db_column='inspection_id',
        related_name='i_j_punch_item',
        verbose_name='Originating Inspection',
        blank=True,
        null=True,
        db_index=False,
    )

    PUNCH_CATEGORY_CHOICES = [
        ('A', 'Category A'),
        ('B', 'Category B'),
        ('C', 'Category C'),
        ('D', 'Category D'),
    ]
    punch_category = models.CharField(
        max_length=1,
        choices=PUNCH_CATEGORY_CHOICES,
        db_column='punch_category',
        verbose_name='Punch Category'
    )

    punch_code = models.CharField(
        max_length=64,
        db_column='punch_code',
        verbose_name='Punch Code'
    )

    punch_title = models.CharField(
        max_length=255,
        db_column='punch_title',
        verbose_name='Punch Title'
    )

    punch_description = models.CharField(
        max_length=2000,
        db_column='punch_description',
        verbose_name='Punch Description'
    )

    PUNCH_STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('READY_FOR_CLOSE', 'Ready for Close'),
        ('CLOSED', 'Closed'),
        ('ACCEPTED', 'Accepted'),
    ]
    punch_status = models.CharField(
        max_length=16,
        choices=PUNCH_STATUS_CHOICES,
        default='OPEN',
        db_column='punch_status',
        verbose_name='Punch Status'
    )

    raised_by = models.ForeignKey(
        'core.AuthUser',
        on_delete=models.SET_NULL,
        db_column='raised_by',
        related_name='au_j_pi',
        verbose_name='Raised By',
        blank=True,
        null=True,
    )

    raised_date = models.DateField(
        db_column='raised_date',
        verbose_name='Raised Date'
    )

    target_close_date = models.DateField(
        db_column='target_close_date',
        verbose_name='Target Close Date',
        blank=True,
        null=True
    )

    closed_date = models.DateField(
        db_column='closed_date',
        verbose_name='Closed Date',
        blank=True,
        null=True
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
        db_table = 'punch_item'
        app_label = 'or'
        verbose_name_plural = 'E | Punch Items'
        ordering = ['project_id', 'punch_category', 'punch_code']
        unique_together = (
            ('project_id', 'punch_code'),
        )

