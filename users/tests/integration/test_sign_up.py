from django import test
from django.contrib.auth import get_user_model
from django.urls import reverse

UserModel = get_user_model()


class TestSignUpView(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("users:sign-up")
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
