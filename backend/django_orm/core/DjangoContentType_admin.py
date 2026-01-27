from django.contrib import admin
from utils.admin_base import BaseAdmin

from .DjangoContentType_model import DjangoContentType


@admin.register(DjangoContentType)
class DjangoContentTypeAdmin(BaseAdmin):
    pass
