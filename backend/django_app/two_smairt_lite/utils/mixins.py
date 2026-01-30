# backend/django_orm/utils/mixins.py
from django.db import models
from django.utils.timezone import now


class MixinsModel(models.Model):
    """
    Base mixin for all 2SMAiRT models (Access-friendly).

    • Uses DateField (not DateTime)
    • Uses 'Y'/'N' flags instead of booleans
    • Supports soft delete via is_deleted / deleted_at
    • All dates nullable for seed flexibility
    """

    # --- Audit dates (optional)
    created_at = models.DateField(null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)

    # --- Soft delete controls
    IS_DELETED_CHOICES = [('Y', 'Y'), ('N', 'N')]
    is_deleted = models.CharField(
        max_length=1,
        choices=[('Y', 'Y'), ('N', 'N')],
        default='N',  # app-level default
        db_column='is_deleted',
        verbose_name='Soft Delete Check',
    )
    deleted_at = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True
        get_latest_by = 'updated_at'

    # --- Soft delete methods (explicit, lightweight)
    def soft_delete(self):
        self.is_deleted = 'Y'
        self.deleted_at = now().date()
        self.save(update_fields=['is_deleted', 'deleted_at'])

    def undelete(self):
        self.is_deleted = 'N'
        self.deleted_at = None
        self.save(update_fields=['is_deleted', 'deleted_at'])
