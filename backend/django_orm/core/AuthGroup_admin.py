from django.contrib import admin
from utils.admin_base import BaseAdmin

from .AuthGroup_model import AuthGroup


@admin.register(AuthGroup)
class AuthGroupAdmin(BaseAdmin):
    pass
