from django import test
from django.contrib.auth import get_user
from django.contrib.auth import get_user_model
from django.urls import reverse

UserModel = get_user_model()


class TestSignOutView(test.TestCase):
    fixtures = ["users"]

    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("users:sign-out")
        cls.url_redirect = reverse("tasks:list")

    def setUp(self) -> None:
        self.client = test.Client()

    def test_user_signed_out(self):
        self.client.force_login(UserModel.objects.get(username="butime"))
        self.client.post(self.url_path)
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)

    def test_redirects(self):
        response = self.client.post(self.url_path)
        self.assertRedirects(response, self.url_redirect)
