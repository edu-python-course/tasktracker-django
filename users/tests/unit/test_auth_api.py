from django.contrib.auth import get_user_model
from rest_framework import test
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse

from users.resources import AuthTokenAPIView

UserModel = get_user_model()


class TestAuthTokenAPIView(test.APITestCase):
    fixtures = ["users"]

    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("api:users:auth-token")
        cls.credentials = {
            "username": "prombery87",
            "password": "ieZeiSh5k",
        }
        cls.user = UserModel.objects.get(pk=2)

    def setUp(self) -> None:
        self.factory = test.APIRequestFactory()
        self.view = AuthTokenAPIView.as_view()

    def test_auth_token_created(self):
        request = self.factory.post(self.url_path, self.credentials)
        self.view(request)
        self.assertTrue(Token.objects.filter(user=self.user).exists())
