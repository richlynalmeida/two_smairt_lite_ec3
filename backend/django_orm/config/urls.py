from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # ─────────────────────────────────────────────
    # API Contracts (temporary Django host)
    # ─────────────────────────────────────────────
    path("api/v1/", include("utils.contract.v1.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
