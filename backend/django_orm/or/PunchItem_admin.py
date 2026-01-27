from django.contrib import admin
from utils.admin_base import BaseAdmin

from .PunchItem_model import PunchItem


@admin.register(PunchItem)
class PunchItemAdmin(BaseAdmin):
    pass