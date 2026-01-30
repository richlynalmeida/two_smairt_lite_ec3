from django.contrib import admin
from utils.admin_base import BaseAdmin

from .CompanyCategory_model import CompanyCategory


@admin.register(CompanyCategory)
class CompanyCategoryAdmin(BaseAdmin):
    pass
