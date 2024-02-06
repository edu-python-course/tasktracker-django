"""
Users application forms

"""

from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Field, Submit
from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

UserModel = get_user_model()


class SignUpForm(forms.Form):
    """
    User sign up (registration) form implementation

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

    def clean_username(self):
        """
        Validate username input before signing up

        :raise: ValidationError if username is already taken

        """

        username = self.cleaned_data["username"]
        if UserModel.objects.filter(username=username).exists():
            raise ValidationError("username already taken")

        return username

    def clean_confirm_password(self):
        """
        Validate confirm password matches password input

        """

        password = self.cleaned_data["password"]
        confirm_password = self.cleaned_data["confirm_password"]
        if password != confirm_password:
            error_msg = "passwords don't match"
            self.add_error("password", error_msg)
            self.add_error("confirm_password", error_msg)

        return confirm_password


class SignInForm(forms.Form):
    """
    User sign in (log in) form implementation

    """

    username = forms.CharField()
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

    def clean(self):
        """
        Check username and password to authenticate user

        """

        try:
            user = UserModel.objects.get(username=self.cleaned_data["username"])
        except UserModel.DoesNotExist:
            raise ValidationError("invalid username or password")

        if not user.check_password(self.cleaned_data["password"]):
            raise ValidationError("invalid username or password")


class UserModelForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ("first_name", "last_name", "image")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("first_name"),
            Field("last_name"),
            Field("image"),
            Submit("submit", "Save", css_class="w-100 mt-2")
        )

    def clean_image(self):
        return self.cleaned_data.get("image") or UserModel.get_default_image()
