"""
Users application views

"""

from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView

from users.forms import SignInForm, SignUpForm, UserModelForm

UserModel = get_user_model()


class UserProfileView(LoginRequiredMixin, UpdateView):
    http_method_names = ["get", "post"]
    model = UserModel
    form_class = UserModelForm
    template_name = "users/profile.html"
    success_url = reverse_lazy("users:profile")
    login_url = reverse_lazy("users:sign-in")

    def get_object(self, queryset=None):
        return self.request.user


class SignUpView(FormView):
    """
    Handle a new user registration

    """

    http_method_names = ["get", "post"]
    form_class = SignUpForm
    template_name = "auth/signup.html"
    success_url = reverse_lazy("users:sign-in")

    def form_valid(self, form):
        del form.cleaned_data["confirm_password"]
        UserModel.objects.create_user(**form.cleaned_data)

        return super().form_valid(form)


class SignInView(FormView):
    """
    Handle existing users authentication

    """

    http_method_names = ["get", "post"]
    template_name = "auth/signin.html"
    form_class = SignInForm
    success_url = reverse_lazy("users:profile")

    def form_valid(self, form):
        login(self.request, form.instance)

        return super().form_valid(form)

    def get_success_url(self):
        return self.success_url


class SignOutView(LogoutView):
    """
    Handle requests to log out the user

    """

    http_method_names = ["post"]
    next_page = reverse_lazy("tasks:list")
