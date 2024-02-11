"""
Users application views

"""

from django.contrib.auth import get_user_model
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from users.forms import SignUpForm

UserModel = get_user_model()


def user_profile_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to user's profile

    """

    ctx = {
        "first_name": "Dora",
        "last_name": "Headstrong",
        "email": "DoraHeadstrong@dayrep.com",
        "get_full_name": lambda: "Dora Headstrong",
    }

    return render(request, "users/profile.html", ctx)


@require_http_methods(["GET", "POST"])
def sign_up_view(request: HttpRequest) -> HttpResponse:
    """
    Register a new user in the system

    """

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            del form.cleaned_data["confirm_password"]
            UserModel.objects.create_user(**form.cleaned_data)

            return redirect("users:sign-in")

    else:
        form = SignUpForm()

    return render(request, "auth/signup.html", {"form": form})


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
