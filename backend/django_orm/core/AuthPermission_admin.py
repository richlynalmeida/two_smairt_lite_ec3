from django.contrib import admin
from utils.admin_base import BaseAdmin

from .AuthPermission_model import AuthPermission


@admin.register(AuthPermission)
class AuthPermissionAdmin(BaseAdmin):
    pass
