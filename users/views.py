"""
Users application views

"""

from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import FormView, UpdateView

from users.forms import SignInForm, SignUpForm, UserModelForm

UserModel = get_user_model()


@login_required(login_url=reverse_lazy("users:sign-in"))
@require_http_methods(["GET", "POST"])
def user_profile_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to user profile view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    if request.method == "POST":
        form = UserModelForm(
            request.POST,
            request.FILES,
            instance=request.user
        )
        if form.is_valid():
            form.save()

            return redirect("users:profile")

    else:
        form = UserModelForm(instance=request.user)

    return render(request, "users/profile.html", {"form": form})


class UserProfileView(LoginRequiredMixin, UpdateView):
    http_method_names = ["get", "post"]
    model = UserModel
    form_class = UserModelForm
    template_name = "users/profile.html"
    success_url = reverse_lazy("users:profile")
    login_url = reverse_lazy("users:sign-in")

    def get_object(self, queryset=None):
        return self.request.user


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
            del form.cleaned_data["confirm_password"]
            UserModel.objects.create_user(**form.cleaned_data)

            return redirect("users:sign-in")

    else:
        form = SignUpForm()

    return render(request, "auth/signup.html", {"form": form})


class SignUpView(FormView):
    http_method_names = ["get", "post"]
    form_class = SignUpForm
    template_name = "auth/signup.html"
    success_url = reverse_lazy("users:sign-in")

    def form_valid(self, form):
        del form.cleaned_data["confirm_password"]
        UserModel.objects.create_user(**form.cleaned_data)

        return super().form_valid(form)


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
        form = SignInForm(request.POST)
        if form.is_valid():
            user = UserModel.objects.get(username=form.cleaned_data["username"])
            login(request, user)
            # noinspection PyTypeChecker
            url = request.GET.get("next", reverse_lazy("users:profile"))

            return redirect(url)

    else:
        form = SignInForm()

    return render(request, "auth/signin.html", {"form": form})


class SignInView(FormView):
    http_method_names = ["get", "post"]
    template_name = "auth/signin.html"
    form_class = SignInForm
    success_url = reverse_lazy("users:profile")

    def form_valid(self, form):
        user = UserModel.objects.get(username=form.cleaned_data["username"])
        login(self.request, user)

        return super().form_valid(form)

    def get_success_url(self):
        return self.request.GET.get("next", self.success_url)


def auth_sign_out_view(request: HttpRequest) -> HttpResponse:
    """
    Handle requests to sign out view

    :param request: HttpRequest object
    :type request: :class: `django.http.HttpRequest`

    :return: HttpResponse object
    :rtype: :class:`django.http.HttpResponse`

    """

    logout(request)

    return redirect("tasks:list")


class SignOutView(LogoutView):
    next_page = reverse_lazy("tasks:list")
