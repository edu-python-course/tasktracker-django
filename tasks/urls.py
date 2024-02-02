"""
Tasks application URL configuration

"""

from django.urls import path

from tasks import views

app_name = "tasks"
urlpatterns = [
    path("create/", views.task_create_view, name="create"),
    path("<int:pk>/", views.task_detail_view, name="detail"),
    path("<int:pk>/update/", views.task_update_view, name="update"),
    path("<int:pk>/delete/", views.task_delete_view, name="delete"),
    path("", views.task_list_view, name="list"),
]
