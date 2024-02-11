"""
Users application forms

"""

from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth import authenticate, get_user_model

UserModel = get_user_model()


class SignUpForm(forms.Form):
    """
    Sign up form

    Collects and validates the user inputs to register a new user.

    """

    username = forms.CharField(max_length=64)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = "w-50 m-auto"
        self.helper.form_id = "formAuth"
        self.helper.form_method = "post"
        self.helper.attrs["aria-label"] = "SignUpForm"
        self.helper.layout = Layout(
            FloatingField("username"),
            FloatingField("email"),
            FloatingField("password"),
            FloatingField("confirm_password"),
            Submit("submit", "Sign Up",
                   css_class="w-100 my-2 fs-5")
        )

    def clean_username(self) -> str:
        """
        Validate username input before signing up the user

        Username should be unique within the task tracker system.

        :raise: `django.forms.ValidationError`

        """

        username = self.cleaned_data.get("username")
        if UserModel.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already taken")

        return username

    def clean_email(self) -> str:
        """
        Validate email input before signing up the user

        Email address should be unique within the task tracker system.

        :raise: `django.forms.ValidationError`

        """

        email = self.cleaned_data.get("email")
        if UserModel.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already registered")

        return email

    def clean_confirm_password(self) -> str:
        """
        Validate confirm password matches password input

        """

        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password:
            err_msg = "Passwords don't match"
            self.add_error("password", err_msg)
            self.add_error("confirm_password", err_msg)

        return confirm_password


class SignInForm(forms.Form):
    """
    Sign in form

    Collects and validates the user inputs to log in a user.

    """

    instance: UserModel = None

    username = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = "w-50 m-auto"
        self.helper.form_id = "formAuth"
        self.helper.form_method = "post"
        self.helper.attrs["aria-label"] = "SignInForm"
        self.helper.layout = Layout(
            FloatingField("username"),
            FloatingField("password"),
            Submit("submit", "Sign In",
                   css_class="w-100 my-2 fs-5")
        )

    def clean(self) -> None:
        """
        Validate user credentials

        """

        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        self.instance = authenticate(username=username, password=password)

        if self.instance is None:
            raise forms.ValidationError("Invalid username or password")
