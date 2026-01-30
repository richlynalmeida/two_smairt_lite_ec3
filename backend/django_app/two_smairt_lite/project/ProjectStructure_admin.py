from django.contrib import admin
from utils.admin_base import BaseAdmin

from .ProjectStructure_model import ProjectStructure


@admin.register(ProjectStructure)
class ProjectStructureAdmin(BaseAdmin):
    pass