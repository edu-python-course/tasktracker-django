"""
Tasks application URL configuration

"""

from django.urls import path

from tasks import views

app_name = "tasks"
urlpatterns = [
    path("create/", views.task_create_view, name="create"),
    path("<uuid:pk>/", views.task_detail_view, name="detail"),
    path("<uuid:pk>/update/", views.task_update_view, name="update"),
    path("<uuid:pk>/delete/", views.task_delete_view, name="delete"),
    path("", views.task_list_view, name="list"),
]
