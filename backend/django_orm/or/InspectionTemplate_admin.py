from django.contrib import admin
from utils.admin_base import BaseAdmin

from .InspectionTemplate_model import InspectionTemplate


@admin.register(InspectionTemplate)
class InspectionTemplateAdmin(BaseAdmin):
    pass