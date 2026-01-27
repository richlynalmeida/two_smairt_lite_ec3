from django.db import models
from utils.mixins import MixinsModel

class AuthUserGroup(models.Model):
    auth_user_group_id = models.AutoField(primary_key=True, db_column='id', verbose_name='Auth User Group ID')
    auth_user_id = models.ForeignKey('core.AuthUser', on_delete=models.RESTRICT, db_column='user_id',
                             related_name='au_j_aug', verbose_name='Authorised User')
    auth_group_id = models.ForeignKey('core.AuthGroup', on_delete=models.RESTRICT, db_column='group_id',
                              related_name='ag_j_aug', verbose_name='Authorised Group')

    class Meta:
        db_table = 'auth_user_groups'
        managed = False
        unique_together = (('auth_user_id', 'auth_group_id'),)
        verbose_name_plural = "User Management / D / Authorised User Group"

    def __str__(self): return self.auth_user_group_id

    def __label__(self): return f"{self.auth_user_group_id} – {self.auth_user_id}"

    def __repr__(self):
        return "<AuthUserGroup {}>".format(
            f"{self.auth_user_group_id} - {self.auth_user_id}")
