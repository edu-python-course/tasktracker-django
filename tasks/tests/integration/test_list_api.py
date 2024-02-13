from http import HTTPStatus

from django.contrib.auth import get_user_model
from rest_framework import test
from rest_framework.reverse import reverse

UserModel = get_user_model()


class TestTasksResourceListAPI(test.APITestCase):
    fixtures = ["users", "tokens"]

    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("api:tasks:list")
        cls.admin = UserModel.objects.get(pk=1)
        cls.reporter = UserModel.objects.get(pk=2)
        cls.assignee = UserModel.objects.get(pk=3)
        cls.data = {
            "summary": "Test tasks resource list API views"
        }

    def setUp(self) -> None:
        self.client = test.APIClient()

    def test_safe_methods(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_unauthorized_restricted_to_create(self):
        response = self.client.post(self.url_path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)

    def test_admins_restricted_to_create(self):
        self.client.force_authenticate(token=self.admin.auth_token)
        response = self.client.post(self.url_path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.FORBIDDEN)
