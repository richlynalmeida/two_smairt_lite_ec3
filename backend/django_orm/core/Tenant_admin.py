from django.contrib import admin
from utils.admin_base import BaseAdmin

from .Tenant_model import Tenant

@admin.register(Tenant)
class TenantAdmin(BaseAdmin):
    pass
