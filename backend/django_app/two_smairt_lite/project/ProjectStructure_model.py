from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from utils.mixins import MixinsModel


class ProjectStructure(MixinsModel):
    project_structure_id = models.BigAutoField(
        primary_key=True,
        db_column='project_structure_id',
        verbose_name='Project Structure ID'
    )

    project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE,
        db_column='project_id',
        related_name='structures',
        verbose_name='Project'
    )

    parent_project_structure = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        db_column='parent_project_structure_id',
        related_name='children',
        verbose_name='Parent Structure Node',
        blank=True,
        null=True
    )

    structure_code = models.CharField(
        max_length=50,
        db_column='structure_code',
        verbose_name='Structure Code'
    )

    structure_title = models.CharField(
        max_length=255,
        db_column='structure_title',
        verbose_name='Structure Title'
    )

    structure_level = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(6)],
        db_column='structure_level',
        verbose_name='Structure Level (1–6)'
    )

    STRUCTURE_ROLE_CHOICES = [
        ('SPATIAL', 'Spatial – grouping by physical location or layout'),
        ('SYSTEMIC', 'Systemic – grouping by system relationships'),
        ('PROCESS', 'Process – grouping by execution or workflow logic'),
        ('PRESENTATION', 'Presentation – grouping for views, dashboards, or rollups'),
        ('TRANSIENT', 'Transient – grouping intended to be temporary or non-persistent'),
    ]

    structure_role = models.CharField(
        max_length=20,
        choices=STRUCTURE_ROLE_CHOICES,
        default='SPATIAL',
        db_column='structure_role',
        verbose_name='Structure Role',
        help_text=(
            'Defines the lens used to organise the project structure. '
            'This describes how information is grouped for understanding or navigation, '
            'not physical assets, disciplines, or project phases.'
        )
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
        verbose_name='Is Active'
    )

    sort_order = models.PositiveIntegerField(
        default=0,
        db_column='sort_order',
        verbose_name='Sort Order'
    )

    class Meta:
        managed = True
        db_table = 'project_structure'
        app_label = 'project'
        verbose_name_plural = 'Project Structures'
        ordering = ['project_id', 'structure_level', 'sort_order', 'structure_code']
        unique_together = (
            ('project', 'parent_project_structure', 'structure_code'),
        )
        indexes = [
            models.Index(fields=['project'], name='idx_ps_project'),
            models.Index(fields=['parent_project_structure'], name='idx_ps_parent'),
            models.Index(fields=['project', 'structure_level'], name='idx_ps_project_level'),
            models.Index(fields=['project', 'structure_role'], name='idx_ps_project_role'),
        ]

    def __str__(self):
        return f"{self.structure_code} – {self.structure_title}"

    def __repr__(self):
        return f"<ProjectStructure {self.structure_code} (L{self.structure_level})>"

    def __label__(self):
        return f"{self.structure_code} – {self.structure_title}"
