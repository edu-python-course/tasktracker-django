"""
Users application views

"""

from django.http import HttpRequest, HttpResponse


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
