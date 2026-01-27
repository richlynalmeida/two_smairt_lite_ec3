from django.db import models
from utils.mixins import MixinsModel


class AuthGroup(models.Model):
    auth_group_id = models.AutoField(primary_key=True, db_column='id', verbose_name='Group ID')
    auth_group_name = models.CharField(unique=True, max_length=150, db_column='name', verbose_name='Group Name')

    class Meta:
        managed = False
        db_table = 'auth_group'
        app_label = 'core'
        verbose_name_plural = "User Management / B / Authorised Group"
        ordering = ['auth_group_name']

    def __str__(self): return self.auth_group_name

    def __label__(self): return f"{self.auth_group_id} – {self.auth_group_name}"

    def __repr__(self):
        return "<AuthGroup {}>".format(
            f"{self.auth_group_id} - {self.auth_group_name}")
