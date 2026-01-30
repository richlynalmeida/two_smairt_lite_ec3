from django.contrib import admin

# ---- Branding ----
admin.site.site_header = "2SMAiRT Administration"
admin.site.site_title = "2SMAiRT Admin"
admin.site.index_title = "2SMAiRT Control Panel"

# ---- Force-load admin infrastructure ----
from . import admin_base  # noqa
from . import admin_mixins  # noqa

print("🔥 2SMAiRT admin system loaded")
