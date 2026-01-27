import uuid
from django.conf import settings
from django.db import models
from django.utils.timezone import now


class MixinsModel(models.Model):
    created_at = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="created_%(class)s_set",
        db_column="created_by_id"
    )

    updated_at = models.DateField(null=True, blank=True)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="updated_%(class)s_set",
        db_column="updated_by_id"
    )

    IS_DELETED_CHOICES = [('Y', 'Y'), ('N', 'N')]
    is_deleted = models.CharField(
        max_length=1,
        choices=IS_DELETED_CHOICES,
        default='N',
        db_column='is_deleted',
        verbose_name='Soft Delete Check'
    )
    deleted_at = models.DateField(null=True, blank=True)
    deleted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="deleted_%(class)s_set",
        db_column="deleted_by_id"
    )

    IS_ACTIVE_CHOICES = [('Y', 'Y'), ('N', 'N')]
    is_active = models.CharField(
        max_length=1,
        choices=IS_ACTIVE_CHOICES,
        default='Y',
        db_column='is_active',
        verbose_name='Active Check'
    )

    uuid = models.UUIDField(
        editable=False,
        null=True,
        blank=True,
        unique=True,
        default=uuid.uuid4
    )

    class Meta:
        abstract = True
        get_latest_by = "updated_at"

    def save(self, *args, **kwargs):
        timestamp = now().replace(microsecond=0)

        if not self.created_at:
            self.created_at = timestamp
        self.updated_at = timestamp

        # If soft-deleted and deleted_at exists, ensure it's truncated too
        if self.is_deleted == 'Y' and self.deleted_at:
            self.deleted_at = self.deleted_at.replace(microsecond=0)
        elif self.is_deleted == 'Y' and not self.deleted_at:
            self.deleted_at = timestamp

        super().save(*args, **kwargs)

    def soft_delete(self, user=None):
        self.is_deleted = 'Y'
        self.deleted_at = now().replace(microsecond=0)
        if user:
            self.deleted_by = user
        self.save()

    def undelete(self):
        self.is_deleted = 'N'
        self.deleted_at = None
        self.deleted_by = None
        self.save()
