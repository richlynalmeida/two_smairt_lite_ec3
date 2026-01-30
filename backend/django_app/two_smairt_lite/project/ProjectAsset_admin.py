from django.contrib import admin
from utils.admin_base import BaseAdmin

from .ProjectAsset_model import ProjectAsset


@admin.register(ProjectAsset)
class ProjectAssetAdmin(BaseAdmin):
    pass