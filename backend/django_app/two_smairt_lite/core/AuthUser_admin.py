from django.contrib import admin
from utils.admin_base import BaseAdmin

from .AuthUser_model import AuthUser


@admin.register(AuthUser)
class AuthUserAdmin(BaseAdmin):
    search_fields = ("username", "first_name", "last_name", "email")
