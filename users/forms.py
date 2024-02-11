"""
Users application forms

"""

from django import forms


class SignUpForm(forms.Form):
    """
    Sign up form

    Collects and validates the user inputs to register a new user.

    """

    username = forms.CharField(max_length=64)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
