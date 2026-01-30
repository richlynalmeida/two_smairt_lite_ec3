from django.contrib import admin
from utils.admin_base import BaseAdmin

from .AuthUserGroup_model import AuthUserGroup


@admin.register(AuthUserGroup)
class AuthUserGroupAdmin(BaseAdmin):
    pass
