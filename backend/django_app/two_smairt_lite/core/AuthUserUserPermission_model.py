from django.db import models
from utils.mixins import MixinsModel

class AuthUserUserPermission(MixinsModel):
    auth_user_user_permission_id = models.AutoField(primary_key=True, db_column='id', verbose_name="Authorised User User Permission")
    auth_user_id = models.ForeignKey('core.AuthUser', on_delete=models.RESTRICT, db_column='user_id',
                             related_name='au_j_auup', verbose_name='Authorised User')
    auth_permission_id = models.ForeignKey('core.AuthPermission', on_delete=models.RESTRICT, db_column='permission_id',
                              related_name='ap_j_auup', verbose_name='Authorised Permission')

    class Meta:
        db_table = 'auth_user_user_permissions'
        managed = False
        unique_together = (('auth_user_id', 'auth_permission_id'),)
        verbose_name_plural = "User Management / F / Authorised User User Permissions"

    def __str__(self): return self.auth_user_user_permission_id

    def __label__(self): return f"{self.auth_user_user_permission_id} – {self.auth_user_id}"

    def __repr__(self):
        return "<AuthUserUserPermission {}>".format(
            f"{self.auth_user_user_permission_id} - {self.auth_user_id}")