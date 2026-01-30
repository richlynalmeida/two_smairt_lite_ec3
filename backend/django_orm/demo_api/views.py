import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from project.models import Project, ProjectStructure

@csrf_exempt
def create_project_structure(request):
    if request.method != "POST":
        return JsonResponse({"success": False, "error": "POST only"}, status=405)

    try:
        payload = json.loads(request.body)
    except Exception as e:
        return JsonResponse(
            {"success": False, "error": f"Invalid JSON: {str(e)}"},
            status=400
        )

    project = Project.objects.first()
    if not project:
        return JsonResponse(
            {"success": False, "error": "No project found"},
            status=500
        )

    parent = None
    parent_id = payload.get("parent_project_structure_id")
    if parent_id:
        try:
            parent = ProjectStructure.objects.get(
                project_structure_id=parent_id
            )
        except ProjectStructure.DoesNotExist:
            return JsonResponse(
                {"success": False, "error": "Parent not found"},
                status=400
            )

    try:
        node = ProjectStructure.objects.create(
            project=project,
            parent_project_structure=parent,
            structure_code=payload.get("structure_code"),
            structure_title=payload.get("structure_title"),
            structure_level=payload.get("structure_level"),
            structure_role=payload.get("structure_role", "SPATIAL"),
            sort_order=payload.get("sort_order", 0),
            comments=payload.get("comments", "")
        )
    except Exception as e:
        return JsonResponse(
            {"success": False, "error": f"DB error: {str(e)}"},
            status=500
        )

    return JsonResponse({
        "success": True,
        "node": {
            "id": node.project_structure_id,
            "name": node.structure_title,
            "code": node.structure_code,
            "type": node.structure_role,
            "level": node.structure_level,
            "created_at": node.created_at.isoformat()
            if node.created_at else None,
            "children": []
        }
    })

# ---------------------------------------------------------------------
# Helper: serialize a ProjectStructure node into API contract
# ---------------------------------------------------------------------
def serialize_node(n):
    return {
        "id": n.project_structure_id,
        "name": n.structure_title,
        "code": n.structure_code,
        "type": n.structure_role,
        "level": n.structure_level,
        "created_at": n.created_at.isoformat()
        if n.created_at else None,
        "children": []
    }


# ---------------------------------------------------------------------
# List project structures as a TREE (single root)
# ---------------------------------------------------------------------
def list_project_structures(request):
    project = Project.objects.first()
    if not project:
        return JsonResponse({}, safe=False)

    nodes = ProjectStructure.objects.filter(
        project=project,
        is_active='Y'
    ).order_by(
        "structure_level",
        "sort_order",
        "structure_code"
    )

    # Build lookup map
    node_map = {}
    root = None

    for n in nodes:
        node_map[n.project_structure_id] = serialize_node(n)

    # Assemble tree
    for n in nodes:
        node_data = node_map[n.project_structure_id]

        if n.parent_project_structure_id:
            parent = node_map.get(n.parent_project_structure_id)
            if parent:
                parent["children"].append(node_data)
        else:
            # No parent = root node
            root = node_data

    return JsonResponse(root or {}, safe=False)
