"""
Users application views

"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from tasks.views import tasks


def user_profile_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to user profile view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    ctx = {
        "assigned_tasks": tasks[:1]
    }

    return render(request, "users/profile.html", ctx)


def auth_sign_up_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to signup view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    return render(request, "auth/signup.html")


def auth_sign_in_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to signup view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    return render(request, "auth/signin.html")


def auth_sign_out_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to sign out view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    return redirect("tasks:list")
