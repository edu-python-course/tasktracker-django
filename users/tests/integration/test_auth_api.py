from http import HTTPStatus

from rest_framework import test
from rest_framework.reverse import reverse


class TestAuthTokenAPIView(test.APITestCase):
    fixtures = ["users"]

    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("api:users:auth-token")
        cls.credentials = {
            "username": "prombery87",
            "password": "ieZeiSh5k",
        }

    def setUp(self) -> None:
        self.client = test.APIClient()

    def test_valid_credentials(self):
        response = self.client.post(self.url_path, self.credentials)
        self.assertIn(b"user_pk", response.content)
        self.assertIn(b"token", response.content)

    def test_invalid_credentials(self):
        credentials = self.credentials.copy()
        credentials["username"] = "invalid"
        response = self.client.post(self.url_path, credentials)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

        credentials = self.credentials.copy()
        credentials["password"] = "invalid"
        response = self.client.post(self.url_path, credentials)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
