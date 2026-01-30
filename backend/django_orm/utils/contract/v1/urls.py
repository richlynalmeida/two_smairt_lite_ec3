from django.urls import path

from .health import health
from demo_api.views import (
    list_project_structures,
    create_project_structure,
)

urlpatterns = [
    # Health check (already working)
    path("health/", health),

    # Project Structure (READ)
    path(
        "project-structure/list/",
        list_project_structures,
        name="project-structure-list",
    ),

    # Project Structure (WRITE)
    path(
        "project-structure/create/",
        create_project_structure,
        name="project-structure-create",
    ),
]
