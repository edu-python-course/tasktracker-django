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
from django.http import HttpRequest, HttpResponse
from django.urls import path


def task_list_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to task list view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    return HttpResponse(b"task list view")


def task_create_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to task create view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    return HttpResponse(b"task create view")


def task_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Handle requests to task detail view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`
    :param pk: task primary key
    :type pk: int

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    return HttpResponse(b"task detail view: %d" % pk)


def task_update_view(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Handle requests to task update view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`
    :param pk: task primary key
    :type pk: int

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    return HttpResponse(b"task update view: %d" % pk)


def task_delete_view(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Handle requests to task delete view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`
    :param pk: task primary key
    :type pk: int

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    return HttpResponse(b"task delete view: %d" % pk)


def user_profile_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to user profile view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    return HttpResponse(b"user profile view")


def auth_sign_up_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to signup view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    return HttpResponse(b"auth sign up view")


def auth_sign_in_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to signup view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    return HttpResponse(b"auth sign in view")


def auth_sign_out_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to sign out view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    return HttpResponse(b"auth sign out view")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("profile/", user_profile_view),
    path("sign-up/", auth_sign_up_view),
    path("sign-in/", auth_sign_in_view),
    path("sign-out/", auth_sign_out_view),
    path("create/", task_create_view),
    path("<int:pk>/", task_detail_view),
    path("<int:pk>/update/", task_update_view),
    path("<int:pk>/delete/", task_delete_view),
    path("", task_list_view),
]
