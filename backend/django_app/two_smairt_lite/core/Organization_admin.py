from django.contrib import admin
from utils.admin_base import BaseAdmin

from .Organization_model import Organization

@admin.register(Organization)
class OrganizationAdmin(BaseAdmin):
    pass
