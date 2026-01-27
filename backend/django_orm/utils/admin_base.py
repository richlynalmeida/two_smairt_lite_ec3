# backend/django_orm/utils/admin_base.py
from django.contrib import admin
from django.utils.http import urlencode
from django.utils.html import format_html
from .admin_mixins import PrettyNumberMixin  # your existing formatter

# --- Actions ---
def archive_soft_delete(modeladmin, request, queryset):
    for obj in queryset:
        if hasattr(obj, "soft_delete"):
            obj.soft_delete()
archive_soft_delete.short_description = "Archive (soft delete selected)"

def unarchive_restore(modeladmin, request, queryset):
    for obj in queryset:
        if hasattr(obj, "undelete"):
            obj.undelete()
unarchive_restore.short_description = "Unarchive (restore selected)"

# --- Simple list filter for Y/N deleted flag ---
class IsDeletedFilter(admin.SimpleListFilter):
    title = "Archived?"
    parameter_name = "is_deleted"
    def lookups(self, request, model_admin): return (("N","No"),("Y","Yes"))
    def queryset(self, request, qs):
        val = self.value()
        return qs.filter(is_deleted=val) if val in ("Y","N") else qs

class NumericColumnsMixin(PrettyNumberMixin):
    """Factory helpers for neat numeric columns without copy/paste."""
    @staticmethod
    def money_col(field):
        @admin.display(description=field.replace("_", " ").title())
        def _col(obj):
            return PrettyNumberMixin.fmt_money(getattr(obj, field, None))
        return _col

    @staticmethod
    def num_col(field, digits=2, label=None):
        @admin.display(description=label or field.replace("_", " ").title())
        def _col(obj):
            return PrettyNumberMixin.fmt_num(getattr(obj, field, None), digits=digits)
        return _col

    @staticmethod
    def pct_col(field, digits=1, label=None):
        @admin.display(description=label or field.replace("_", " ").title())
        def _col(obj):
            return PrettyNumberMixin.fmt_pct(getattr(obj, field, None), digits=digits)
        return _col

    @staticmethod
    def volatility_badge_col(p50_field, p90_field, label="Volatility"):
        @admin.display(description=label)
        def _col(obj):
            return PrettyNumberMixin.volatility_badge(
                getattr(obj, p50_field, None),
                getattr(obj, p90_field, None),
            )
        return _col

class BaseAdmin(NumericColumnsMixin, admin.ModelAdmin):
    """Low-magic defaults for all models."""
    list_per_page = 50
    save_on_top = True
    actions = [archive_soft_delete, unarchive_restore,]
    list_filter = (IsDeletedFilter,)  # adds a clean Y/N toggle

    # Hide archived rows by default unless ?show_deleted=Y
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if "is_deleted" in [f.name for f in self.model._meta.fields]:
            if request.GET.get("show_deleted") != "Y":
                qs = qs.filter(is_deleted="N")
        return qs

    # Make audit fields read-only if present
    def get_readonly_fields(self, request, obj=None):
        ro = list(super().get_readonly_fields(request, obj))
        for name in ("created_at", "updated_at", "deleted_at", "is_deleted"):
            if any(f.name == name for f in self.model._meta.fields) and name not in ro:
                ro.append(name)
        return ro

    # Add a simple “Show/Hide archived” toggle (optional template use)
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        params = request.GET.copy()
        params["show_deleted"] = "N" if request.GET.get("show_deleted") == "Y" else "Y"
        extra_context["toggle_deleted_url"] = f"{request.path}?{urlencode(params)}"
        extra_context["showing_deleted"] = request.GET.get("show_deleted") == "Y"
        return super().changelist_view(request, extra_context=extra_context)

    # Prefer updated_at if present for date_hierarchy
    def get_date_hierarchy(self, request):
        names = [f.name for f in self.model._meta.fields]
        if "updated_at" in names: return "updated_at"
        if "created_at" in names: return "created_at"
        return super().get_date_hierarchy(request)
