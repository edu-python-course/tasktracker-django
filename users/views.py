"""
Users application views

"""

from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods

from users.forms import SignInForm, SignUpForm

UserModel = get_user_model()


@login_required(login_url=reverse_lazy("users:sign-in"))
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


@require_http_methods(["GET", "POST"])
def sign_in_view(request: HttpRequest) -> HttpResponse:
    """
    Authenticate a user

    """

    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            login(request, form.instance)

            redirect_to = request.GET.get(
                "next",
                reverse_lazy("users:profile")
            )

            return redirect(redirect_to)

    else:
        form = SignInForm()

    return render(request, "auth/signin.html", {"form": form})


class SignOutView(LogoutView):
    """
    Handle requests to log out the user

    """

    http_method_names = ["post"]
    next_page = reverse_lazy("tasks:list")
