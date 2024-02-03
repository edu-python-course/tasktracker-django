from django import test
from django.urls import reverse


class TestUserProfileView(test.TestCase):
    def setUp(self) -> None:
        self.url_path = reverse("users:profile")
        self.template_name = "users/profile.html"
        self.client = test.Client()

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)


class TestSignUpView(test.TestCase):
    def setUp(self) -> None:
        self.url_path = reverse("users:sign-up")
        self.template_name = "auth/signup.html"
        self.client = test.Client()

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)


class TestSignInView(test.TestCase):
    def setUp(self) -> None:
        self.url_path = reverse("users:sign-in")
        self.template_name = "auth/signin.html"
        self.client = test.Client()

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)


class TestSignOutView(test.TestCase):
    def setUp(self) -> None:
        self.url_path = reverse("users:sign-out")
        self.client = test.Client()

    def test_redirect(self):
        response = self.client.get(self.url_path)
        self.assertRedirects(response, reverse("tasks:list"))
