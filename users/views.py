"""
Users application views

"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from users.forms import SignInForm, SignUpForm


def user_profile_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to user profile view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    return render(request, "users/profile.html")


@require_http_methods(["GET", "POST"])
def auth_sign_up_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to signup view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            ...

    else:
        form = SignUpForm()

    return render(request, "auth/signup.html", {"form": form})


@require_http_methods(["GET", "POST"])
def auth_sign_in_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to signup view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            ...

    else:
        form = SignInForm()

    return render(request, "auth/signin.html", {"form": form})


def auth_sign_out_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to sign out view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    return redirect("tasks:list")
