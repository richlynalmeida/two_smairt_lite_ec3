from django.contrib import admin
from utils.admin_base import BaseAdmin

from .AuthUserUserPermission_model import AuthUserUserPermission


@admin.register(AuthUserUserPermission)
class AuthUserUserPermissionAdmin(BaseAdmin):
    pass
