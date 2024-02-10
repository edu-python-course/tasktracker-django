from django import test
from django.urls import reverse


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
        cls.template_name = "auth/signup.html"

    def setUp(self) -> None:
        self.client = test.Client()

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)


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
