"""
Users application forms

"""

from django import forms


class SignUpForm(forms.Form):
    """
    User sign up (registration) form implementation

    """

    username = forms.CharField(max_length=64)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)


class SignInForm(forms.Form):
    """
    User sign in (log in) form implementation

    """

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
