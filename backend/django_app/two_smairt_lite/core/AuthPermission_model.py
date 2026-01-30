from django.db import models
from utils.mixins import MixinsModel

class AuthPermission(models.Model):
    auth_permission_id = models.AutoField(primary_key=True, db_column='id', verbose_name='Authorised Permission ID')
    auth_permission_name = models.CharField(max_length=255, db_column='name', verbose_name='Authorised Permission Name' )
    content_type_id = models.ForeignKey('core.DjangoContentType', on_delete=models.RESTRICT,
        db_column='content_type_id', related_name='dct_j_ap',
                                     verbose_name='Django Content Type ID', db_index=False)
    codename = models.CharField(max_length=100, verbose_name='Codename', db_column='codename')

    class Meta:
        db_table = 'auth_permission'
        app_label = 'core'
        managed = False
        verbose_name_plural = "User Management / C / Authorised Permissions"
        unique_together = (('content_type_id', 'codename'),)

    def __str__(self): return self.auth_permission_id

    def __label__(self): return f"{self.auth_permission_id} – {self.auth_permission_name}"

    def __repr__(self):
        return "<AuthPermission {}>".format(
            f"{self.auth_permission_id} - {self.auth_permission_name}")