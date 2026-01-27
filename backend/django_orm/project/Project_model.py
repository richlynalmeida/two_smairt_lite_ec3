from django.db import models
from utils.mixins import MixinsModel
#
# class Project(MixinsModel):
#     project_id = models.BigAutoField(primary_key=True, db_column='project_id', verbose_name='Project  ID')
#
#     project_code  = models.CharField(max_length=32, db_column='project_code', verbose_name='Project Code', unique=True)
#     project_title = models.CharField(max_length=255, db_column='project_title', verbose_name='Project Title')
#     venue         = models.CharField(max_length=255, db_column='venue', verbose_name='Project Venue')
#     comments      = models.CharField(max_length=2000, db_column='comments', verbose_name='Comments', blank=True, null=True)
#
#     company_item_id = models.ForeignKey(
#         'core.CompanyItem', on_delete=models.RESTRICT,
#         db_column='company_item_id', related_name='ci_j_pi',
#         verbose_name='Owning Company', db_index=False,   # explicit idx below
#     )
#
#     calendar_set_id = models.ForeignKey(
#         'core.CalendarSet', on_delete=models.RESTRICT,
#         db_column='calendar_set_id', related_name='cs_j_pi',
#         verbose_name='Calendar Set', db_index=False,     # explicit idx below (composite)
#     )
#
#     project_status_type_id = models.ForeignKey(
#         'project.ProjectStatusType', on_delete=models.RESTRICT,
#         db_column='project_status_type_id', related_name='pst_j_pi',
#         verbose_name='Project Status Type', blank=True, null=True, db_index=False,  # explicit idx below
#     )
#
#     base_currency_code = models.CharField(max_length=3, db_column='base_currency_code', verbose_name='Base Currency (ISO3)', default='USD')
#
#     start_date  = models.DateField(db_column='start_date',  verbose_name='Start Date')
#     finish_date = models.DateField(db_column='finish_date', verbose_name='Finish Date')
#     baseline_start_date  = models.DateField(db_column='baseline_start_date',  verbose_name='Baseline Start',  blank=True, null=True)
#     baseline_finish_date = models.DateField(db_column='baseline_finish_date', verbose_name='Baseline Finish', blank=True, null=True)
#
#     IS_DEFAULT_CHOICES = [('Y','Y'),('N','N')]
#     is_default = models.CharField(max_length=1, choices=IS_DEFAULT_CHOICES, default='Y', db_column='is_default', verbose_name='Is Default Check')
#
#     class Meta:
#         managed = True
#         db_table = 'project'
#         app_label = 'project'
#         verbose_name_plural = 'Project'
#         ordering = ['project_code']
#
#     def __str__(self):
#         return f"{self.project_code} - {self.project_title}"
#
#     def __repr__(self):
#         return f"<Project {self.project_code} - {self.project_title}>"
#
#     def __label__(self):
#         return f"{self.project_code} - {self.project_title}"
class Project(MixinsModel):
    project_id = models.BigAutoField(primary_key=True)

    project_code  = models.CharField(max_length=32, unique=True)
    project_title = models.CharField(max_length=255)
    venue         = models.CharField(max_length=255)
    comments      = models.CharField(max_length=2000, blank=True, null=True)

    IS_ACTIVE_CHOICES = [('Y', 'Y'), ('N', 'N')]
    is_active = models.CharField(
        max_length=1,
        choices=IS_ACTIVE_CHOICES,
        default='Y',
        db_column='is_active',
        verbose_name='Is Active Check'
    )

    start_date  = models.DateField()
    finish_date = models.DateField()

    class Meta:
        managed = True
        db_table = 'project'
        app_label = 'project'
        verbose_name_plural = 'Project'
        ordering = ['project_code']

    def __str__(self):
        return f"{self.project_code} – {self.project_title}"
