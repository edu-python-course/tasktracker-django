"""
Tasks application API routes

"""

from django.urls import path

from tasks import resources

app_name = "tasks"
urlpatterns = [
    path("tasks/", resources.TaskModelViewSet.as_view({
        "get": "list",
        "post": "create",
    }), name="tasks-list"),
    path("tasks/<uuid:pk>/", resources.TaskModelViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }), name="tasks-detail")
]
