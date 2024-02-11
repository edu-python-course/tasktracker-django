from django import test
from django.contrib.auth import get_user_model
from django.urls import reverse

UserModel = get_user_model()


class TestUserProfileView(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("users:profile")
        cls.template_name = "users/profile.html"

    def setUp(self) -> None:
        self.client = test.Client()

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)


class TestSignUpView(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("users:sign-up")
        cls.redirect = reverse("users:sign-in")
        cls.template_name = "auth/signup.html"
        cls.payload = {
            "username": "butime",
            "email": "butime@example.com",
            "password": "Zeiriev1oo",
            "confirm_password": "Zeiriev1oo",
        }

    def setUp(self) -> None:
        self.client = test.Client()

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)

    def test_user_creation(self):
        self.client.post(self.url_path, data=self.payload)
        qs = UserModel.objects.filter(email=self.payload["email"])
        self.assertTrue(qs.exists())

    def test_response_redirects(self):
        response = self.client.post(self.url_path, self.payload)
        self.assertRedirects(response, self.redirect)


class TestSignInView(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("users:sign-in")
        cls.template_name = "auth/signin.html"

    def setUp(self) -> None:
        self.client = test.Client()

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)


class TestSignOutView(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("users:sign-out")
        cls.url_redirect = reverse("tasks:list")

    def setUp(self) -> None:
        self.client = test.Client()

    def test_redirects(self):
        response = self.client.get(self.url_path)
        self.assertRedirects(response, self.url_redirect)
