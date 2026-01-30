from django.urls import path
from .views import (
    create_project_structure,
    list_project_structures,
)

urlpatterns = [
    path("project-structure/create/", create_project_structure),
    path("project-structure/list/", list_project_structures),
]
