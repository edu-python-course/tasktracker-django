"""
Users application views

"""

from django.http.request import HttpRequest
from django.http.response import HttpResponse


def user_profile_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to user's profile

    """

    return HttpResponse("user profile")


def sign_up_view(request: HttpRequest) -> HttpResponse:
    """
    Register a new user in the system

    """

    return HttpResponse("sign up")


def sign_in_view(request: HttpRequest) -> HttpResponse:
    """
    Authenticate a user

    """

    return HttpResponse("sign in")


def sign_out_view(request: HttpRequest) -> HttpResponse:
    """
    Sing out the authenticated user

    """

    return HttpResponse("sign out")
