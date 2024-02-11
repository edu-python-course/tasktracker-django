"""
Tasks application URL configuration

"""

from django.urls import path

from tasks import views

app_name = "tasks"
urlpatterns = [
    path("create/", views.TaskCreateView.as_view(), name="create"),
    path("<uuid:pk>/", views.TaskDetailView.as_view(), name="detail"),
    path("<uuid:pk>/update/", views.TaskUpdateView.as_view(), name="update"),
    path("<uuid:pk>/delete/", views.TaskDeleteView.as_view(), name="delete"),
    path("", views.task_list_view, name="list"),
]
