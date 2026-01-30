from django.contrib import admin
from utils.admin_base import BaseAdmin

from .CompanyItem_model import CompanyItem

@admin.register(CompanyItem)
class CompanyItemAdmin(BaseAdmin):
    search_fields = ("company_code", "company_name")
