"""
Tasks application API routes

"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from tasks.resources import TaskModelViewSet

router = DefaultRouter()
router.register(r"tasks", TaskModelViewSet, basename="tasks")

app_name = "tasks"
urlpatterns = [
    path("", include(router.urls)),
]
