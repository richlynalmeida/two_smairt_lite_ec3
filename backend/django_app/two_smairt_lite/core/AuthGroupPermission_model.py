from django.db import models
from utils.mixins import MixinsModel


class AuthGroupPermission(models.Model):
    auth_group_permission_id = models.AutoField(primary_key=True, db_column='id', verbose_name='Authorised Group Permission ID')
    auth_group_id = models.ForeignKey('core.AuthGroup', on_delete=models.RESTRICT, db_column='group_id',
                              related_name='ag_j_agp', verbose_name='Authorised Group')
    permission_id = models.ForeignKey('core.AuthPermission', on_delete=models.RESTRICT, db_column='permission_id',
                              related_name='ap_j_agp', verbose_name='Permission ID')

    class Meta:
        db_table = 'auth_group_permissions'
        app_label = 'core'
        managed = False
        verbose_name_plural = "User Management / E / Authorised Group Permission"

    def __str__(self): return self.auth_group_permission_id

    def __label__(self): return f"{self.auth_group_id} – {self.auth_group_permission_id}"

    def __repr__(self):
        return "<AuthGroupPermission {}>".format(
            f"{self.auth_group_id} - {self.auth_group_permission_id}")
