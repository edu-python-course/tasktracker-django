"""
Users application views

"""

from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render


def user_profile_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to user's profile

    """

    return render(request, "users/profile.html")


def sign_up_view(request: HttpRequest) -> HttpResponse:
    """
    Register a new user in the system

    """

    return render(request, "auth/signup.html")


def sign_in_view(request: HttpRequest) -> HttpResponse:
    """
    Authenticate a user

    """

    return render(request, "auth/signin.html")


def sign_out_view(request: HttpRequest) -> HttpResponse:
    """
    Sing out the authenticated user

    """

    return redirect("tasks:list")
