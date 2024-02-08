"""
URL configuration for tasktracker project.

The `urlpatterns` list routes URLs to views. For more information please
see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/

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

from tasks import views as tasks
from users import views as users

urlpatterns = [
    path("admin/", admin.site.urls),
    path("sign-up/", users.sign_up_view),
    path("sign-in/", users.sign_in_view),
    path("sign-out/", users.sign_out_view),
    path("profile/", users.user_profile_view),
    path("create/", tasks.task_create_view),
    path("<int:pk>/", tasks.task_detail_view),
    path("<int:pk>/update/", tasks.task_update_view),
    path("<int:pk>/delete/", tasks.task_delete_view),
    path("", tasks.task_list_view),
]
