"""
Tasks application API routes

"""

from django.urls import path

from tasks import resources

app_name = "tasks"
urlpatterns = [
    path("tasks/", resources.tasks_list, name="tasks-list"),
    path("tasks/<uuid:pk>/", resources.tasks_detail, name="tasks-detail")
]
