from django.contrib import admin
from utils.admin_base import BaseAdmin

from .AuthGroupPermission_model import AuthGroupPermission


@admin.register(AuthGroupPermission)
class AuthGroupPermissionAdmin(BaseAdmin):
    pass
