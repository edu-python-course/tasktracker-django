from django import test
from django.contrib.auth import get_user_model

from users import forms

UserModel = get_user_model()


class TestSignUpForm(test.TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.username = "acen1999"
        cls.email = "email@example.com"
        cls.password = "cieted3eiPo"
        cls.form_class = forms.SignUpForm

    def setUp(self) -> None:
        UserModel.objects.create_user(
            username=self.username,
            password=self.password,
        )

    def test_username_taken_validation(self):
        form = self.form_class({
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "confirm_password": self.password,
        })
        self.assertFalse(form.is_valid())
        self.assertFormError(form, "username", "username already taken")

    def test_passwords_dont_match_validation(self):
        error_msg = "passwords don't match"
        form = self.form_class({
            "username": "butime",
            "email": self.email,
            "password": self.password,
            "confirm_password": "Zeiriev1oo",
        })
        self.assertFalse(form.is_valid())
        self.assertFormError(form, "password", [error_msg])
        self.assertFormError(form, "confirm_password", [error_msg])

    def test_validation_pass(self):
        form = self.form_class({
            "username": "butime",
            "email": "butime@example.com",
            "password": "Zeiriev1oo",
            "confirm_password": "Zeiriev1oo",
        })
        self.assertTrue(form.is_valid())


class TestSignInForm(test.TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.username = "acen1999"
        cls.password = "cieted3eiPo"
        cls.form_class = forms.SignInForm

    def setUp(self) -> None:
        UserModel.objects.create_user(
            username=self.username,
            password=self.password,
        )

    def test_invalid_username(self):
        form = self.form_class({
            "username": "butime",
            "password": self.password,
        })
        errors = ["invalid username or password"]
        self.assertFalse(form.is_valid())
        self.assertListEqual(form.errors["__all__"], errors)

    def test_invalid_password(self):
        form = self.form_class({
            "username": self.username,
            "password": "Zeiriev1oo",
        })
        errors = ["invalid username or password"]
        self.assertFalse(form.is_valid())
        self.assertListEqual(form.errors["__all__"], errors)

    def test_validation_pass(self):
        form = self.form_class({
            "username": self.username,
            "password": self.password,
        })
        self.assertTrue(form.is_valid())
