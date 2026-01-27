from django.contrib import admin
from utils.admin_base import BaseAdmin

from .Project_model import Project


@admin.register(Project)
class ProjectAdmin(BaseAdmin):
    search_fields = ("project_code", "project_title")