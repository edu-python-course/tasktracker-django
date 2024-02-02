"""
URL configuration for tasktracker project.

The `urlpatterns` list routes URLs to views. For more information please
see: https://docs.djangoproject.com/en/5.0/topics/http/urls/

Examples:

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")

Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")

Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))

"""

from django.contrib import admin
from django.urls import path

from tasks import views as tasks_views
from users import views as users_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("profile/", users_views.user_profile_view, name="profile"),
    path("sign-up/", users_views.auth_sign_up_view, name="sign-up"),
    path("sign-in/", users_views.auth_sign_in_view, name="sign-in"),
    path("sign-out/", users_views.auth_sign_out_view, name="sign-out"),
    path("create/", tasks_views.task_create_view, name="create"),
    path("<int:pk>/", tasks_views.task_detail_view, name="detail"),
    path("<int:pk>/update/", tasks_views.task_update_view, name="update"),
    path("<int:pk>/delete/", tasks_views.task_delete_view, name="delete"),
    path("", tasks_views.task_list_view, name="list"),
]
