from django import test
from django.contrib.auth import get_user
from django.urls import reverse


class TestSignInView(test.TestCase):
    fixtures = ["users"]

    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("users:sign-in")
        cls.template_name = "auth/signin.html"
        cls.payload = {
            "username": "wheed1997",
            "password": "enohR4cog",
        }

    def setUp(self) -> None:
        self.client = test.Client()

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)

    def test_user_authenticated(self):
        self.client.post(self.url_path, self.payload)
        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)

    def test_response_redirects(self):
        response = self.client.post(self.url_path, self.payload)
        self.assertRedirects(response, reverse("users:profile"))
