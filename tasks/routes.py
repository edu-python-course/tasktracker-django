"""
Tasks application API routes

"""

from django.urls import path

from tasks import resources

urlpatterns = [
    path("tasks/", resources.tasks_list_resource),
    path("tasks/<uuid:pk>/", resources.tasks_detail_resource),
]
