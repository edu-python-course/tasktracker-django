"""
Tasks application API routes

"""

from django.urls import path

from tasks.resources import TaskModelViewSet

tasks_list = TaskModelViewSet.as_view({
    "get": "list",
    "post": "create",
})
tasks_detail = TaskModelViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})

app_name = "tasks"
urlpatterns = [
    path("tasks/", tasks_list, name="list"),
    path("tasks/<uuid:pk>/", tasks_detail, name="detail"),
]
